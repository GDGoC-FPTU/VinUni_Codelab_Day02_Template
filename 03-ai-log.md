Beautifful_Lưu Xuân Dũng_2A202602746
# 03 — AI Log & Reflection

## Mục tiêu sử dụng AI

Tôi dùng AI như một thought-partner để mở rộng danh sách pain point của các công ty thành viên Vingroup, phản biện các metric, và biến ý tưởng thành một scope có thể kiểm thử. AI không được dùng như nguồn xác thực số liệu nội bộ; các con số trong bài được đánh dấu là giả định pilot.

## Nhật ký tương tác

| Lần | Prompt/tác vụ | AI hỗ trợ gì | Tôi kiểm tra và chỉnh sửa thế nào |
|---:|---|---|---|
| 1 | “Gợi ý các bottleneck vận hành có thể tối ưu bằng AI tại VinFast, Xanh SM, Vinhomes, Vinpearl, Vinmec.” | Đưa ra danh sách ban đầu theo các lens lặp lại, tốn thời gian và stakeholder pain. | Tôi bỏ các gợi ý quá chung chung như “dùng chatbot tăng trải nghiệm”, chỉ giữ các vấn đề có actor, quy trình, đầu vào/đầu ra và điểm nghẽn cụ thể. |
| 2 | “Đóng vai CFO và trưởng vận hành, phản biện card sự cố pin thấp: metric nào thiếu và rule-based có thể làm gì?” | Chỉ ra rằng LLM không nên tự quyết định trạm sạc khi có ngưỡng an toàn rõ ràng; cần baseline thay vì tự khẳng định tiết kiệm. | Tôi chuyển kiến trúc từ “AI dispatcher” thành **rule + LLM feature**. Rule xử lý pin, khoảng cách, cổng sạc và escalation; LLM chỉ tạo bản nháp. |
| 3 | “Hãy đề xuất future-state flow có Human-in-the-loop và fallback.” | Gợi ý bước lấy dữ liệu, xếp hạng lựa chọn, tạo draft và duyệt. | Tôi bổ sung điều kiện cụ thể: pin `<5%`, dữ liệu mâu thuẫn, JSON sai schema hoặc API lỗi đều phải quay về điều phối viên xử lý thủ công. |
| 4 | “Viết bản nháp hướng dẫn tài xế khi pin 2% và yêu cầu đi tới trạm 8 km.” | AI có thể đưa ra văn phong rõ ràng, nhưng nếu prompt không đủ chặt có xu hướng cố đáp ứng yêu cầu người dùng. | Tôi coi đây là trường hợp adversarial: system prompt phải bắt buộc `dispatch_mobile_charger`, không được đưa chỉ dẫn trạm xa, và output chỉ là `[DRAFT_ONLY]`. |

## Ví dụ AI sai hoặc có nguy cơ hallucination

AI có thể đề xuất các số như “80 sự cố/ngày”, “giảm 15% doanh thu” hoặc nêu tên API/dashboard như thể đó là dữ liệu thật. Những thông tin đó không có nguồn trong đề bài nên không thể dùng làm fact. AI cũng có thể gọi một trạm sạc là “còn chỗ” nếu không được cấp dữ liệu thời gian thực.

Tôi đã sửa bằng ba nguyên tắc:

1. Đổi mọi số không có nguồn thành “giả định scoping” hoặc “metric cần đo baseline”.
2. Chỉ cho LLM diễn đạt từ danh sách trạm đã được rule engine/API tin cậy lọc; LLM không tự bịa trạm, khoảng cách hay trạng thái chỗ trống.
3. Tách “đề xuất” khỏi “hành động”: output là JSON/bản nháp `[DRAFT_ONLY]`, điều phối viên mới là người gửi tin hoặc gọi cứu hộ.

## Reflection cá nhân

Bài tập làm tôi nhận ra “dùng AI” không đồng nghĩa với việc trao quyền quyết định cho mô hình. Với sự cố pin, quyết định an toàn có ngưỡng rõ nên rule-based phù hợp hơn; LLM có giá trị ở phần tóm tắt và soạn nội dung tiếng Việt. Câu hỏi hữu ích nhất khi làm việc với AI là: *“Điều gì phải được kiểm tra bằng dữ liệu và rule trước khi LLM được phép tạo câu trả lời?”*

Nếu làm tiếp, tôi sẽ thu thập log ẩn danh, gắn nhãn outcome đúng/sai cùng điều phối viên, chạy shadow mode và đánh giá theo median handling time, tỉ lệ sửa draft, tỉ lệ escalation đúng. Chỉ khi dữ liệu chứng minh lợi ích và không có vi phạm ranh giới, tôi mới đề xuất triển khai pilot thật.
