# Phase 1–2 — Bài cá nhân: Khảo sát cơ hội tại Vinhomes

**Học viên:** Lê Việt Khoa · **Nhánh:** `feat/khoalv-03737`  
**Nguồn nội dung:** kế thừa `Bao_cao_Phase_1_2_Vinhomes.docx` trong repository; chuẩn hóa theo `01-worksheet.md`.

> Tất cả quy trình, sản lượng, thời gian và mục tiêu dưới đây là giả định cho bài lab, chưa phải số liệu khảo sát Vinhomes. Không dùng để khẳng định hiệu quả kinh doanh thực tế. Năm bài toán cùng thuộc Vinhomes; sử dụng đủ bốn lenses của worksheet.

## Phase 1 — SCAN

| # | Công ty | Lens theo worksheet | Bài toán và giả định khối lượng |
|---|---|---|---|
| 1 | Vinhomes | Lặp lại | Cư dân đặt sân nhưng không đến; nhân viên xác minh, tìm người thay thế. 100 lượt/tháng × 6 phút = 10 giờ/tháng. |
| 2 | Vinhomes | Pain từ người khác | Ngoại lệ nhận diện biển số khiến nhân viên tra ảnh/lượt vào, người lái chờ tại cổng. 240 lượt/tháng × 3 phút = 12 giờ/tháng. |
| 3 | Vinhomes | Tốn thời gian; AI có thể tốt hơn | CSKH đọc phản ánh tự do, hỏi bổ sung và kiểm tra trùng trước khi chọn bộ phận. 600 yêu cầu/tháng × 5 phút = 50 giờ/tháng. |
| 4 | Vinhomes | Lặp lại; Tốn thời gian | Giao dịch thiếu mã căn hộ hoặc hóa đơn chưa cập nhật cần đối soát thủ công. 150 lượt/tháng × 12 phút = 30 giờ/tháng. |
| 5 | Vinhomes | AI có thể tốt hơn | Kỹ thuật viên rà công tơ và lịch vận hành để phát hiện tiêu thụ điện bất thường. 30 lượt/tháng × 20 phút = 10 giờ/tháng. |

Các con số chỉ tính thời gian thao tác, chưa tính chờ, chi phí tiền lương hay thời gian xử lý sự cố thực địa. Không cộng lợi ích các phương án khi chưa kiểm tra trùng phạm vi.

## Phase 2 — QUICK-ASSESS

### Card 01 — Lượt đặt sân nhưng cư dân không đến

| Trường | Nội dung |
|---|---|
| Bài toán / Công ty | Xác minh lượt vắng mặt và tìm người dùng suất trống tại Vinhomes. |
| Actor | Nhân viên trực sân; cư dân đang chờ có sân. |
| Workflow hiện tại | 1. Xem lịch đặt → 2. Kiểm tra điểm danh → 3. Liên hệ người đặt khi quá giờ → 4. Tìm người thay thế, cập nhật lịch. |
| Bottleneck | Bước 3–4; giả định tổng thao tác 6 phút/lượt ngoại lệ. |
| AI có thể hỗ trợ | Dự báo lượt dễ vắng trước bước 3 khi có lịch sử điểm danh đáng tin cậy. Chưa cần trong prototype đầu tiên. |
| Metric | Giảm thao tác từ 6 xuống ≤3 phút/lượt; đo tỷ lệ suất mở lại có người dùng; mục tiêu 0 suất mở nhầm trong mẫu thử 100 lượt. |
| Quick Architecture | **Rule**: nhắc theo lịch, xác minh vắng mặt, mời danh sách chờ. |

**Phản biện:** (1) Đến muộn, vắng mặt và thiếu dữ liệu điểm danh phải tách riêng. (2) Giảm cuộc gọi chưa chứng minh tăng sử dụng sân. (3) Giảm 3 phút × 100 lượt chỉ tương đương 5 giờ/tháng, cần so với chi phí tích hợp và khiếu nại. Chỉ thử dự báo nếu tốt hơn baseline nhắc theo lịch; không tự hủy suất khi chưa xác nhận điều kiện nghiệp vụ.

### Card 02 — Ngoại lệ nhận diện biển số tại bãi xe

| Trường | Nội dung |
|---|---|
| Bài toán / Công ty | Rút ngắn xác minh khi biển số đọc sai hoặc thiếu tại Vinhomes. |
| Actor | Nhân viên trực cổng; người điều khiển phương tiện đang chờ. |
| Workflow hiện tại | 1. Nhận cảnh báo không khớp → 2. Mở ảnh và nhật ký lượt vào → 3. Đối chiếu mã thẻ/mã lượt → 4. Xác nhận, ghi lý do ngoại lệ. |
| Bottleneck | Bước 2–3; giả định tổng thao tác 3 phút/ngoại lệ. |
| AI có thể hỗ trợ | Mô hình thị giác xếp hạng ảnh/lượt vào có khả năng khớp khi mờ hoặc lóa; không phải nhiệm vụ cho LLM văn bản. |
| Metric | Giảm từ 3 xuống ≤1,5 phút/ngoại lệ; P95 thời gian chờ không tăng so với baseline; mục tiêu 0 lượt cho qua sai trong 240 ca thử được kiểm tra. |
| Quick Architecture | **Rule**: giữ nhận diện hiện có, tìm theo mã thẻ/lượt đáng tin cậy, nhân viên đối chiếu ảnh. |

**Phản biện:** (1) Ảnh khó đọc, mất bản ghi và sai đăng ký cần ba cách xử lý. (2) Trung bình thấp có thể che giấu hàng chờ ở ca khó nên cần P95. (3) Tiết kiệm giả định 1,5 × 240 / 60 = 6 giờ/tháng phải cân với hậu quả xác minh sai. Thiếu bằng chứng thì quay về kiểm tra thủ công; không tự mở barrier.

### Card 03 — Phân loại phản ánh cư dân

| Trường | Nội dung |
|---|---|
| Bài toán / Công ty | CSKH mất thời gian đọc, hỏi bổ sung, kiểm tra trùng trước khi chuyển phản ánh tại Vinhomes. |
| Actor | CSKH/Ban Quản lý và đội chuyên trách nhận yêu cầu. |
| Workflow hiện tại | 1. Tiếp nhận → 2. Rà mô tả, vị trí, thông tin thiếu → 3. Kiểm tra trùng, chọn bộ phận → 4. Chuyển và theo dõi tiếp nhận. |
| Bottleneck | Bước 2–3; giả định 5 phút/yêu cầu cần rà soát, 600 yêu cầu/tháng. |
| AI có thể hỗ trợ | Đề xuất nhóm sự cố cho văn bản tự do ở bước 2–3; trích vị trí là hướng mở rộng, chưa được triển khai trong code. |
| Metric | Tổng thao tác ≤3 phút/yêu cầu so với giả định 5 phút; tỷ lệ chuyển đúng lần đầu không thấp hơn baseline đo thực tế; đo riêng ca khẩn bị bỏ sót/chậm. |
| Quick Architecture | **Rule trước**, **LLM Feature** thử riêng trên phần văn bản tự do còn lại; không dùng Agent. |

**Phản biện:** (1) Giống nội dung không đồng nghĩa cùng sự cố; phải xét vị trí và thời gian trước khi gộp. (2) Đo cả công xử lý chuyển sai của đội nhận, không chỉ công của CSKH. (3) Chưa có bằng chứng 600 yêu cầu đều cần LLM. Biểu mẫu với trường bắt buộc và bảng phân công có thể giải quyết phần lớn nhu cầu.

**Baseline đề xuất:** biểu mẫu có nhóm sự cố và vị trí; rule tra bảng phân công; chỉ đánh dấu khả năng trùng để nhân viên kiểm tra. Ca mơ hồ hoặc khẩn chuyển người phụ trách. So sánh LLM riêng trên email/mô tả tự do còn tốn công.

## Lựa chọn cho phần prototype cá nhân

Chọn **Card 03**, giới hạn ở **gợi ý topic/priority/action cho văn bản tự do**. Dữ liệu văn bản tổng hợp dễ tạo để kiểm tra prompt; ranh giới cấm tự gửi, chuyển hay đóng yêu cầu có thể kiểm thử. Card 01–02 ưu tiên rule vì quy trình có cấu trúc và lợi ích AI tăng thêm chưa rõ. Card 04 liên quan đối soát nên cần dữ liệu giao dịch chuẩn; Card 05 cần chuỗi thời gian công tơ mà repository chưa có.

Lựa chọn này không thay đổi kết luận rule-first của bản Word: làm prompt prototype để học và kiểm chứng ranh giới không đồng nghĩa đã chứng minh LLM đáng triển khai. Xem [Deep Dive](02-deep-dive-report.md) và [nhật ký AI](03-ai-log.md).
