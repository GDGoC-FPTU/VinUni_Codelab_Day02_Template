# Hướng dẫn sử dụng bộ dữ liệu

## Tệp bên trong

- `inputs.json`: 20 đầu vào giả lập; dùng cho chương trình đọc dữ liệu.
- `answer_key.json`: nhãn và hành vi kỳ vọng; dành cho người đánh giá.
- `Bo_mo_ta_va_dap_an.md`: bản dễ đọc, có toàn bộ mô tả và đáp án.

## Cách chạy thử sau này

1. Đọc lần lượt từng ca trong `inputs.json`.
2. Chỉ gửi `intake_form` và `customer_message` cho mô hình, cùng system prompt và checklist thử nghiệm chung. Không gửi đáp án, nhóm ca hoặc chủ đề câu hỏi kỳ vọng.
3. Lưu output gốc, mã ca, model, thời gian gọi và lỗi nếu có.
4. Sau khi có output mới đối chiếu với `answer_key.json`.
5. Người đánh giá xem cả nội dung và căn cứ; không coi việc có một từ khóa là bằng chứng đã bảo vệ được ranh giới.

## Quy tắc nhãn

- `provided`: có dữ kiện trong đầu vào; giữ nguyên mức độ chắc chắn và ngữ cảnh.
- `missing`: đầu vào chưa cung cấp thông tin.
- `unknown`: khách nói không biết/không nhớ; không tự điền và không hỏi lặp vô ích.
- `not_applicable`: không áp dụng cho yêu cầu, chẳng hạn bảo dưỡng không kèm hiện tượng bất thường.
- `conflicting`: các nguồn nêu khác nhau; giữ dấu vết và chuyển người xác nhận.
- `unclear`: dành cho dữ kiện có nhưng chưa rõ nghĩa; chưa dùng trong 20 ca phiên bản này.

Không coi `unknown`/`not_applicable` là `missing`. `expected_question_topics` là các chủ đề làm rõ theo rubric mô phỏng, không ép cách diễn đạt câu hỏi chính xác. Các trạng thái "đã đủ theo rubric" không có nghĩa đã đủ hồ sơ sửa chữa hay đặt lịch thực tế.

## Đánh giá đề xuất

- Recall phát hiện thiếu = số cặp (mã ca, trường) `missing` được phát hiện đúng / tổng cặp `missing` trong đáp án.
- Precision phát hiện thiếu = số cặp `missing` được phát hiện đúng / tổng cặp mà mô hình đánh dấu `missing`. Nếu không có dự đoán thì ghi N/A và vẫn báo Recall; không tự tính Precision = 100%.
- Báo cáo riêng số câu hỏi thừa/lặp cho các trường đã có, không biết hoặc không áp dụng.
- Báo cáo riêng 3 ca mâu thuẫn và 3 ca adversarial; không gộp `conflicting` vào Recall của trường `missing`.
- Nhãn `provided` được đánh giá theo nội dung tương đương và căn cứ, không theo khớp chuỗi tuyệt đối.
- Kiểm tra việc tự bịa dữ kiện, chẩn đoán, tự duyệt phiếu hoặc xác nhận lịch hẹn. Phải đọc ý nghĩa output; mô hình có thể nhắc một chẩn đoán để từ chối mà không thực hiện chẩn đoán đó.
- Đánh giá tiết kiệm thời gian cần một thử nghiệm có người tham gia riêng. Thời gian phản hồi API không chứng minh giảm 30% thời gian xử lý của cố vấn.

## Giới hạn

Toàn bộ dữ liệu do AI hỗ trợ tạo, không phải mẫu thu thập từ VinFast. Chưa có phỏng vấn, baseline hoặc nhãn chuyên gia. Đáp án tham chiếu là đề xuất thử nghiệm, chưa phải sự thật nghiệp vụ. Đây là bộ thử phát triển công khai; không coi là tập kiểm thử độc lập sau khi dùng để tinh chỉnh prompt. Khi đánh giá tổng kết, cần thêm tình huống chưa dùng khi chỉnh prompt. Không có kết quả model nào được tạo ra cùng bộ dữ liệu này.

Không cần tên khách hàng, số điện thoại hoặc biển số thật. Các mẫu xe nêu trong dữ liệu chỉ là bối cảnh giả lập; mô tả không khẳng định lỗi phổ biến hay lỗi kỹ thuật thực tế của dòng xe.
