# Báo cáo phân tích sâu: Điều phối sự cố pin xe điện Xanh SM

## Phát biểu bài toán

| Trường thông tin | Nội dung |
|---|---|
| Actor / người vận hành | Điều phối viên phòng điều hành Xanh SM và tài xế báo sự cố pin. |
| Quy trình hiện tại | Điều phối viên nhận cuộc gọi, tìm xe trên bản đồ, kiểm tra trạm còn chỗ và loại đầu sạc, soạn hướng dẫn rồi gửi. Thời gian xử lý trung bình là 15 phút. |
| Nút thắt | Tìm trạm và soạn tin thủ công mất khoảng 10 phút, đồng thời có thể tạo đề xuất không an toàn về khoảng cách hoặc đầu sạc. |
| Tác động kinh doanh | Xe dừng hoạt động làm chậm chuyến tiếp theo, tăng thời gian tài xế chờ và tạo thêm khối lượng việc có thể tránh cho điều phối viên. Các ước tính này cần được đối chiếu bằng log sản xuất trước khi triển khai. |
| Chỉ số thành công | 90% sự cố có bản nháp để duyệt trong vòng 3 phút; độ chính xác về trạm/đầu sạc đạt 98%; không có lượt gửi tự động. |
| Ranh giới vận hành | AI được đọc dữ liệu vị trí và trạm đã được phê duyệt để tạo bản nháp. AI không được tự gửi, bịa dữ liệu, ghi đè luật khoảng cách hoặc pin, hay tự quyết định vấn đề an toàn nếu chưa có điều phối viên duyệt. |

## Quy trình hiện tại

1. Tài xế gọi phòng điều hành (2 phút) -> bàn giao cho điều phối viên.
2. Điều phối viên tra cứu GPS của xe (2 phút) -> bàn giao dữ liệu từ hệ thống telematics cho người vận hành.
3. Điều phối viên tìm trạm còn chỗ và loại đầu sạc (5 phút) -> nút thắt chính.
4. Điều phối viên viết hướng dẫn và liên hệ tài xế (5 phút) -> nút thắt thứ hai.
5. Điều phối viên chuyển sang đội sạc di động khi cần (1 phút).

**Tổng thời gian:** khoảng 15 phút mỗi sự cố.

## Quy trình tương lai và mức độ phù hợp của AI

1. Nhận sự cố và kiểm tra các trường dữ liệu bắt buộc.
2. **Luật:** nếu pin dưới 5%, loại bỏ các trạm xa hơn 5 km và yêu cầu điều xe sạc di động.
3. **Tra cứu có cấu trúc:** lấy khoảng cách, trạng thái và khả năng tương thích đầu sạc hiện tại của trạm.
4. **Tính năng LLM:** soạn hướng dẫn tiếng Việt chỉ từ dữ kiện đã truy xuất và đặt `[DRAFT_ONLY]` ở đầu.
5. **Human-in-the-loop:** điều phối viên xem, chỉnh sửa nếu cần và phê duyệt việc gửi.
6. **Fallback:** nếu thiếu dữ liệu, độ tin cậy thấp hoặc model lỗi, quay về quy trình thủ công hiện tại.

Mức độ phù hợp là một tính năng LLM được hỗ trợ bởi các luật an toàn tất định, không phải một agent tự chủ. LLM xử lý việc tạo ngôn ngữ; code chịu trách nhiệm về khoảng cách, ngưỡng pin, khả năng tương thích và quyền phê duyệt.

## Đánh giá

- Mức độ sẵn sàng dữ liệu: **CHƯA SẴN SÀNG** cho đến khi dữ liệu trạng thái trạm, GPS và log sự cố được làm sạch và xây dựng baseline.
- Kiểm soát rủi ro: **CÓ THỂ TRIỂN KHAI prototype nội bộ giới hạn** vì mọi đầu ra chỉ là bản nháp để duyệt và logic pin quan trọng là tất định.
- Mức độ sẵn sàng của bên liên quan: chạy pilot với điều phối viên, đo tỷ lệ chỉnh sửa và thu thập các trường hợp lỗi.

**Quyết định: CÓ THỂ TRIỂN KHAI prototype giới hạn có con người duyệt; CHƯA SẴN SÀNG cho điều phối tự động trong môi trường production.**
