"""Verify the offline/live boundary with synthetic subprocess results."""
import importlib.util
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock

PATH = Path(__file__).resolve().parents[1] / "tools" / "check_submission.py"
spec = importlib.util.spec_from_file_location("submission_checks", PATH)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def test_default_never_calls_live_grader_even_if_key_exists(monkeypatch):
    secret = "synthetic-offline-test-key"
    monkeypatch.setenv("GEMINI_API_KEY", secret)
    call = MagicMock(return_value=SimpleNamespace(returncode=0))
    monkeypatch.setattr(checker.subprocess, "run", call)
    report = checker.run_checks()
    assert report["passed"] is True
    assert report["live_autograder"] == "not_run"
    assert all(len(args.args[0]) > 2 for args in call.call_args_list)
    assert secret not in str(report)


def test_requested_live_without_key_cannot_claim_pass(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    monkeypatch.setattr(checker.subprocess, "run", MagicMock(return_value=SimpleNamespace(returncode=0)))
    report = checker.run_checks(live=True)
    assert report["passed"] is False
    assert report["live_autograder"] == "not_run_no_key"


def test_live_grader_failure_is_preserved(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "synthetic-offline-test-key")

    def fake_run(command, **kwargs):
        is_live = command == [checker.sys.executable, "autograder/autograder.py"]
        return SimpleNamespace(returncode=1 if is_live else 0)

    monkeypatch.setattr(checker.subprocess, "run", fake_run)
    report = checker.run_checks(live=True)
    assert report["passed"] is False
    assert report["live_autograder"] == "failed"
