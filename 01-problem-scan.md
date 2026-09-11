# Phase 1 — SCAN

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | Xanh SM / VinFast | Stakeholder Pain | Tài xế xe điện có thể gặp tình huống pin xuống mức nguy cấp nhưng việc quyết định tiếp tục tới trạm sạc, đổi trạm hay yêu cầu hỗ trợ khẩn cấp cần cân nhắc nhiều yếu tố như mức pin, khoảng cách và khả năng tiếp cận trạm. Đề xuất AI Emergency Decision Copilot hỗ trợ đưa ra phương án an toàn và chuyển sang cứu hộ/mobile charger khi vượt ranh giới an toàn. |
| 2 | Vinmec | Time-consuming | Sau khi bệnh nhân xuất viện, nhân viên y tế phải theo dõi nhiều thông tin rời rạc như triệu chứng tự báo cáo, chỉ số sức khỏe và lịch sử điều trị. Đề xuất AI hỗ trợ triage các trường hợp có dấu hiệu bất thường để ưu tiên bác sĩ review sớm, nhưng không tự chẩn đoán hoặc đưa quyết định điều trị. |
| 3 | Vinhomes | Repetitive | Các yêu cầu bảo trì của cư dân có thể đến dưới dạng text, ảnh hoặc video và cần được phân loại thủ công theo loại sự cố, mức độ nghiêm trọng và đội kỹ thuật phụ trách. Đề xuất Multimodal Maintenance Triage dùng AI để phân loại sự cố, ước lượng severity và route ticket tới đúng đội vận hành. |
| 4 | Vinpearl / VinWonders | AI-upgrade | Khi xảy ra sự cố như phòng không phù hợp, dịch vụ bị gián đoạn hoặc lịch trình thay đổi, nhân viên phải tra cứu nhiều chính sách và phương án thay thế trước khi phản hồi khách. Đề xuất AI Disruption Recovery Copilot tổng hợp chính sách và tạo các phương án rebooking, refund hoặc compensation để nhân viên phê duyệt. |
| 5 | VinFast | Time-consuming | Dữ liệu bảo hành, lịch sử sửa chữa và phản ánh lỗi có thể chứa các mẫu sự cố lặp lại nhưng việc phát hiện sớm các cụm lỗi theo linh kiện hoặc dòng xe là khó nếu xử lý thủ công. Đề xuất AI Warranty & Failure Intelligence để nhóm các triệu chứng tương tự, phát hiện pattern bất thường và tạo hypothesis phục vụ kỹ sư điều tra. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```
## QUICK PROBLEM CARD #1 — Vinhomes Multimodal Maintenance Triage

**Bài toán (1 câu):**  
Tự động phân loại các yêu cầu bảo trì của cư dân từ text, ảnh hoặc video theo loại sự cố, mức độ nghiêm trọng và đội kỹ thuật phụ trách để giảm thời gian xử lý ticket.

**Công ty thành viên:**  
- [ ] VinFast
- [ ] Xanh SM
- [x] Vinhomes
- [ ] Vinmec
- [ ] Khác

**Ai đang đau (Actor)?**  
Nhân viên vận hành/CSKH Vinhomes, đội kỹ thuật bảo trì và cư dân đang chờ xử lý sự cố.

**Workflow thủ công hiện tại (3–5 bước):**
1. Cư dân gửi yêu cầu kèm mô tả/ảnh/video.  
2. Nhân viên CSKH đọc nội dung và kiểm tra media.  
3. Nhân viên phân loại loại sự cố và mức độ ưu tiên.  
4. Ticket được chuyển sang đội kỹ thuật tương ứng.  
5. Đội kỹ thuật tiếp nhận và xử lý.

**Bước nào tốn thời gian/lỗi nhất?**  
Bước 2–3: đọc nội dung, hiểu ảnh và xác định severity/routing.  
⏱ Target baseline giả định: khoảng **5–10 phút/ticket**.

**AI có thể nhảy vào hỗ trợ ở bước nào?**  
Ngay sau khi cư dân gửi ticket:
- Phân tích text + image.
- Phân loại loại sự cố.
- Ước lượng severity.
- Đề xuất đội kỹ thuật/SLA.
- Các case nguy hiểm hoặc confidence thấp chuyển cho human review.

**Đo thành công bằng gì (Metric có số)?**
- ≥ **90%** ticket được phân loại dưới **30 giây**.
- ≥ **85% routing accuracy** tới đúng nhóm kỹ thuật.
- Giảm median triage time từ **5–10 phút → <1 phút**.
- **100%** case safety-critical phải được escalate sang human.

**Quick Architecture:**  
- [ ] No AI
- [ ] Rule
- [x] LLM
- [x] Agent

**Lý do:**  
Multimodal model xử lý text + ảnh; rule giữ các safety boundary; agent có thể tạo/routing work order sau khi được xác nhận.

---

## QUICK PROBLEM CARD #2 — Xanh SM / VinFast EV Emergency Decision Copilot

**Bài toán (1 câu):**  
Hỗ trợ tài xế xe điện đưa ra quyết định an toàn khi pin ở mức thấp/nguy cấp dựa trên mức pin, vị trí, khoảng cách tới trạm sạc và tình trạng vận hành.

**Công ty thành viên:**  
- [x] VinFast
- [x] Xanh SM
- [ ] Vinhomes
- [ ] Vinmec
- [ ] Khác

**Ai đang đau (Actor)?**  
Tài xế Xanh SM, nhân viên điều phối/cứu hộ và khách hàng đang trên chuyến xe.

**Workflow thủ công hiện tại (3–5 bước):**
1. Tài xế phát hiện mức pin thấp/nguy cấp.  
2. Tài xế hoặc dispatcher tìm trạm sạc gần nhất.  
3. Kiểm tra khoảng cách và khả năng xe có thể tới trạm.  
4. Dispatcher quyết định điều hướng tới trạm hoặc gọi hỗ trợ.  
5. Tài xế thực hiện phương án được duyệt.

**Bước nào tốn thời gian/lỗi nhất?**  
Bước 2–4: tổng hợp nhiều tín hiệu và chọn phương án an toàn trong điều kiện gấp.  
⏱ Target baseline giả định: **3–8 phút/case**.

**AI có thể nhảy vào hỗ trợ ở bước nào?**  
AI Copilot tổng hợp:
- State of Charge.
- GPS.
- Khoảng cách tới trạm.
- Trạng thái trạm.
- Operational safety rules.

Sau đó đề xuất:
- đi trạm,
- đổi trạm,
- hoặc dispatch mobile charger/cứu hộ.

**Operational Boundary quan trọng:**  
Nếu pin **<5%**, hệ thống không được khuyến nghị một trạm vượt quá ngưỡng khoảng cách an toàn đã định nghĩa; phải ưu tiên phương án cứu hộ/mobile charging và human confirmation.

**Đo thành công bằng gì (Metric có số)?**
- Decision recommendation dưới **10 giây**.
- ≥ **95% compliance** với safety rules trong adversarial tests.
- Giảm thời gian xử lý từ **3–8 phút → <1 phút**.
- **0 unsafe recommendation** trong test set critical-battery.

**Quick Architecture:**  
- [ ] No AI
- [x] Rule
- [x] LLM
- [x] Agent

**Lý do:**  
Safety threshold phải là deterministic rule; LLM giải thích và tổng hợp context; agent có thể gọi tool tra trạm, GPS hoặc dispatch system.

---

## QUICK PROBLEM CARD #3 — VinFast Warranty & Failure Intelligence

**Bài toán (1 câu):**  
Phát hiện sớm các mẫu lỗi lặp lại từ warranty claims, repair history và phản ánh kỹ thuật để hỗ trợ kỹ sư tìm ra component hoặc nhóm xe có nguy cơ bất thường.

**Công ty thành viên:**  
- [x] VinFast
- [ ] Xanh SM
- [ ] Vinhomes
- [ ] Vinmec
- [ ] Khác

**Ai đang đau (Actor)?**  
Kỹ sư chất lượng, kỹ sư bảo hành, đội service center và nhóm reliability/product engineering.

**Workflow thủ công hiện tại (3–5 bước):**
1. Service center ghi nhận triệu chứng và lịch sử sửa chữa.  
2. Warranty data được tổng hợp từ nhiều nguồn.  
3. Kỹ sư đọc và nhóm các case có triệu chứng tương tự.  
4. Kiểm tra component, batch hoặc dòng xe liên quan.  
5. Tạo investigation hypothesis và escalates cho engineering team.

**Bước nào tốn thời gian/lỗi nhất?**  
Bước 2–4: đọc lượng lớn mô tả tự do và liên kết các case giống nhau.  
⏱ Target baseline giả định: **hàng chục phút đến nhiều giờ** cho một investigation batch.

**AI có thể nhảy vào hỗ trợ ở bước nào?**
- Chuẩn hóa symptom descriptions.
- Semantic clustering các case tương tự.
- Phát hiện pattern bất thường.
- Tạo candidate hypothesis.
- Xếp hạng các cluster cần kỹ sư kiểm tra trước.

AI **không được tự kết luận root cause** hoặc phát lệnh recall.

**Đo thành công bằng gì (Metric có số)?**
- Giảm thời gian first-pass analysis ≥ **70%**.
- ≥ **85% precision** cho các cluster lỗi được kỹ sư xác nhận.
- Top critical pattern được surface trong **<5 phút** sau batch ingestion.
- **100% root-cause/recall decisions** phải do kỹ sư/người có thẩm quyền phê duyệt.

**Quick Architecture:**  
- [ ] No AI
- [ ] Rule
- [x] LLM
- [x] Agent

**Lý do:**  
LLM phù hợp với warranty text không cấu trúc; retrieval/clustering hỗ trợ tìm pattern; agent có thể truy vấn nhiều nguồn dữ liệu nhưng quyết định cuối vẫn là human-in-the-loop.
