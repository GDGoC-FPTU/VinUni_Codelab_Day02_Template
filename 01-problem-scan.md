# Lab 02 — Báo cáo Problem Scan (Vin Smart Future)

## 🔍 Phase 1 — SCAN

Dưới đây là 5 bài toán vận hành thực tế tại Vingroup (Tập trung vào VinFast và Xanh SM):

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **VinFast** | AI có thể tốt hơn | **Dự đoán bảo trì pin (Predictive Maintenance):** Phân tích dữ liệu cảm biến để cảnh báo bảo dưỡng trước khi hỏng. |
| 2 | **Xanh SM** | Tốn thời gian | **Tối ưu điều phối xe về trạm sạc:** Tự động phân luồng xe cuối ca về các trạm sạc còn trống để tránh ùn ứ. |
| 3 | **VinFast** | Pain từ người khác | **Phân tích trạng thái người lái (Driver State Analysis):** Phát hiện tài xế buồn ngủ/căng thẳng qua camera để cảnh báo an toàn. |
| 4 | **Xanh SM** | Lặp lại | **Giải quyết khiếu nại cước phí:** Tự động đối chiếu GPS và traffic log để xử lý khiếu nại cước phí đột biến. |
| 5 | **VinFast** | Tốn thời gian | **Trợ lý bán hàng cá nhân hóa:** AI chat phân tích nhu cầu, tư vấn xe phù hợp và tự động book lịch lái thử. |


## 🃏 Phase 2 — QUICK-ASSESS

Lựa chọn 3 bài toán tiềm năng nhất để phân tích nhanh:

### QUICK PROBLEM CARD #1
*   **Bài toán (1 câu):** Tự động phân tích dữ liệu cảm biến để cảnh báo lịch bảo dưỡng pin sớm cho tài xế VinFast.
*   **Công ty thành viên:** [x] VinFast
*   **Ai đang đau (Actor)?** Chủ xe (rủi ro hỏng hóc dọc đường), Xưởng dịch vụ (quá tải vì sửa chữa ngoài dự kiến).
*   **Workflow thủ công hiện tại:** 
    1. Khách hàng đợi đến lịch bảo dưỡng định kỳ hoặc xe báo lỗi. ──> 2. Khách mang xe đến xưởng. ──> 3. Kỹ thuật viên cắm máy đọc lỗi. ──> 4. Xử lý sửa chữa/thay thế.
*   **Bước nào tốn thời gian/lỗi nhất?** Bước 3 & 4 (Phát hiện bệnh trễ dẫn đến tốn thời gian sửa chữa lớn).
*   **AI có thể nhảy vào hỗ trợ ở bước nào?** Phân tích liên tục dữ liệu Telemetry của xe và gửi cảnh báo tự động trên App VinFast trước khi xe báo lỗi cứng.
*   **Đo thành công bằng gì?** Giảm tỉ lệ xe phải cứu hộ do hỏng pin đột xuất xuống 20%.
*   **Quick Architecture:** [x] LLM / ML Model (Dự đoán chuỗi thời gian)

### QUICK PROBLEM CARD #2
*   **Bài toán (1 câu):** Điều hướng tài xế Xanh SM về đúng các trạm sạc còn trụ trống vào cuối ca làm việc để tránh chờ đợi.
*   **Công ty thành viên:** [x] Xanh SM
*   **Ai đang đau (Actor)?** Tài xế (phải đợi sạc lâu), Trưởng ca điều vận.
*   **Workflow thủ công hiện tại:** 
    1. Hết ca, tài xế tự tìm trạm sạc gần nhất trên app. ──> 2. Lái xe đến trạm sạc. ──> 3. Nếu trạm kín chỗ, tài xế phải ngồi chờ hoặc tự tìm trạm khác. ──> 4. Sạc xe.
*   **Bước nào tốn thời gian/lỗi nhất?** Bước 3 (Chờ đợi tại trạm sạc - có thể tốn 30-45 phút vô ích).
*   **AI có thể nhảy vào hỗ trợ ở bước nào?** Trước Bước 1. AI phân tích mức pin của toàn bộ đội xe và mật độ trạm sạc để tự động gán trạm sạc đích cho từng tài xế.
*   **Đo thành công bằng gì?** Giảm thời gian chờ đợi có trụ sạc của tài xế xuống dưới 5 phút.
*   **Quick Architecture:** [x] Rule-based Optimization + LLM thông báo.

### QUICK PROBLEM CARD #3
*   **Bài toán (1 câu):** Tự động xử lý khiếu nại của khách hàng Xanh SM về việc cước phí tăng cao do tài xế đi đường vòng hoặc kẹt xe.
*   **Công ty thành viên:** [x] Xanh SM
*   **Ai đang đau (Actor)?** Khách hàng (bức xúc), Nhân viên CSKH (quá tải).
*   **Workflow thủ công hiện tại:** 
    1. Khách gửi khiếu nại cước. ──> 2. CSKH mở log chuyến đi, xem lại bản đồ. ──> 3. Tra cứu tình trạng giao thông tại thời điểm đó. ──> 4. Gọi điện giải thích hoặc hoàn tiền.
*   **Bước nào tốn thời gian/lỗi nhất?** Bước 2 & 3 (Kiểm tra chéo dữ liệu thủ công - mất 10 phút/ca).
*   **AI có thể nhảy vào hỗ trợ ở bước nào?** AI tự động lấy log GPS, so khớp với Google Maps Traffic API và draft luôn câu trả lời giải thích hợp lý hoặc đề xuất hoàn tiền.
*   **Đo thành công bằng gì?** Giảm thời gian xử lý ticket khiếu nại cước từ 10 phút xuống còn 1 phút/ticket.
*   **Quick Architecture:** [x] LLM Feature (Xử lý ngôn ngữ tự nhiên + Function Calling).
