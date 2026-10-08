# 03 — AI Log & Reflection (Cá nhân)

> Vin Smart Future — AI Product Scoping Lab
> Phản ánh trung thực về quá trình dùng AI (Claude) làm thought-partner trong buổi lab.

---

## 🤝 AI đã giúp gì?

* **Brainstorm & mở rộng ý tưởng bài toán (Phase 1 — SCAN):** Khi tôi chưa có ý tưởng cụ thể, AI đưa ra danh sách bài toán tiềm năng theo từng công ty thành viên Vingroup (VinFast, Xanh SM, Vinhomes, Vinmec, Vinpearl) để tôi chọn lọc thay vì phải tự nghĩ từ đầu.
* **Soạn thảo theo đúng khung mẫu (template):** AI giúp điền nhanh bảng SCAN, 3 Quick Problem Card, và báo cáo Deep-Dive (Problem Statement 6-field, Current/Future-State Workflow) đúng format worksheet, tiết kiệm thời gian trình bày để tôi tập trung vào nội dung.
* **Viết code khung an toàn (Phase 4):** AI giúp viết `SYSTEM_PROMPT` chi tiết và hàm `evaluate_prompt()` gọi Gemini SDK đúng cú pháp (`google-genai`), điều tôi chưa quen thao tác.
* **Debug môi trường:** Khi chạy script bị lỗi `UnicodeEncodeError` (do console Windows không hỗ trợ emoji) và lỗi `404 NOT_FOUND` (do đặt sai tên model), AI giúp xác định đúng nguyên nhân thay vì đoán mò.

---

## ⚠️ AI trả lời sai / hallucination ở đâu?

* **Tự ý sửa vượt phạm vi yêu cầu:** Khi tôi chỉ yêu cầu "hoàn thiện đoạn Code" trong `prompt_prototype.py`, AI đã tự động thêm một đoạn xử lý encoding UTF-8 và một adversarial test case thứ 3 (kèm logic kiểm tra mới) mà tôi không yêu cầu. Việc này khiến code thay đổi nhiều hơn phạm vi cần thiết và có thể gây khó hiểu khi tôi không chủ động yêu cầu các phần đó.
* **Ý tưởng ban đầu còn chung chung:** Ở vòng brainstorm đầu tiên cho Phase 1, các bài toán AI đề xuất khá giống với ví dụ mẫu có sẵn (`02-deliverable-example.md`) và chưa đủ "thực tế" theo đúng ý tôi muốn.

---

## 🛠️ Tôi đã sửa prompt/ranh giới như thế nào?

* Tôi yêu cầu AI **"chỉ sửa đoạn TODO thôi"** để buộc nó revert lại các thay đổi ngoài phạm vi (bỏ đoạn UTF-8 fix và test case thứ 3 tự thêm), giữ code sát với starter template gốc.
* Tôi yêu cầu AI đưa ra **các bài toán khác/thực tế hơn** thay vì chấp nhận batch ý tưởng đầu tiên, sau đó tự chọn lọc và kết hợp lại thành danh sách SCAN cuối cùng theo đúng góc nhìn của mình.
* Khi gặp lỗi API (`API key not valid`, `model not found`), tôi yêu cầu AI giải thích rõ nguyên nhân trước khi tự ý sửa code, để tránh AI "sửa bừa" theo phỏng đoán.

---

## 📌 Bài học rút ra

Làm việc với AI hiệu quả nhất khi tôi đưa ra ranh giới rõ ràng cho từng yêu cầu (ví dụ: "chỉ sửa phần này thôi") và luôn kiểm tra lại output trước khi chấp nhận, thay vì để AI tự quyết định phạm vi công việc. Đây cũng chính là bài học cốt lõi của cả lab: AI cần có **Operational Boundary** rõ ràng và cơ chế con người xác nhận (HITL) trước khi hành động.
