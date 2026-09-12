Tên nhóm: 
Thành viên Nguyễn Hải Nam - namhaii631@gmail.com
           Trần Thị Thu Huyền - thuhientranthi.ai@gmail.com
           Bùi Phương Duy - phuongduy080804@gmail.com 
           Nguyễn Trần Bảo Tâm - ntbtbaotam@gmail.com

# 01 — Problem Scan & Quick Problem Cards

**Vai trò:** AI Product Engineer tại Vin Smart Future  
**Mảng ưu tiên:** Vincom Retail/Vingroup — vận hành bãi đỗ xe trung tâm thương mại

> Tất cả thời gian, lưu lượng và tỷ lệ trong bài là **baseline giả thuyết phục vụ scoping**, không phải số liệu nội bộ đã xác minh. Cần đo lại bằng camera/sensor logs, vé xe và khảo sát vận hành trước khi triển khai.

---

# 🔍 Phase 1 — SCAN (Cá nhân)

Sử dụng các lens **Repetitive, Time-consuming, AI-upgrade và Stakeholder Pain** để quét các bottleneck trong vận hành bãi đỗ xe.

| # | Đơn vị | Lens | Vấn đề vận hành |
|---:|---|---|---|
| 1 | Vincom | Stakeholder Pain | Khách mất nhiều thời gian chạy vòng để tìm ô đỗ còn trống, đặc biệt cuối tuần và giờ cao điểm. |
| 2 | Vincom | Time-consuming | Nhân viên điều phối phải quan sát camera/bộ đàm rồi hướng từng xe đến khu còn chỗ. |
| 3 | Vincom | AI-upgrade | Biển điện tử chỉ báo số chỗ theo tầng nhưng không hiểu nhu cầu như gần thang máy, chỗ xe điện hoặc chỗ tiếp cận. |
| 4 | Vincom | Repetitive | Nhân viên tổng hợp thủ công tình trạng đầy/chỗ trống và thời gian tìm chỗ theo ca vận hành. |
| 5 | Vincom | Stakeholder Pain | Khách quên vị trí xe và phải nhờ bảo vệ dò tìm theo biển số/khu vực nhớ mang máng. |
| 6 | Vincom | Time-consuming | Nhân viên phải xử lý xe đi nhầm làn, ùn tại điểm giao cắt và phân luồng lại khi một khu bất ngờ đầy. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân)

Từ danh sách trên, tôi chọn 3 bài toán có pain rõ, metric có thể đo và có khả năng prototype để làm Quick Problem Cards.

## Quick Problem Card #1 — QR Parking Assistant: tìm ô và ghi nhớ vị trí xe

| Thành phần | Nội dung |
|---|---|
| **Bài toán (1 câu)** | Khách quét QR tại cổng/cột mốc để mở web app, nhận gợi ý ô phù hợp và sau khi đỗ có thể lưu vị trí để tìm lại xe. |
| **Công ty thành viên** | Vincom Retail / Vingroup |
| **Ai đang đau (Actor)?** | Người lái xe là actor chính; nhân viên điều phối bãi xe là actor phụ. |
| **Workflow thủ công hiện tại** | (1) Xe vào bãi → (2) xem biển tầng → (3) chạy tìm ô → (4) gặp khu đầy thì quay lại/đổi tầng → (5) hỏi nhân viên nếu cần → (6) tự nhớ/chụp vị trí xe → (7) lúc về tự tìm lại xe. |
| **Bước tốn thời gian/lỗi nhất** | Bước 3–5; baseline giả thuyết khoảng **8–15 phút/lượt** vào giờ cao điểm. |
| **AI có thể hỗ trợ ở đâu?** | LLM hiểu nhu cầu tự nhiên như “xe điện, gần thang máy”; rule/routing engine lọc và xếp hạng ô; web app lưu phiên đỗ và hướng dẫn tìm lại xe. |
| **Metric có số** | Giảm median thời gian tìm chỗ xuống **<5 phút**; ≥95% gợi ý tại thời điểm trả kết quả là ô còn trống; ≥95% phiên đã xác nhận có thể dẫn lại đúng zone xe. |
| **Quick Architecture** | **LLM Feature + Rule/Optimization + Routing + Session Store** |
| **Rủi ro chính** | Dữ liệu occupancy chậm; nhiều xe cùng nhận một ô; chỉ dẫn gây mất tập trung; không được tự cấp ô ưu tiên khi chưa xác thực. |

---

## Quick Problem Card #2 — Tìm lại xe trong bãi

| Thành phần | Nội dung |
|---|---|
| **Bài toán (1 câu)** | Hỗ trợ khách xác định khu vực đã đỗ và nhận chỉ dẫn quay lại xe khi quên vị trí. |
| **Công ty thành viên** | Vincom Retail / Vingroup |
| **Ai đang đau (Actor)?** | Khách hàng; nhân viên an ninh/bãi xe. |
| **Workflow thủ công hiện tại** | (1) Khách báo quên vị trí → (2) cung cấp biển số/khu vực nhớ được → (3) nhân viên dò camera/log → (4) xác minh chủ xe → (5) hướng dẫn khách tới khu vực. |
| **Bước tốn thời gian/lỗi nhất** | Dò nhiều màn hình camera/log và xác minh; baseline giả thuyết **15–30 phút/lượt**. |
| **AI có thể hỗ trợ ở đâu?** | Tra log nhận diện biển số, thu hẹp zone có khả năng chứa xe và sinh hướng dẫn ngắn tới khu vực sau khi đã xác minh quyền truy cập. |
| **Metric có số** | ≥90% case xác định đúng zone trong **<3 phút**; **100%** case phải qua bước xác minh quyền truy cập trước khi hiển thị vị trí. |
| **Quick Architecture** | **ANPR/CV + Search + Rule**, LLM chỉ dùng để giải thích/hướng dẫn. |
| **Rủi ro chính** | Lộ vị trí xe cho người không phải chủ xe; nhận diện sai biển số; dữ liệu camera không đầy đủ. |

---

## Quick Problem Card #3 — Dự báo đầy bãi và hỗ trợ phân luồng

| Thành phần | Nội dung |
|---|---|
| **Bài toán (1 câu)** | Dự báo khu/tầng sắp đầy để nhân viên chủ động đổi hướng xe trước khi ùn tắc hình thành. |
| **Công ty thành viên** | Vincom Retail / Vingroup |
| **Ai đang đau (Actor)?** | Trưởng ca và nhân viên điều phối bãi xe; tài xế bị ảnh hưởng gián tiếp. |
| **Workflow thủ công hiện tại** | (1) Theo dõi camera/đếm xe → (2) nhận báo khu đầy → (3) liên lạc bộ đàm → (4) đổi hướng xe → (5) cập nhật biển báo. |
| **Bước tốn thời gian/lỗi nhất** | Phản ứng thường xảy ra sau khi khu vực đã bắt đầu ùn; dữ liệu phân tán giữa camera, bộ đàm và quan sát tại chỗ. |
| **AI có thể hỗ trợ ở đâu?** | Forecast occupancy 15–30 phút và tạo cảnh báo sớm; rule/optimization đề xuất khu thay thế để nhân viên quyết định. |
| **Metric có số** | Cảnh báo trước **≥15 phút**; mục tiêu giảm thời gian ùn tại điểm giao cắt **25%**; false-alarm rate phải nằm trong ngưỡng vận hành được chấp nhận. |
| **Quick Architecture** | **Forecasting + Rule + Optimization** |
| **Rủi ro chính** | Forecast sai có thể chuyển ùn tắc sang khu khác; cần dữ liệu lịch sử nên khó prototype hoàn chỉnh chỉ bằng prompt trong một buổi. |

---

# 📌 Đánh giá cá nhân trước khi sang phần làm nhóm

| Tiêu chí (1–5) | Card #1 Tìm ô | Card #2 Tìm xe | Card #3 Dự báo đầy |
|---|---:|---:|---:|
| Tác động trải nghiệm | 5 | 4 | 5 |
| Workflow dễ quan sát | 5 | 4 | 4 |
| Metric đo được | 5 | 4 | 4 |
| MVP khả thi | 4 | 4 | 3 |
| Rủi ro kiểm soát được | 4 | 3 | 3 |
| Phù hợp bài lab | 5 | 4 | 3 |
| **Tổng** | **28** | **23** | **22** |

## Đề xuất cá nhân

Tôi đề xuất **Card #1 — QR Parking Assistant** để mang sang phần thảo luận nhóm vì bài toán có pain rõ, workflow quan sát được, metric dễ đo và có thể prototype trong phạm vi buổi lab.

Scope cá nhân đề xuất cho MVP:
1. Quét QR để xác định điểm bắt đầu.
2. Nhập nhu cầu bằng text hoặc chọn form fallback.
3. Hệ thống gợi ý top ô phù hợp.
4. Người dùng xác nhận “Tôi đã đỗ” hoặc quét QR tại zone để lưu vị trí.
5. Khi ra về, quét QR gần thang máy/cột mốc để nhận tuyến đi bộ tới vị trí đã lưu.

> **Lưu ý:** Đây mới là **đề xuất cá nhân**. Việc nhóm có chọn Card #1 để Deep-Dive hay không sẽ được quyết định ở Phase 3 của bài lab.
