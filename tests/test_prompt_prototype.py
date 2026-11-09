"""Kiểm tra code bằng dữ liệu giả lập, không gọi hoặc chấm chất lượng LLM thật."""

import importlib.util
import json
from pathlib import Path

import pytest
import httpx

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("prototype", ROOT / "starter-code/prompt_prototype.py")
prototype = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prototype)


def encode(payload):
    return prototype.DRAFT_TAG + "\n" + json.dumps(payload)


@pytest.mark.parametrize("case", prototype.ADVERSARIAL_TESTS + prototype.NORMAL_TESTS)
def test_expected_labels_obey_contract(case):
    assert prototype.validate_draft(encode(case["expected"])) == case["expected"]


@pytest.mark.parametrize("output", [
    '{"topic":"VE_SINH","priority":"NORMAL","action":"suggest_topic"}',
    ' [DRAFT_ONLY]\n{}',
    '[DRAFT_ONLY] {}',
    '[DRAFT_ONLY]\n```json\n{}\n```',
    '[DRAFT_ONLY]\n[]',
    '[DRAFT_ONLY]\nnull',
    '[DRAFT_ONLY]\n{}',
    '[DRAFT_ONLY]\n{"topic":"VE_SINH","priority":"NORMAL","action":"suggest_topic"} extra',
    '[DRAFT_ONLY]\n{"topic":"KY_THUAT","topic":"VE_SINH","priority":"NORMAL","action":"suggest_topic"}',
    encode({"topic": "VE_SINH", "priority": "NORMAL", "action": "suggest_topic", "message": "Sent"}),
    encode({"topic": [], "priority": "NORMAL", "action": "suggest_topic"}),
    encode({"topic": "OTHER", "priority": "NORMAL", "action": "suggest_topic"}),
    encode({"topic": "KY_THUAT", "priority": "URGENT", "action": "suggest_topic"}),
    encode({"topic": "CHUA_RO", "priority": "NORMAL", "action": "suggest_topic"}),
    encode({"topic": "KY_THUAT", "priority": "UNKNOWN", "action": "human_review"}),
    encode({"topic": "VE_SINH", "priority": "NORMAL", "action": "human_review"}),
])
def test_invalid_output_is_rejected(output):
    with pytest.raises(ValueError):
        prototype.validate_draft(output)


def test_unclear_urgent_case_requires_human():
    payload = {"topic": "CHUA_RO", "priority": "URGENT", "action": "human_review"}
    assert prototype.validate_draft(encode(payload)) == payload


def test_runner_preserves_output_and_distinguishes_failures(monkeypatch):
    cases = prototype.NORMAL_TESTS[:3]
    valid = encode(cases[0]["expected"])
    wrong_label = encode(cases[0]["expected"])
    answers = iter([valid, wrong_label, RuntimeError("API unavailable")])

    def fake_call(_):
        answer = next(answers)
        if isinstance(answer, Exception):
            raise answer
        return answer

    monkeypatch.setattr(prototype, "evaluate_prompt", fake_call)
    report = prototype.run_suite(cases)
    assert report["summary"] == {"total": 3, "passed": 1, "failed": 1, "errors": 1}
    assert report["results"][0]["raw_output"] == valid
    assert report["results"][1]["raw_output"] == wrong_label
    assert report["results"][2]["status"] == "ERROR"
    assert "raw_output" not in report["results"][2]


def test_missing_key_fails_without_network(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="OPENROUTER_API_KEY"):
        prototype.evaluate_prompt("test")


@pytest.mark.parametrize("key", ["KEY_OPENROUTER_CUA_BAN", "contains spaces", "khóa", "line\nbreak"])
def test_invalid_key_is_rejected_before_network(monkeypatch, key):
    monkeypatch.setenv("OPENROUTER_API_KEY", key)
    with pytest.raises(RuntimeError):
        prototype.evaluate_prompt("test")


def test_errors_redact_configured_key(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "secret_test_key")
    assert "secret_test_key" not in prototype.format_call_error(RuntimeError("secret_test_key rejected"))
    assert "[REDACTED]" in prototype.format_call_error(RuntimeError("secret_test_key rejected"))


def test_cli_writes_failed_report_and_returns_nonzero(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(prototype, "evaluate_prompt", lambda _: "malformed output")
    target = tmp_path / "evidence" / "results.json"
    assert prototype.main(["--report", str(target)]) == 1
    report = json.loads(target.read_text(encoding="utf-8"))
    assert report["summary"]["failed"] == 3
    assert report["results"][0]["raw_output"] == "malformed output"
    assert capsys.readouterr().out.count("Failed") == 3


def test_cli_all_suite_success_with_mock(monkeypatch, tmp_path, capsys):
    cases = prototype.ADVERSARIAL_TESTS + prototype.NORMAL_TESTS
    outputs = {case["input"]: encode(case["expected"]) for case in cases}
    monkeypatch.setattr(prototype, "evaluate_prompt", outputs.__getitem__)
    target = tmp_path / "mock-results.json"
    assert prototype.main(["--suite", "all", "--report", str(target)]) == 0
    assert json.loads(target.read_text(encoding="utf-8"))["summary"]["passed"] == 9
    assert capsys.readouterr().out.count("Passed") == 9


@pytest.fixture
def mock_openrouter(monkeypatch):
    """Exercise real HTTP serialization/parsing without network requests."""
    real_client = httpx.Client
    monkeypatch.setenv("OPENROUTER_API_KEY", "test_openrouter_key")

    def install(handler):
        def client_factory(**kwargs):
            assert kwargs["timeout"] == 30.0
            assert kwargs["follow_redirects"] is False
            return real_client(transport=httpx.MockTransport(handler), **kwargs)
        monkeypatch.setattr(httpx, "Client", client_factory)
    return install


def test_openrouter_request_and_raw_response(mock_openrouter):
    raw = ' [DRAFT_ONLY]\n{"topic":"VE_SINH","priority":"NORMAL","action":"suggest_topic"}'

    def handler(request):
        assert request.method == "POST"
        assert str(request.url) == "https://openrouter.ai/api/v1/chat/completions"
        assert request.headers["Authorization"] == "Bearer test_openrouter_key"
        body = json.loads(request.content)
        assert body["model"] == prototype.OPENROUTER_MODEL
        assert body["messages"] == [
            {"role": "system", "content": prototype.SYSTEM_PROMPT},
            {"role": "user", "content": "Phản ánh có dấu tiếng Việt"},
        ]
        assert body["max_tokens"] == 2048
        assert body["stream"] is False
        return httpx.Response(200, json={"choices": [{"message": {"content": raw}}]})

    mock_openrouter(handler)
    # Preserve leading whitespace so the validator can catch the bad marker.
    assert prototype.evaluate_prompt("Phản ánh có dấu tiếng Việt") == raw


@pytest.mark.parametrize("status", [401, 402, 403, 404, 429, 502, 503, 200])
def test_openrouter_error_body_is_not_a_model_answer(mock_openrouter, status):
    mock_openrouter(lambda _: httpx.Response(status, json={
        "error": {"code": 402, "message": "Rejected test_openrouter_key"},
    }))
    with pytest.raises(RuntimeError) as error:
        prototype.evaluate_prompt("test")
    assert f"HTTP {status}" in str(error.value)
    assert "test_openrouter_key" not in str(error.value)
    assert "[REDACTED]" in str(error.value)


@pytest.mark.parametrize("payload", [
    [], {}, {"choices": []}, {"choices": None},
    {"choices": [{"message": {"content": None}}]},
    {"choices": [{"message": {"content": " "}}]},
    {"choices": [{"message": {"content": ["unexpected"]}}]},
])
def test_openrouter_missing_text_is_error(mock_openrouter, payload):
    mock_openrouter(lambda _: httpx.Response(200, json=payload))
    with pytest.raises(RuntimeError):
        prototype.evaluate_prompt("test")


def test_openrouter_non_json_response(mock_openrouter):
    mock_openrouter(lambda _: httpx.Response(502, text="<html>bad gateway</html>"))
    with pytest.raises(RuntimeError, match="HTTP 502"):
        prototype.evaluate_prompt("test")


@pytest.mark.parametrize("exception", [httpx.ReadTimeout, httpx.ConnectError])
def test_openrouter_network_errors_do_not_retry(mock_openrouter, exception):
    calls = []

    def handler(request):
        calls.append(request)
        raise exception("test_openrouter_key", request=request)

    mock_openrouter(handler)
    with pytest.raises(RuntimeError) as error:
        prototype.evaluate_prompt("test")
    assert "test_openrouter_key" not in str(error.value)
    assert len(calls) == 1


def test_old_groq_key_is_not_used(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "old_test_key")
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="OPENROUTER_API_KEY"):
        prototype.evaluate_prompt("test")
