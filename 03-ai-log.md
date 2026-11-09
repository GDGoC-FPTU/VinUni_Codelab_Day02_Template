# Nhật ký sử dụng AI

## 1. Mục tiêu và phương pháp ban đầu

- **Mục tiêu:** tìm các cơ hội cải thiện vận hành cho Xanh SM/Green SM và thu hẹp thành một hướng MVP có thể đo lường.
- **Phương pháp:** dùng **ChatGPT Web**, bắt đầu từ mẹo brainstorming trong worksheet để mở rộng nhiều hướng, bật chế độ **high reasoning**, và dùng **web search** để kiểm tra các tính năng hiện có cùng tài liệu nghiên cứu liên quan.

## 2. Đóng góp hữu ích của AI

AI giúp tạo và sắp xếp năm cơ hội tiềm năng:

1. Tối ưu điều phối xe theo khu vực, thời điểm và nhu cầu.
2. Tối ưu kế hoạch sạc, giảm thời gian xe chờ và thiếu xe khi cao điểm.
3. Dự báo nhu cầu và bố trí xe/tài xế theo ca.
4. Phát hiện sớm rủi ro bảo dưỡng, downtime và phân bổ lịch sửa chữa.
5. Đối soát doanh thu, chuyến đi, thời gian hoạt động và các ngoại lệ giữa nhiều hệ thống.

Các **chỉ số ứng viên** gồm: tỷ lệ hoàn thành chuyến, thời gian chờ/đỗ, số km rỗng, mức sử dụng xe, thời gian sạc và tỷ lệ sẵn sàng, downtime bảo dưỡng, chi phí mỗi chuyến, chênh lệch doanh thu cần đối soát, và tỷ lệ ngoại lệ được xử lý trong SLA.

Một hướng MVP khả thi là **đối soát có xử lý ngoại lệ**: tự động ghép dữ liệu chuyến–doanh thu–thời gian hoạt động, gắn cờ sai lệch (thiếu chuyến, trùng chuyến, doanh thu bất thường hoặc trạng thái không khớp), rồi đưa các trường hợp cần người duyệt vào hàng đợi.

## 3. Điều chỉnh sau kiểm chứng

- Các con số theo năm trong bản scan chỉ là **ước tính theo giả định**, chẳng hạn 100.000 chuyến/ngày, 10.000 xe, 80.000 VND/giờ lao động và 30.000 VND/giờ đóng góp. Chúng **không phải** số liệu đã xác nhận về tổn thất hay khoản tiết kiệm của Green SM.
- Green SM đã có tính năng chính thức trong V-App về gợi ý lộ trình sạc và danh sách phiên sạc, đồng thời đã có đặt lịch bảo dưỡng trực tuyến. Vì vậy, phạm vi được điều chỉnh từ “xây lại tính năng cho tài xế” sang **tối ưu ở cấp đội xe và xử lý ngoại lệ**, nơi còn cần tổng hợp dữ liệu, ưu tiên hành động và giám sát kết quả.

## 4. Nguồn tham khảo

- [Green SM: tính năng gợi ý lộ trình sạc và danh sách phiên sạc trên V-App](https://www.greensm.com/vn-vi/news/ra-mat-tinh-nang-moi-goi-y-lo-trinh-sac-va-danh-sach-phien-sac-tren-ung-dung-v-app?utm_source=chatgpt.com)
- [Green SM: đặt lịch bảo dưỡng, sửa chữa qua ứng dụng Green SM Driver](https://www.greensm.com/vn-vi/news/huong-dan-dat-lich-bao-duong-sua-chua-xe-qua-ung-dung-green-sm-driver-1?utm_source=chatgpt.com)
- [Ma, Connors và Viti (2024)](https://orbilu.uni.lu/handle/10993/63841)
- [Nghiên cứu trên *Quarterly Journal of Economics*](https://doi.org/10.1093/qje/qjae044) — trang nhà xuất bản không fetch trực tiếp được trong lần kiểm tra lại.

## 5. Phản ánh của sinh viên

- AI đã giúp em làm gì nhanh hơn (mở rộng cơ hội, đặt tên chỉ số, thu hẹp MVP)?
- Phần nào vẫn chưa chắc chắn vì thiếu dữ liệu nội bộ hoặc chưa kiểm chứng được?
- Em đã độc lập sửa hoặc loại bỏ kết luận nào của AI sau khi kiểm tra nguồn và tính năng hiện có?
- Nếu tiếp tục, em sẽ xin dữ liệu nào để kiểm định các giả định và đo hiệu quả MVP?
