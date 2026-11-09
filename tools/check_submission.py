"""Run submission checks without exposing credentials or changing the grader.

Default: offline checks only. --live additionally runs the original full grader
inheriting credentials from the user's terminal. It makes real Gemini calls.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def run_checks(live: bool = False) -> dict:
    checks = [
        ("offline_tests", ["-m", "pytest", "-q", "tests"]),
        ("deliverables", ["autograder/autograder.py", "--section-a"]),
        ("system_prompt", ["autograder/autograder.py", "--check-code-1"]),
        ("sdk_wiring_static", ["autograder/autograder.py", "--check-code-2"]),
        ("adversarial_cases", ["autograder/autograder.py", "--check-code-3"]),
    ]
    report = {"live_requested": live, "live_autograder": "not_run", "checks": []}
    if live:
        # Inspect presence only; never include environment values in reports.
        if os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"):
            checks.append(("full_autograder_live", ["autograder/autograder.py"]))
        else:
            report["live_autograder"] = "not_run_no_key"
            print("Chưa chạy API thật: thiếu khóa trong terminal hiện tại.", file=sys.stderr)
    for name, arguments in checks:
        print(f"\n[CHECK] {name}", flush=True)
        started = time.perf_counter()
        try:
            result = subprocess.run([sys.executable, *arguments], cwd=ROOT, timeout=90)
            returncode = result.returncode
        except subprocess.TimeoutExpired:
            returncode = 124
            print("Kiểm tra hết thời gian; chưa đạt.", file=sys.stderr)
        except OSError:
            returncode = 1
            print("Không khởi chạy được kiểm tra; chưa đạt.", file=sys.stderr)
        report["checks"].append({
            "name": name,
            "returncode": returncode,
            "elapsed_seconds": round(time.perf_counter() - started, 3),
        })
        if name == "full_autograder_live":
            report["live_autograder"] = "passed" if returncode == 0 else "failed"
    report["passed"] = (
        all(check["returncode"] == 0 for check in report["checks"])
        and (not live or report["live_autograder"] == "passed")
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="Gọi Gemini qua autograder thật; cần khóa trong cùng terminal")
    args = parser.parse_args()
    report = run_checks(live=args.live)
    output = ROOT / "artifacts" / "submission-check.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nBáo cáo: {output}")
    print("Đạt các kiểm tra đã yêu cầu." if report["passed"] else "Còn kiểm tra chưa đạt; xem kết quả phía trên.")
    if not args.live:
        print("Chưa chạy autograder gọi API thật. Dùng --live trong terminal đã export khóa.")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
