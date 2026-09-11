# 📑 02 — Problem Deep-Dive Report: Xanh SM Intelligent Dispatcher Co-pilot

> **Học phần:** Lab 02 — AI Product Scoping (Vin Smart Future)  
> **Đơn vị:** Vin Smart Future — Khối Công Nghệ Tập Đoàn Vingroup  
> **Bộ phận thụ hưởng:** Khối Vận Hành Taxi Điện — Xanh SM (GSM)  
> **Người thực hiện:** AI Product Engineer  
> **Trạng thái phê duyệt:** **GO (Approved for Implementation)**  

---

## 🏛️ 1. Bối cảnh dự án (Project Context)

Tôi là AI Product Engineer tại **Vin Smart Future**. Đơn vị chúng tôi được giao trọng trách phối hợp chặt chẽ với Khối Vận Hành của **GSM (Xanh SM)** nhằm tối ưu hóa hiệu suất điều vận đội xe taxi điện tại các đô thị lớn (Hà Nội, TP.HCM, Đà Nẵng).

Qua khảo sát thực tế tại **Trung tâm Điều vận Xanh SM Hà Nội**, các Điều phối viên (Dispatchers) đang chịu áp lực quá tải nghiêm trọng trong việc xử lý các tình huống khẩn cấp liên quan đến **sự cố pin cạn kiệt (< 10%) và trạm sạc VinFast quá tải / hỏng trụ** trong giờ cao điểm. Việc tra cứu và soạn thảo chỉ dẫn hoàn toàn bằng tay dẫn đến thời gian chờ đợi kéo dài, tài xế hoang mang, xe có nguy cơ chết máy giữa đường gây ùn tắc giao thông và ảnh hưởng tiêu cực đến uy tín thương hiệu Vingroup.

Báo cáo Deep-Dive này phân tích chi tiết quy trình hiện tại, xác lập ranh giới vận hành, đề xuất kiến trúc AI phù hợp và đưa ra quyết định triển khai.

---

# 🏗️ Gate 1 — Current-State Workflow Mapping (20 Điểm)

### 1.1. Sơ đồ quy trình thủ công hiện tại (5 bước)

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │     │ Tra cứu định │     │ Tra cứu trạm │     │ Soạn thảo    │
│ gọi sự cố    │ ──> │ vị GPS xe    │ ──> │ sạc VinFast  │ ──> │ tin chỉ dẫn  │
│              │     │              │     │ còn trụ trống│     │ gửi tài xế   │
│ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │
│ ⏱ 2 phút     │     │ ⏱ 2 phút     │     │ ⏱ 5 phút 🔴  │     │ ⏱ 5 phút 🔴  │
│ In: Hotline  │     │ In: Biển số  │     │ In: Vị trí   │     │ In: Tra cứu  │
│ Out: Log sự cố│    │ Out: Toạ độ  │     │ Out: Địa chỉ │     │ Out: SMS     │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                     │
                                                                     ▼
                                                              ┌──────────────┐
                                                              │ Bước 5       │
                                                              │ Gọi xe cứu   │
                                                              │ hộ pin (nếu  │
                                                              │ pin < 5%)    │
                                                              │ Ai: Dispatch │
                                                              │ ⏱ 1 phút     │
                                                              └──────────────┘
🔴 = Điểm nghẽn nghiêm trọng (Bottleneck)
⏱ Tổng thời gian xử lý trung bình: 15 phút / sự cố.
```

### 1.2. Bảng phân tích chi tiết từng bước & Điểm chuyển giao (Handoffs)

| Bước | Tác vụ | Người thực hiện | Dữ liệu đầu vào (Input) | Dữ liệu đầu ra (Output) | Thời gian (⏱) | Điểm chuyển giao (Handoff) & Bottleneck |
|---|---|---|---|---|---|---|
| **1** | Tiếp nhận cuộc gọi khẩn cấp | Dispatcher | Cuộc gọi từ tài xế qua tổng đài điều vận | Bản ghi sự cố: Biển số xe, dòng xe (VF5/e34/VF8), % pin hiện tại | 2 phút | 🔄 Handoff từ Tài xế $\rightarrow$ Dispatcher. |
| **2** | Định vị xe thực địa | Dispatcher | Biển số xe | Tọa độ GPS thời gian thực trên bản đồ nội bộ Fleet Management | 2 phút | 🔄 Handoff giữa Hotline $\rightarrow$ Phần mềm Fleet Tracking. |
| **3** | Tra cứu trụ sạc VinFast khả dụng | Dispatcher | Tọa độ GPS xe, dòng xe (chuẩn cổng CCS2/GBT) | Địa chỉ trạm sạc gần nhất còn trụ trống phù hợp | **5 phút 🔴** | **🔴 Bottleneck 1:** Phải mở song song Dashboard V-GREEN/VinFast, lọc thủ công loại trụ sạc còn trống và phù hợp công suất xe. |
| **4** | Soạn tin nhắn hướng dẫn đường đi | Dispatcher | Địa chỉ trạm sạc, ghi chú đường đi | Tin nhắn SMS / App Driver Notification | **5 phút 🔴** | **🔴 Bottleneck 2:** Gõ tin nhắn văn bản tiếng Việt có dấu thủ công trên bàn phím, dễ gõ sai địa chỉ hoặc quên lưu ý đường cấm xe taxi. |
| **5** | Kích hoạt xe cứu hộ pin (nếu pin < 5%) | Dispatcher | Tình trạng pin cạn kiệt nguy cấp | Cuộc gọi / Lệnh điều xe Mobile Charger | 1 phút | 🔄 Handoff Dispatcher $\rightarrow$ Đội cứu hộ pin lưu động. |

---

# 🎯 Gate 2 — Problem Statement (6-Field) & Metrics (20 Điểm)

| STT | Trường thông tin (Field) | Nội dung chi tiết chuẩn Vin Smart Future |
|:---:|---|---|
| **1** | **Actor / Operator** | **Điều phối viên (Dispatcher)** thuộc Trung tâm Điều vận Xanh SM (GSM), chịu trách nhiệm giám sát và hỗ trợ trực tiếp 24/7 cho đội xe taxi điện. |
| **2** | **Current Workflow** | Khi tài xế báo cạn pin hoặc trạm sạc quá tải, điều phối viên thực hiện 5 bước thủ công: nghe điện thoại, tra cứu định vị GPS xe, mở bản đồ trạm sạc VinFast tìm trụ trống, gõ tin nhắn chỉ dẫn gửi qua App tài xế, và gọi xe cứu hộ nếu xe báo pin dưới 5%. |
| **3** | **Bottleneck** | **Bước 3 & 4 (chiếm 10/15 phút):** Tra cứu thủ công sự tương thích giữa chuẩn cổng sạc của từng dòng xe (VF5, VF8, VF9) với trụ sạc trống, và soạn thảo văn bản chỉ đường chi tiết bằng tiếng Việt. |
| **4** | **Business Impact** | • Trung bình **80-100 sự cố pin/ngày** tại Hà Nội & TP.HCM.<br>• Lãng phí **20-25 giờ công/ngày** của đội ngũ điều phối viên.<br>• Tài xế phải chờ đợi lâu dẫn đến trễ chuyến, hủy cuốc, gây thiệt hại ước tính **~15% doanh thu ca chạy** và rủi ro xe dừng giữa đường gây ách tắc giao thông. |
| **5** | **Success Metric** | 1. **Hiệu suất vận hành (Efficiency):** Giảm thời gian xử lý sự cố từ **15 phút xuống dưới 3 phút/lượt** (giảm 80%).<br>2. **Độ chính xác nghiệp vụ (Quality):** Đạt tỷ lệ **$\ge 98\%$** gợi ý đúng trạm sạc còn trụ trống tương thích cổng sạc.<br>3. **Mức độ hài lòng của tài xế (CSAT):** Tăng điểm đánh giá hỗ trợ từ 3.2 lên $\ge 4.5/5.0$. |
| **6** | **Operational Boundary** | • **Được phép:** Tự động tổng hợp dữ liệu GPS xe, truy vấn API trạm sạc VinFast khả dụng, và soạn thảo tin nhắn chỉ dẫn.<br>• **CẤM TUYỆT ĐỐI (Boundary 1):** AI không được tự ý bắn tin nhắn ra thực địa mà không có tiền tố **`[DRAFT_ONLY]`** và bắt buộc phải qua sự phê duyệt của Dispatcher (Bắt buộc Human-in-the-loop).<br>• **CẤM TUYỆT ĐỐI (Boundary 2):** Nếu pin xe báo **$< 5\%$**, AI tuyệt đối không được hướng dẫn tài xế đến trạm sạc xa quá $5\text{km}$. AI phải tự động trả về lệnh điều xe cứu hộ pin lưu động: `{"action": "dispatch_mobile_charger", "reason": "<explain_why>"}`. |

---

# 🤖 Gate 3 — Future-State Flow & AI Fit (10 Điểm)

### 3.1. Ma trận phân tích lựa chọn kiến trúc (AI-Fit Matrix)

| Tiêu chí so sánh | Rule-based Code | **LLM Feature (Được chọn)** | Autonomous Multi-Agent |
|---|---|---|---|
| **Khả năng xử lý ngôn ngữ** | Rập khuôn, cứng nhắc, khó xử lý mô tả đa dạng của tài xế | **Xuất sắc, sinh lời dặn dò thân thiện, chi tiết, phù hợp ngữ cảnh** | Dư thừa năng lực, khó kiểm soát |
| **Độ phức tạp tích hợp** | Thấp | **Vừa phải, dễ nhúng vào hệ thống Dispatch sẵn có** | Rất cao, khó debug |
| **Độ an toàn & Ranh giới** | Rất cao nhưng không linh hoạt | **Kiểm soát chặt chẽ qua System Prompt & HITL** | Nguy cơ tự hành sai lệch cao |
| **Chi phí vận hành (Token)** | 0$ | **Rất thấp (Gemini 2.5 Flash tối ưu chi phí)** | Cao do nhiều vòng suy luận loop |
| **Kết luận** | Loại (không xử lý được prompt chỉ dẫn tự nhiên) | **CHỌN (Tối ưu nhất cho bài toán Co-pilot)** | Loại (rủi ro an toàn điều vận) |

### 3.2. Sơ đồ quy trình tương lai (Future-State Flow with HITL & Fallback)

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc    │     │ 🔵 Auto-pull │     │ 🔵 AI sinh   │     │ 🟢 Dispatch  │
│ gọi sự cố    │ ──> │ vị trí GPS & │ ──> │ bản nháp chỉ │ ──> │ duyệt 1-click│
│              │     │ trạm sạc API │     │ dẫn kèm tag  │     │ & gửi App TX │
│ Ai: Dispatch │     │              │     │ [DRAFT_ONLY] │     │              │
│ ⏱ 1 phút     │     │ ⏱ 5 giây     │     │ ⏱ 5 giây     │     │ ⏱ 30 giây    │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                 │
                                                 ▼ (Nếu pin < 5%)
                                          ┌──────────────┐
                                          │ 🔵 Trigger   │
                                          │ cứu hộ pin:  │
                                          │ dispatch_    │
                                          │ mobile_      │
                                          │ charger      │
                                          └──────────────┘
                                                 │
                                                 ▼ (Nếu AI gặp sự cố / Timeout)
                                          ↩️ Fallback:
                                          Hệ thống hiển thị danh sách trạm thô,
                                          Dispatcher gõ tin nhắn tay như cũ.
```

* 🔵 **AI Steps:** Tự động gọi API trích xuất GPS và trạng thái trạm sạc V-GREEN; LLM (Gemini 2.5 Flash) tổng hợp và sinh tin nhắn chỉ dẫn thân thiện kèm tiền tố `[DRAFT_ONLY]`.
* 🟢 **Human-in-the-Loop (HITL):** Điều phối viên chỉ cần đọc lướt, kiểm tra thực địa trong 15-30 giây và nhấn nút "Phê duyệt & Gửi".
* ↩️ **Fallback Plan:** Nếu Gemini API timeout (> 5s) hoặc trả về lỗi, hệ thống tự động fallback về màn hình danh sách trạm sạc thô để Dispatcher xử lý thủ công, đảm bảo 0% gián đoạn dịch vụ.

---

# ⚖️ Gate 4 — Decision Quality & Risk Assessment (10 Điểm)

### 4.1. Quyết định: **GO (Triển khai ngay)**

Dự án hội đủ cả 3 trụ cột thành công:
1. **Desirability (Nhu cầu bức thiết):** Giảm tải trực tiếp cho điều phối viên và bảo vệ an toàn cho hàng nghìn tài xế Xanh SM mỗi ngày.
2. **Feasibility (Khả thi công nghệ):** Kiến trúc LLM Feature với Gemini 2.5 Flash đã được kiểm chứng bằng mã nguồn nguyên mẫu `prompt_prototype.py`, vượt qua toàn bộ các bài test ranh giới an toàn.
3. **Viability (Hiệu quả kinh tế):** Tiết kiệm ~25 giờ công/ngày, giảm tỉ lệ hủy chuyến giờ cao điểm, thu hồi vốn đầu tư (ROI) trong vòng dưới 2 tháng.

### 4.2. Bảng quản trị rủi ro & giải pháp giảm thiểu

| Rủi ro tiềm ẩn (Risk) | Mức độ | Kịch bản sự cố | Giải pháp giảm thiểu (Mitigation) |
|---|:---:|---|---|
| **Hallucination trạm sạc** | Cao | AI tự bịa ra trạm sạc không có thật hoặc đã ngừng hoạt động. | **RAG/API Injection:** Chỉ cho phép AI sử dụng danh sách trạm sạc được truy xuất từ API chính thức của VinFast/V-GREEN. |
| **Gửi nhầm chỉ dẫn sai** | Rất cao | AI gửi tin đi khi chưa kiểm tra đường cấm hoặc trạm đã kín chỗ. | **Bắt buộc HITL qua tag `[DRAFT_ONLY]`:** Hệ thống chặn tầng API, không có chữ ký duyệt của Dispatcher thì không thể phát tin. |
| **Cạn pin giữa đường** | Nghiêm trọng | Xe còn dưới 5% pin nhưng AI vẫn điều xe đi trạm sạc xa 8km. | **Hard Boundary Code Assertion:** Quy tắc cứng trong System Prompt và Regex filter: pin < 5% tự động kích hoạt `dispatch_mobile_charger`. |
| **API Gemini bị gián đoạn** | Trung bình | Mất kết nối internet hoặc API Gemini quá tải. | **Graceful Fallback:** Tự động chuyển về giao diện tra cứu bảng biểu thủ công truyền thống trong vòng 3 giây. |

---

## 🏁 Kết luận

Dự án **Xanh SM Intelligent Dispatcher Co-pilot** là một case study điển hình của Vin Smart Future trong việc kết hợp hài hòa giữa **Sức mạnh ngôn ngữ của LLM** và **Ranh giới an toàn nghiêm ngặt (Operational Boundaries)**, mang lại giá trị thực tiễn to lớn cho hệ sinh thái Vingroup.
