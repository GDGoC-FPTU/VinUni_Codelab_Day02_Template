# 📋 01 — Problem Scan & Quick Problem Cards (Vin Smart Future)

> **Học phần:** Lab 02 — AI Product Scoping (Vin Smart Future)  
> **Đơn vị:** Vin Smart Future — Khối Công Nghệ Tập Đoàn Vingroup  
> **Người thực hiện:** AI Product Engineer  
> **Dự án mục tiêu:** Hệ thống Điều phối Thông minh Xanh SM (GSM Intelligent Dispatcher Co-pilot)  

---

## 🏛️ 1. Bối cảnh vai trò (Context & Role)

Tôi là AI Product Engineer tại **Vin Smart Future** — đơn vị công nghệ tập trung của Tập đoàn Vingroup, chịu trách nhiệm nghiên cứu, phát triển và tích hợp các giải pháp AI/tự động hóa cho các công ty thành viên: **VinFast, Xanh SM (GSM), Vinhomes, Vinmec, Vinpearl**.

Mục tiêu của tài liệu này là:
1. **Phase 1 (SCAN):** Sử dụng **4 Lenses** (Lặp lại, Tốn thời gian, AI có thể tốt hơn, Pain từ người khác) để rà quét các nút thắt vận hành (operational bottlenecks) thực tế trên toàn hệ sinh thái Vingroup.
2. **Phase 2 (QUICK-ASSESS):** Chọn lọc và xây dựng **3 Quick Problem Cards** chi tiết, từ đó lập luận lựa chọn bài toán có độ khả thi cao nhất, ranh giới an toàn rõ ràng nhất để tiến hành Deep-Dive và lập trình Prompt Prototype.

---

# 🔍 Phase 1 — SCAN: Danh sách bài toán vận hành (4 Lenses)

| # | Subsidiary (Công ty thành viên) | Lens | Tên bài toán / Bottleneck | Mô tả ngắn bài toán | Ước tính tổn thất / Bottleneck thực tế |
|---|---|---|---|---|---|
| **1** | **Xanh SM (GSM)** | **Tốn thời gian** | **Hỗ trợ xử lý sự cố hết pin / trạm sạc thực địa của tài xế EV** | Khi tài xế taxi điện báo pin yếu hoặc trạm sạc quá tải, điều phối viên phải tra cứu bản đồ, kiểm tra trụ sạc VinFast trống, và soạn tin chỉ dẫn thủ công. | Mất 12-15 phút/lượt; ~80-100 ca/ngày tại các thành phố lớn; lãng phí ~20 giờ làm việc/ngày của điều vận, tài xế trễ cuốc và ức chế. |
| **2** | **VinFast** | **AI có thể tốt hơn** | **Chẩn đoán sơ bộ mã lỗi xe điện từ mô tả tự nhiên của khách hàng** | Khách hàng mô tả lỗi qua hotline/app bằng tiếng Việt đời thường (*"xe kêu cụp cụp khi qua gờ giảm tốc"*), nhân viên CSKH mất thời gian phân loại sang mã lỗi OBD-II. | Mất 15-20 phút/cuộc gọi; tỷ lệ phân loại sai xưởng dịch vụ ~18%, kéo dài thời gian chờ tiếp nhận tại xưởng. |
| **3** | **Vinhomes** | **Lặp lại** | **Phân loại & điều hướng phản ánh, khiếu nại cư dân trên App Resident** | Hàng nghìn phản ánh mỗi ngày (hỏng đèn hành lang, mất nước, tiếng ồn, đăng ký sửa chữa) được nhân viên ban quản lý đọc và phân loại thủ công từng ticket. | Thời gian phản hồi trung bình 12-24 giờ; 25% ticket bị chuyển nhầm bộ phận kỹ thuật / an ninh. |
| **4** | **Vinmec** | **Pain từ người khác** | **Soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary)** | Bác sĩ lâm sàng phải đọc lại toàn bộ kết quả xét nghiệm, chẩn đoán hình ảnh và diễn biến bệnh để tổng hợp thành bản tóm tắt xuất viện dễ hiểu cho bệnh nhân. | Mất 25-35 phút/bệnh nhân; bác sĩ phàn nàn quá tải hành chính, giảm thời gian khám bệnh trực tiếp. |
| **5** | **Vinpearl** | **Tốn thời gian** | **Xử lý email đặt phòng khách đoàn (Group Booking) phức tạp** | Đại lý lữ hành gửi email dài dòng nhiều yêu cầu đặc biệt (loại phòng, suất ăn, vé VinWonders), nhân viên sales phải so khớp quỹ phòng thủ công. | Mất 30-45 phút/báo giá; thời gian phản hồi chậm khiến khách đoàn chuyển sang đối thủ cạnh tranh. |
| **6** | **Xanh SM (GSM)** | **Lặp lại** | **Phân tích lý do khách hàng hủy chuyến và đánh giá 1-sao** | Hàng chục nghìn log hủy cuốc và ghi âm cuộc gọi mỗi tuần không được tổng hợp có cấu trúc để tìm nguyên nhân gốc (app lag, tài xế đón chậm, trôi định vị). | Mất 2 ngày/tuần của chuyên viên QA; báo cáo insight chậm 1 tuần so với thời gian thực. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

---

### 📇 QUICK PROBLEM CARD #1 (Selected Case — Điểm sáng vận hành Xanh SM)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                       │
│                                                                             │
│ Bài toán (1 câu): Tài xế Xanh SM báo sự cố cạn pin giữa đường, cần điều phối│
│ trạm sạc VinFast khả dụng gần nhất hoặc kích hoạt xe cứu hộ pin khẩn cấp.   │
│                                                                             │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes                  │
│                     [ ] Vinmec   [ ] Khác: ________________                │
│                                                                             │
│ Ai đang đau (Actor)?                                                        │
│ • Tài xế Xanh SM: Đang chở khách hoặc trên đường đón, xe sắp cạn pin.       │
│ • Điều phối viên (Dispatcher): Quá tải tra cứu GPS, Dashboard trạm sạc.     │
│                                                                             │
│ Workflow thủ công hiện tại (5 bước):                                        │
│   1. Tài xế gọi hotline điều vận báo sự cố pin / trạm sạc đầy.              │
│   ──> 2. Điều phối viên tra cứu vị trí GPS thực tế của xe trên hệ thống.    │
│   ──> 3. Mở Dashboard trạm sạc VinFast, tìm trụ sạc trống tương thích cổng. │
│   ──> 4. Soạn thảo tin nhắn SMS/App chỉ dẫn đường đi và gửi cho tài xế.     │
│   ──> 5. Nếu pin < 5% hoặc xe dừng hẳn, gọi điều phối xe cứu hộ pin.        │
│                                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                                            │
│ • Bước 3 & Bước 4 (⏱ 10 - 12 phút/lượt).                                   │
│   (Tra cứu trụ sạc tương thích cổng CCS2/GBT và gõ tin nhắn chỉ đường).    │
│                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                       │
│ • Hỗ trợ Bước 3 & Bước 4: Tự động tổng hợp vị trí GPS + Trạng thái trạm    │
│   sạc -> LLM tự động soạn thảo bản nháp chỉ dẫn (gắn nhãn [DRAFT_ONLY])     │
│   hoặc phát hiện pin < 5% để kích hoạt đề xuất xe sạc pin di động ngay.     │
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                        │
│ • Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút (Efficiency).       │
│ • Độ chính xác gợi ý trạm sạc còn trụ trống tương thích đạt >= 98%.         │
│                                                                             │
│ Quick Architecture:                                                         │
│ [ ] No AI        [ ] Rule        [x] LLM Feature        [ ] Agentic Loop    │
│ (Lý do: Cần LLM sinh nội dung chỉ dẫn linh hoạt, nhưng phải có Dispatcher   │
│ duyệt - Human-in-the-loop để đảm bảo an toàn tuyệt đối cho xe điện).        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 QUICK PROBLEM CARD #2 (Vinhomes Resident Feedback Triage)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                       │
│                                                                             │
│ Bài toán (1 câu): Phân loại tự động và điều hướng ticket phản ánh, khiếu nại│
│ của cư dân trên App Vinhomes Resident đến đúng ban quản lý chuyên trách.    │
│                                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes                  │
│                     [ ] Vinmec   [ ] Khác: ________________                │
│                                                                             │
│ Ai đang đau (Actor)?                                                        │
│ • Cư dân Vinhomes: Bức xúc vì gửi phản ánh sự cố mà nhiều giờ chưa hồi đáp. │
│ • Lễ tân / CSKH Ban quản lý: Quá tải vì phải đọc, gán nhãn hàng trăm ticket.│
│                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                        │
│   1. Cư dân gõ phản ánh qua App Vinhomes Resident.                          │
│   ──> 2. Nhân viên CSKH đọc nội dung, xác định tòa nhà và loại sự cố.       │
│   ──> 3. Tạo ticket nội bộ và gán thủ công sang Đội Kỹ thuật/An ninh/Cây xanh│
│   ──> 4. Soạn tin phản hồi xác nhận tiếp nhận cho cư dân.                   │
│                                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                                            │
│ • Bước 2 & Bước 3 (⏱ 4 - 8 tiếng chờ đợi xử lý hàng đợi ticket).            │
│                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                       │
│ • Bước 2 & Bước 3: Đọc hiểu văn bản tiếng Việt tự nhiên, trích xuất thực thể│
│   (Vị trí, Mức độ khẩn cấp, Phòng ban phụ trách) và tự động route ticket.   │
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                        │
│ • Giảm thời gian phân loại & xác nhận từ 12 giờ ──> dưới 10 phút.           │
│ • Tỉ lệ định tuyến đúng phòng ban chuyên trách đạt >= 92%.                  │
│                                                                             │
│ Quick Architecture:                                                         │
│ [ ] No AI        [ ] Rule        [x] LLM Feature        [ ] Agentic Loop    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 QUICK PROBLEM CARD #3 (VinFast Smart Charging Port & Station Advisor)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                       │
│                                                                             │
│ Bài toán (1 câu): Trợ lý ảo VinFast tự động tra cứu và gợi ý trạm sạc tương │
│ thích chuẩn cổng sạc (CCS2, GBT, AC) và công suất phù hợp theo từng dòng xe.│
│                                                                             │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes                  │
│                     [ ] Vinmec   [ ] Khác: ________________                │
│                                                                             │
│ Ai đang đau (Actor)?                                                        │
│ • Chủ xe VinFast (VF3, VF5, VF8, VF9): Loay hoay tìm trạm có trụ sạc nhanh  │
│   và đúng chuẩn cổng sạc hỗ trợ xe của mình khi đi đường dài.               │
│ • Tổng đài viên VinFast Hotline: Mất nhiều thời gian giải thích thủ công.   │
│                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                        │
│   1. Chủ xe gọi điện thoại hoặc gửi câu hỏi qua trợ lý màn hình xe.         │
│   ──> 2. Tổng đài viên xác nhận dòng xe, vị trí hiện tại và dung lượng pin. │
│   ──> 3. Tra cứu danh mục trạm sạc VinFast gần nhất có hỗ trợ chuẩn sạc xe. │
│   ──> 4. Hướng dẫn địa chỉ và trạng thái cổng sạc khả dụng cho tài xế.      │
│                                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                                            │
│ • Bước 2 & Bước 3 (⏱ 4 - 6 phút/cuộc gọi).                                  │
│                                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                                       │
│ • Bước 3 & Bước 4: Nhận diện dòng xe từ dữ liệu telemetry, tự động query   │
│   API bản đồ trạm sạc và trả kết quả trạm sạc tối ưu tức thì.               │
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                        │
│ • Thời gian gợi ý trạm sạc: từ 5 phút ──> dưới 5 giây.                      │
│ • 100% trạm sạc được gợi ý tương thích chuẩn sạc của dòng xe đang lái.      │
│                                                                             │
│ Quick Architecture:                                                         │
│ [ ] No AI        [x] Rule        [ ] LLM Feature        [ ] Agentic Loop    │
│ (Lý do: Phần lớn logic tra cứu trạm sạc tương thích cổng sạc là dữ liệu quan│
│ hệ có cấu trúc cố định; chỉ cần Rule + API Database Lookup là tối ưu).      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết định lựa chọn bài toán cho Deep-Dive & Lập trình Prompt

### ✅ Bài toán được chọn: **Card #1 — Hỗ trợ xử lý sự cố hết pin / trạm sạc Xanh SM (GSM)**

### ⚖️ Lập luận phân tích & so sánh:

1. **Vì sao chọn Card #1 (Xanh SM Sự cố sạc pin):**
   * **Giá trị thực tế khẩn cấp:** Sự cố cạn pin của taxi điện trên đường ảnh hưởng trực tiếp đến an toàn giao thông, gây tắc đường, trễ chuyến của hành khách và stress nặng nề cho tài xế.
   * **Ranh giới an toàn (Operational Boundary) cực kỳ rõ ràng và có thể kiểm thử bằng code:**
     * **Ranh giới 1:** Bắt buộc mọi tin nhắn hướng dẫn soạn thảo phải có tiền tố `[DRAFT_ONLY]` để điều phối viên duyệt trước khi gửi, ngăn chặn AI tự ý gửi chỉ dẫn sai lệch ra thực địa (Human-in-the-loop).
     * **Ranh giới 2:** Khi pin xe rơi vào mức nguy cấp (`< 5%`), AI **tuyệt đối không được** chỉ đường đến trạm sạc xa quá 5km, mà phải kích hoạt điều phối **Xe Sạc Pin Di Động (Mobile Charger Dispatch)**.
   * **Khả thi công nghệ cao:** Phối hợp giữa LLM Feature (xử lý ngôn ngữ tự nhiên tiếng Việt thân thiện) và Rule-based logic (ngưỡng pin 5%, khoảng cách 5km), hoàn toàn phù hợp để triển khai nguyên mẫu kỹ thuật trên **Gemini 2.5 Flash**.

2. **Vì sao không chọn hoặc hoãn lại các Card khác:**
   * **Card #2 (Vinhomes CSKH):** Mặc dù khối lượng công việc lớn, nhưng rủi ro pháp lý về tranh chấp nhà ở, phí dịch vụ và quyền sở hữu đòi hỏi chính sách bảo mật nội bộ và quy trình kiểm duyệt phức tạp hơn. Cần chuẩn hóa dữ liệu CRM trước khi đưa AI vào.
   * **Card #3 (VinFast Trạm sạc):** Bài toán tra cứu cổng sạc cơ bản phù hợp hơn với **Rule-based API Query** (SQL / Map Engine). Việc dùng LLM thuần túy cho bài toán này là lạm dụng công nghệ (Over-engineering), dễ sinh hallucination về vị trí địa lý.

### 🏁 Đánh giá quyết định: **GO** (Sẵn sàng cho Phase 3 Deep-Dive và Phase 4 Code Prototype).
