# 📝 Phase 6 — AI Log & Reflection

Trong buổi lab này, tôi đã đóng vai trò là một AI Product Engineer tại Vin Smart Future và sử dụng AI (LLM) như một người đồng nghiệp (thought-partner) để brainstorm, đánh giá và thiết kế giải pháp cho bài toán vận hành. Dưới đây là nhật ký phản ánh quá trình làm việc với AI:

### 1. AI đã giúp tôi như thế nào? (What went well?)
* **Brainstorming ý tưởng nhanh chóng:** Khi tôi cần tìm các bài toán thực tế dựa trên 4 Lenses (Lặp lại, Tốn thời gian, AI-upgrade, Stakeholder Pain), AI đã cung cấp các ví dụ rất sát với đặc thù kinh doanh của hệ sinh thái Vingroup (như đọc bệnh án tại Vinmec, phân loại ticket Vinhomes, tìm lỗi xe điện VinFast).
* **Định hình cấu trúc (Structuring):** AI làm rất tốt việc đưa các ý tưởng lộn xộn vào trong các format chuẩn như *Quick Problem Card* hay *Problem Statement 6-field*, giúp tôi tiết kiệm thời gian gõ văn bản và tập trung hơn vào việc tinh chỉnh logic.
* **Stress-test logic:** Khi đóng vai trò là "Trưởng phòng Vận hành khắt khe", AI đã chỉ ra những kẽ hở trong thiết kế (ví dụ: rủi ro AI tự động gửi tin nhắn cho khách hàng mà không có sự kiểm duyệt). Điều này giúp tôi nhận ra tầm quan trọng của việc thêm bước **Human-in-the-loop (HITL)** vào quy trình.

### 2. AI đã sai hoặc gặp hạn chế ở điểm nào? (What went wrong/Limitations?)
* **Đôi khi quá lạc quan về công nghệ:** Ban đầu, AI có xu hướng đề xuất các giải pháp Agent tự động hóa 100% (Fully Autonomous) thay vì bắt đầu từ những LLM Features nhỏ và an toàn. 
* **Thiếu context thực tế cục bộ:** AI có thể mô tả quy trình chung chung (ví dụ: "Bác sĩ đọc hồ sơ") nhưng không nắm được chính xác tên các phần mềm nội bộ (như HIS, PACS) hoặc luồng phối hợp thực tế giữa các phòng ban nếu tôi không cung cấp context rõ ràng.
* **Metric thiếu thực tế:** Ở một số đề xuất đầu tiên, AI đưa ra các chỉ số Success Metric thiếu cơ sở (ví dụ: đòi hỏi độ chính xác 99.9% ngay từ phase 1), khiến bài toán trở nên bất khả thi để pilot.

### 3. Tôi đã điều chỉnh/sửa lỗi AI như thế nào? (How I guided the AI?)
* **Thiết lập Operational Boundary:** Tôi phải chủ động sử dụng prompt bắt buộc AI vạch ra ranh giới rõ ràng "Được làm gì" và "Tuyệt đối không được làm gì" để kéo AI về thực tế vận hành an toàn.
* **Bổ sung Fallback:** Khi vẽ Future-State Flow, tôi yêu cầu AI luôn phải thêm đường lùi (Fallback) trong trường hợp Confidence Score thấp, để đảm bảo hệ thống không bị "cứng nhắc" khi gặp dữ liệu lạ.
* **Prompt Engineering:** Thay vì hỏi chung chung "Làm sao để áp dụng AI vào Vinhomes?", tôi đã học cách cung cấp role cụ thể và yêu cầu output theo định dạng bảng (Markdown table) để dễ dàng đối chiếu và đưa vào Worksheet.

---
**Kết luận:** AI là một công cụ xuất sắc để mở rộng ý tưởng (divergent thinking) và tạo bản nháp (drafting), nhưng tư duy phản biện (critical thinking) để xác định giới hạn, rủi ro, và ra quyết định Go/No-Go cuối cùng vẫn phụ thuộc hoàn toàn vào kỹ sư AI Product.
