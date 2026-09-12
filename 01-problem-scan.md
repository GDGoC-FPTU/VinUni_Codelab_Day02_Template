# Lab 02 — Problem Scan & Quick Problem Cards

## Phạm vi và cách dùng số liệu

Nhóm đóng vai AI Product Engineer tại Vin Smart Future và tập trung vào vận hành xe điện Xanh SM. Số liệu quy mô được lấy từ nguồn công khai; thời gian xử lý và số sự cố/ngày trong ví dụ lớp học chỉ là **giả định cần xác minh bằng log nội bộ**, không được trình bày như số liệu kinh doanh đã công bố.

Nguồn quy mô tham chiếu:

- Green SM công bố đã phục vụ hơn 50 triệu lượt khách và hoạt động tại 36 tỉnh/thành sau một năm: <https://www.greensm.com/vn-vi/news/xanh-sm-vuot-moc-50-trieu-luot-khach-hang-sau-1-nam-ra-mat>
- VinFast/V-GREEN công bố mạng lưới hơn 150.000 cổng sạc tại 63 tỉnh/thành: <https://vinfastauto.com/vn_vi/dich-vu-pin-oto-dien>
- VinFast công bố 111 xưởng dịch vụ tại 63 tỉnh/thành vào cuối tháng 11/2024: <https://vinfastauto.com/vn_vi/vinfast-la-hang-xe-so-huu-nhieu-xuong-dich-vu-nhat-viet-nam>

## Phase 1 — SCAN

| # | Đơn vị | Lens | Bài toán vận hành |
|---:|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Điều phối viên phải tra GPS, kiểm tra trạm sạc/cổng sạc và soạn hướng dẫn khi tài xế báo pin yếu hoặc hết pin. |
| 2 | Xanh SM | Lặp lại | Phân loại tin nhắn sự cố của tài xế thành pin yếu, lỗi sạc, tai nạn, lỗi ứng dụng hoặc cần cứu hộ rồi chuyển đúng đội. |
| 3 | Xanh SM | Stakeholder pain | Tổng hợp ghi chú và phản hồi để phân loại nguyên nhân khách hủy chuyến, phục vụ phân tích vận hành. |
| 4 | VinFast/V-GREEN | Lặp lại | Đối chiếu phiên sạc với khiếu nại hóa đơn và phí chiếm chỗ tại trạm sạc. |
| 5 | VinFast | AI-upgrade | Phân loại mô tả tiếng Việt tự do của khách hàng về lỗi xe, tạo bản tóm tắt cho xưởng dịch vụ gần nhất. |

## Phase 2 — QUICK-ASSESS

### Quick Problem Card 1 — Điều phối sự cố hết pin

- **Bài toán:** Khi tài xế Xanh SM báo pin yếu/hết pin, điều phối viên cần nhanh chóng tìm một trạm đang khả dụng, phù hợp với xe và đủ gần, hoặc chuyển cứu hộ.
- **Actor:** Tài xế, điều phối viên và đội cứu hộ/sạc lưu động.
- **Quy trình hiện tại:** nhận cuộc gọi → hỏi biển số, loại xe, % pin và vị trí → mở bản đồ → kiểm tra trạm/cổng phù hợp → soạn hướng dẫn → gọi cứu hộ nếu không an toàn.
- **Bottleneck:** tra cứu và soạn hướng dẫn; kịch bản worked example của lab giả định khoảng 10/15 phút mỗi lượt, cần đo lại bằng log thực tế.
- **AI hỗ trợ:** trích xuất dữ kiện từ tiếng Việt tự do, gọi bộ luật an toàn, xếp hạng trạm hợp lệ và tạo bản nháp cho điều phối viên.
- **Metric prototype:** thời gian tạo phương án dưới 3 phút; ≥98% chọn đúng trạm/cổng trên tập test đã gán nhãn; 100% trường hợp pin dưới 5% chuyển cứu hộ; 100% nội dung có `[DRAFT_ONLY]`.
- **Quick Architecture:** Rule engine + LLM Feature + Human-in-the-loop; không dùng agent tự trị.

### Quick Problem Card 2 — Phân loại sự cố tài xế

- **Bài toán:** Tin nhắn/cuộc gọi của tài xế cần được phân loại và chuyển đúng nhóm hỗ trợ.
- **Actor:** Điều phối viên trực tổng đài.
- **Quy trình hiện tại:** đọc/nghe phản ánh → ghi chú → chọn nhóm sự cố → chuyển đội phụ trách → theo dõi phản hồi.
- **Bottleneck:** nội dung tự do, thiếu dữ kiện, dễ chuyển nhầm nhóm trong giờ cao điểm.
- **AI hỗ trợ:** trích xuất biển số, vị trí, mức pin; phân loại; hỏi lại trường còn thiếu; tạo tóm tắt có cấu trúc.
- **Metric prototype:** ≥90% phân loại đúng; 100% tín hiệu nguy hiểm được gắn `urgent`; dưới 30 giây để tạo ticket có cấu trúc.
- **Quick Architecture:** LLM Feature + rules cho từ khóa an toàn + người duyệt.

### Quick Problem Card 3 — Đối chiếu khiếu nại phiên sạc

- **Bài toán:** Nhân viên hỗ trợ phải đối chiếu lời khiếu nại với thời lượng, điện năng và chính sách phí của phiên sạc.
- **Actor:** Nhân viên CSKH VinFast/V-GREEN.
- **Quy trình hiện tại:** nhận ticket → tìm phiên sạc → đối chiếu biểu phí → xác định sai lệch → tạo đề xuất xử lý → quản lý duyệt hoàn phí nếu có.
- **Bottleneck:** tìm đúng phiên và đọc mô tả tự do; phần tính phí có cấu trúc nhưng dễ nhập nhầm.
- **AI hỗ trợ:** LLM trích xuất dữ kiện và tạo tóm tắt; rule-based tính phí. AI không được quyết định hoàn tiền.
- **Metric prototype:** 100% phép tính phí do code thực hiện; ≥95% ticket trích xuất đúng mã trạm/thời điểm; 0 lần tự động hoàn tiền.
- **Quick Architecture:** Rule + LLM Feature + Human-in-the-loop.

## Lựa chọn

Nhóm chọn **Card 1 — Điều phối sự cố hết pin** vì có tác động thời gian thực, dữ liệu đầu vào rõ ràng, có thể mô phỏng an toàn và thể hiện tốt cả AI-fit, operational boundary, structured output, adversarial testing và fallback.
