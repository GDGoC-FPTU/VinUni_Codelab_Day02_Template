# Lab 02 — Worksheet: AI Product Scoping (Vin Smart Future)

---

## 🏛️ 1. Bối cảnh thực tế: Vin Smart Future (Vingroup)

**Vingroup** — Tập đoàn tư nhân lớn nhất Việt Nam — vừa sáp nhập toàn bộ các phòng ban công nghệ thuộc các công ty thành viên thành một đơn vị công nghệ thống nhất mang tên **Vin Smart Future**. 

Nhiệm vụ của **Vin Smart Future** là xây dựng các giải pháp AI, số hóa, và tự động hóa cốt lõi để nâng cao hiệu suất vận hành và trải nghiệm khách hàng xuyên suốt các công ty thành viên:
* 🚗 **VinFast:** Hệ thống xe điện thông minh (EV), trợ lý AI ảo trong xe, dự đoán bảo trì pin, và quản lý chuỗi cung ứng sản xuất.
* 🚕 **Xanh SM (GSM):** Vận hành đội xe taxi/xe máy điện thông minh, điều vận thông minh (Smart Dispatching), tối ưu hóa lộ trình di chuyển.
* 🏢 **Vinhomes:** Quản lý đô thị thông minh (Smart Cities), trợ lý cư dân thông minh, tối ưu hóa mức tiêu thụ năng lượng.
* 🏥 **Vinmec:** Y tế thông minh, chẩn đoán hình ảnh bằng AI, tối ưu hóa quản lý hồ sơ bệnh án.
* 🎢 **Vinpearl / VinWonders:** Trải nghiệm du lịch số hóa, quản lý phòng và luồng khách thông minh tại các khu vui chơi.

Trong buổi Lab hôm nay, nhóm của bạn sẽ đóng vai trò là **AI Product Engineer** tại **Vin Smart Future**, tiến hành tìm kiếm, scoping, phân tích độ khả thi, thiết lập ranh giới vận hành, và xây dựng một **bản mẫu kỹ thuật (prompt prototype)** cho một bài toán cụ thể thuộc một trong những mảng kinh doanh trên.

---

## 📊 2. Cơ cấu tính điểm bài lab

### 👥 Điểm nhóm (60 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **G1. Workflow Mapping** | 20 | Problem Deep-Dive | Vẽ chi tiết quy trình hiện tại: các bước, handoff, thời gian, bottleneck |
| **G2. Problem Statement** | 20 | Problem Deep-Dive | Problem Statement 6-field bám sát thực tế, metric có số và ranh giới rõ ràng |
| **G3. AI Fit & Future Flow** | 10 | Problem Deep-Dive | So sánh Rule vs LLM vs Agent, future flow có bước AI, ranh giới và Fallback |
| **G4. Decision Quality** | 10 | Problem Deep-Dive | Quyết định Go/Not Yet/No-Go trung thực và có chứng cứ rõ ràng |

### 👤 Điểm cá nhân (40 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **I1. Scan & Cards** | 15 | Quick Cards | Liệt kê 5 problems sử dụng 3 lenses, hoàn thiện 3 quick cards chất lượng |
| **I2. Prototyping** | 10 | 02-lab/ | Chạy thử nghiệm programmatic prompt prototype thành công |
| **I3. AI Log & Reflection** | 15 | 03-ai-log.md | Phản ánh trung thực về việc dùng AI làm thought-partner (giúp gì, sai gì, sửa gì) |

---

# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

*Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI.*
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vinhomes | Lặp lại (Repetitive) | Phân loại hàng ngàn yêu cầu hỗ trợ (bảo trì, khiếu nại, dịch vụ) từ cư dân trên app Vinhomes Resident mỗi ngày và gán cho đúng phòng ban xử lý. |
| 2 | Vinmec | Tốn thời gian (Time-consuming) | Bác sĩ mất nhiều thời gian đọc, tổng hợp hồ sơ bệnh án cũ và các kết quả xét nghiệm rời rạc để đưa ra tóm tắt tình trạng bệnh nhân trong các ca hội chẩn/chuyển ca. |
| 3 | VinFast | Stakeholder Pain | Kỹ thuật viên bảo hành tại xưởng mất nhiều thời gian tra cứu hàng ngàn trang tài liệu HDSD và sơ đồ mạch điện phức tạp để tìm cách xử lý các mã lỗi (DTC) hiếm gặp trên xe EV. |
| 4 | Vinpearl | AI-upgrade | Khách hàng hỏi về lịch trình vui chơi, giá vé, hoặc yêu cầu tư vấn tour qua fanpage/chatbot hiện tại chỉ nhận được các câu trả lời rập khuôn theo kịch bản (rule-based) gây nhàm chán và tỷ lệ drop-off cao. |
| 5 | Xanh SM | Lặp lại (Repetitive) | CSKH phải nghe/đọc và tóm tắt lại các báo cáo sự cố từ tài xế (xe hỏng, khách hủy chuyến, tai nạn nhẹ) để nhập lên hệ thống quản lý Jira/CRM. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1 - VINHOMES                            │
│                                                             │
│ Bài toán: Phân loại và dự thảo phản hồi tự động cho các yêu │
│ cầu/khiếu nại của cư dân trên app.                          │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH (Ban quản lý Vinhomes). │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Đọc ticket ──> 2. Xác định loại lỗi (điện/nước/an ninh)│
│   ──> 3. Soạn phản hồi ──> 4. Assign cho kỹ thuật viên.     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 8-10 phút)   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Đọc ticket, tự động   │
│ phân loại (Tag) và dự thảo sẵn câu trả lời.                 │
│                                                             │
│ Đo thành công bằng gì? Giảm thời gian xử lý ticket từ       │
│ 10 phút xuống < 2 phút/ticket. Độ chính xác phân loại > 90%.│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2 - VINMEC                              │
│                                                             │
│ Bài toán: Tự động tổng hợp và trích xuất thông tin quan     │
│ trọng từ hồ sơ bệnh án đa nguồn của bệnh nhân.              │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ chuyên khoa, Điều dưỡng trưởng. │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Mở HIS ──> 2. Đọc từng phiếu xét nghiệm/khám cũ ──>    │
│   3. Ghi chú tay tóm tắt ──> 4. Viết báo cáo hội chẩn.      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 15-20 phút)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Trích xuất Entity (chỉ│
│ số bất thường, bệnh nền) và tạo đoạn tóm tắt bệnh sử ngắn.  │
│                                                             │
│ Đo thành công bằng gì? Tiết kiệm 10 phút/bệnh nhân. Không   │
│ bỏ sót (Recall = 100%) các bệnh nền nghiêm trọng (Dị ứng).  │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3 - VINFAST                             │
│                                                             │
│ Bài toán: Trợ lý AI tra cứu mã lỗi (DTC) và quy trình sửa   │
│ chữa từ tài liệu kỹ thuật dành cho xưởng dịch vụ.           │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Kỹ thuật viên (KTV) sửa chữa tại xưởng.│
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Đọc mã lỗi từ máy Scan ──> 2. Mở file PDF HDSD ──>     │
│   3. Ctrl+F tìm mã lỗi ──> 4. Đọc quy trình xử lý.          │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 10-30 phút)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Tìm kiếm semantic và  │
│ tổng hợp trực tiếp các bước sửa chữa từ kho tài liệu.       │
│                                                             │
│ Đo thành công bằng gì? Giảm thời gian tra cứu từ 20 phút    │
│ xuống < 1 phút. Cung cấp chính xác trang tài liệu tham chiếu│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

---

# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)
**Vẽ quy trình hiện tại:** 
* Cư dân gửi ticket khiếu nại/yêu cầu qua App Vinhomes Resident. 🔄 **Handoff** (App -> CSKH)
* Nhân viên CSKH đọc ticket trên hệ thống. (1 phút)
* 🔴 **Bottleneck:** Xác định loại sự cố (điện, nước, an ninh...), tra cứu quy định và xác định bộ phận xử lý phù hợp. (3-5 phút)
* 🔴 **Bottleneck:** Tự soạn thảo tin nhắn phản hồi cho cư dân. (3-5 phút)
* Gán (Assign) ticket cho bộ phận liên quan trên phần mềm. 🔄 **Handoff** (CSKH -> Kỹ thuật viên) (1 phút)
* Ghi rõ thời gian vận hành trung bình: **Tổng cộng = 8-12 phút/lượt**.

## 3.2. Problem Statement (6-field) & Metrics (15 min)
Điền đầy đủ 6 trường thông tin của bài toán:

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên Chăm sóc khách hàng (CSKH) tại Ban quản lý các khu đô thị Vinhomes. |
| **2. Current Workflow** | Nhân viên đọc yêu cầu trên hệ thống CRM, phân tích nội dung, xác định bộ phận liên quan, tự gõ tay soạn thảo câu trả lời và gán ticket cho kỹ thuật viên. |
| **3. Bottleneck** | Bước phân loại (cần đọc hiểu ngữ cảnh văn bản) và bước soạn thảo câu trả lời tốn nhiều thời gian, dễ rập khuôn hoặc sai sót khi lượng ticket quá tải. |
| **4. Business Impact** | Tốn khoảng 10 phút/ticket. Với hàng ngàn ticket mỗi ngày, SLA phản hồi cư dân bị chậm, cần nhiều nhân sự CSKH, làm giảm mức độ hài lòng (CSAT). |
| **5. Success Metric** | AI tự động tag (phân loại) và sinh bản nháp câu trả lời cho >90% ticket dưới 5 giây. Giảm thời gian xử lý thủ công của CSKH từ 10 phút xuống < 2 phút/ticket. |
| **6. Operational Boundary** | - AI **ĐƯỢC PHÉP**: Gắn tag phân loại, soạn sẵn bản nháp (draft) dựa trên rule/SOP.<br>- AI **TUYỆT ĐỐI KHÔNG ĐƯỢC**: Tự động gửi thẳng phản hồi cho cư dân khi chưa có người duyệt (đặc biệt với các khiếu nại về tiền, bồi thường, pháp lý).<br>- **Cần duyệt (HITL)**: CSKH luôn phải đọc lại và bấm "Duyệt & Gửi". |

## 3.3. Future-State Flow & AI Fit (25 min)
* **Xác định mức AI Fit (AI-Fit Matrix):** Giải pháp thuộc nhóm nào? [ ] Rule / State-Machine [x] LLM Feature [ ] Agentic Loop.
* **Vẽ Future-State Flow:**
  1. Cư dân gửi ticket qua App.
  2. 🔵 **AI Step:** LLM tự động phân tích ngữ nghĩa ticket, gắn thẻ (Tagging) loại sự cố và sinh ra một bản dự thảo (draft) phản hồi.
  3. 🟢 **Human Step (HITL):** Nhân viên CSKH xem ticket, kiểm tra tag, đọc và chỉnh sửa nhanh bản nháp, sau đó bấm "Gửi cư dân & Assign KTV".
  4. ↩️ **Fallback:** Nếu LLM gặp ticket quá ngắn, ngôn ngữ không rõ ràng, hoặc độ tự tin thấp, hệ thống không sinh bản nháp mà giữ nguyên trạng thái "Chờ xử lý thủ công" để nhân viên tự làm.

---

# 💻 Phase 4 — TECHNICAL PROMPT PROTOTYPE (Nhóm, 30 min)

Để đảm bảo kỹ sư của Vin Smart Future luôn giữ vững năng lực lập trình, nhóm của bạn sẽ tiến hành **lập trình bản mẫu prompt** trực tiếp trên **Gemini 2.5 Flash** bằng Python để stress-test hệ thống.

### Hướng dẫn thực hiện:
1. Mở file [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py) bằng VS Code/Cursor.
2. Hoàn thiện các nội dung sau:
   * **System Prompt:** Viết chỉ thị cực kỳ nghiêm ngặt quy định vai trò, nhiệm vụ, định dạng output và **Operational Boundary (Ranh giới cấm)** của mô hình.
   * **Structured Output:** Định nghĩa định dạng JSON output rõ ràng.
   * **Adversarial Test Cases:** Viết ít nhất 3 prompts "tấn công" (Adversarial inputs) cố tình dụ AI vượt ranh giới hoặc đưa ra câu trả lời không được phép để kiểm tra xem ranh giới của bạn có thực sự vững chắc.
3. Chạy file python:
   ```bash
   python3 prompt_prototype.py
   ```
4. Kiểm tra xem các ranh giới an toàn có bị LLM phá vỡ hay không và ghi lại kết quả vào worksheet.

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

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

---

# 📝 Phase 6 — REFLECTION (Cá nhân)
*Ghi nhận phản ánh của cá nhân bạn về việc phối hợp với AI trong buổi học hôm nay vào file `03-ai-log.md`.*
