# 01 — Problem Scan | Lab 02: AI Product Scoping (Vin Smart Future)

> **Học viên:** Nguyễn Minh Kiệt
> **Vai trò giả định:** AI Product Engineer — Vin Smart Future (Vingroup)
> **Nội dung:** Phase 1 (SCAN) + Phase 2 (QUICK-ASSESS)

---

## 🏛️ Bối cảnh: Tôi là ai và tôi quét bài toán như thế nào?

Tôi là **AI Product Engineer** tại **Vin Smart Future**. Nền tảng của tôi là **vận hành chuỗi cung ứng và kho lạnh**, nên khi quét qua các công ty thành viên Vingroup, tôi tập trung vào một dạng lãng phí rất cụ thể mà dân vận hành nhìn thấy hằng ngày:

> **"Nhân sự có chuyên môn cao đang ngồi gõ lại dữ liệu, tra cứu thủ công và soạn văn bản lặp lại — thay vì ra quyết định."**

Đây là dạng rò rỉ hiệu suất khó thấy trên báo cáo tài chính (vì nó nằm trong quỹ lương cố định), nhưng lại là nơi **LLM cho ROI nhanh nhất** vì đầu vào là **ngôn ngữ tiếng Việt phi cấu trúc** — thứ mà phần mềm rule-based truyền thống 20 năm qua không giải quyết được.

**Nguyên tắc tự đặt ra khi scan:**
1. **Không chọn bài toán "hào nhoáng"** (self-driving, AI chẩn đoán bệnh) — vượt scope của một lab và vượt khẩu vị rủi ro của Vingroup.
2. **Ưu tiên bài toán có "văn bản tiếng Việt bẩn" ở giữa quy trình** — đó là dấu hiệu chắc chắn nhất của AI-fit.
3. **Mỗi bài toán phải trả lời được:** *Ai đang gõ phím? Gõ bao lâu? Gõ bao nhiêu lượt/ngày?*

> ⚠️ **Ghi chú về số liệu:** Tôi không có quyền truy cập dữ liệu vận hành nội bộ của Vingroup. Tất cả con số tổn thất trong tài liệu này là **ước tính có dẫn giải (estimated, with shown derivation)**, được neo vào các số liệu công bố công khai (xem mục *Nguồn & Giả định* ở cuối file). Chúng dùng để **định cỡ độ lớn bài toán (order of magnitude)**, không phải để báo cáo tài chính. Bước đầu tiên của dự án thật bắt buộc phải là **đo baseline thực tế**.

---

# 🔍 Phase 1 — SCAN: Danh sách bài toán của tôi

### 📝 List bài toán của tôi:

| # | Subsidiary | Lens | Mô tả ngắn bài toán | Tổn thất ước tính |
|---|------------|------|---------------------|-------------------|
| 1 | **Vinhomes** | Lặp lại | Nhân viên bàn giao căn hộ phải **gõ lại biên bản nghiệm thu viết tay + ảnh chụp lỗi** của cư dân vào hệ thống work-order, tự phân loại lỗi theo ngành (điện / nước / sơn / thạch cao / cửa) và gán đúng nhà thầu. | ~20 phút/căn × ~8.000 căn/đợt bàn giao ≈ **333 công/đợt**; ~15% phiếu gán sai ngành → nhà thầu đi lại 2 lần |
| 2 | **Xanh SM** | Pain từ người khác | Nhân viên CSKH **phân xử tranh chấp cước phí**: đọc khiếu nại tiếng Việt của khách, tải lộ trình GPS, đối chiếu với lộ trình dự kiến, đọc ghi chú tài xế, rồi soạn thư trả lời giải thích. Cả khách và tài xế đều phàn nàn vì chậm. | ~12 phút/vụ × ~800 vụ/ngày ≈ **160 giờ/ngày ≈ 20 FTE**; SLA phản hồi 24–48h |
| 3 | **VinFast** | Lặp lại | Kỹ thuật viên xưởng dịch vụ phải **lập hồ sơ yêu cầu bảo hành (warranty claim)**: viết diễn giải sự cố, tự chọn *causal part code* + *labor operation code* trong danh mục hàng nghìn mã. Sai mã → hãng từ chối claim → làm lại. | ~25 phút/claim × ~400 claim/ngày; tỉ lệ từ chối vòng đầu ~15% → **~21.000 claim/năm phải làm lại** + chậm hoàn tiền cho xưởng |
| 4 | **VinFast** | Tốn thời gian | Nhân viên kế hoạch vật tư phải **đọc thủ công hàng trăm email/file Excel xác nhận ETA lô hàng linh kiện nhập khẩu** (mỗi nhà cung cấp một định dạng riêng) rồi gõ lại ngày giao dự kiến vào hệ thống MRP. | ~3–5 phút/email × ~250 email/ngày ≈ **~16 giờ/ngày**; ETA cập nhật trễ 1–2 ngày → sai lệch kế hoạch sản xuất |
| 5 | **Vinmec** | AI có thể tốt hơn | Nhân viên tiếp đón phải **đọc hợp đồng bảo hiểm sức khỏe tư nhân (PDF, hàng chục công ty, điều khoản loại trừ khác nhau)** để xác nhận quyền lợi trước thủ thuật và soạn công văn bảo lãnh viện phí. Khách hàng ngồi chờ tại quầy, nhận câu trả lời chậm và rập khuôn. | ~35 phút/ca bảo lãnh; khách chờ trung bình **>30 phút tại quầy**; sai sót quyền lợi → tranh chấp viện phí sau xuất viện |
| 6 | **Xanh SM** | Tốn thời gian | Tổng đài **xử lý đồ khách bỏ quên trên xe (lost & found)**: dò chuyến theo mô tả mơ hồ của khách ("tầm 8h tối hôm qua, xe trắng, gần Vincom"), gọi tài xế xác minh, hẹn điểm trả đồ. | ~18 phút/vụ, tỉ lệ tìm thấy thấp vì mô tả không khớp dữ liệu chuyến |

**✅ Lens coverage:** Lặp lại (#1, #3) · Tốn thời gian (#4, #6) · AI có thể tốt hơn (#5) · Pain từ người khác (#2) — **đủ cả 4 lenses.**
**✅ Subsidiary coverage:** Vinhomes · Xanh SM · VinFast · Vinmec — **4 công ty thành viên.**

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

**Top 3 được chọn:** **#1 (Vinhomes — Biên bản bàn giao)**, **#2 (Xanh SM — Tranh chấp cước)**, **#3 (VinFast — Hồ sơ bảo hành)**.

**Lý do loại #4, #5, #6:**
- **#4 (ETA nhà cung cấp):** Bài toán tốt nhưng lời giải đúng về dài hạn là **ép nhà cung cấp dùng EDI/API chuẩn**, không phải dùng AI đọc email mãi mãi. AI ở đây là "băng dán" cho một vấn đề quy trình → điểm Decision Quality sẽ yếu.
- **#5 (Vinmec bảo lãnh bảo hiểm):** Giá trị cao nhưng **rủi ro pháp lý/tài chính lớn nhất** (cam kết sai quyền lợi = Vinmec chịu tiền). Cần baseline dữ liệu và phê duyệt pháp chế trước — thuộc nhóm *NOT YET*.
- **#6 (Lost & found):** Tần suất và tổn thất tài chính thấp hơn hẳn 3 thẻ còn lại; ảnh hưởng thương hiệu là chính, không phải hiệu suất vận hành.

---

## Card #1 — Vinhomes: Số hóa biên bản nghiệm thu bàn giao căn hộ

```text
┌──────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                            │
│                                                                  │
│ Bài toán (1 câu): Biên bản nghiệm thu lỗi khi bàn giao căn hộ    │
│ (viết tay + ảnh chụp) phải được gõ lại, phân loại theo ngành     │
│ và gán nhà thầu hoàn toàn thủ công.                              │
│                                                                  │
│ Công ty thành viên: [x] Vinhomes                                 │
│                                                                  │
│ Ai đang đau (Actor)?                                             │
│   - Chuyên viên Bàn giao (người gõ lại, ~20 phút/căn)            │
│   - Cư dân (chờ sửa lỗi lâu, phải nhắc lại nhiều lần)            │
│   - Nhà thầu (đến nơi mới biết sai ngành → công đi lại)          │
│                                                                  │
│ Workflow thủ công hiện tại (5 bước):                             │
│   1. Cư dân + NV đi kiểm tra căn hộ, ghi lỗi ra biên bản giấy    │
│      và chụp ảnh bằng điện thoại (~25–40 mục lỗi/căn)            │
│   → 2. NV về văn phòng, gõ lại từng dòng lỗi vào hệ thống        │
│      work-order                                                  │
│   → 3. NV tự phân loại mỗi lỗi theo ngành thầu                   │
│      (điện / nước / sơn / thạch cao / cửa - nhôm kính)           │
│   → 4. NV gán nhà thầu phụ trách + đặt hạn xử lý (SLA)           │
│   → 5. Theo dõi, đóng lỗi, soạn thông báo gửi cư dân             │
│                                                                  │
│ Bước nào tốn thời gian/lỗi nhất?                                 │
│   Bước 2 + 3 (⏱ ~20 phút/căn) — gõ lại dữ liệu đã tồn tại       │
│   dưới dạng chữ viết tay/ảnh, cộng phân loại thủ công.           │
│   Tỉ lệ gán sai ngành ước tính ~15% → nhà thầu đi lại 2 lần.     │
│                                                                  │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                            │
│   Bước 2 + 3: LLM đa phương thức đọc ảnh biên bản viết tay và    │
│   ảnh chụp lỗi → trích xuất danh sách lỗi có cấu trúc (vị trí,   │
│   mô tả, mức độ) → đề xuất ngành thầu + mã lỗi chuẩn → đổ ra     │
│   BẢN NHÁP phiếu work-order để NV duyệt 1 lần trên màn hình.     │
│                                                                  │
│ Đo thành công bằng gì (Metric có số)?                            │
│   ── Metric CHÍNH (thứ xuất hiện trên P&L) ──                    │
│   M1. Số ngày đóng toàn bộ lỗi của một căn hộ (defect closure    │
│       cycle time): giảm ≥ 30% so với baseline.                   │
│   M2. Tỉ lệ cư dân ký biên bản nghiệm thu ngay lần đầu:          │
│       tăng ≥ 10 điểm phần trăm.                                  │
│   M3. Tỉ lệ nhà thầu phải đi lại lần 2 do gán sai ngành:         │
│       15% ──> dưới 5% (⇒ độ chính xác phân loại phải đạt         │
│       ≥ 95%, KHÔNG phải 92% như bản nháp đầu tiên).              │
│                                                                  │
│   ── Metric PHỤ (hiệu suất nội bộ) ──                            │
│   M4. Thời gian nhập liệu + phân loại: 20 phút ──> dưới 8 phút   │
│       /căn, với cơ chế HITL CÓ CHỌN LỌC theo độ tin cậy:         │
│       mục AI tự tin cao → duyệt theo lô; mục tự tin thấp →       │
│       bắt buộc người đọc đối chiếu từng dòng.                    │
│                                                                  │
│   ⚠️ Baseline của M1 và M2 hiện CHƯA ĐO. Sprint 0 của dự án      │
│   không viết code — mà bấm giờ và đếm trên ~30 căn hộ thật.      │
│                                                                  │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent      │
│   → LLM Feature (vision + extraction + classification),          │
│     kết hợp bảng ánh xạ RULE cố định cho bước gán nhà thầu       │
│     (ngành → nhà thầu theo hợp đồng từng tòa nhà).              │
│                                                                  │
│ ⚠️ CẢNH BÁO PHẠM VI (kết quả sau stress-test):                   │
│ Ước tính ~70% giá trị bài toán này đạt được bằng MỘT APP         │
│ CHECKLIST (dropdown) — không cần AI. Phạm vi AI phải thu hẹp     │
│ còn 3 việc mà checklist KHÔNG làm được:                          │
│   (a) đọc ghi chú tự do/ngoài lề của cư dân;                     │
│   (b) gán đúng ảnh chụp vào từng dòng lỗi;                       │
│   (c) số hóa hồ sơ bàn giao tồn đọng đã ký bằng giấy.            │
│ Xem mục "Tự phản biện" để biết lập luận đầy đủ.                  │
│                                                                  │
│ Ranh giới đề xuất: AI CHỈ tạo bản nháp. Biên bản nghiệm thu là   │
│ chứng từ pháp lý có chữ ký cư dân → BẮT BUỘC người duyệt (HITL). │
│ AI KHÔNG được tự sửa/bỏ bớt mục lỗi cư dân đã ghi.               │
└──────────────────────────────────────────────────────────────────┘
```

---

## Card #2 — Xanh SM: Phân xử tranh chấp cước phí chuyến đi

```text
┌──────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                            │
│                                                                  │
│ Bài toán (1 câu): Nhân viên CSKH phải thủ công đối chiếu lộ       │
│ trình GPS với khiếu nại tiếng Việt của khách để quyết định        │
│ hoàn/không hoàn cước, rồi tự soạn thư giải thích.                │
│                                                                  │
│ Công ty thành viên: [x] Xanh SM (GSM)                            │
│                                                                  │
│ Ai đang đau (Actor)?                                             │
│   - Nhân viên CSKH (~12 phút/vụ, ~800 vụ/ngày)                   │
│   - Khách hàng (chờ phản hồi 24–48h, mất niềm tin)               │
│   - Tài xế (bị trừ tiền trước, khiếu nại ngược lại)              │
│                                                                  │
│ Workflow thủ công hiện tại (5 bước):                             │
│   1. Nhận khiếu nại qua app/hotline ("đi vòng", "chờ lâu quá",   │
│      "sao đắt hơn giá báo")                                      │
│   → 2. Tra mã chuyến, tải lộ trình GPS thực tế                   │
│   → 3. So sánh thủ công với lộ trình & giá dự kiến; kiểm tra     │
│      thời gian chờ, phụ phí, điểm dừng phát sinh                 │
│   → 4. Đọc ghi chú tài xế / nghe ghi âm (nếu có)                 │
│   → 5. Ra quyết định hoàn tiền + tự soạn thư trả lời khách       │
│                                                                  │
│ Bước nào tốn thời gian/lỗi nhất?                                 │
│   Bước 3 + 5 (⏱ ~8/12 phút): đối chiếu dữ liệu nhiều nguồn và    │
│   soạn thư giải thích. Thư viết vội thường rập khuôn → khách      │
│   khiếu nại lần 2 (tái mở ticket).                               │
│                                                                  │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                            │
│   Bước 1: LLM phân loại loại khiếu nại từ tiếng Việt tự do       │
│           (đi vòng / phụ phí chờ / sai điểm đến / gian lận app). │
│   Bước 3: RULE engine tính chênh lệch quãng đường & cước         │
│           (đây là toán học — KHÔNG dùng LLM).                    │
│   Bước 5: LLM soạn NHÁP thư trả lời, viện dẫn đúng con số        │
│           rule engine đưa ra.                                    │
│                                                                  │
│ Đo thành công bằng gì (Metric có số)?                            │
│   M1. Thời gian xử lý: 12 phút ──> dưới 3 phút/vụ.               │
│   M2. Tỉ lệ vụ giá trị nhỏ (< 100.000đ) được hệ thống đề xuất    │
│       quyết định và CSKH chỉ bấm duyệt: ≥ 70%.                   │
│   M3. SLA phản hồi lần đầu: 24h ──> dưới 2h.                     │
│   M4. Tỉ lệ tái mở ticket (khách khiếu nại lần 2): giảm ≥ 30%.   │
│                                                                  │
│ Quick Architecture: [ ] No AI  [x] Rule  [x] LLM  [ ] Agent      │
│   → HYBRID có chủ đích: RULE quyết định con số, LLM chỉ đọc      │
│     hiểu đầu vào và diễn đạt đầu ra. Đây là câu trả lời cho      │
│     phản biện "sao không dùng rule-based cho rẻ?" — phần tính     │
│     toán ĐÚNG là rule; phần AI là ngôn ngữ, chỗ rule bất lực.    │
│                                                                  │
│ Ranh giới đề xuất: AI KHÔNG được tự động chuyển tiền hoàn.       │
│ Vụ > 100.000đ hoặc nghi ngờ gian lận → bắt buộc chuyển người.    │
│ AI KHÔNG được đưa ra cam kết bồi thường ngoài biểu phí.          │
└──────────────────────────────────────────────────────────────────┘
```

---

## Card #3 — VinFast: Trợ lý lập hồ sơ yêu cầu bảo hành tại xưởng dịch vụ

```text
┌──────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                            │
│                                                                  │
│ Bài toán (1 câu): Kỹ thuật viên phải tự viết diễn giải sự cố và  │
│ tự chọn causal part code + labor code trong danh mục hàng nghìn  │
│ mã; sai mã thì hãng từ chối claim và xưởng phải làm lại.         │
│                                                                  │
│ Công ty thành viên: [x] VinFast                                  │
│                                                                  │
│ Ai đang đau (Actor)?                                             │
│   - Kỹ thuật viên / Cố vấn dịch vụ (~25 phút hành chính/claim)   │
│   - Bộ phận Warranty của hãng (phải review claim viết sơ sài)    │
│   - Xưởng dịch vụ (bị chậm hoàn tiền vì claim bị treo)           │
│                                                                  │
│ Workflow thủ công hiện tại (5 bước):                             │
│   1. Tiếp nhận mô tả lỗi của khách (tiếng Việt đời thường)       │
│   → 2. Chẩn đoán, đọc mã lỗi DTC, sửa chữa                       │
│   → 3. KTV viết diễn giải 3C (Complaint–Cause–Correction)        │
│      bằng tay vào hệ thống                                       │
│   → 4. KTV tự tra và chọn causal part code + labor op code       │
│      trong danh mục lớn (dễ chọn nhầm mã gần giống)              │
│   → 5. Gửi claim; nếu bị từ chối → nhận phản hồi, sửa, gửi lại   │
│                                                                  │
│ Bước nào tốn thời gian/lỗi nhất?                                 │
│   Bước 3 + 4 (⏱ ~18/25 phút). Đây cũng là nguồn gốc của          │
│   ~15% claim bị từ chối vòng đầu → mỗi vụ mất thêm ~20 phút      │
│   và kéo dài chu kỳ thu hồi tiền bảo hành.                       │
│                                                                  │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                            │
│   Bước 3: LLM đọc mô tả khách + mã DTC + ghi chú sửa chữa → soạn │
│           NHÁP diễn giải 3C đúng chuẩn hãng yêu cầu.             │
│   Bước 4: RAG truy xuất danh mục mã + lịch sử claim tương tự đã  │
│           được duyệt → đề xuất Top-3 mã kèm độ tin cậy và lý do. │
│                                                                  │
│ Đo thành công bằng gì (Metric có số)?                            │
│   M1. Thời gian hành chính/claim: 25 phút ──> dưới 8 phút.       │
│   M2. Tỉ lệ claim được duyệt ngay vòng đầu (first-pass yield):   │
│       85% ──> ≥ 95%.                                             │
│   M3. Mã đúng nằm trong Top-3 gợi ý của AI: ≥ 90%.               │
│                                                                  │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent      │
│   → LLM Feature + RAG trên danh mục mã và kho claim lịch sử.     │
│     KHÔNG dùng Agentic Loop: quy trình cố định, không cần tự     │
│     lập kế hoạch nhiều bước.                                     │
│                                                                  │
│ Ranh giới đề xuất: AI CHỈ gợi ý, KTV là người chọn mã cuối cùng  │
│ (claim bảo hành là chứng từ tài chính với hãng). AI KHÔNG được    │
│ tự gửi claim. AI KHÔNG được suy đoán nguyên nhân kỹ thuật ngoài   │
│ dữ liệu chẩn đoán thực tế — nếu không đủ căn cứ phải trả về      │
│ "insufficient_evidence" thay vì bịa diễn giải.                   │
└──────────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Đề xuất của cá nhân cho nhóm (đưa bài toán nào vào Deep-Dive?)

> 📌 **Ghi chú về quá trình:** đề xuất ban đầu của tôi là **Card #1**. Sau khi chạy stress-test CFO/Vận hành (mục kế tiếp), tôi **đã đổi đề xuất**. Tôi giữ lại cả hai phiên bản ở đây vì bản thân việc đổi ý là bằng chứng của quá trình scoping trung thực.

### Đề xuất ban đầu (trước stress-test) — và chỗ nó sai

**Chọn Card #1**, với lý do: *"đây là bài toán mà rule-based hoàn toàn bất lực, vì đầu vào là ảnh và chữ viết tay tiếng Việt."*

**Lập luận này đã gãy khi bị phản biện.** Đầu vào là chữ viết tay **vì quy trình chọn để nó là chữ viết tay**. Một app checklist với từ điển lỗi đóng (~60–120 mục) xóa bỏ tiền đề đó, và cùng với nó là phần lớn bài toán AI. Tôi đã tự đặt ra tiền đề rồi tự giải nó.

### Đề xuất sau stress-test

**Chọn Card #3 — VinFast, Trợ lý lập hồ sơ yêu cầu bảo hành.**

| Tiêu chí | Card #1 Vinhomes | Card #2 Xanh SM | Card #3 VinFast |
|---|---|---|---|
| Dễ vẽ current-state workflow (G1) | ⭐⭐⭐ Rõ, 5 bước quan sát được | ⭐⭐ Nhiều nhánh điều kiện | ⭐⭐⭐ Quy trình chuẩn hóa sẵn theo hãng |
| Metric bám P&L, đo được baseline (G2) | ⭐⭐ Phải đo lại từ đầu | ⭐⭐⭐ Có sẵn log ticket | ⭐⭐⭐ First-pass yield là chỉ số tài chính có sẵn |
| Rủi ro khi AI sai (G4) | ⭐⭐⭐ Thấp — bản nháp có chữ ký duyệt | ⭐ Liên quan tiền hoàn | ⭐⭐ Kiểm soát được vì KTV chọn mã cuối |
| **Chịu được đòn "dùng dropdown thay AI"?** | ❌ **KHÔNG** — danh mục lỗi là tập đóng ~100 mục | ⚠️ Một phần | ✅ **CÓ** — danh mục hàng nghìn mã, chọn mã đòi hỏi suy luận từ diễn giải kỹ thuật, không thể đưa vào dropdown |

**Lý do chọn #3:** đây là thẻ duy nhất **sống sót nguyên vẹn** qua phản biện *"tại sao không dùng rule-based/dropdown cho rẻ?"*. Khi danh mục lựa chọn có hàng nghìn mã và việc chọn đúng mã đòi hỏi **đọc hiểu diễn giải kỹ thuật rồi suy luận**, dropdown không phải lời giải — đó chính là định nghĩa của một bài toán LLM + RAG thật sự. Ngoài ra `first-pass yield` là chỉ số tài chính hãng **đã theo dõi sẵn**, nên baseline có ngay, không phải bịa.

**Phương án thay thế nếu nhóm vẫn muốn làm Vinhomes:** giữ Card #1 nhưng **thu hẹp phạm vi** còn 3 việc checklist không làm được (ghi chú tự do của cư dân / gán ảnh vào dòng lỗi / hồ sơ tồn đọng), và kết luận trung thực là **GO CÓ ĐIỀU KIỆN**, kèm khuyến nghị rằng app checklist mới là lời giải đúng cho phần còn lại.

**Nếu nhóm muốn bài toán "gai góc" nhất để tranh luận:** chọn **Card #2** — nó buộc nhóm phân định rạch ròi **phần nào là Rule, phần nào là LLM**, đúng nội dung ăn điểm Gate G3.

---

# 🛡️ Tự phản biện (Stress-test: đóng vai CFO & Trưởng phòng Vận hành)

Tôi đã dán **Card #1** vào LLM với prompt đóng vai *"CFO và Trưởng phòng Vận hành cực kỳ khắt khe"*. Dưới đây là ba đòn phản biện nhận được, **nguyên văn tinh thần**, kèm đánh giá trung thực của tôi về đòn nào thắng.

## 🔴 Đòn 1 — Metric tự mâu thuẫn về mặt số học

> *"M2 đặt độ chính xác ≥ 92%. M3 đặt tỉ lệ đi lại lần 2 xuống dưới 5%. Nhưng 15% đi lại lần 2 **chính là** 85% độ chính xác — anh viết một con số hai lần để độn danh sách metric cho có vẻ chặt chẽ. Tệ hơn: muốn misroute dưới 5% thì độ chính xác phải trên **95%**, không phải 92%. Hai metric của anh không thể cùng đạt.*
>
> *Và mâu thuẫn thứ hai nghiêm trọng hơn: anh hứa dưới **4 phút/căn**, trong khi mỗi căn có **25–40 mục lỗi**. Đó là **~7 giây/dòng** để đối chiếu bản trích xuất của AI với chữ viết tay gốc. Anh chọn một trong hai: nhân viên **thực sự kiểm tra** → không thể 4 phút; hoặc nhân viên **bấm duyệt cho xong** → thì 'HITL bắt buộc' của anh chỉ là trang trí, và Vinhomes vừa tạo ra quy trình nơi một mô hình AI diễn giải chứng từ pháp lý có chữ ký cư dân mà không ai đọc lại. Metric tốc độ và ranh giới an toàn của anh triệt tiêu lẫn nhau."*

**🟥 Đánh giá: ĐÒN NÀY THẮNG TUYỆT ĐỐI. Không cãi được.**

Đây là lỗi thật trong bản nháp đầu của tôi. Đã sửa trong Card #1:
- Gộp M2 và M3 thành **một** metric, và sửa ngưỡng độ chính xác **92% → ≥ 95%** cho khớp số học.
- Bỏ mục tiêu 4 phút; thay bằng **dưới 8 phút** kèm cơ chế **HITL có chọn lọc theo độ tin cậy** (tự tin cao → duyệt lô; tự tin thấp → bắt buộc đọc từng dòng). Đây mới là cách làm HITL thật, thay vì HITL toàn bộ với tốc độ viễn tưởng.

## 🔴 Đòn 2 — "Anh đang tiết kiệm loại tiền không tồn tại trong P&L"

> *"'333 công/đợt' nghe to. Nhưng sau khi triển khai, tôi giảm được bao nhiêu đầu người? Không ai cả. Chuyên viên bàn giao vẫn ăn lương đủ, họ chỉ rảnh hơn. Đây là **phantom savings** — nó không bao giờ xuất hiện trên báo cáo tài chính của tôi.*
>
> *Thứ thực sự tốn tiền ở khâu bàn giao thì anh không đo: **số ngày đóng lỗi** (cư dân chưa nhận nhà, biên bản chưa ký), **tỉ lệ ký biên bản thành công ngay lần đầu** (mỗi lần từ chối ký là một lần lùi lịch), và **chi phí nhà thầu đi lại** (cái này mới ra tiền mặt thật, mà anh để ở metric phụ). Anh đang tối ưu tốc độ gõ phím của một cost center. Tôi không mua tốc độ gõ phím."*

**🟥 Đánh giá: ĐÒN NÀY THẮNG.**

Đã đảo trục metric của Card #1: **số ngày đóng lỗi** và **tỉ lệ ký biên bản lần đầu** lên làm metric **chính**; thời gian gõ phím tụt xuống **metric phụ**. Đây là thay đổi làm mạnh trực tiếp Gate G2.

## 🔴 Đòn 3 — "Anh dùng AI để chữa vết thương anh tự gây ra"

> *"Anh mô tả bài toán là 'phân loại lỗi'. Sai. Bài toán thật là: năm 2026 mà Vinhomes vẫn đi nghiệm thu bằng giấy và bút."*

Lập luận rule-based của phía phản biện:

| | App checklist (rule-based) | Giải pháp LLM của tôi |
|---|---|---|
| Nhập liệu | **Bằng 0** — nhập tại chỗ | Gõ lại bằng AI, vẫn phải review |
| Độ chính xác phân loại | **100%** — chọn từ từ điển đóng | ~95%, cần người kiểm |
| Định tuyến nhà thầu | Bảng ánh xạ tất định | Bảng ánh xạ tất định (**giống hệt**) |
| Chi phí biến đổi/căn | **0đ** | Chi phí inference × 40 mục × 8.000 căn |
| Chạy ở tầng hầm không sóng | ✅ Có | ❌ Không |
| Truy vết kiểm toán | Bản ghi có cấu trúc, sạch | Bản diễn giải của mô hình trên chứng từ pháp lý |
| Rủi ro hallucination | **Không tồn tại** | Có — trên văn bản đã có chữ ký |

> *"Anh đang đề nghị tôi chi tiền để dạy một mô hình đọc chữ viết tay — thứ lẽ ra ngay từ đầu không nên được viết tay."*

Phản biện này cũng bác luôn lý lẽ tự vệ ban đầu của tôi (*"app làm chậm buổi nghiệm thu vì cư dân vẫn muốn ký giấy"*): cư dân ký **bản in ra từ app** hoặc ký số; và checklist **nhanh hơn** viết tay — giấy chỉ *có cảm giác* nhanh vì chi phí bị đẩy sang cho nhân viên văn phòng buổi tối.

**🟧 Đánh giá: ĐÒN NÀY THẮNG PHẦN LỚN — và nó phá hỏng chính đề xuất ban đầu của tôi.**

Danh mục lỗi bàn giao căn hộ là **tập hợp đóng, hữu hạn** (~60–120 mục: trầy sơn, ố trần, rò silicone, lệch cánh cửa, ổ cắm không điện, áp lực nước yếu…). Đây đúng là định nghĩa sách giáo khoa của bài toán **thuộc về dropdown, không thuộc về LLM**.

**Phần giá trị AI còn sống sót — và chỉ phần này:**
1. **Ghi chú tự do của cư dân** — cư dân viết ngoài lề những thứ không dropdown nào chứa nổi (*"bếp có mùi lạ khi mở nước nóng"*). LLM đọc hiểu và định tuyến được; checklist thì không.
2. **Gán ảnh ↔ dòng lỗi** — app vẫn sinh ra ~40 tấm ảnh mà ai đó phải gán vào đúng mục lỗi. LLM vision làm được, và đây là công việc thật.
3. **Hồ sơ tồn đọng** — các đợt bàn giao đã xong đang nằm dưới dạng giấy/scan.
4. **Thời gian triển khai** — đổi quy trình nghiệm thu trên toàn bộ dự án và toàn bộ nhà thầu BQL là một **chương trình thay đổi tổ chức**, mất nhiều quý; AI đọc được thứ đang tồn tại **hôm nay**.

**Nhưng nói thẳng:** nếu Vinhomes triển khai được app checklist thì **họ nên làm**, và AI tụt xuống thành tính năng hỗ trợ hẹp, không phải sản phẩm chính.

---

## 📌 Kết luận rút ra từ stress-test

1. **Đổi đề xuất Deep-Dive từ Card #1 sang Card #3 (VinFast warranty)** — thẻ duy nhất mà đòn *"dùng dropdown đi"* không áp dụng được, vì danh mục có hàng nghìn mã và việc chọn mã đòi hỏi suy luận từ diễn giải kỹ thuật.
2. **Nếu vẫn làm Card #1 → thu hẹp phạm vi** còn 4 điểm ở trên và kết luận **GO CÓ ĐIỀU KIỆN**, kèm khuyến nghị app checklist cho phần còn lại.
3. **Bài học chung:** trước khi đề xuất bất kỳ giải pháp LLM nào, phải hỏi *"đầu vào phi cấu trúc này là tất yếu, hay do quy trình tự tạo ra?"* Nếu do quy trình tự tạo ra — **sửa quy trình rẻ hơn mua AI**.

---

# 📚 Nguồn & Giả định (minh bạch số liệu)

**Số liệu công khai dùng làm điểm neo:**

| Điểm neo | Giá trị | Nguồn |
|---|---|---|
| Căn hộ Vinhomes đang vận hành | > 110.000 căn, phục vụ ~493.000 cư dân | DNSE (dẫn báo cáo Vinhomes) |
| Giao xe VinFast 2025 | 196.919 xe điện toàn cầu; ~176.000 xe tại Việt Nam; ~53.000 xe bán cho GSM | VietnamPlus, VietnamBiz |
| Thị phần Xanh SM (Green SM) | ~55% thị trường taxi công nghệ Việt Nam, Quý I/2026 | VnEconomy / CafeF |

**Chuỗi suy luận cho các con số tổn thất (để giảng viên kiểm chứng logic):**

- **#1 Vinhomes:** giả định một đợt bàn giao đại đô thị ~8.000 căn; mỗi căn ~25–40 mục lỗi; ~20 phút gõ lại + phân loại → 8.000 × 20 phút ÷ 60 ÷ 8 giờ ≈ **333 công**.
- **#2 Xanh SM:** giả định ~200.000 chuyến/ngày toàn hệ thống, tỉ lệ tranh chấp cước ~0,4% (mức phổ biến ngành gọi xe) → ~800 vụ/ngày × 12 phút ≈ **160 giờ/ngày ≈ 20 FTE**.
- **#3 VinFast:** giả định đội xe còn hạn bảo hành tại Việt Nam ~400.000 xe, tỉ lệ ~0,35 claim/xe/năm → ~140.000 claim/năm ≈ **~400 claim/ngày**; tỉ lệ từ chối vòng đầu 15% (mức phổ biến ngành ô tô) → **~21.000 claim/năm phải làm lại**.

> 🔴 **Cảnh báo trung thực:** mọi tỉ lệ phần trăm ở trên là **giả định tham chiếu ngành**, chưa được xác nhận bởi dữ liệu Vingroup. Chúng dùng để xếp hạng ưu tiên bài toán, **không** dùng để cam kết ROI.

---

*Hoàn thành Phase 1 & Phase 2 — Lab 02, Vin Smart Future.*
