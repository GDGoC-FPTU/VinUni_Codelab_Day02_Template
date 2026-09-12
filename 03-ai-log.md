# Nhật ký sử dụng AI và phản ánh cá nhân

## AI đã hỗ trợ như thế nào

Tôi sử dụng LLM như một người đồng hành tư duy để mở rộng danh sách bài toán, so sánh hướng tiếp cận Rule với LLM và Agent, đồng thời phản biện các chỉ số trong quick card. Gợi ý hữu ích nhất là phải tách quyết định an toàn tất định khỏi phần sinh ngôn ngữ.

## Điểm yếu của bản nháp đầu tiên

Ý tưởng ban đầu cho phép model đề xuất trực tiếp trạm gần nhất. Điều này không an toàn vì trạm gần nhất chưa chắc tương thích đầu sạc, còn chỗ hoặc đủ gần với lượng pin còn lại. Prompt đầu tiên cũng nói trợ lý nên hỗ trợ gửi tin nhắn, khiến ranh giới quyền phê duyệt trở nên không rõ ràng.

## Những điều chỉnh đã thực hiện

Tôi điều chỉnh thiết kế để code kiểm tra ngưỡng pin, khoảng cách, trạng thái trạm và loại đầu sạc trước khi LLM nhận các dữ kiện được phép sử dụng. System prompt hiện yêu cầu `[DRAFT_ONLY]` ở đầu mọi phản hồi, cấm tự động gửi và yêu cầu điều xe sạc di động khi pin dưới 5% nhưng không có trạm gần an toàn. Khi thiếu dữ liệu, hệ thống quay về quy trình thủ công thay vì đoán.

## Kiểm thử

Đã kiểm thử hai trường hợp adversarial: yêu cầu pin 2% đi đến trạm cách 8 km và yêu cầu bỏ thẻ bản nháp để gửi ngay. Prototype offline tạo action điều xe sạc di động cho trường hợp đầu tiên và giữ `[DRAFT_ONLY]` cho trường hợp thứ hai. Trước khi triển khai vận hành, vẫn cần chạy lại với Gemini thật trên các log đại diện.

## Phản ánh

Bài học chính là một prompt tốt không thể thay thế cơ chế phân quyền, kiểm tra dữ liệu và giám sát. Prototype hữu ích để kiểm thử hành vi ngôn ngữ, còn các luật, bước con người duyệt và cơ chế fallback mới bảo vệ được quy trình thực tế.
