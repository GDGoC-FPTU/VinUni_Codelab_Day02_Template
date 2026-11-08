# Nhật Ký Tương Tác AI & Bài Học Rút Ra (AI Thought-Partner Log)

- **Học viên:** Nguyễn Văn Tùng (nguyenvantung011204@gmail.com)
- **Bài lab:** Lab 02 — AI Product Scoping (Vin Smart Future)
- **Đề tài cá nhân:** Trợ lý AI Hỗ trợ Soạn thảo Ticket Leo thang Cảnh báo An ninh Mạng từ VinSOC Tier 1 lên VinSOC Tier 2 (Hệ thống Y tế Vinmec)
- **Công cụ AI sử dụng:** Gemini 2.5 Flash / Claude (đóng vai trò người phản biện và hỗ trợ tư duy)

---

## 1. AI đã giúp tôi những việc gì trong buổi học?

Trong quá trình làm bài Lab 02, tôi đã sử dụng AI như một người đồng hành (Thought-Partner) để cùng thảo luận và giải quyết các vấn đề:

1. **Gợi ý và brainstorm bài toán:** Khi bắt đầu với 4 lenses, tôi dùng prompt nhờ AI liệt kê các quy trình thủ công tốn thời gian tại các công ty của Vingroup. AI đã gợi ý cho tôi bối cảnh về trung tâm vận hành an ninh mạng (VinSOC) bảo vệ hệ thống y tế Vinmec, giúp tôi nhận ra điểm nghẽn lớn nhất của chuyên viên Tier 1 là mất quá nhiều thời gian để copy log và tự gõ ticket leo thang.
2. **Hỗ trợ định hình Schema đầu ra:** AI giúp tôi cấu trúc lại các trường thông tin cần thiết của một ticket an ninh chuẩn (tiêu đề, tóm tắt executive summary, mã kỹ thuật MITRE ATT&CK, các hành động đề xuất cho Tier 2) để đảm bảo kết quả trả về là JSON chuẩn, không bị thừa text linh tinh.
3. **Cùng xây dựng các kịch bản kiểm thử (Adversarial Tests):** Tôi nhờ AI đóng vai kẻ tấn công, đưa ra các câu lệnh prompt injection giả lập (như chèn lệnh bảo AI bỏ qua quy tắc và tự động cô lập máy chủ) để tôi kiểm tra xem ranh giới an toàn của mình đã đủ chặt chẽ chưa.

---

## 2. AI đã trả lời sai, ảo giác (Hallucination) hoặc gợi ý nguy hiểm ở đâu?

Làm việc thực tế với AI giúp tôi nhận thấy mô hình ngôn ngữ lớn rất dễ mắc phải các sai lầm nếu con người không kiểm soát kỹ:

1. **Ảo giác tự bịa ra địa chỉ IP (IoC Hallucination):** Khi tôi thử nghiệm đưa vào một đoạn log chỉ có lệnh kiểm tra người dùng nội bộ (`whoami`) và không hề có kết nối mạng ra ngoài, nhưng trong câu hỏi lại yêu cầu tìm IP của kẻ tấn công, AI ban đầu đã tự ý "bịa" ra một địa chỉ IP lạ và một tên miền độc hại để trả lời cho đầy đủ. Điều này trong an ninh mạng là cực kỳ nguy hiểm vì sẽ khiến đội Tier 2 đi điều tra một đối tượng không có thật.
2. **Thiên kiến tự động hóa quá đà đe dọa an toàn bệnh viện:** Khi tôi hỏi cách xử lý sự cố ransomware, AI ban đầu đề xuất viết script tự động cô lập máy chủ (network isolation) ngay khi phát hiện nghi vấn. Tôi đã phải bác bỏ ngay gợi ý này vì trong môi trường bệnh viện Vinmec, nếu cô lập nhầm một máy chủ lưu ảnh y khoa (PACS) hay máy trạm phòng cấp cứu/phòng mổ thì sẽ làm gián đoạn việc cứu chữa bệnh nhân.
3. **Bỏ sót dữ liệu cá nhân y tế:** AI ban đầu chỉ nhắc tôi lọc mật khẩu thông thường, mà không để ý rằng log trong bệnh viện thường chứa mã bệnh nhân (PID), số CCCD hoặc mã bảo hiểm y tế. Nếu gửi thẳng dữ liệu này lên AI đám mây thì sẽ vi phạm quy định bảo vệ dữ liệu cá nhân (Nghị định 13/2023/NĐ-CP).

---

## 3. Tôi đã sửa Prompt, Schema và đặt lại Ranh giới (Guardrails) như thế nào?

Từ những sai sót trên, tôi đã tự điều chỉnh lại hệ thống theo các nguyên tắc an toàn:

1. **Không cho AI tự trích xuất IP/Hash:** Tôi chuyển hoàn toàn việc bắt địa chỉ IP, mã băm và tên miền cho code Python (dùng biểu thức chính quy Regex) xử lý. AI chỉ nhận danh sách IP đã được xác thực từ code để diễn giải ngữ nghĩa, cấm tuyệt đối AI tự thêm các chỉ số IoC mới vào ticket.
2. **Thiết lập ranh giới an toàn lâm sàng (Clinical Safety):** Tôi bổ sung quy định nghiêm ngặt vào System Prompt: AI chỉ được phép đóng vai trò hỗ trợ soạn nháp (`draft_only: True`), nghiêm cấm AI tự động gọi lệnh ngắt mạng. Mọi cảnh báo liên quan đến máy chủ y tế đều phải có người kiểm tra và có sự xác nhận của IT bệnh viện trước khi hành động.
3. **Bổ sung bộ lọc che giấu dữ liệu bệnh nhân:** Viết thêm các mẫu regex để tự động che giấu mã bệnh nhân (`PID=[REDACTED]`), số CCCD và thông tin nhạy cảm trước khi gửi dữ liệu vào mô hình.

---

## 4. Tự phản ánh cá nhân (Personal Reflection)

- **Về mô hình Human-in-the-Loop trong y tế:** Tôi nhận ra rằng trong môi trường bệnh viện, tính sẵn sàng (Availability) của hệ thống liên quan trực tiếp đến tính mạng con người. Một mô hình AI dù thông minh đến đâu cũng luôn có tỷ lệ sai số (False Positive). Vì vậy, con người bắt buộc phải là người kiểm duyệt cuối cùng, AI chỉ nên là trợ lý hỗ trợ soạn thảo giúp con người làm việc nhanh hơn và bớt mệt mỏi hơn.
- **Về quá trình chạy thử nghiệm:** Tôi đã tự chạy các lệnh kiểm thử trên máy, chạy thử script prompt prototype ở cả chế độ offline và chạy thử với API Gemini để quan sát cách mô hình phản hồi trước các câu hỏi bẫy.
- **Điểm tôi tâm đắc nhất:** Việc kết hợp giữa code Python truyền thống (để làm sạch dữ liệu và trích xuất thông tin chính xác) cùng với LLM (để viết văn bản tóm tắt mạch lạc) là hướng tiếp cận rất thực tế, vừa an toàn vừa tận dụng được sức mạnh của AI.

