# 01 — Problem Scan & Quick Problem Cards

## Bối cảnh

Tôi đóng vai AI Product Engineer tại Vin Smart Future. Mục tiêu của đợt scan là tìm các điểm nghẽn vận hành có thể cải thiện bằng AI nhưng vẫn kiểm soát được rủi ro.

## Phase 1 — SCAN

| # | Công ty | Lens | Bài toán vận hành |
|---:|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Điều phối viên xử lý thủ công sự cố hết pin hoặc lỗi sạc của tài xế; tra cứu vị trí và trạm sạc mất khoảng 15 phút mỗi lượt. |
| 2 | VinFast | Lặp lại | Nhân viên đối soát hóa đơn sạc và số liệu trạm sạc đối tác theo tuần bằng nhiều bảng dữ liệu rời rạc. |
| 3 | Vinhomes | AI-upgrade | Phản hồi cư dân trên ứng dụng phải được phân loại và chuyển bộ phận thủ công, làm chậm SLA phản hồi. |
| 4 | Vinmec | Tốn thời gian | Bác sĩ phải tự viết tóm tắt hồ sơ xuất viện trong 20–30 phút mỗi bệnh nhân. |
| 5 | Vinpearl/VinWonders | Pain từ stakeholder | Nhân viên chăm sóc khách hàng lặp lại việc trả lời câu hỏi về vé, giờ hoạt động và quy định khu vui chơi. |
| 6 | Xanh SM | Lặp lại | Nhân viên tổng hợp lý do hủy chuyến từ cuộc gọi và ghi chú tài xế để tìm lỗi theo khu vực. |

## Phase 2 — QUICK-ASSESS

### Card #1 — Xử lý sự cố sạc pin thực địa

- **Công ty:** Xanh SM
- **Bài toán:** Tài xế báo pin thấp hoặc hết pin giữa đường, cần tìm phương án sạc an toàn.
- **Actor:** Tài xế và điều phối viên trung tâm vận hành.
- **Workflow hiện tại:** Nhận cuộc gọi → tra GPS → tìm trạm còn chỗ và tương thích → soạn hướng dẫn → gọi cứu hộ nếu cần.
- **Bottleneck:** Tra cứu trạm và soạn hướng dẫn, khoảng 10–12 phút/lượt.
- **AI hỗ trợ:** Tổng hợp dữ liệu, soạn tin nhắn hướng dẫn dạng draft.
- **Metric:** Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút; độ chính xác trạm phù hợp đạt tối thiểu 98%.
- **Quick Architecture:** LLM Feature kết hợp Rule/State Machine.

### Card #2 — Phân loại khiếu nại cư dân

- **Công ty:** Vinhomes
- **Bài toán:** Khiếu nại trên ứng dụng phải đọc và chuyển thủ công đến đúng bộ phận.
- **Actor:** Nhân viên CSKH và cư dân.
- **Workflow hiện tại:** Nhận ticket → đọc nội dung → xác định nhóm vấn đề → chuyển bộ phận → soạn phản hồi.
- **Bottleneck:** Đọc, phân loại và chuyển ticket trong giờ cao điểm.
- **AI hỗ trợ:** Phân loại chủ đề, trích xuất mức độ khẩn cấp và đề xuất draft phản hồi.
- **Metric:** 85% ticket được phân loại trong dưới 10 giây; giảm thời gian phản hồi đầu tiên từ 12 giờ xuống dưới 2 giờ.
- **Quick Architecture:** Rule router + LLM Feature.

### Card #3 — Tóm tắt hồ sơ xuất viện

- **Công ty:** Vinmec
- **Bài toán:** Bác sĩ mất nhiều thời gian chuyển thông tin lâm sàng thành bản tóm tắt dễ hiểu.
- **Actor:** Bác sĩ điều trị và bộ phận hồ sơ bệnh án.
- **Workflow hiện tại:** Đọc hồ sơ → chọn chẩn đoán và thuốc → viết tóm tắt → rà soát → ký duyệt.
- **Bottleneck:** Tổng hợp thông tin từ nhiều ghi chú và hệ thống.
- **AI hỗ trợ:** Tạo bản nháp có trích dẫn nguồn trong hồ sơ để bác sĩ rà soát.
- **Metric:** Giảm thời gian soạn từ 25 phút xuống dưới 8 phút; 100% bản tóm tắt phải được bác sĩ duyệt.
- **Quick Architecture:** LLM Feature có Human-in-the-loop.

## Lựa chọn cho Deep-Dive

Chọn **Card #1 — Xử lý sự cố sạc pin thực địa của Xanh SM** vì đây là bài toán có tác động vận hành thời gian thực, metric rõ ràng và có thể giới hạn AI ở việc tra cứu/soạn draft. Không cho AI tự gửi tin hoặc tự điều xe giúp rủi ro được kiểm soát tốt hơn so với các bài toán y tế hay tranh chấp cư dân.

