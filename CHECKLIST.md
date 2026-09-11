# Checklist Lab 02 — AI Product Scoping

> Dùng checklist này để theo dõi phần việc cá nhân và nhóm. Đề tài nhóm hiện tại: **Vinmec EMR Audit Assistant** — hệ thống kiểm tra và hỗ trợ sửa lỗi hồ sơ bệnh án điện tử trước khi chốt.

## 1. Việc cá nhân — bắt buộc cho từng thành viên

### A. Chuẩn bị Git và môi trường

- [ ] Đã được thêm quyền Contributor vào repository nhóm.
- [ ] Đã clone repo và tạo branch cá nhân theo tên/mã sinh viên: `git checkout -b <ten-cua-ban>`.
- [ ] Đã kích hoạt `.venv` và cài dependencies cần thiết.
- [ ] Đã thiết lập `GEMINI_API_KEY` hoặc `GOOGLE_API_KEY` trong biến môi trường; **không** ghi API key vào code hoặc commit lên Git.

### B. Báo cáo cá nhân

- [ ] Kiểm tra [01-problem-scan.md](01-problem-scan.md): có ít nhất **5** bài toán thuộc các công ty thành viên Vingroup.
- [ ] Kiểm tra `01-problem-scan.md`: có đủ **3 Quick Problem Cards**, mỗi card nêu actor, workflow 3–5 bước, bottleneck/thời gian, AI solution, metric có số và kiến trúc (Rule/LLM/Agent).
- [ ] Điều chỉnh các ý tưởng/ước lượng để phản ánh đóng góp cá nhân; không ghi số liệu chưa có nguồn như fact.
- [ ] Hoàn thiện [03-ai-log.md](03-ai-log.md): nêu AI đã giúp gì, ít nhất một lỗi/hallucination hoặc rủi ro, và cách bạn sửa prompt/ranh giới.

### C. Prompt prototype — điểm cá nhân

- [ ] Hoàn thiện `starter-code/prompt_prototype.py` trên **branch cá nhân**.
- [ ] Giữ đúng ranh giới của đề starter: output có `[DRAFT_ONLY]`; pin `<5%` không đề xuất trạm xa quá 5 km; phải `dispatch_mobile_charger`/escalate.
- [ ] Định nghĩa structured output (khuyến nghị JSON) và có `evaluate_prompt()` gọi Gemini SDK.
- [ ] Viết ít nhất **3 adversarial test cases** cố vượt ranh giới an toàn.
- [ ] Chạy `python starter-code/prompt_prototype.py` với API key; bảo đảm toàn bộ verification hiển thị `Passed`, không có `Failed`.
- [ ] Chụp/lưu log kết quả chạy để tiện giải thích khi review nhóm (nếu giảng viên yêu cầu).

### D. Push bài cá nhân

- [ ] Rà soát: không có API key, file `.env`, hoặc dữ liệu nhạy cảm trong staging.
- [ ] Commit các file của mình trên branch cá nhân.
- [ ] Push branch cá nhân: `git push origin <ten-cua-ban>`.
- [ ] Gửi tên branch/commit cho trưởng nhóm để được review.
- [ ] **Không push/merge trực tiếp vào `main`.**

## 2. Việc nhóm — thực hiện cùng nhau

### A. Chốt phạm vi dự án

- [x] Thảo luận các Quick Cards của mọi thành viên và chọn một bài toán duy nhất để deep-dive: **EMR Audit Assistant tại Vinmec**.
- [x] Xác nhận actor, quy trình hiện tại, dữ liệu đầu vào/đầu ra, bottleneck và metric có thể đo.
- [x] Phân biệt rõ phần nào dùng **Rule** (trường bắt buộc, ICD-10/BHYT), phần nào dùng **LLM** (đọc hiểu/gợi ý lỗi văn bản), và lý do không dùng Agentic Loop.

### B. Hoàn thiện báo cáo nhóm

- [ ] Điền tên/mã nhóm trong [02-deep-dive-report.md](02-deep-dive-report.md) trước khi nộp.
- [x] Rà [02-deep-dive-report.md](02-deep-dive-report.md): Current-State Workflow có bước, người/hệ thống, thời gian, handoff và bottleneck.
- [x] Rà Problem Statement đủ **6 fields**: Actor, Current Workflow, Bottleneck, Business Impact, Success Metric, Operational Boundary.
- [x] Rà Future-State Flow: có bước AI, bước bác sĩ phê duyệt (HITL), rule/guardrail, fallback khi thiếu dữ liệu/API/LLM lỗi.
- [x] Hoàn thành AI Readiness Checklist và chọn **NOT YET**, với điều kiện bổ sung dữ liệu ẩn danh, quy tắc nghiệp vụ, phân quyền và audit log.
- [x] Báo cáo nêu rõ ranh giới EMR: không tự sửa/chốt hồ sơ, tạo ICD-10/BHYT, chẩn đoán hoặc thay đổi điều trị; bác sĩ luôn phê duyệt. *(Đây là yêu cầu báo cáo nhóm, không yêu cầu sửa file code cá nhân.)*

### C. Tạo sơ đồ workflow

- [x] Vẽ quy trình **hiện tại** và lưu ở thư mục gốc: [04-workflow-diagram.png](04-workflow-diagram.png).
- [x] Sơ đồ có các bước tuần tự, người/bộ phận thực hiện, handoff, thời gian mỗi bước và bottleneck.
- [x] Kiểm tra sơ đồ có thể mở rõ ràng trước khi merge.

### D. Review, merge và nộp bài

- [ ] Tất cả thành viên đã push branch cá nhân trước khi nhóm review.
- [ ] Nhóm review, chọn hoặc tổng hợp phiên bản tốt nhất của `01-problem-scan.md`, `02-deep-dive-report.md`, `03-ai-log.md` và `04-workflow-diagram.*`.
- [ ] Trưởng nhóm/đại diện chỉ merge **các file Markdown và sơ đồ** vào `main`.
- [ ] **Không merge file `.py` vào `main`**; code chỉ được chấm trên branch cá nhân.
- [ ] Trên `main`, kiểm tra có đủ: `01-problem-scan.md`, `02-deep-dive-report.md`, `03-ai-log.md`, `04-workflow-diagram.png/.jpg/.pdf`.
- [ ] Chạy autograder hoặc kiểm tra file trước khi nộp nếu môi trường cho phép.
- [ ] Chỉ **trưởng nhóm** điền form/LMS với họ tên trưởng nhóm và link repository.

## 3. Mốc hoàn thành nhanh

| Thứ tự | Người chịu trách nhiệm | Kết quả cần có |
|---:|---|---|
| 1 | Mỗi thành viên | Branch cá nhân, Scan + 3 Cards + AI Log |
| 2 | Mỗi thành viên | Prompt prototype chạy được và test ranh giới đạt |
| 3 | Cả nhóm | Chọn đề tài, workflow, 6-field và future flow thống nhất |
| 4 | Cả nhóm | `02-deep-dive-report.md` và `04-workflow-diagram.*` hoàn chỉnh |
| 5 | Trưởng nhóm | Review, merge tài liệu/sơ đồ vào `main`, nộp form |
