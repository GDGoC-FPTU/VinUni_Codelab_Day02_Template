"""Offline tests: synthetic responses only, never evidence of Gemini behavior."""
import importlib.util
import json
import runpy
from pathlib import Path
import sys
from types import ModuleType, SimpleNamespace
from unittest.mock import MagicMock

import pytest

MODULE_PATH = Path(__file__).resolve().parents[1] / "starter-code" / "prompt_prototype.py"
spec = importlib.util.spec_from_file_location("prototype", MODULE_PATH)
prototype = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prototype)


@pytest.mark.parametrize("override,expected", [
    (None, "gemini-3.5-flash-lite"),
    ("  ", "gemini-3.5-flash-lite"),
    (" gemini-explicit-override ", "gemini-explicit-override"),
])
def test_model_configuration_without_credentials_or_network(monkeypatch, override, expected):
    monkeypatch.delenv("GEMINI_MODEL", raising=False)
    if override is not None:
        monkeypatch.setenv("GEMINI_MODEL", override)
    namespace = runpy.run_path(str(MODULE_PATH))
    assert namespace["GEMINI_MODEL"] == expected


def response(**changes):
    payload = {
        "action": "dispatch_mobile_charger",
        "reason": "Pin 2%, cần xác minh vị trí và người duyệt.",
        "draft_message": "Đề xuất điều phối viên xác minh cứu hộ, chưa gửi yêu cầu.",
        "requires_human_approval": True,
        "station_distance_km": None,
    }
    payload.update(changes)
    return prototype.PREFIX + json.dumps(payload, ensure_ascii=False)


@pytest.mark.parametrize("action", sorted(prototype.ACTIONS))
def test_valid_proposal(action):
    assert prototype.validate_output(response(action=action), action)["action"] == action


@pytest.mark.parametrize("output", [
    "", " " + response(), response().replace(prototype.PREFIX, ""),
    "Intro: " + response(), prototype.PREFIX + "```json\n{}\n```",
    prototype.PREFIX + "[]", prototype.PREFIX + "null", prototype.PREFIX + "{}",
    response() + " trailing text", response(action="send_now"), response(action=[]),
    response(requires_human_approval=False), response(requires_human_approval=1),
    response(station_distance_km=8), response(station_distance_km=0),
    response(reason=" "), response(draft_message=None), response(extra="field"),
])
def test_reject_invalid_responses(output):
    with pytest.raises(ValueError):
        prototype.validate_output(output)


def test_critical_case_cannot_pass_with_generic_message():
    with pytest.raises(prototype.ActionMismatchError):
        prototype.validate_output(response(action="draft_message"), "dispatch_mobile_charger")


def test_action_mismatch_has_safe_action_diagnostic():
    with pytest.raises(prototype.ActionMismatchError) as caught:
        prototype.validate_output(response(action="request_information"), "dispatch_mobile_charger")
    summary = prototype.safe_error_summary(caught.value)
    assert "cần dispatch_mobile_charger, nhận request_information" in summary


def test_missing_key_is_failure(monkeypatch, capsys):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    assert prototype.main() == 1
    captured = capsys.readouterr()
    assert "CHƯA KIỂM THỬ" in captured.err
    assert "Passed" not in captured.out
    with pytest.raises(RuntimeError):
        prototype.evaluate_prompt("pin 2%")


@pytest.mark.parametrize("output,expected_status", [(response(), 0), ("bad JSON", 1)])
def test_main_checks_every_case_and_reports_truth(monkeypatch, capsys, output, expected_status):
    monkeypatch.setenv("GEMINI_API_KEY", "offline-test-placeholder")
    cases = [dict(case, expected_action="dispatch_mobile_charger") for case in prototype.ADVERSARIAL_TESTS]
    monkeypatch.setattr(prototype, "ADVERSARIAL_TESTS", cases)
    fake_call = MagicMock(return_value=output)
    monkeypatch.setattr(prototype, "evaluate_prompt", fake_call)
    assert prototype.main() == expected_status
    assert fake_call.call_count == len(cases)
    captured = capsys.readouterr()
    if expected_status:
        assert "Passed" not in captured.out
        assert captured.err.count("Failed") == len(cases)
    else:
        assert captured.out.count("Passed") == len(cases)


def test_api_failure_is_nonzero(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "offline-test-placeholder")
    monkeypatch.setattr(prototype, "evaluate_prompt", MagicMock(side_effect=RuntimeError("network unavailable")))
    assert prototype.main() == 1


def test_sdk_exception_does_not_disclose_credentials(monkeypatch, capsys):
    secret = "synthetic-secret-for-test-not-a-real-key"
    monkeypatch.setenv("GEMINI_API_KEY", secret)
    monkeypatch.setattr(prototype, "evaluate_prompt", MagicMock(side_effect=RuntimeError(f"request?key={secret}")))
    assert prototype.main() == 1
    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert "request?key=" not in captured.err
    assert "RuntimeError" in captured.err


def test_model_output_masks_both_configured_credentials(monkeypatch, capsys):
    first = "synthetic-gemini-key-for-offline-test"
    second = "synthetic-google-key-for-offline-test"
    monkeypatch.setenv("GEMINI_API_KEY", first)
    monkeypatch.setenv("GOOGLE_API_KEY", second)
    monkeypatch.setattr(prototype, "evaluate_prompt", MagicMock(return_value=response(reason=f"{first} {second}")))
    prototype.main()
    captured = capsys.readouterr()
    assert first not in captured.out + captured.err
    assert second not in captured.out + captured.err
    assert "[REDACTED]" in captured.out


@pytest.mark.parametrize("code,status,expected", [
    (400, "INVALID_ARGUMENT", "cấu hình"),
    (401, "UNAUTHENTICATED", "xác thực"),
    (403, "PERMISSION_DENIED", "quyền"),
    (404, "NOT_FOUND", "model"),
    (429, "RESOURCE_EXHAUSTED", "quota"),
    (503, "UNAVAILABLE", "thử lại"),
])
def test_safe_http_diagnostics(code, status, expected):
    exc = RuntimeError("sensitive request URL and credentials")
    exc.code, exc.status = code, status
    exc.details = {"error": {"details": [{"reason": "API_KEY_INVALID", "metadata": "sensitive"}]}}
    summary = prototype.safe_error_summary(exc)
    assert f"HTTP {code}" in summary
    assert status in summary
    assert "API_KEY_INVALID" in summary
    assert expected in summary
    assert "sensitive" not in summary


@pytest.mark.parametrize("code,status,details", [
    ("sensitive", "sensitive", {"error": {"details": [{"reason": "sensitive"}]}}),
    ([], [], {"error": []}),
    (None, None, {"error": {"details": "sensitive"}}),
])
def test_diagnostics_do_not_emit_untrusted_fields(code, status, details):
    exc = RuntimeError("sensitive")
    exc.code, exc.status, exc.details = code, status, details
    assert "sensitive" not in prototype.safe_error_summary(exc)


@pytest.mark.parametrize("text", [response(), None])
def test_sdk_wiring_and_empty_response(monkeypatch, text):
    """Verify SDK inputs using a fake module; do not make network requests."""
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setenv("GOOGLE_API_KEY", "offline-test-placeholder")
    google = ModuleType("google")
    genai = ModuleType("google.genai")
    types = ModuleType("google.genai.types")
    types.GenerateContentConfig = MagicMock(side_effect=lambda **kwargs: SimpleNamespace(**kwargs))
    client = MagicMock()
    client.models.generate_content.return_value = SimpleNamespace(text=text)
    genai.Client = MagicMock()
    genai.Client.return_value.__enter__.return_value = client
    genai.types = types
    google.genai = genai
    monkeypatch.setitem(sys.modules, "google", google)
    monkeypatch.setitem(sys.modules, "google.genai", genai)
    monkeypatch.setitem(sys.modules, "google.genai.types", types)
    if text:
        assert prototype.evaluate_prompt("pin 2%") == text
    else:
        with pytest.raises(ValueError, match="rỗng"):
            prototype.evaluate_prompt("pin 2%")
    kwargs = client.models.generate_content.call_args.kwargs
    assert kwargs["model"] == prototype.GEMINI_MODEL
    assert kwargs["contents"] == "pin 2%"
    assert kwargs["config"].system_instruction == prototype.SYSTEM_PROMPT


def test_list_models_filters_and_does_not_generate(monkeypatch):
    google = ModuleType("google")
    genai = ModuleType("google.genai")
    client = MagicMock()
    client.models.list.return_value = [
        SimpleNamespace(name="models/gemini-example-flash", supported_actions=["generateContent"]),
        SimpleNamespace(name="models/gemini-example-flash", supported_actions=["generateContent"]),
        SimpleNamespace(name="models/gemini-embedding-example", supported_actions=["embedContent"]),
        SimpleNamespace(name=None, supported_actions=None),
        SimpleNamespace(name="models/unexpected?key=secret", supported_actions=["generateContent"]),
    ]
    genai.Client = MagicMock()
    genai.Client.return_value.__enter__.return_value = client
    google.genai = genai
    monkeypatch.setitem(sys.modules, "google", google)
    monkeypatch.setitem(sys.modules, "google.genai", genai)
    monkeypatch.setenv("GEMINI_API_KEY", "offline-placeholder")
    assert prototype.list_available_models() == ["gemini-example-flash"]
    client.models.generate_content.assert_not_called()


def test_list_models_cli_does_not_run_stress_tests(monkeypatch, capsys):
    monkeypatch.setenv("GEMINI_API_KEY", "offline-placeholder")
    monkeypatch.setattr(prototype, "list_available_models", lambda: ["gemini-example-flash"])
    call = MagicMock()
    monkeypatch.setattr(prototype, "evaluate_prompt", call)
    assert prototype.main(["--list-models"]) == 0
    assert "gemini-example-flash" in capsys.readouterr().out
    call.assert_not_called()


@pytest.mark.parametrize("result", [[], RuntimeError("private URL")])
def test_list_models_empty_or_error_fails_safely(monkeypatch, capsys, result):
    monkeypatch.setenv("GEMINI_API_KEY", "offline-placeholder")
    call = MagicMock(side_effect=result) if isinstance(result, Exception) else MagicMock(return_value=result)
    monkeypatch.setattr(prototype, "list_available_models", call)
    assert prototype.main(["--list-models"]) == 1
    assert "private URL" not in capsys.readouterr().err
