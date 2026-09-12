# Quét bài toán - Vin Smart Future

## Bảng quét cơ hội

| # | Công ty thành viên | Lăng kính | Bài toán vận hành |
|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Điều phối viên xử lý thủ công các sự cố pin xe điện và tìm trạm sạc phù hợp. |
| 2 | VinFast | Lặp lại | Nhân viên tài chính đối chiếu hóa đơn trạm sạc với dữ liệu telemetry hằng tuần. |
| 3 | Vinhomes | AI có thể tốt hơn | Phản ánh của cư dân được phân loại và chuyển đến các ban quản lý bằng thao tác thủ công. |
| 4 | Vinmec | Nỗi đau của bên liên quan | Bác sĩ mất 20-30 phút để soạn tóm tắt xuất viện cho mỗi bệnh nhân. |
| 5 | Vinpearl | Tốn thời gian | Nhân viên đọc email đặt phòng theo đoàn và kiểm tra phòng trống thủ công. |

## Quick Card 1: Điều phối sự cố pin xe điện

- **Actor:** Điều phối viên Xanh SM và tài xế đang gặp sự cố.
- **Quy trình hiện tại:** Nhận cuộc gọi -> xác định vị trí xe -> tìm trạm còn chỗ -> kiểm tra tương thích đầu sạc -> soạn hướng dẫn -> điều phối viên gửi.
- **Nút thắt:** Tìm kiếm và soạn hướng dẫn chiếm khoảng 10 trong tổng số 15 phút mỗi sự cố.
- **AI hỗ trợ:** Lấy dữ liệu trạm theo cấu trúc và soạn tin nhắn ngắn gọn; tuyệt đối không tự động gửi.
- **Chỉ số:** Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút, đồng thời duy trì độ chính xác về trạm và đầu sạc trên 98%.
- **Kiến trúc:** Dùng luật cho khoảng cách và an toàn pin, LLM để soạn bản nháp, con người phê duyệt trước khi gửi.

## Quick Card 2: Phân loại phản ánh cư dân Vinhomes

- **Actor:** Điều phối viên dịch vụ cư dân.
- **Quy trình hiện tại:** Đọc phản ánh -> xác định loại vấn đề/tòa nhà -> chuyển cho bộ phận phụ trách -> trả lời cư dân.
- **Nút thắt:** Phân loại thủ công vào giờ cao điểm.
- **AI hỗ trợ:** Phân loại và soạn phản hồi, kèm trường độ tin cậy và căn cứ.
- **Chỉ số:** Chuyển đúng bộ phận 90% phiếu trong dưới 30 giây; vẫn bắt buộc con người duyệt các vấn đề pháp lý, thanh toán và an toàn.
- **Kiến trúc:** Bộ lọc ưu tiên dựa trên luật kết hợp với LLM để phân loại và soạn nháp.

## Quick Card 3: Tóm tắt xuất viện Vinmec

- **Actor:** Bác sĩ và đội ngũ hồ sơ bệnh án.
- **Quy trình hiện tại:** Xem hồ sơ -> chọn chẩn đoán và thay đổi thuốc -> viết tóm tắt -> bác sĩ ký duyệt.
- **Nút thắt:** Trích xuất và định dạng lặp lại, mất 20-30 phút mỗi bệnh nhân.
- **AI hỗ trợ:** Chỉ soạn nháp từ hồ sơ đã được phê duyệt; đánh dấu dữ kiện thiếu hoặc mâu thuẫn.
- **Chỉ số:** Giảm 50% thời gian soạn thảo mà không thay đổi quyết định lâm sàng đã ký.
- **Kiến trúc:** Truy xuất và kiểm tra tất định kết hợp với LLM soạn nháp; bắt buộc bác sĩ phê duyệt.
