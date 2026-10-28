# 01 — Problem Scan & Quick Problem Cards

## 1. Phase 1 — SCAN

Trong vai trò AI Product Engineer tại Vin Smart Future, nhóm tập trung vào các pain point có tính lặp lại, tốn thời gian, có khả năng nâng cấp bằng AI và xuất phát từ stakeholder pain.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Điều phối viên phải xử lý thủ công các báo cáo sự cố sạc pin/hết pin của tài xế, tra cứu vị trí và tìm phương án hỗ trợ. |
| 2 | Vinhomes | AI-upgrade | Phản ánh/khiếu nại của cư dân cần được phân loại và chuyển đến đúng bộ phận xử lý; nội dung đa dạng và có thể diễn đạt tự nhiên. |
| 3 | VinFast | Lặp lại | Nhân viên phải đối chiếu dữ liệu sạc điện từ nhiều nguồn với hóa đơn/đối soát tài chính theo định kỳ. |
| 4 | Xanh SM | Pain từ người khác | Phải tổng hợp ghi âm cuộc gọi và ghi chú tài xế để phân loại nguyên nhân khách hủy chuyến. |
| 5 | Vinmec | Tốn thời gian | Bác sĩ mất thời gian tổng hợp thông tin từ bệnh án, xét nghiệm và ghi chú để soạn bản tóm tắt xuất viện. |

> Lưu ý: các con số vận hành chi tiết trong các Quick Card dưới đây là **giả định dùng cho bài lab/prototype**, không phải số liệu nội bộ đã được xác minh.

---

## 2. Phase 2 — QUICK-ASSESS

### Quick Problem Card #1 — Vinhomes: Phân loại & điều hướng phản ánh cư dân

**Bài toán:** Phân loại nội dung phản ánh của cư dân và route đến đúng bộ phận xử lý.

**Công ty:** Vinhomes

**Actor:** Nhân viên CSKH/ban quản lý tòa nhà.

**Workflow hiện tại:**
1. Cư dân gửi phản ánh trên ứng dụng.
2. Nhân viên đọc nội dung.
3. Xác định loại sự cố và bộ phận phụ trách.
4. Chuyển ticket.
5. Theo dõi/ghi nhận kết quả.

**Bottleneck:** Đọc và phân loại thủ công.

**Giả định baseline:** 8 phút/ticket.

**AI hỗ trợ:** Phân loại intent, trích xuất thông tin chính và đề xuất routing.

**Success Metric:**
- Giảm thời gian phân loại từ 8 phút xuống dưới 1 phút/ticket.
- ≥95% ticket được route đúng nhóm trong tập kiểm thử.

**Quick Architecture:** LLM Feature + Rule-based routing.

**Operational Boundary:** AI chỉ đề xuất phân loại/routing; các trường hợp liên quan tranh chấp, pháp lý, phí hoặc quyền lợi cư dân phải chuyển người xử lý.

---

### Quick Problem Card #2 — Xanh SM: Xử lý sự cố sạc pin thực địa

**Bài toán:** Hỗ trợ dispatcher xử lý báo cáo hết pin/sự cố sạc của tài xế.

**Công ty:** Xanh SM

**Actor:** Tài xế và dispatcher.

**Workflow hiện tại:**
1. Tài xế báo sự cố.
2. Dispatcher tra cứu vị trí xe.
3. Tra cứu phương án/trạm sạc phù hợp.
4. Soạn hướng dẫn cho tài xế.
5. Điều phối cứu hộ nếu cần.

**Bottleneck:** Tra cứu thông tin và soạn hướng dẫn.

**Giả định baseline:** 15 phút/lượt.

**AI hỗ trợ:** Tóm tắt sự cố và draft hướng dẫn từ dữ liệu đã được hệ thống kiểm chứng.

**Success Metric:**
- Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút.
- ≥98% draft chỉ sử dụng thông tin trạm/đường đi đã được hệ thống cung cấp.

**Quick Architecture:** LLM Feature.

**Operational Boundary:** AI không tự gửi chỉ dẫn; dispatcher phải duyệt. Nếu pin ở mức nguy hiểm hoặc dữ liệu không đủ tin cậy, chuyển sang phương án cứu hộ/fallback.

---

### Quick Problem Card #3 — Xanh SM: Phân tích lý do hủy chuyến

**Bài toán:** Tự động phân loại nguyên nhân hủy chuyến từ ghi âm cuộc gọi và ghi chú tài xế.

**Công ty:** Xanh SM

**Actor:** Nhân viên vận hành/analyst.

**Workflow hiện tại:**
1. Thu thập ghi âm và ghi chú.
2. Nghe/đọc nội dung.
3. Gán nhóm nguyên nhân.
4. Tổng hợp theo ngày/tuần.
5. Tìm pattern.

**Bottleneck:** Nghe và phân loại lượng lớn dữ liệu.

**Giả định baseline:** 10 phút/trường hợp.

**AI hỗ trợ:** Speech-to-text + LLM classification/summarization.

**Success Metric:**
- Giảm thời gian phân loại xuống dưới 1 phút/trường hợp.
- F1 ≥0.90 trên tập test đã gán nhãn.

**Quick Architecture:** LLM Feature.

**Operational Boundary:** AI chỉ phân tích dữ liệu phục vụ vận hành; không tự động quy kết lỗi cho tài xế/khách hàng hoặc đưa ra quyết định kỷ luật.

---

## 3. Lựa chọn bài toán Deep-Dive

Nhóm chọn **Quick Problem Card #1 — Phân loại & điều hướng phản ánh cư dân Vinhomes**.

### Lý do lựa chọn

- Workflow có cấu trúc rõ.
- Input chủ yếu là ngôn ngữ tự nhiên, phù hợp LLM classification/extraction.
- Có thể đặt HITL dễ dàng.
- Có thể xây baseline rule-based để so sánh.
- Rủi ro được kiểm soát tốt hơn các bài toán y tế hoặc an toàn xe.
- Có metric định lượng rõ: thời gian xử lý và routing accuracy.

Card #2 có giá trị vận hành cao nhưng liên quan đến an toàn khi xe hết pin; Card #3 phù hợp phân tích offline nhưng ít tác động trực tiếp đến xử lý real-time.
