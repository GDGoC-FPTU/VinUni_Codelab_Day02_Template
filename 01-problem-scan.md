# 01 — Problem Scan & Quick Problem Cards

## Phase 1 — SCAN

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup

1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày.
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên.
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn.
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn.

### Danh sách bài toán

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Xanh SM                         | AI-upgrade | Complex customer-support escalation copilot for lost items, fare errors, and trip incidents; drafts only, with human approval for customer-facing action, escalation, and privacy-safe handling of trip data. |
| 2 | Xanh SM                         | Lặp lại | Detect and explain reconciliation exceptions for fares, promotions, bonuses, refunds, and driver income while the rule engine decides final money. |
| 3 | Xanh SM                         | Lặp lại | Post-check shift handover photos for damage and image quality, and route suspicious cases to a supervisor. |
| 4 | Xanh SM                         | Tốn thời gian | Prioritize vehicle incidents and suggest a workshop/schedule using fault descriptions and maintenance history, without safety diagnosis or repair approval. |
| 5 | Xanh SM                         | Stakeholder Pain | Fleet-level charging schedule using demand, battery, queues, and station capacity, without rebuilding existing V-App charging features; human dispatchers approve changes, and safety limits, driver privacy, and charger controls remain enforced. |

**Evidence note:** Official Green SM sources from **Khối Đồng hành & Phát triển Bác Tài Xanh**: [“Ra mắt tính năng mới: Gợi ý lộ trình sạc và danh sách phiên sạc trên ứng dụng V-App”](https://www.greensm.com/vn-vi/news/ra-mat-tinh-nang-moi-goi-y-lo-trinh-sac-va-danh-sach-phien-sac-tren-ung-dung-v-app?utm_source=chatgpt.com) (V-App charging/session features) and [“Hướng dẫn đặt lịch bảo dưỡng, sửa chữa xe qua ứng dụng Green SM Driver”](https://www.greensm.com/vn-vi/news/huong-dan-dat-lich-bao-duong-sua-chua-xe-qua-ung-dung-green-sm-driver-1?utm_source=chatgpt.com) (online maintenance booking). These confirm existing product capabilities; internal workload, time, and annual loss figures are not publicly confirmed, so numeric business cases must be labeled hypothetical pilot assumptions.

---

## Phase 2 — QUICK-ASSESS

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây.

### QUICK PROBLEM CARD #1

**Bài toán (1 câu):** Hỗ trợ nhân viên xử lý nhanh các khiếu nại CSKH phức tạp như mất tài sản, sai cước hoặc sự cố chuyến đi.

**Công ty thành viên:** [ ] VinFast  [x] Xanh SM  [ ] Vinhomes
[ ] Vinmec  [ ] Vinpearl  [ ] Khác: ____________________

**Ai đang đau (Actor)?** Nhân viên chăm sóc khách hàng và khách hàng có khiếu nại cần phối hợp nhiều bộ phận.

**Workflow thủ công hiện tại (3–5 bước):**

1. Tiếp nhận và phân loại nội dung khiếu nại.
2. Tra cứu lịch sử chuyến, cước, tài xế và các lần tương tác trước.
3. Liên hệ tài xế hoặc bộ phận liên quan để xác minh.
4. Chuyển cấp vụ việc nếu cần và soạn phản hồi cho khách hàng.
5. Theo dõi kết quả xử lý và đóng khiếu nại.

**Bước nào tốn thời gian/lỗi nhất?** Tra cứu nhiều hệ thống, xác minh và chuyển đúng bộ phận.
**Thời gian xử lý:** 15 phút/lượt

**AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 1–4: tóm tắt hồ sơ, đề xuất tuyến xử lý và soạn phản hồi nháp. Nhân viên phải duyệt trước khi gửi; AI không tự quyết định bồi thường hoặc truy cập dữ liệu ngoài quyền hạn.

**Đo thành công bằng gì (Metric có số)?** Giảm thời gian xử lý trung bình từ 15 phút xuống dưới 8 phút/lượt; ít nhất 85% vụ việc được chuyển đúng bộ phận ngay lần đầu; tỷ lệ khiếu nại mở lại không vượt quá 5%.

**Quick Architecture:** [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent

---

### QUICK PROBLEM CARD #2

**Bài toán (1 câu):** Tối ưu lịch sạc toàn đội xe để giảm thời gian xe chờ và tăng thời gian sẵn sàng nhận chuyến.

**Công ty thành viên:** [ ] VinFast  [x] Xanh SM  [ ] Vinhomes
[ ] Vinmec  [ ] Vinpearl  [ ] Khác: ____________________

**Ai đang đau (Actor)?** Điều phối viên đội xe và tài xế phải cân bằng nhu cầu chuyến, mức pin và tình trạng trạm sạc.

**Workflow thủ công hiện tại (3–5 bước):**

1. Theo dõi nhu cầu chuyến và số xe đang online theo khu vực.
2. Kiểm tra mức pin, vị trí xe và thời gian ca làm.
3. Xem tình trạng hàng đợi và công suất các trạm sạc.
4. Đề xuất hoặc phân bổ thời điểm/trạm sạc cho các xe cần sạc.
5. Điều chỉnh lịch khi nhu cầu chuyến hoặc tình trạng trạm thay đổi.

**Bước nào tốn thời gian/lỗi nhất?** Tổng hợp dữ liệu nhiều nguồn và điều chỉnh khi nhu cầu hoặc hàng đợi thay đổi.
**Thời gian xử lý:** 10 phút/lần cập nhật

**AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 2–4: dự báo nhu cầu ngắn hạn, xếp hạng xe/trạm cần ưu tiên và đề xuất lịch sạc. Điều phối viên duyệt thay đổi; AI không tự điều khiển bộ sạc hoặc vi phạm giới hạn an toàn.

**Đo thành công bằng gì (Metric có số)?** Giảm thời gian chờ sạc trung bình ít nhất 20%; giảm thời gian xe không có chuyến do chờ sạc từ 10 xuống dưới 7 phút/xe/ngày; duy trì tỷ lệ xe sẵn sàng nhận chuyến trên 95%.

**Quick Architecture:** [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent

---

### QUICK PROBLEM CARD #3

**Bài toán (1 câu):** Hậu kiểm ảnh bàn giao ca và checklist xe để phát hiện sớm hư hỏng hoặc ảnh không đạt chất lượng.

**Công ty thành viên:** [ ] VinFast  [x] Xanh SM  [ ] Vinhomes
[ ] Vinmec  [ ] Vinpearl  [ ] Khác: ____________________

**Ai đang đau (Actor)?** Nhân viên giám sát đội xe và nhân viên kiểm tra phương tiện sau mỗi ca.

**Workflow thủ công hiện tại (3–5 bước):**

1. Tài xế hoàn thành checklist và chụp ảnh bàn giao xe.
2. Nhân viên kiểm tra ảnh và đối chiếu với thông tin ca trước.
3. Đánh dấu ảnh mờ, thiếu góc chụp hoặc có dấu hiệu hư hỏng.
4. Liên hệ tài xế/giám sát để xác minh trường hợp nghi vấn.
5. Cập nhật kết quả và chuyển xe đi kiểm tra nếu cần.

**Bước nào tốn thời gian/lỗi nhất?** Xem và so sánh nhiều ảnh, dễ bỏ sót vết xước hoặc ảnh không đủ chất lượng.
**Thời gian xử lý:** 2 phút/xe/lượt

**AI có thể nhảy vào hỗ trợ ở bước nào?** Bước 2–3: kiểm tra chất lượng ảnh, so sánh ảnh giữa hai ca và đánh dấu vùng nghi vấn. Giám sát viên phải xác minh trước khi kết luận xe có hư hỏng.

**Đo thành công bằng gì (Metric có số)?** Giảm thời gian hậu kiểm từ 2 phút xuống dưới 1 phút/xe; đạt ít nhất 95% ảnh đạt yêu cầu được nhận diện đúng; tỷ lệ bỏ sót hư hỏng nghiêm trọng dưới 2%.

**Quick Architecture:** [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent
