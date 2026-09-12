# 02 — Deep-Dive Report | Lab 02: AI Product Scoping (Vin Smart Future)

> **Bài toán được chọn:** Card #3 — **VinFast: Trợ lý lập hồ sơ yêu cầu bảo hành (Warranty Claim Co-pilot)**
> **Nội dung:** Phase 3 (DEEP-DIVE) + Phase 5 (EVALUATE)

---

## 🗳️ Vì sao nhóm chọn bài toán này?

Ở Phase 2, đề xuất ban đầu của nhóm là **Card #1 (Vinhomes — số hóa biên bản nghiệm thu)**. Sau khi chạy stress-test đóng vai CFO/Trưởng phòng Vận hành, đề xuất đó **đã bị bác bỏ**: danh mục lỗi bàn giao là một tập hợp đóng ~60–120 mục, nên **một app checklist (dropdown) giải quyết được ~70% giá trị mà không cần AI**. Chi tiết ở `01-problem-scan.md`.

Card #3 là thẻ **duy nhất sống sót** qua đòn phản biện *"tại sao không dùng rule-based/dropdown cho rẻ?"*, vì:

| | Vinhomes (Card #1) | VinFast Warranty (Card #3) |
|---|---|---|
| Kích thước không gian lựa chọn | ~60–120 mục lỗi | **Hàng nghìn** mã part + mã labor |
| Cách chọn đúng | Nhìn là biết → **dropdown** | Phải **đọc hiểu diễn giải kỹ thuật rồi suy luận** |
| Baseline có sẵn không? | Chưa đo, phải dựng từ đầu | **Có sẵn** — `first-pass yield` là chỉ số hãng đã theo dõi |
| Đầu vào phi cấu trúc là tất yếu? | ❌ Không — do quy trình tự tạo ra | ✅ **Có** — lời kể của khách và diễn giải kỹ thuật vốn là văn bản tự do |

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping

**Quy trình lập hồ sơ bảo hành hiện tại tại một xưởng dịch vụ VinFast** *(chỉ tính phần hành chính hồ sơ, không tính thời gian sửa chữa vật lý)*

```text
┌───────────────┐   ┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ Bước 1        │   │ Bước 2        │   │ Bước 3        │   │ Bước 4    🔴  │
│ Tiếp nhận xe, │   │ Chẩn đoán:    │   │ Sửa chữa      │   │ Viết diễn    │
│ ghi lời kể    │──▶│ cắm máy, đọc  │──▶│ thực tế       │──▶│ giải 3C      │
│ của khách     │🔄 │ mã lỗi DTC    │   │               │ 🔄│ (Complaint-  │
│               │   │               │   │               │   │ Cause-Correc)│
│ Ai: Cố vấn DV │   │ Ai: KTV       │   │ Ai: KTV       │   │ Ai: KTV      │
│ ⏱ 5 phút      │   │ ⏱ 15 phút     │   │ ⏱ biến thiên  │   │ ⏱ 10 phút 🔴 │
│ In: Lời khách │   │ In: Phiếu RO  │   │ In: Chẩn đoán │   │ In: Ghi chú  │
│    (tiếng Việt│   │ Out: Mã DTC   │   │ Out: Xe đã sửa│   │    rời rạc   │
│     đời thường)│  │               │   │               │   │ Out: Văn bản │
│ Out: Phiếu RO │   │               │   │               │   │    tự do     │
└───────────────┘   └───────────────┘   └───────────────┘   └───────────────┘
                                                                    │
        ┌───────────────────────────────────────────────────────────┘
        ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────────────────────────┐
│ Bước 5    🔴  │   │ Bước 6        │   │ Bước 7                            │
│ Tra & chọn    │   │ Gửi claim lên │   │ Hãng review claim                 │
│ causal part   │──▶│ hệ thống      │──▶│  ├─ Duyệt (85%) ──▶ Hoàn tiền     │
│ code + labor  │ 🔄│ warranty hãng │ 🔄│  └─ TỪ CHỐI (15%) ──▶ trả về      │
│ operation code│   │               │   │      ↻ KTV sửa lại (+20 phút)     │
│               │   │               │   │      ↻ Chu kỳ chờ 3–7 NGÀY        │
│ Ai: KTV       │   │ Ai: KTV/CVDV  │   │ Ai: Bộ phận Warranty của hãng     │
│ ⏱ 8 phút 🔴   │   │ ⏱ 2 phút      │   │ ⏱ 3–7 ngày                        │
│ In: Diễn giải │   │ In: Hồ sơ đủ  │   │ In: Claim                         │
│ Out: 2 mã số  │   │ Out: Claim ID │   │ Out: Duyệt / Từ chối + lý do      │
└───────────────┘   └───────────────┘   └───────────────────────────────────┘

🔴 Bottleneck   🔄 Handoff (chuyển giao người ↔ người / người ↔ hệ thống)

⏱ TỔNG THỜI GIAN HÀNH CHÍNH: 5 + 15 + 10 + 8 + 2 = 40 phút/lượt
   Trong đó phần KTV làm hồ sơ (bước 4+5+6): 20 phút/lượt
   Riêng 2 bottleneck (bước 4+5):            18 phút/lượt  ← 45% tổng thời gian
   Nếu claim bị từ chối: +20 phút làm lại và +3–7 ngày chậm dòng tiền
```

### Phân tích 4 handoff và vì sao chúng gây rò rỉ

| # | Handoff | Thông tin bị mất ở điểm chuyển giao |
|---|---|---|
| 🔄 1 | Cố vấn DV → KTV | Lời kể sinh động của khách (*"đi qua gờ giảm tốc kêu cụp cụp"*) bị rút gọn thành một dòng ngắn trên phiếu RO. Thông tin chẩn đoán quý nhất **bốc hơi ngay bước đầu**. |
| 🔄 2 | KTV (sửa xong) → viết hồ sơ | KTV viết diễn giải **sau khi** đã sửa xong, nhiều khi cuối ca, dựa vào trí nhớ → diễn giải sơ sài, thiếu liên kết nhân quả. |
| 🔄 3 | KTV → hệ thống hãng | KTV là **kỹ sư giỏi tay nghề, không phải người viết tốt**. Hãng lại chấm claim dựa trên **chất lượng văn bản**. Đây là sự lệch pha năng lực gốc rễ của bài toán. |
| 🔄 4 | Xưởng → Bộ phận Warranty | Phản hồi từ chối quay về sau 3–7 ngày, khi KTV đã quên chi tiết ca sửa đó → làm lại càng kém chất lượng. |

> 💡 **Nhận định cốt lõi của nhóm:** đây **không** phải bài toán "nhân viên làm chậm". Đây là bài toán **lệch pha năng lực**: hệ thống bảo hành đòi hỏi kỹ năng viết kỹ thuật và kỹ năng tra cứu mã, trong khi người được giao việc lại được tuyển và đào tạo để sửa xe. AI đúng chỗ ở đây vì nó **bù đúng vào khoảng lệch đó**, không phải để "làm cho nhanh hơn".

---

## 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | **Kỹ thuật viên bảo hành (KTV)** tại xưởng dịch vụ/đại lý ủy quyền VinFast — người trực tiếp viết diễn giải và chọn mã. Phụ: **Cố vấn dịch vụ** (tiếp nhận, gửi claim) và **Bộ phận Warranty của hãng** (người review). |
| **2. Current Workflow** | 7 bước, hoàn toàn thủ công ở khâu hồ sơ. Công cụ đang dùng: hệ thống **DMS/Warranty Portal** của hãng, **máy chẩn đoán** đọc mã DTC, và **danh mục mã part/labor** dạng bảng tra cứu. KTV tự gõ diễn giải 3C bằng tiếng Việt và tự tìm mã trong danh mục hàng nghìn dòng. Tổng hành chính **40 phút/lượt**, riêng khâu hồ sơ **20 phút/lượt**. |
| **3. Bottleneck** | **Bước 4 (viết diễn giải 3C — 10 phút)** và **Bước 5 (chọn causal part code + labor op code — 8 phút)**, chiếm **18/40 phút (45%)**. Đây cũng là nguồn gốc của **~15% claim bị từ chối vòng đầu**: diễn giải không chứng minh được quan hệ nhân quả, hoặc chọn nhầm mã gần giống. Đây chính là khâu **cần xử lý ngôn ngữ tự nhiên nhiều nhất** trong toàn quy trình. |
| **4. Business Impact** | *(ước tính — xem phần Giả định)* Với ~**400 claim/ngày** trên toàn hệ thống: <br>• **~133 giờ/ngày** KTV làm hồ sơ thay vì sửa xe (20 phút × 400).<br>• **~21.000 claim/năm bị từ chối vòng đầu** (15%), mỗi claim tốn thêm ~20 phút làm lại → **~7.000 giờ/năm** công làm lại.<br>• **Dòng tiền:** mỗi claim bị từ chối kéo dài chu kỳ hoàn tiền thêm **3–7 ngày**, ảnh hưởng trực tiếp vốn lưu động của xưởng/đại lý.<br>• **Chi phí cơ hội lớn nhất:** giờ công KTV là **năng lực khan hiếm** — mỗi giờ làm hồ sơ là một giờ không có xe nào được sửa, kéo dài thời gian chờ của khách. |
| **5. Success Metric** | **M1 (chính — tài chính):** `First-pass yield` của claim tăng từ **85% → ≥ 95%** trong 3 tháng.<br>**M2 (chính — vận hành):** Thời gian KTV làm hồ sơ giảm từ **20 phút → dưới 8 phút/claim**.<br>**M3 (chất lượng mô hình):** Mã đúng nằm trong **Top-3 gợi ý** của AI đạt **≥ 90%**; và **≥ 80%** số claim có mã đúng ở **vị trí Top-1**.<br>**M4 (an toàn):** **100%** claim gửi đi có dấu vết KTV đã xác nhận mã — không có claim nào do AI tự chọn mã mà không ai duyệt.<br>**M5 (chống gian lận metric):** tỉ lệ claim bị hãng **thu hồi sau kiểm toán (clawback)** **không tăng** so với baseline. *(Metric này bắt buộc phải có — nếu thiếu, nhóm có thể "đạt" M1 bằng cách dạy AI viết claim khéo hơn để lọt cửa review, chứ không phải claim đúng hơn.)* |
| **6. Operational Boundary** | ✅ **AI ĐƯỢC PHÉP:** đọc lời kể khách + mã DTC + ghi chú sửa chữa; soạn **BẢN NHÁP** diễn giải 3C có gắn thẻ `[DRAFT_ONLY]`; truy xuất (RAG) danh mục mã và kho claim lịch sử đã được duyệt; **gợi ý Top-3 mã** kèm **độ tin cậy** và **trích dẫn claim tương tự** làm căn cứ.<br><br>🚫 **AI TUYỆT ĐỐI KHÔNG ĐƯỢC:** tự gửi claim lên hệ thống hãng; tự chọn mã cuối cùng thay KTV; **bịa ra quan hệ nhân quả kỹ thuật** không có trong dữ liệu chẩn đoán — nếu thiếu căn cứ phải trả về `"insufficient_evidence"` thay vì viết cho có; đề xuất mã chỉ vì mã đó **hay được duyệt** (đây là cửa dẫn tới gian lận bảo hành); chỉnh sửa hay lược bớt lời kể gốc của khách.<br><br>🟢 **ĐIỂM BẮT BUỘC DUYỆT (HITL):** (1) KTV xác nhận mã cuối cùng — **không có nút "duyệt tất cả"**; (2) claim có giá trị vượt ngưỡng hoặc độ tin cậy AI < 0.7 → bắt buộc **Cố vấn dịch vụ duyệt lần hai**. |

---

## 3.3. Future-State Flow & AI Fit

### Xác định mức AI Fit (AI-Fit Matrix)

| Mức | Chọn? | Lý do |
|---|:--:|---|
| **Rule / State-Machine** | ⚠️ **Một phần** | Dùng RULE cho: lọc danh mục mã theo dòng xe + mã DTC, kiểm tra tính hợp lệ của mã, xếp hạng thống kê *"mã hay dùng nhất cho DTC này"*. **Phần này phải làm TRƯỚC và làm rẻ** — nó tự nó đã giải quyết được các ca phổ biến. |
| **LLM Feature** | ✅ **CHỌN** | Phần rule không làm được: **đọc hiểu lời kể tiếng Việt đời thường của khách**, **soạn diễn giải 3C có lập luận nhân quả**, và **suy luận từ mô tả kỹ thuật ra mã ở phần đuôi dài (long tail)**. Kết hợp **RAG** trên kho claim lịch sử đã duyệt. |
| **Agentic Loop** | ❌ **KHÔNG** | Quy trình **cố định, tuyến tính**, không cần mô hình tự lập kế hoạch nhiều bước hay tự gọi công cụ vòng lặp. Dùng Agent ở đây chỉ làm tăng bề mặt rủi ro và chi phí mà không thêm giá trị. Đúng tinh thần *"Problem First, AI Second"*. |

> **Kết luận AI Fit: `LLM Feature + RAG`, đặt TRÊN một lớp Rule engine.**

### Future-State Flow

```text
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ Bước 1        │   │ Bước 2        │   │ Bước 3        │
│ Tiếp nhận xe, │   │ Chẩn đoán:    │   │ Sửa chữa      │
│ ghi lời kể    │──▶│ đọc mã DTC    │──▶│ thực tế       │
│ khách (GIỮ    │   │ (tự động đẩy  │   │ (KTV ghi chú  │
│ NGUYÊN VĂN)   │   │ vào hệ thống) │   │ ngắn, giọng   │
│ Ai: Cố vấn DV │   │ Ai: KTV+Máy   │   │ nói cũng được)│
│ ⏱ 5 phút      │   │ ⏱ 15 phút     │   │ Ai: KTV       │
└───────────────┘   └───────────────┘   └───────────────┘
                                                │
        ┌───────────────────────────────────────┘
        ▼
┌─────────────────────────┐   ┌─────────────────────────┐
│ Bước 4  🔵 AI STEP      │   │ Bước 5  🔵 AI STEP      │
│ LLM đọc: lời kể khách + │   │ RULE lọc danh mục theo  │
│ mã DTC + ghi chú KTV    │──▶│ dòng xe & DTC, rồi RAG  │
│ → soạn NHÁP diễn giải   │   │ truy xuất claim lịch sử │
│ 3C, gắn [DRAFT_ONLY]    │   │ đã duyệt → gợi ý TOP-3  │
│ ⏱ ~15 giây              │   │ mã + độ tin cậy + lý do │
│                         │   │ ⏱ ~10 giây              │
│ ↩️ Nếu thiếu căn cứ →   │   │ ↩️ Nếu tin cậy < 0.7 →  │
│ trả "insufficient_      │   │ KHÔNG gợi ý, chuyển     │
│ evidence", KHÔNG bịa    │   │ thẳng sang tra tay      │
└─────────────────────────┘   └─────────────────────────┘
                                          │
        ┌─────────────────────────────────┘
        ▼
┌─────────────────────────┐   ┌─────────────────────────┐
│ Bước 6  🟢 HUMAN (HITL) │   │ Bước 7                  │
│ KTV đọc nháp, sửa nếu   │──▶│ Gửi claim lên hệ thống  │
│ cần, CHỌN MÃ cuối cùng  │   │ hãng                    │
│ (không có "duyệt tất cả")│  │ Ai: KTV / Cố vấn DV     │
│ Ai: KTV                 │   │ ⏱ 2 phút                │
│ ⏱ ~6 phút               │   │                         │
│                         │   │ Kỳ vọng: first-pass     │
│ 🟢 Nếu tin cậy < 0.7    │   │ yield 85% → ≥95%        │
│ HOẶC giá trị claim lớn  │   │ ⇒ vòng lặp từ chối      │
│ → Cố vấn DV duyệt lần 2 │   │   3–7 ngày giảm mạnh    │
└─────────────────────────┘   └─────────────────────────┘

🔵 AI Step   🟢 Human Step (HITL)   ↩️ Fallback

⏱ TỔNG HÀNH CHÍNH MỚI: 5 + 15 + ~0,5 + 6 + 2 ≈ 28,5 phút/lượt
   Riêng khâu hồ sơ của KTV: 20 phút ──▶ ~6,5 phút (đạt mục tiêu M2 < 8 phút)
```

### Cơ chế Fallback (bắt buộc, 3 tầng)

| Tình huống | Fallback |
|---|---|
| LLM trả JSON sai định dạng / lỗi parse | Hệ thống **im lặng bỏ qua gợi ý**, hiển thị form tra cứu thủ công như cũ. **Tuyệt đối không hiển thị nội dung lỗi cho KTV** để tránh KTV copy nhầm. |
| Độ tin cậy < 0.7 | Không gợi ý mã. Chỉ hiện thông báo *"Không đủ căn cứ — vui lòng tra thủ công"*. **Thà không gợi ý còn hơn gợi ý sai** — vì gợi ý sai có độ tin cậy cao là thứ khiến KTV bấm duyệt theo quán tính. |
| API Gemini/LLM sập | Quy trình **thoái lui hoàn toàn về thủ công**. Hệ thống cũ **không được gỡ bỏ** trong ít nhất 2 quý đầu. |
| AI trả `insufficient_evidence` | Hiện rõ lý do thiếu căn cứ gì (*"không có mã DTC"*, *"ghi chú sửa chữa trống"*) để KTV bổ sung — biến fallback thành **hướng dẫn cải thiện dữ liệu đầu vào**. |

---

# 🏁 Phase 5 — EVALUATE

## 5.1. Stress-test Card #3 trước khi quyết định

Nhóm áp dụng đúng phương pháp đã dùng để loại Card #1 — tự tấn công thẻ mình vừa chọn:

| # | Phản biện (CFO / Trưởng phòng Vận hành) | Đánh giá & xử lý |
|---|---|---|
| 1 | *"Anh huấn luyện AI trên claim lịch sử **đã được duyệt**. Nhưng claim được duyệt ≠ claim đúng — trong đó có cả những claim sai mà hãng sót. Anh đang dạy mô hình **tái tạo lỗi đã lọt lưới**."* | 🟥 **Thắng. Đòn nguy hiểm nhất.** Xử lý: kho RAG **chỉ lấy** claim đã duyệt **VÀ đã thanh toán VÀ đã qua cửa sổ kiểm toán**, **loại bỏ** mọi claim từng bị thu hồi (clawback). Thêm **M5** vào bộ metric để giám sát đúng rủi ro này. |
| 2 | *"First-pass yield tăng từ 85% lên 95% — làm sao anh biết là nhờ AI chứ không phải nhờ giao diện mới?"* | 🟥 **Thắng.** Xử lý: triển khai dạng **A/B theo xưởng** (một nhóm xưởng dùng AI, nhóm đối chứng chỉ đổi giao diện), tối thiểu 4 tuần, thay vì so sánh trước–sau. |
| 3 | *"Sao không làm một **ô tìm kiếm tốt hơn** + xếp hạng 'mã hay dùng nhất cho DTC này'? Thuần thống kê, không cần LLM."* | 🟧 **Thắng một phần — và nhóm chấp nhận.** Ước tính lớp rule/thống kê này lấy được **~50% giá trị** với chi phí rất thấp. ⇒ Nhóm **đưa nó vào Giai đoạn 1 và làm trước**; LLM chỉ phụ trách phần rule bất lực: **soạn diễn giải 3C** và **phần đuôi dài của mã**. Điều này làm **thu hẹp scope AI**, và đó là kết quả tốt. |
| 4 | *"Tại sao không cấm KTV viết ẩu, ép họ viết đủ ý bằng form bắt buộc?"* | ⬜ **Không thắng.** Form bắt buộc chỉ chuyển gánh nặng chứ không giảm: KTV vẫn phải tự nghĩ ra nội dung, chỉ khác là bị chặn không cho gửi. Rủi ro thực tế là KTV gõ cho có để qua cửa. Bản chất bài toán là **lệch pha năng lực**, không phải thiếu kỷ luật. |

## 5.2. AI Readiness Checklist

| # | Tiêu chí | Đánh giá của nhóm |
|---|---|---|
| 1 | **Có sẵn dữ liệu mẫu/logs sạch để test?** | ✅ **CÓ — đây là điểm mạnh nhất của bài toán này.** Hệ thống warranty của hãng vốn đã lưu **toàn bộ claim lịch sử** kèm nhãn duyệt/từ chối và **lý do từ chối**. Đây là tập dữ liệu **có nhãn sẵn, miễn phí** — không phải đi gán nhãn thủ công. ⚠️ Điều kiện: phải lọc theo nguyên tắc ở phản biện #1. |
| 2 | **Rủi ro khi AI sai có nằm trong tầm kiểm soát?** | ✅ **CÓ.** Đầu ra luôn là **bản nháp**; KTV **bắt buộc** chọn mã cuối; có ngưỡng tin cậy 0.7; có fallback 3 tầng; claim giá trị lớn cần duyệt hai lớp. Rủi ro tệ nhất là **claim bị từ chối như hiện nay** — tức là quay về baseline, không tạo ra thiệt hại mới. ⚠️ Rủi ro còn lại cần giám sát: **gian lận bảo hành do AI tối ưu "khả năng được duyệt"** → đã chặn bằng ranh giới và M5. |
| 3 | **Stakeholders sẵn sàng thay đổi quy trình?** | ⚠️ **CHƯA CHẮC — đây là rủi ro lớn nhất còn lại.** KTV có động lực rõ (đỡ việc giấy tờ, được hoàn tiền nhanh hơn). Nhưng **Bộ phận Warranty của hãng** có thể phản đối: nếu claim đột nhiên được viết "chuẩn" hàng loạt, họ sẽ nghi ngờ chất lượng thực chất. ⇒ **Bắt buộc kéo bộ phận Warranty vào từ ngày đầu** với tư cách đồng thiết kế, không phải người bị áp đặt. |

## 5.3. Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future

### ✅ **GO — nhưng với scope thu hẹp có điều kiện (Conditional GO)**

**Phạm vi Giai đoạn 1 (8 tuần):**
- **1 dòng xe** (chọn dòng có sản lượng claim lớn nhất) × **1 khu vực** × **Top 50 loại claim phổ biến nhất**.
- **Làm lớp RULE/thống kê TRƯỚC** (lọc mã theo DTC + xếp hạng mã hay dùng) và **đo riêng giá trị của nó**.
- **Chỉ sau đó** mới bật lớp LLM cho diễn giải 3C + long-tail, và đo **giá trị tăng thêm** của LLM so với lớp rule.
- Triển khai **A/B theo xưởng**, không so sánh trước–sau.

### Justification (dựa trên bằng chứng kỹ thuật và chi phí)

**1. Bằng chứng dữ liệu — mạnh.** Đây là lý do chính để GO. Khác với hầu hết dự án AI phải bỏ tiền gán nhãn, bài toán này có **tập dữ liệu có nhãn sẵn**: mọi claim lịch sử đều kèm kết quả duyệt/từ chối và lý do. Baseline `first-pass yield` cũng đã được hãng theo dõi sẵn ⇒ **không cần bịa baseline**, và có thể chứng minh hiệu quả bằng số ngay trong quý đầu.

**2. Bằng chứng AI-fit — mạnh.** Bài toán sống sót qua đòn phản biện đã giết chết Card #1: không gian lựa chọn hàng nghìn mã và việc ánh xạ **văn bản kỹ thuật tự do → mã** là bài toán ngữ nghĩa thật, không thể quy về dropdown. Đây đúng là chỗ LLM có lợi thế không thể thay thế.

**3. Bằng chứng rủi ro — chấp nhận được.** Kịch bản xấu nhất là claim bị từ chối — **đúng bằng hiện trạng**. Không có rủi ro an toàn tính mạng (khác Vinmec), không có rủi ro chuyển tiền tự động (khác Card #2 Xanh SM). Ranh giới vận hành đủ chặt và đã được kiểm chứng bằng adversarial test ở Phase 4.

**4. Lý do thu hẹp scope — trung thực.** Nhóm **thừa nhận** phản biện #3: khoảng **một nửa giá trị** có thể đạt bằng rule/thống kê thuần, rẻ hơn nhiều. Nếu triển khai cả gói và gọi đó là "thành công của AI", nhóm sẽ **không biết phần nào thực sự do LLM tạo ra**. Vì vậy Giai đoạn 1 cố tình tách hai lớp và đo riêng. **Nếu lớp rule một mình đã đưa first-pass yield lên ~93%, nhóm khuyến nghị DỪNG và không triển khai LLM** — tiết kiệm chi phí inference cho Vingroup.

**5. Điều kiện để chuyển sang NOT YET.** Dự án tự động hạ xuống *NOT YET* nếu một trong các điều sau xảy ra ở Sprint 0:
- Baseline `first-pass yield` thực tế đo được **> 93%** (bài toán không đủ lớn để đáng làm).
- Bộ phận Warranty của hãng **không đồng ý tham gia đồng thiết kế**.
- Kho claim lịch sử sau khi lọc clawback còn **< 5.000 mẫu** cho dòng xe được chọn (không đủ để RAG hoạt động tốt).

---

## 📚 Giả định & Nguồn

**Điểm neo công khai:** VinFast giao **196.919 xe điện** toàn cầu năm 2025, trong đó **~176.000 xe tại Việt Nam** ([VietnamPlus](https://en.vietnamplus.vn/vinfast-sets-record-with-nearly-176000-ev-deliveries-in-vietnam-in-2025-post335909.vnp)).

**Chuỗi suy luận cho con số trong báo cáo:**
- Đội xe còn hạn bảo hành tại Việt Nam ước tính **~400.000 xe** (tích lũy nhiều năm giao hàng).
- Tỉ lệ claim bảo hành **~0,35 claim/xe/năm** (mức tham chiếu phổ biến ngành ô tô với đội xe còn trẻ) → **~140.000 claim/năm ≈ ~400 claim/ngày**.
- Thời gian hành chính **40 phút/lượt** và tỉ lệ **từ chối vòng đầu 15%**: mức tham chiếu ngành, **chưa xác nhận bằng dữ liệu VinFast**.

> 🔴 **Cảnh báo trung thực:** toàn bộ tỉ lệ phần trăm ở trên là **giả định tham chiếu ngành**, không phải dữ liệu nội bộ Vingroup. Chúng dùng để **định cỡ độ lớn bài toán** và xếp thứ tự ưu tiên — **không** dùng để cam kết ROI. Sprint 0 của dự án **không viết code**, mà là **đo baseline thật**.

---

*Hoàn thành Phase 3 & Phase 5 — Lab 02, Vin Smart Future.*
