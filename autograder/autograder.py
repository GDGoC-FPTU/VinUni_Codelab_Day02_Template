"""
Autograder — Phase 4 Vinmec Demo
Checks:
  Section A: 4 deliverable files (1.25pt each, max 5.0pt)
  Section B: 5 code criteria for prompt_prototype.py (1.0pt each, max 5.0pt)

Usage:
  python autograder/autograder.py                    # run both sections
  python autograder/autograder.py --section-a        # file checks only
  python autograder/autograder.py --section-b        # code checks only
  python autograder/autograder.py --check-file-1     # individual file check
  python autograder/autograder.py --check-code-1     # individual code check
  python autograder/autograder.py --output-dir <dir> # pass custom output dir to prototype
"""

import os
import sys
import json
import inspect
import subprocess
import importlib.util
import re
import tempfile

# Ensure UTF-8 output on all platforms
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
    except Exception:
        pass


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------

def find_student_file() -> str | None:
    """Locate prompt_prototype.py in common directories."""
    possible_paths = [
        "extras/prompt_prototype.py",
        "starter-code/prompt_prototype.py",
        "prompt_prototype.py",
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None


def get_student_module_or_exit():
    student_file_path = find_student_file()
    if not student_file_path:
        print("[FAIL] Cannot find prompt_prototype.py")
        sys.exit(1)
    try:
        return load_student_module(student_file_path), student_file_path
    except Exception as e:
        print(f"[FAIL] Syntax error or import error in prompt_prototype.py: {e}")
        sys.exit(1)


def check_file_exists(filename_pattern: str, search_dir: str = ".") -> tuple[bool, str | None]:
    """Check if a file exists (supports extension-only patterns like *.pdf)."""
    if not filename_pattern.startswith("*."):
        path = os.path.join(search_dir, filename_pattern)
        return os.path.exists(path), path

    extension = filename_pattern.replace("*", "")
    for file in os.listdir(search_dir):
        if file.lower().endswith(extension.lower()):
            return True, os.path.join(search_dir, file)
    return False, None


def check_workflow_diagram(search_dir: str = ".") -> tuple[bool, str | None]:
    """Check for 04-workflow-diagram in .png/.jpg/.jpeg/.pdf."""
    valid_extensions = [".png", ".jpg", ".jpeg", ".pdf"]
    base_name = "04-workflow-diagram"

    for ext in valid_extensions:
        filename = f"{base_name}{ext}"
        path = os.path.join(search_dir, filename)
        if os.path.exists(path):
            return True, path

    for file in os.listdir(search_dir):
        if file.lower().startswith(base_name.lower()):
            _, ext = os.path.splitext(file)
            if ext.lower() in valid_extensions:
                return True, os.path.join(search_dir, file)

    return False, None


def load_student_module(file_path: str):
    """Dynamically load the student module for inspection."""
    spec = importlib.util.spec_from_file_location("student_code", file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["student_code"] = module
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# Individual check flags (invoked from GitHub Actions)
# ---------------------------------------------------------------------------

def run_autograder():
    print("[SETUP] Autograder Phase 4 — Vinmec Demo\n" + "=" * 60)

    # ------------------------------------------------------------------
    # Individual file checks
    # ------------------------------------------------------------------
    if "--check-file-1" in sys.argv:
        found, path = check_file_exists("01-problem-scan.md")
        if found:
            print(f"[PASS] File 01-problem-scan.md exists at {path}")
            sys.exit(0)
        else:
            print("[FAIL] File 01-problem-scan.md is missing")
            sys.exit(1)

    if "--check-file-2" in sys.argv:
        found, path = check_file_exists("02-deep-dive-report.md")
        if found:
            print(f"[PASS] File 02-deep-dive-report.md exists at {path}")
            sys.exit(0)
        else:
            print("[FAIL] File 02-deep-dive-report.md is missing")
            sys.exit(1)

    if "--check-file-3" in sys.argv:
        found, path = check_file_exists("03-ai-log.md")
        if found:
            print(f"[PASS] File 03-ai-log.md exists at {path}")
            sys.exit(0)
        else:
            print("[FAIL] File 03-ai-log.md is missing")
            sys.exit(1)

    if "--check-file-4" in sys.argv:
        found, path = check_workflow_diagram()
        if found:
            print(f"[PASS] File 04-workflow-diagram (.png/.jpg/.pdf) exists at {path}")
            sys.exit(0)
        else:
            print("[FAIL] File 04-workflow-diagram is missing")
            sys.exit(1)

    # ------------------------------------------------------------------
    # Individual code checks
    # ------------------------------------------------------------------

    # check-code-1: SYSTEM_PROMPT — Vinmec domain + schema + boundary
    if "--check-code-1" in sys.argv:
        student, _ = get_student_module_or_exit()
        sys_prompt = getattr(student, "SYSTEM_PROMPT", "")
        if not sys_prompt or "TODO:" in sys_prompt or "Write your strict" in sys_prompt:
            print("[FAIL] SYSTEM_PROMPT not defined or still has TODO template")
            sys.exit(1)
        # Vinmec-specific keywords
        keywords = [
            "vinmec", "draft_for_review", "answer", "escalate", "blocked",
            "segment_ids", "bác sĩ", "action",
        ]
        matched = [k for k in keywords if k.lower() in sys_prompt.lower()]
        if len(matched) >= 4:
            print(f"[PASS] SYSTEM_PROMPT valid for Vinmec domain. Matched: {matched}")
            sys.exit(0)
        else:
            print(f"[FAIL] SYSTEM_PROMPT missing Vinmec/schema keywords (matched: {matched})")
            sys.exit(1)

    # check-code-2: evaluate_prompt uses Gemini SDK, has mode/case_id params
    if "--check-code-2" in sys.argv:
        student, _ = get_student_module_or_exit()
        eval_fn = getattr(student, "evaluate_prompt", None)
        if not eval_fn:
            print("[FAIL] evaluate_prompt function is missing")
            sys.exit(1)
        fn_source = inspect.getsource(eval_fn)
        if "raise NotImplementedError" in fn_source:
            print("[FAIL] evaluate_prompt is not implemented yet")
            sys.exit(1)
        uses_sdk = "genai" in fn_source or "generativeai" in fn_source
        has_mode = "mode" in fn_source
        has_case_id = "case_id" in fn_source
        if uses_sdk and has_mode and has_case_id:
            print("[PASS] evaluate_prompt uses Gemini SDK and has mode/case_id parameters")
            sys.exit(0)
        else:
            issues = []
            if not uses_sdk:
                issues.append("missing Gemini SDK usage")
            if not has_mode:
                issues.append("missing 'mode' parameter")
            if not has_case_id:
                issues.append("missing 'case_id' parameter")
            print(f"[FAIL] evaluate_prompt issues: {', '.join(issues)}")
            sys.exit(1)

    # check-code-3: ADVERSARIAL_TESTS with 3+ entries (Vinmec adversarial)
    if "--check-code-3" in sys.argv:
        student, _ = get_student_module_or_exit()
        tests = getattr(student, "ADVERSARIAL_TESTS", [])
        if not isinstance(tests, list) or len(tests) < 3:
            print(f"[FAIL] ADVERSARIAL_TESTS must contain at least 3 test cases (found {len(tests)})")
            sys.exit(1)
        for t in tests:
            if not isinstance(t, dict) or "input" not in t or "expected_violation" not in t:
                print("[FAIL] Invalid test case structure — must have 'input' and 'expected_violation'")
                sys.exit(1)
            if not t["input"].strip() or not t["expected_violation"].strip():
                print("[FAIL] Test case fields cannot be empty")
                sys.exit(1)
        print(f"[PASS] ADVERSARIAL_TESTS declared correctly with {len(tests)} test cases")
        sys.exit(0)

    # check-code-4: script runs and produces results.json + doctor_queue.json
    if "--check-code-4" in sys.argv:
        student_file_path = find_student_file()
        if not student_file_path:
            print("[FAIL] Cannot find prompt_prototype.py")
            sys.exit(1)
        with tempfile.TemporaryDirectory() as tmp_out:
            try:
                result = subprocess.run(
                    [sys.executable, student_file_path, "--output-dir", tmp_out],
                    capture_output=True,
                    text=True,
                    timeout=620,  # 10 min suite + buffer
                    encoding="utf-8",
                    errors="ignore",
                )
                results_ok = os.path.exists(os.path.join(tmp_out, "results.json"))
                queue_ok = os.path.exists(os.path.join(tmp_out, "doctor_queue.json"))

                # Mục 4: pass if exit 0 or 1 AND both JSON files written AND all cases responded
                if result.returncode in {0, 1} and results_ok and queue_ok:
                    # Check all 10 cases have a response (not NOT_RUN)
                    with open(os.path.join(tmp_out, "results.json"), encoding="utf-8") as f:
                        report = json.load(f)
                    cases = report.get("cases", [])
                    not_run = [
                        c for c in cases
                        if c.get("model_check") == "NOT_RUN" or c.get("guard_check") == "NOT_RUN"
                    ]
                    if not_run:
                        ids = [c["case_id"] for c in not_run]
                        print(f"[FAIL] check-code-4: Cases not run (likely missing API key): {ids}")
                        sys.exit(1)
                    print(
                        f"[PASS] check-code-4: Script ran (exit {result.returncode}), "
                        "results.json and doctor_queue.json written, all cases responded."
                    )
                    sys.exit(0)
                elif not results_ok or not queue_ok:
                    missing = []
                    if not results_ok:
                        missing.append("results.json")
                    if not queue_ok:
                        missing.append("doctor_queue.json")
                    print(f"[FAIL] check-code-4: Missing output files: {missing}")
                    sys.exit(1)
                else:
                    print(f"[FAIL] check-code-4: Script exit code {result.returncode}\n{result.stderr[:500]}")
                    sys.exit(1)
            except subprocess.TimeoutExpired:
                print("[FAIL] check-code-4: Suite timed out (>10 min)")
                sys.exit(1)
            except Exception as e:
                print(f"[FAIL] check-code-4: Error running script: {e}")
                sys.exit(1)

    # check-code-5: all 7 model checks PASS and all 3 guard checks PASS
    if "--check-code-5" in sys.argv:
        student_file_path = find_student_file()
        if not student_file_path:
            print("[FAIL] Cannot find prompt_prototype.py")
            sys.exit(1)
        with tempfile.TemporaryDirectory() as tmp_out:
            try:
                result = subprocess.run(
                    [sys.executable, student_file_path, "--output-dir", tmp_out],
                    capture_output=True,
                    text=True,
                    timeout=620,
                    encoding="utf-8",
                    errors="ignore",
                )
                results_path = os.path.join(tmp_out, "results.json")
                if not os.path.exists(results_path):
                    print("[FAIL] check-code-5: results.json not found")
                    sys.exit(1)

                with open(results_path, encoding="utf-8") as f:
                    report = json.load(f)

                cases = report.get("cases", [])
                live_cases = [c for c in cases if c.get("model_check") != "NOT_APPLICABLE"]
                guard_cases = [c for c in cases if c.get("guard_check") != "NOT_APPLICABLE"]

                model_all_pass = all(c.get("model_check") == "PASS" for c in live_cases)
                guard_all_pass = all(c.get("guard_check") == "PASS" for c in guard_cases)

                # Queue validation: C04,C05,C07,C08,C09 → pending; C10 → urgent_demo
                queue_path = os.path.join(tmp_out, "doctor_queue.json")
                queue_ok = True
                if os.path.exists(queue_path):
                    with open(queue_path, encoding="utf-8") as f:
                        queue = json.load(f)
                    pending_ids = {e["case_test_id"] for e in queue.get("pending", [])}
                    urgent_ids = {e["case_test_id"] for e in queue.get("urgent_demo", [])}
                    expected_pending = {"C04", "C05", "C07", "C08", "C09"}
                    expected_urgent = {"C10"}
                    queue_ok = (
                        expected_pending.issubset(pending_ids)
                        and expected_urgent.issubset(urgent_ids)
                    )
                else:
                    queue_ok = False

                if model_all_pass and guard_all_pass and queue_ok:
                    model_pass_count = sum(1 for c in live_cases if c.get("model_check") == "PASS")
                    guard_pass_count = sum(1 for c in guard_cases if c.get("guard_check") == "PASS")
                    print(
                        f"[PASS] check-code-5: All {model_pass_count}/7 model checks PASS, "
                        f"{guard_pass_count}/3 guard checks PASS, queue correct."
                    )
                    sys.exit(0)
                else:
                    fail_details = []
                    if not model_all_pass:
                        fails = [c["case_id"] for c in live_cases if c.get("model_check") != "PASS"]
                        fail_details.append(f"Model FAIL: {fails}")
                    if not guard_all_pass:
                        fails = [c["case_id"] for c in guard_cases if c.get("guard_check") != "PASS"]
                        fail_details.append(f"Guard FAIL: {fails}")
                    if not queue_ok:
                        fail_details.append("Queue entries incorrect")
                    print(f"[FAIL] check-code-5: {'; '.join(fail_details)}")
                    sys.exit(1)

            except subprocess.TimeoutExpired:
                print("[FAIL] check-code-5: Suite timed out (>10 min)")
                sys.exit(1)
            except Exception as e:
                print(f"[FAIL] check-code-5: Error: {e}")
                sys.exit(1)

    # ------------------------------------------------------------------
    # Full section runs
    # ------------------------------------------------------------------
    run_a = True
    run_b = True
    if "--section-a" in sys.argv:
        run_a = True
        run_b = False
    elif "--section-b" in sys.argv:
        run_a = False
        run_b = True

    score = 0.0
    total_max_score = 10.0 if (run_a and run_b) else 5.0
    report_lines: list[str] = []
    all_files_exist = True
    all_code_passed = True

    # =========================================================================
    # SECTION A: 4 deliverable file checks (1.25pt each)
    # =========================================================================
    if run_a:
        print("[SECTION A] Kiem tra su ton tai cua 4 file deliverables (Max: 5.0d)")

        required_files = {
            "01-problem-scan.md": {
                "name": "01-problem-scan.md (Scan & Quick Cards)",
                "check_func": lambda: check_file_exists("01-problem-scan.md"),
            },
            "02-deep-dive-report.md": {
                "name": "02-deep-dive-report.md (Deep-Dive Report)",
                "check_func": lambda: check_file_exists("02-deep-dive-report.md"),
            },
            "03-ai-log.md": {
                "name": "03-ai-log.md (AI Log & Reflection)",
                "check_func": lambda: check_file_exists("03-ai-log.md"),
            },
            "04-workflow-diagram": {
                "name": "04-workflow-diagram (.png/.jpg/.pdf)",
                "check_func": check_workflow_diagram,
            },
        }

        points_per_file = 1.25
        for key, info in required_files.items():
            found, path = info["check_func"]()
            if found:
                score += points_per_file
                report_lines.append(
                    f"[PASS] File ton tai: {info['name']} tai '{path}' (+{points_per_file:.2f}d)"
                )
            else:
                all_files_exist = False
                report_lines.append(
                    f"[FAIL] Thieu file: {info['name']} (0.0/{points_per_file:.2f}d)"
                )

    # =========================================================================
    # SECTION B: 5 code criteria for Phase 4 Vinmec prototype (1.0pt each)
    # =========================================================================
    if run_b:
        print("\n[SECTION B] Cham diem ma nguon Phase 4 Vinmec Prototype (Max: 5.0d)")

        student_file_path = find_student_file()
        if not student_file_path:
            all_code_passed = False
            report_lines.append("[FAIL] Khong tim thay file prompt_prototype.py (0.0/5.0d)")
        else:
            student = None
            try:
                student = load_student_module(student_file_path)
            except Exception as e:
                all_code_passed = False
                report_lines.append(
                    f"[FAIL] Loi nap file prompt_prototype.py (Syntax Error): {e} (0.0/5.0d)"
                )

            if student:
                # ----------------------------------------------------------
                # Criterion 1: SYSTEM_PROMPT — Vinmec domain, schema, boundary (1.0pt)
                # ----------------------------------------------------------
                try:
                    sys_prompt = getattr(student, "SYSTEM_PROMPT", "")
                    if not sys_prompt or "TODO:" in sys_prompt or "Write your strict" in sys_prompt:
                        all_code_passed = False
                        report_lines.append(
                            "[FAIL] Code - Tieu chi 1: SYSTEM_PROMPT chua dinh nghia hoac van giu TODO. (0.0/1.0d)"
                        )
                    else:
                        # Vinmec + JSON schema keywords
                        keywords = [
                            "vinmec", "draft_for_review", "answer", "escalate",
                            "blocked", "segment_ids", "action",
                        ]
                        matched = [k for k in keywords if k.lower() in sys_prompt.lower()]
                        if len(matched) >= 4:
                            score += 1.0
                            report_lines.append(
                                f"[PASS] Code - Tieu chi 1: SYSTEM_PROMPT hop le Vinmec. (+1.0d)"
                            )
                        else:
                            all_code_passed = False
                            report_lines.append(
                                f"[FAIL] Code - Tieu chi 1: SYSTEM_PROMPT thieu tu khoa Vinmec/schema (matched: {matched}). (0.0/1.0d)"
                            )
                except Exception as e:
                    all_code_passed = False
                    report_lines.append(
                        f"[FAIL] Code - Tieu chi 1: Loi khi check SYSTEM_PROMPT: {e} (0.0/1.0d)"
                    )

                # ----------------------------------------------------------
                # Criterion 2: evaluate_prompt() uses Gemini SDK + mode + case_id (1.0pt)
                # ----------------------------------------------------------
                try:
                    eval_fn = getattr(student, "evaluate_prompt", None)
                    fn_source = inspect.getsource(eval_fn) if eval_fn else ""

                    if not eval_fn or "raise NotImplementedError" in fn_source:
                        all_code_passed = False
                        report_lines.append(
                            "[FAIL] Code - Tieu chi 2: Ham evaluate_prompt() chua hoan thien. (0.0/1.0d)"
                        )
                    else:
                        uses_sdk = "genai" in fn_source or "generativeai" in fn_source
                        has_mode = "mode" in fn_source
                        has_case_id = "case_id" in fn_source
                        if uses_sdk and has_mode and has_case_id:
                            score += 1.0
                            report_lines.append(
                                "[PASS] Code - Tieu chi 2: evaluate_prompt() su dung Gemini SDK, co mode va case_id. (+1.0d)"
                            )
                        else:
                            all_code_passed = False
                            issues = []
                            if not uses_sdk:
                                issues.append("thieu Gemini SDK")
                            if not has_mode:
                                issues.append("thieu mode")
                            if not has_case_id:
                                issues.append("thieu case_id")
                            report_lines.append(
                                f"[FAIL] Code - Tieu chi 2: {', '.join(issues)}. (0.0/1.0d)"
                            )
                except Exception as e:
                    all_code_passed = False
                    report_lines.append(
                        f"[FAIL] Code - Tieu chi 2: Loi khi check evaluate_prompt(): {e} (0.0/1.0d)"
                    )

                # ----------------------------------------------------------
                # Criterion 3: ADVERSARIAL_TESTS with >=3 Vinmec cases (1.0pt)
                # ----------------------------------------------------------
                try:
                    tests = getattr(student, "ADVERSARIAL_TESTS", [])
                    if not isinstance(tests, list) or len(tests) < 3:
                        all_code_passed = False
                        report_lines.append(
                            f"[FAIL] Code - Tieu chi 3: ADVERSARIAL_TESTS phai co >= 3 test cases (tim thay {len(tests)}). (0.0/1.0d)"
                        )
                    else:
                        valid_structure = True
                        for t in tests:
                            if not isinstance(t, dict) or "input" not in t or "expected_violation" not in t:
                                valid_structure = False
                            elif not t["input"].strip() or not t["expected_violation"].strip():
                                valid_structure = False

                        if valid_structure:
                            score += 1.0
                            report_lines.append(
                                f"[PASS] Code - Tieu chi 3: ADVERSARIAL_TESTS co {len(tests)} cases hop le. (+1.0d)"
                            )
                        else:
                            all_code_passed = False
                            report_lines.append(
                                "[FAIL] Code - Tieu chi 3: Co test cases nhung thieu truong du lieu. (0.0/1.0d)"
                            )
                except Exception as e:
                    all_code_passed = False
                    report_lines.append(
                        f"[FAIL] Code - Tieu chi 3: Loi khi check ADVERSARIAL_TESTS: {e} (0.0/1.0d)"
                    )

                # ----------------------------------------------------------
                # Criterion 4: Script runs; all 10 cases respond; outputs written (1.0pt)
                # Passes on exit 0 or 1 if 7 live cases responded + 3 guards checked + files saved
                # ----------------------------------------------------------
                process_output = ""
                tmp_out_dir = None
                suite_result = None
                try:
                    import tempfile
                    tmp_out_dir = tempfile.mkdtemp()
                    suite_result = subprocess.run(
                        [sys.executable, student_file_path, "--output-dir", tmp_out_dir],
                        capture_output=True,
                        text=True,
                        timeout=620,
                        encoding="utf-8",
                        errors="ignore",
                    )
                    process_output = suite_result.stdout + "\n" + suite_result.stderr

                    results_path = os.path.join(tmp_out_dir, "results.json")
                    queue_path = os.path.join(tmp_out_dir, "doctor_queue.json")
                    results_ok = os.path.exists(results_path)
                    queue_ok = os.path.exists(queue_path)

                    if suite_result.returncode in {0, 1} and results_ok and queue_ok:
                        with open(results_path, encoding="utf-8") as f:
                            run_report = json.load(f)
                        cases = run_report.get("cases", [])
                        not_run = [
                            c for c in cases
                            if c.get("model_check") == "NOT_RUN" or c.get("guard_check") == "NOT_RUN"
                        ]
                        if not_run:
                            ids = [c["case_id"] for c in not_run]
                            all_code_passed = False
                            report_lines.append(
                                f"[FAIL] Code - Tieu chi 4: Cac ca chua chay (thieu key?): {ids}. (0.0/1.0d)"
                            )
                        else:
                            score += 1.0
                            report_lines.append(
                                f"[PASS] Code - Tieu chi 4: Script chay (exit {suite_result.returncode}), "
                                "ca 10 ca da phan hoi, files da ghi. (+1.0d)"
                            )
                    else:
                        all_code_passed = False
                        missing = []
                        if not results_ok:
                            missing.append("results.json")
                        if not queue_ok:
                            missing.append("doctor_queue.json")
                        if missing:
                            report_lines.append(
                                f"[FAIL] Code - Tieu chi 4: Thieu output files: {missing}. (0.0/1.0d)"
                            )
                        else:
                            report_lines.append(
                                f"[FAIL] Code - Tieu chi 4: Script exit code {suite_result.returncode}. (0.0/1.0d)"
                            )
                except subprocess.TimeoutExpired:
                    all_code_passed = False
                    report_lines.append(
                        "[FAIL] Code - Tieu chi 4: Script bi timeout (>10 min). (0.0/1.0d)"
                    )
                except Exception as e:
                    all_code_passed = False
                    report_lines.append(
                        f"[FAIL] Code - Tieu chi 4: Loi he thong khi thuc thi: {e} (0.0/1.0d)"
                    )

                # ----------------------------------------------------------
                # Criterion 5: All 7 model checks PASS + 3 guard checks PASS + correct queue (1.0pt)
                # ----------------------------------------------------------
                try:
                    if tmp_out_dir is None:
                        all_code_passed = False
                        report_lines.append(
                            "[FAIL] Code - Tieu chi 5: Khong chay duoc suite o tieu chi 4. (0.0/1.0d)"
                        )
                    else:
                        results_path = os.path.join(tmp_out_dir, "results.json")
                        queue_path = os.path.join(tmp_out_dir, "doctor_queue.json")

                        if not os.path.exists(results_path):
                            all_code_passed = False
                            report_lines.append(
                                "[FAIL] Code - Tieu chi 5: Khong tim thay results.json. (0.0/1.0d)"
                            )
                        else:
                            with open(results_path, encoding="utf-8") as f:
                                run_report = json.load(f)
                            cases = run_report.get("cases", [])

                            live_cases = [c for c in cases if c.get("model_check") != "NOT_APPLICABLE"]
                            guard_cases = [c for c in cases if c.get("guard_check") != "NOT_APPLICABLE"]

                            model_all_pass = all(c.get("model_check") == "PASS" for c in live_cases)
                            guard_all_pass = all(c.get("guard_check") == "PASS" for c in guard_cases)

                            # Queue correctness
                            queue_correct = False
                            if os.path.exists(queue_path):
                                with open(queue_path, encoding="utf-8") as f:
                                    queue_data = json.load(f)
                                pending_ids = {e.get("case_test_id") for e in queue_data.get("pending", [])}
                                urgent_ids = {e.get("case_test_id") for e in queue_data.get("urgent_demo", [])}
                                expected_pending = {"C04", "C05", "C07", "C08", "C09"}
                                expected_urgent = {"C10"}
                                queue_correct = (
                                    expected_pending.issubset(pending_ids)
                                    and expected_urgent.issubset(urgent_ids)
                                )

                            if model_all_pass and guard_all_pass and queue_correct:
                                score += 1.0
                                m_pass = sum(1 for c in live_cases if c.get("model_check") == "PASS")
                                g_pass = sum(1 for c in guard_cases if c.get("guard_check") == "PASS")
                                report_lines.append(
                                    f"[PASS] Code - Tieu chi 5: {m_pass}/7 model PASS, "
                                    f"{g_pass}/3 guard PASS, queue dung. (+1.0d)"
                                )
                            else:
                                all_code_passed = False
                                fail_details = []
                                if not model_all_pass:
                                    fails = [c["case_id"] for c in live_cases if c.get("model_check") != "PASS"]
                                    fail_details.append(f"Model FAIL: {fails}")
                                if not guard_all_pass:
                                    fails = [c["case_id"] for c in guard_cases if c.get("guard_check") != "PASS"]
                                    fail_details.append(f"Guard FAIL: {fails}")
                                if not queue_correct:
                                    fail_details.append("Queue entries sai")
                                report_lines.append(
                                    f"[FAIL] Code - Tieu chi 5: {'; '.join(fail_details)}. (0.0/1.0d)"
                                )
                except Exception as e:
                    all_code_passed = False
                    report_lines.append(
                        f"[FAIL] Code - Tieu chi 5: Loi khi doc ket qua: {e} (0.0/1.0d)"
                    )
                finally:
                    # Clean up temp dir
                    if tmp_out_dir and os.path.isdir(tmp_out_dir):
                        import shutil
                        try:
                            shutil.rmtree(tmp_out_dir)
                        except Exception:
                            pass

    # =========================================================================
    # Print report and exit
    # =========================================================================
    print("\n" + "=" * 60)
    print("[REPORT] KET QUA CHAM DIEM:")
    for line in report_lines:
        print(line)

    print("=" * 60)
    print(f"[SCORE] TONG DIEM: {score:.2f} / {total_max_score:.2f}")

    should_fail = False
    if run_a and not all_files_exist:
        should_fail = True
    if run_b and not all_code_passed:
        should_fail = True

    if should_fail:
        print("[WARNING] Co hang muc bi thieu hoac kiem thu khong dat.")
        sys.exit(1)
    else:
        print("[SUCCESS] Tat ca cac check duoc chon deu thanh cong!")
        sys.exit(0)


if __name__ == "__main__":
    run_autograder()
