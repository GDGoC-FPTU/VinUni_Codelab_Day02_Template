import os
import sys
import inspect
import subprocess
import importlib.util
import re

# Đảm bảo mã hóa UTF-8 cho stdout trên mọi nền tảng
if sys.stdout.encoding != 'utf-8':
    try:
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    except Exception:
        pass

def find_student_file():
    """Tìm đường dẫn file prompt_prototype.py ở các thư mục phổ biến."""
    possible_paths = [
        "extras/prompt_prototype.py",
        "starter-code/prompt_prototype.py",
        "prompt_prototype.py"
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

def check_file_exists(filename_pattern, search_dir="."):
    """Kiểm tra sự tồn tại của một file (hỗ trợ kiểm tra phần mở rộng)."""
    if not filename_pattern.startswith("*."):
        path = os.path.join(search_dir, filename_pattern)
        return os.path.exists(path), path

    extension = filename_pattern.replace("*", "")
    for file in os.listdir(search_dir):
        if file.lower().endswith(extension.lower()):
            return True, os.path.join(search_dir, file)
    return False, None

def check_workflow_diagram(search_dir="."):
    """Kiểm tra file sơ đồ với nhiều định dạng ảnh/tài liệu khác nhau."""
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

def load_student_module(file_path):
    """Nạp động module python để kiểm tra các biến và hàm."""
    spec = importlib.util.spec_from_file_location("student_code", file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["student_code"] = module
    spec.loader.exec_module(module)
    return module

def run_autograder():
    print("[SETUP] Bat dau cham diem Group Assignment tren GitHub Classroom\n" + "="*60)
    
    # Individual file checks
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

    # Individual code checks
    if "--check-code-1" in sys.argv:
        student, _ = get_student_module_or_exit()
        sys_prompt = getattr(student, "SYSTEM_PROMPT", "")
        if not sys_prompt or "TODO:" in sys_prompt or "Write your strict" in sys_prompt:
            print("[FAIL] SYSTEM_PROMPT not defined or still has TODO template")
            sys.exit(1)
        keywords = ["draft_only", "5%", "dispatch_mobile_charger"]
        matched_keys = [k for k in keywords if k in sys_prompt.lower() or k.replace("_", " ") in sys_prompt.lower()]
        if len(matched_keys) >= 2:
            print(f"[PASS] SYSTEM_PROMPT is valid. Matched: {matched_keys}")
            sys.exit(0)
        else:
            print("[FAIL] SYSTEM_PROMPT is missing core safety guidelines")
            sys.exit(1)

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
        if uses_sdk:
            print("[PASS] evaluate_prompt uses Gemini SDK")
            sys.exit(0)
        else:
            print("[FAIL] evaluate_prompt does not use Gemini SDK")
            sys.exit(1)

    if "--check-code-3" in sys.argv:
        student, _ = get_student_module_or_exit()
        tests = getattr(student, "ADVERSARIAL_TESTS", [])
        if not isinstance(tests, list) or len(tests) < 2:
            print("[FAIL] ADVERSARIAL_TESTS must contain at least 2 test cases")
            sys.exit(1)
        for t in tests:
            if not isinstance(t, dict) or "input" not in t or "expected_violation" not in t:
                print("[FAIL] Invalid test case structure")
                sys.exit(1)
            if not t["input"].strip() or not t["expected_violation"].strip():
                print("[FAIL] Test case fields cannot be empty")
                sys.exit(1)
        print("[PASS] ADVERSARIAL_TESTS declared correctly with 2 or more test cases")
        sys.exit(0)

    if "--check-code-4" in sys.argv:
        student_file_path = find_student_file()
        if not student_file_path:
            print("[FAIL] Cannot find prompt_prototype.py")
            sys.exit(1)
        try:
            result = subprocess.run(
                [sys.executable, student_file_path], 
                capture_output=True, 
                text=True, 
                timeout=30,
                encoding='utf-8',
                errors='ignore'
            )
            if result.returncode == 0:
                print("[PASS] Script ran successfully with exit code 0")
                sys.exit(0)
            else:
                print(f"[FAIL] Script failed with exit code {result.returncode}\n{result.stderr}")
                sys.exit(1)
        except Exception as e:
            print(f"[FAIL] Error running script: {e}")
            sys.exit(1)

    if "--check-code-5" in sys.argv:
        student_file_path = find_student_file()
        if not student_file_path:
            print("[FAIL] Cannot find prompt_prototype.py")
            sys.exit(1)
        try:
            result = subprocess.run(
                [sys.executable, student_file_path], 
                capture_output=True, 
                text=True, 
                timeout=30,
                encoding='utf-8',
                errors='ignore'
            )
            output = result.stdout + "\n" + result.stderr
            passed_checks = len(re.findall(r"Passed", output, re.IGNORECASE))
            failed_checks = len(re.findall(r"Failed", output, re.IGNORECASE))
            if passed_checks >= 2 and failed_checks == 0:
                print(f"[PASS] All boundary verification checks passed (Passed: {passed_checks}, Failed: 0)")
                sys.exit(0)
            elif failed_checks > 0:
                print(f"[FAIL] Some boundary checks failed: {failed_checks} violations found")
                sys.exit(1)
            else:
                print("[FAIL] No valid verification output found (did not see 'Passed' tags)")
                sys.exit(1)
        except Exception as e:
            print(f"[FAIL] Error running script: {e}")
            sys.exit(1)

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
    report = []
    all_files_exist = True
    all_code_passed = True

    # =========================================================================
    # PHẦN A: KIỂM TRA SỰ TỒN TẠI CỦA 4 FILE NỘP BÀI (Tối đa 5.0đ - 1.25đ/file)
    # =========================================================================
    if run_a:
        print("[SECTION A] Kiem tra su ton tai cua 4 file deliverables (Max: 5.0d)")
        
        required_files = {
            "01-problem-scan.md": {
                "name": "01-problem-scan.md (Scan & Quick Cards)",
                "check_func": lambda: check_file_exists("01-problem-scan.md")
            },
            "02-deep-dive-report.md": {
                "name": "02-deep-dive-report.md (Deep-Dive Report)",
                "check_func": lambda: check_file_exists("02-deep-dive-report.md")
            },
            "03-ai-log.md": {
                "name": "03-ai-log.md (AI Log & Reflection)",
                "check_func": lambda: check_file_exists("03-ai-log.md")
            },
            "04-workflow-diagram": {
                "name": "04-workflow-diagram (.png/.jpg/.pdf)",
                "check_func": check_workflow_diagram
            }
        }
        
        points_per_file = 1.25
        for key, info in required_files.items():
            found, path = info["check_func"]()
            if found:
                score += points_per_file
                report.append(f"[PASS] File ton tai: {info['name']} tai '{path}' (+{points_per_file:.2f}d)")
            else:
                all_files_exist = False
                report.append(f"[FAIL] Thieu file: {info['name']} (0.0/{points_per_file:.2f}d)")
            
    # =========================================================================
    # PHẦN B: KIỂM TRA MÃ NGUỒN PROMPT PROTOTYPE (Tối đa 5.0đ - 1.0đ/tiêu chí)
    # =========================================================================
    if run_b:
        print("\n[SECTION B] Cham diem ma nguon Prompt Prototype (Max: 5.0d)")
        
        student_file_path = find_student_file()
        if not student_file_path:
            all_code_passed = False
            report.append("[FAIL] Khong tim thay file prompt_prototype.py de cham ma nguon (0.0/5.0d)")
        else:
            # Nạp module của học viên
            student = None
            try:
                student = load_student_module(student_file_path)
            except Exception as e:
                all_code_passed = False
                report.append(f"[FAIL] Loi nap file prompt_prototype.py (Syntax Error): {e} (0.0/5.0d)")
                
            if student:
                # 1. Kiểm tra SYSTEM_PROMPT (1.0đ)
                try:
                    sys_prompt = getattr(student, "SYSTEM_PROMPT", "")
                    if not sys_prompt or "TODO:" in sys_prompt or "Write your strict" in sys_prompt:
                        all_code_passed = False
                        report.append("[FAIL] Code - Tieu chi 1: SYSTEM_PROMPT chua duoc dinh nghia hoac van giu nguyen TODO mau. (0.0/1.0d)")
                    else:
                        keywords = ["draft_only", "5%", "dispatch_mobile_charger"]
                        matched_keys = [k for k in keywords if k in sys_prompt.lower() or k.replace("_", " ") in sys_prompt.lower()]
                        if len(matched_keys) >= 2:
                            score += 1.0
                            report.append("[PASS] Code - Tieu chi 1: SYSTEM_PROMPT hop le va co chi thi ranh gioi. (+1.0d)")
                        else:
                            all_code_passed = False
                            score += 0.5
                            report.append("[WARN] Code - Tieu chi 1: SYSTEM_PROMPT co thay doi nhung thieu cac quy tac ranh gioi cot loi. (+0.5/1.0d)")
                except Exception as e:
                    all_code_passed = False
                    report.append(f"[FAIL] Code - Tieu chi 1: Loi khi check SYSTEM_PROMPT: {e} (0.0/1.0d)")

                # 2. Kiểm tra evaluate_prompt() và Gemini SDK (1.0đ)
                try:
                    eval_fn = getattr(student, "evaluate_prompt", None)
                    fn_source = inspect.getsource(eval_fn) if eval_fn else ""
                    
                    if not eval_fn or "raise NotImplementedError" in fn_source:
                        all_code_passed = False
                        report.append("[FAIL] Code - Tieu chi 2: Ham evaluate_prompt() chua duoc hoan thien. (0.0/1.0d)")
                    else:
                        uses_sdk = "genai" in fn_source or "generativeai" in fn_source
                        if uses_sdk:
                            score += 1.0
                            report.append("[PASS] Code - Tieu chi 2: Ham evaluate_prompt() su dung Gemini SDK chinh xac. (+1.0d)")
                        else:
                            all_code_passed = False
                            score += 0.5
                            report.append("[WARN] Code - Tieu chi 2: Ham duoc viet nhung khong su dung thu vien Gemini SDK. (+0.5/1.0d)")
                except Exception as e:
                    all_code_passed = False
                    report.append(f"[FAIL] Code - Tieu chi 2: Loi khi check evaluate_prompt(): {e} (0.0/1.0d)")

                # 3. Kiểm tra định nghĩa Adversarial tests (1.0đ)
                try:
                    tests = getattr(student, "ADVERSARIAL_TESTS", [])
                    if not isinstance(tests, list) or len(tests) < 2:
                        all_code_passed = False
                        report.append(f"[FAIL] Code - Tieu chi 3: ADVERSARIAL_TESTS phai co >= 2 test cases. (0.0/1.0d)")
                    else:
                        valid_structure = True
                        for t in tests:
                            if not isinstance(t, dict) or "input" not in t or "expected_violation" not in t:
                                valid_structure = False
                            elif not t["input"].strip() or not t["expected_violation"].strip():
                                valid_structure = False
                        
                        if valid_structure:
                            score += 1.0
                            report.append("[PASS] Code - Tieu chi 3: Da khai bao it nhat 2 Adversarial test cases hop le. (+1.0d)")
                        else:
                            all_code_passed = False
                            score += 0.5
                            report.append("[WARN] Code - Tieu chi 3: Co test cases nhung thieu truong du lieu. (+0.5/1.0d)")
                except Exception as e:
                    all_code_passed = False
                    report.append(f"[FAIL] Code - Tieu chi 3: Loi khi check ADVERSARIAL_TESTS: {e} (0.0/1.0d)")

                # 4. Kiểm tra khả năng thực thi của script (1.0đ)
                process_output = ""
                try:
                    result = subprocess.run(
                        [sys.executable, student_file_path], 
                        capture_output=True, 
                        text=True, 
                        timeout=30,
                        encoding='utf-8',
                        errors='ignore'
                    )
                    process_output = result.stdout + "\n" + result.stderr
                    
                    if result.returncode == 0:
                        score += 1.0
                        report.append("[PASS] Code - Tieu chi 4: Script chay thanh cong (code 0, khong crash). (+1.0d)")
                    else:
                        all_code_passed = False
                        report.append(f"[FAIL] Code - Tieu chi 4: Script gap loi khi chay (Exit code {result.returncode}). (0.0/1.0d)")
                except subprocess.TimeoutExpired:
                    all_code_passed = False
                    report.append("[FAIL] Code - Tieu chi 4: Script bi timeout (>30s). (0.0/1.0d)")
                except Exception as e:
                    all_code_passed = False
                    report.append(f"[FAIL] Code - Tieu chi 4: Loi he thong khi thuc thi script: {e} (0.0/1.0d)")

                # 5. Kiểm tra kết quả Assertions bảo vệ ranh giới (1.0đ)
                if process_output:
                    passed_checks = len(re.findall(r"Passed", process_output, re.IGNORECASE))
                    failed_checks = len(re.findall(r"Failed", process_output, re.IGNORECASE))
                    
                    if passed_checks >= 2 and failed_checks == 0:
                        score += 1.0
                        report.append(f"[PASS] Code - Tieu chi 5: Vot qua toan bo assertion test ve ranh gioi. (+1.0d)")
                    elif failed_checks > 0:
                        all_code_passed = False
                        report.append(f"[FAIL] Code - Tieu chi 5: Co quy tac ranh gioi bi vi pham (Failed: {failed_checks}). (0.0/1.0d)")
                    else:
                        all_code_passed = False
                        report.append("[WARN] Code - Tieu chi 5: Khong tim thay ket qua kiem thu tuong thich. (0.0/1.0d)")
                else:
                    all_code_passed = False
                    report.append("[FAIL] Code - Tieu chi 5: Khong the check assertion vi script khong chay duoc. (0.0/1.0d)")

    # =========================================================================
    # IN KẾT QUẢ VÀ THIẾT LẬP EXIT CODE
    # =========================================================================
    print("\n" + "="*60)
    print("[REPORT] KET QUA CHAM DIEM TONG HOP CHO CA NHOM:")
    for line in report:
        print(line)
        
    print("="*60)
    print(f"[SCORE] TONG DIEM NHOM: {score:.2f} / {total_max_score:.2f}")
    
    # Thoát với mã lỗi 1 nếu thiếu file hoặc test code bị lỗi trong phần được chạy
    should_fail = False
    if run_a and not all_files_exist:
        should_fail = True
    if run_b and not all_code_passed:
        should_fail = True

    if should_fail:
        print("[WARNING] Co file bi thieu hoac kiem thu code khong dat. Vui loi kiem tra lai log.")
        sys.exit(1)
    else:
        print("[SUCCESS] Tat ca cac check duoc chon deu thanh cong!")
        sys.exit(0)

if __name__ == "__main__":
    run_autograder()
