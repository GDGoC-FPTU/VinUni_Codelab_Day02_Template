# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping
**Vẽ quy trình hiện tại:** 
* Cư dân gửi ticket khiếu nại/yêu cầu qua App Vinhomes Resident. 🔄 **Handoff** (App -> CSKH)
* Nhân viên CSKH đọc ticket trên hệ thống. (1 phút)
* 🔴 **Bottleneck:** Xác định loại sự cố (điện, nước, an ninh...), tra cứu quy định và xác định bộ phận xử lý phù hợp. (3-5 phút)
* 🔴 **Bottleneck:** Tự soạn thảo tin nhắn phản hồi cho cư dân. (3-5 phút)
* Gán (Assign) ticket cho bộ phận liên quan trên phần mềm. 🔄 **Handoff** (CSKH -> Kỹ thuật viên) (1 phút)
* Ghi rõ thời gian vận hành trung bình: **Tổng cộng = 8-12 phút/lượt**.

## 3.2. Problem Statement (6-field) & Metrics
Điền đầy đủ 6 trường thông tin của bài toán:

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên Chăm sóc khách hàng (CSKH) tại Ban quản lý các khu đô thị Vinhomes. |
| **2. Current Workflow** | Nhân viên đọc yêu cầu trên hệ thống CRM, phân tích nội dung, xác định bộ phận liên quan, tự gõ tay soạn thảo câu trả lời và gán ticket cho kỹ thuật viên. |
| **3. Bottleneck** | Bước phân loại (cần đọc hiểu ngữ cảnh văn bản) và bước soạn thảo câu trả lời tốn nhiều thời gian, dễ rập khuôn hoặc sai sót khi lượng ticket quá tải. |
| **4. Business Impact** | Tốn khoảng 10 phút/ticket. Với hàng ngàn ticket mỗi ngày, SLA phản hồi cư dân bị chậm, cần nhiều nhân sự CSKH, làm giảm mức độ hài lòng (CSAT). |
| **5. Success Metric** | AI tự động tag (phân loại) và sinh bản nháp câu trả lời cho >90% ticket dưới 5 giây. Giảm thời gian xử lý thủ công của CSKH từ 10 phút xuống < 2 phút/ticket. |
| **6. Operational Boundary** | - AI **ĐƯỢC PHÉP**: Gắn tag phân loại, soạn sẵn bản nháp (draft) dựa trên rule/SOP.<br>- AI **TUYỆT ĐỐI KHÔNG ĐƯỢC**: Tự động gửi thẳng phản hồi cho cư dân khi chưa có người duyệt (đặc biệt với các khiếu nại về tiền, bồi thường, pháp lý).<br>- **Cần duyệt (HITL)**: CSKH luôn phải đọc lại và bấm "Duyệt & Gửi". |

## 3.3. Future-State Flow & AI Fit
* **Xác định mức AI Fit (AI-Fit Matrix):** Giải pháp thuộc nhóm nào? [ ] Rule / State-Machine [x] LLM Feature [ ] Agentic Loop.
* **Vẽ Future-State Flow:**
  1. Cư dân gửi ticket qua App.
  2. 🔵 **AI Step:** LLM tự động phân tích ngữ nghĩa ticket, gắn thẻ (Tagging) loại sự cố và sinh ra một bản dự thảo (draft) phản hồi.
  3. 🟢 **Human Step (HITL):** Nhân viên CSKH xem ticket, kiểm tra tag, đọc và chỉnh sửa nhanh bản nháp, sau đó bấm "Gửi cư dân & Assign KTV".
  4. ↩️ **Fallback:** Nếu LLM gặp ticket quá ngắn, ngôn ngữ không rõ ràng, hoặc độ tự tin thấp, hệ thống không sinh bản nháp mà giữ nguyên trạng thái "Chờ xử lý thủ công" để nhân viên tự làm.

---

# 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
Dự án Vinhomes Smart Resident Support Co-pilot có tỷ lệ ROI (Return on Investment) cực kỳ rõ ràng. Bằng cách áp dụng LLM Feature kết hợp với cơ chế Human-in-the-loop (CSKH duyệt nội dung [DRAFT_ONLY]), chúng ta loại bỏ được rủi ro AI "ảo giác" (hallucination) phản hồi bậy bạ với khách hàng, đồng thời tuân thủ chặt chẽ ranh giới an toàn (không hứa hẹn thời gian, kích hoạt báo động khẩn cấp). Sự phức tạp về mặt công nghệ ở mức trung bình (có thể triển khai qua API của các foundation models) nhưng mang lại hiệu ứng giải phóng sức lao động khổng lồ, phù hợp để đưa vào Pilot ngay trong Quý tới.
