# Báo cáo Phân tích sâu (Deep-Dive Report)

> **Bài toán được chọn:** Trợ lý hướng dẫn trạm sạc thông minh (VinFast)
> **Kiến trúc đề xuất:** LLM Feature kết hợp Rule-based (RAG Pattern)

---

## 3.1. Current-State Workflow Mapping

Quy trình hiện tại khi khách hàng VinFast cần tìm trạm sạc phù hợp:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │     │ Bước 5       │
│ Khách hàng   │     │ Mở App       │     │ Lọc thủ công │     │ Kiểm tra loại│     │ Lái xe đến   │
│ nhận cảnh báo│ ──→ │ VinFast hoặc │ ──→ │ trạm sạc gần │ ──→ │ cổng sạc phù │ ──→ │ trạm sạc     │
│ pin yếu      │     │ gọi Hotline  │     │ trên bản đồ  │     │ hợp (CCS2/   │     │              │
│              │     │              │     │              │     │ GBT)         │     │              │
│ Ai: Khách    │     │ Ai: Khách    │     │ Ai: Khách /  │     │ Ai: Khách    │     │ Ai: Khách    │
│              │     │              │     │ Tổng đài viên│     │              │     │              │
│ [Time] 1 phút     │     │ [Time] 2 phút     │     │ [Time] 8 phút [Bottleneck]  │     │ [Time] 3 phút [Bottleneck]  │     │ [Time] Tùy kc     │
│ In: Cảnh báo │     │ In: Vị trí   │     │ In: Bản đồ   │     │ In: Thông số │     │ In: Địa chỉ  │
│ Out: Nhận    │     │ Out: Danh    │     │ Out: 1 trạm  │     │ Out: Xác nhận│     │ Out: Sạc xe  │
│ biết pin thấp│     │ sách trạm    │     │ được chọn    │     │ đúng cổng    │     │              │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘

[Bottleneck] = Bottlenecks
[Handoff] Handoff: Bước 3 — Khách hàng có thể gọi Hotline để nhờ Tổng đài viên tra cứu hộ.
[Time] Tổng thời gian xử lý thủ công trung bình: ~14 phút/lượt (chưa tính thời gian lái xe).

Các vấn đề thực tế:
  • Bước 3: Khách phải cuộn bản đồ, zoom vào từng trạm để xem trạng thái "Còn trống" hay "Đầy".
    Nhiều trạm hiển thị "Còn trống" nhưng thực tế đã bị chiếm hoặc đang bảo trì.
  • Bước 4: Khách không nhớ dòng xe mình dùng cổng sạc CCS2 hay GBT,
    dẫn đến đến nơi mới phát hiện không tương thích → phải tìm lại trạm khác.
  • Khi pin dưới mức nguy hiểm (tùy dòng xe), khách vẫn cố lái đến trạm xa
    → rủi ro cạn pin giữa đường, gây mất an toàn giao thông.
```

---

## 3.2. Problem Statement (6-field)

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Khách hàng sở hữu xe điện VinFast (VF5, VFe34, VF8, VF9) và Nhân viên Tổng đài CSKH VinFast. |
| **2. Current Workflow** | Khi pin yếu, khách mở App VinFast xem bản đồ trạm sạc, tự cuộn tìm trạm gần, tự kiểm tra loại cổng sạc phù hợp với dòng xe, rồi lái đến. Nếu không rành, gọi Hotline nhờ tổng đài viên tra cứu thủ công. 5 bước, chủ yếu thủ công, mất trung bình **14 phút/lượt**. |
| **3. Bottleneck** | **Bước 3 & 4** (mất 11 phút): Lọc trạm sạc gần + kiểm tra loại cổng sạc tương thích. Dữ liệu trạm sạc trên App không real-time (độ trễ 5-10 phút), dẫn đến khách đến nơi phát hiện trạm hết chỗ hoặc sai cổng sạc. Tỉ lệ khách phải quay lại tìm trạm khác ước tính ~18%. |
| **4. Business Impact** | Mỗi ngày có ~500 lượt tìm trạm sạc trên App VinFast toàn quốc. 18% trong số đó (90 lượt) phải tìm lại trạm khác, gây lãng phí thời gian khách hàng và **giảm chỉ số NPS (Net Promoter Score)** do trải nghiệm sạc xe kém. Hotline nhận thêm ~120 cuộc gọi hỏi trạm sạc/ngày, mỗi cuộc mất 5-8 phút → chiếm ~15 giờ làm việc/ngày của đội tổng đài. |
| **5. Success Metric** | 1. Giảm thời gian tìm trạm sạc phù hợp từ **14 phút xuống dưới 2 phút** (Efficiency).<br>2. Tỉ lệ đề xuất đúng trạm sạc (đúng cổng, còn trống, trong tầm pin) đạt **≥ 95%** (Quality).<br>3. Giảm cuộc gọi hỏi trạm sạc vào Hotline **≥ 40%** (Cost Saving). |
| **6. Operational Boundary** | **AI ĐƯỢC PHÉP:** Truy xuất API định vị GPS xe, API trạm sạc real-time (trống/bận/bảo trì), thông số kỹ thuật dòng xe; tự động soạn thảo Top 3 gợi ý trạm sạc kèm hướng dẫn đường đi.<br>**TUYỆT ĐỐI CẤM:** ① AI không được đề xuất trạm sạc nằm ngoài tầm pin ước tính còn lại của xe (ngưỡng an toàn tùy theo từng dòng xe: VF5 ≤ 8%, VFe34 ≤ 6%, VF8 ≤ 5%, VF9 ≤ 4%). Khi pin dưới ngưỡng, AI phải kích hoạt **gọi xe cứu hộ pin di động**. ② AI không được tự động điều hướng xe mà không có xác nhận của khách hàng (Bắt buộc Human-in-the-loop). ③ AI không được thu thập hoặc lưu trữ lịch sử di chuyển cá nhân ngoài phiên làm việc hiện tại. |

---

## 3.3. Future-State Flow & AI Fit

### AI Fit: Chọn **LLM Feature** kết hợp Rule-based

**Lý do lựa chọn:**

| Tiêu chí | Rule / State-Machine | LLM Feature (Chon) | Agentic Loop |
|---|---|---|---|
| Phù hợp? | Chỉ lọc trạm gần, không giải thích được bằng ngôn ngữ tự nhiên | **Kết hợp tốt nhất:** Code tính toán chính xác + LLM soạn câu trả lời thân thiện | Quá phức tạp, rủi ro AI tự ý gọi API sai hoặc hallucinate khoảng cách |
| Rủi ro | Trải nghiệm khô khan | **Thấp:** Logic an toàn nằm trong code cứng, LLM chỉ soạn text | Cao: AI có thể phá vỡ ranh giới an toàn |
| Bảo trì | Dễ | **Trung bình** | Khó |

### Future-State Flow

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Khách nhấn   │     │ [AI] Hệ thống │     │ [AI] LLM soạn  │     │ [HITL] Khách     │
│ "Tìm trạm    │ ──→ │ Rule-based   │ ──→ │ tin nhắn gợi │ ──→ │ xem Top 3,   │
│ sạc" trên App│     │ auto-pull:   │     │ ý Top 3 trạm │     │ chọn 1 trạm  │
│              │     │ - Vị trí GPS │     │ kèm giải     │     │ và nhấn      │
│              │     │ - % pin      │     │ thích lý do, │     │ "Dẫn đường"  │
│              │     │ - Dòng xe    │     │ thời gian đi,│     │              │
│              │     │ - Cổng sạc   │     │ số trụ trống │     │              │
│              │     │ - Top 3 trạm │     │              │     │              │
│ ⏱ 5 giây     │     │ ⏱ 3 giây     │     │ ⏱ 5 giây     │     │ ⏱ 10 giây    │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘

⏱ Tổng thời gian mới: ~25 giây (giảm từ 14 phút xuống còn dưới 30 giây).

[AI] = AI Step (Bước 2: Code tính toán; Bước 3: LLM soạn văn bản)
[HITL] = Human Step / HITL (Khách hàng xác nhận chọn trạm)

Fallback:
  • Nếu LLM không thể soạn gợi ý (lỗi API, timeout): Hiển thị danh sách
    Top 3 trạm dạng bảng đơn giản (tên, khoảng cách, số trụ trống) — không cần LLM.
  • Nếu pin dưới ngưỡng an toàn (tùy dòng xe): Bỏ qua tìm trạm, hiển thị
    nút đỏ "GỌI CỨU HỘ PIN DI ĐỘNG" và tự động gửi vị trí xe cho đội cứu hộ.
```

---

## 3.4. Evaluate — AI Readiness Checklist

### Checklist:
1. [x] **Dữ liệu mẫu/logs sạch để test?** — Có. API trạm sạc VinFast đã có sẵn dữ liệu real-time (vị trí, trạng thái trụ, loại cổng). Dữ liệu GPS và thông số pin xe có thể lấy từ hệ thống Telemetry.
2. [x] **Rủi ro khi AI sai có nằm trong tầm kiểm soát?** — Có. Logic an toàn (kiểm tra pin, lọc cổng sạc) nằm trong code Rule-based cứng, không phụ thuộc LLM. LLM chỉ soạn văn bản gợi ý. Có Fallback hiển thị bảng đơn giản khi LLM lỗi. Có cơ chế gọi cứu hộ khi pin nguy hiểm.
3. [x] **Stakeholders sẵn sàng thay đổi quy trình?** — Có. Tính năng này bổ sung trên App hiện tại, không thay đổi quy trình cũ. Khách hàng vẫn có thể tự tìm trạm thủ công nếu muốn.

### Quyết định cuối cùng:

**[x] GO — Bắt đầu xây dựng Prototype với scope hẹp.**

### Justification (Lý giải quyết định):

> Dự án được đánh giá **GO** dựa trên các bằng chứng sau:
>
> 1. **Bài toán rõ ràng và đo lường được:** Bottleneck tìm trạm sạc ảnh hưởng đến ~500 lượt/ngày, có metric cụ thể (thời gian, tỉ lệ đúng, giảm cuộc gọi Hotline).
> 2. **Kiến trúc an toàn:** Logic tính toán quan trọng (lọc cổng sạc, kiểm tra tầm pin) nằm trong code Rule-based, không phụ thuộc vào sự "sáng tạo" của LLM. LLM chỉ đóng vai trò soạn văn bản gợi ý thân thiện — nếu LLM lỗi, hệ thống vẫn hoạt động qua Fallback bảng đơn giản.
> 3. **Ranh giới an toàn nghiêm ngặt:** Ngưỡng pin nguy hiểm được cấu hình riêng cho từng dòng xe (VF5: 8%, VFe34: 6%, VF8: 5%, VF9: 4%), đảm bảo không bao giờ điều hướng xe đến trạm sạc ngoài tầm pin.
> 4. **Chi phí triển khai thấp:** Tận dụng API trạm sạc và Telemetry sẵn có. Chi phí LLM thấp vì mỗi lần gọi chỉ cần soạn 1 đoạn text ngắn (~200 tokens).
> 5. **Không phá vỡ quy trình hiện tại:** Tính năng mới được thêm vào App, khách hàng không bị ép buộc sử dụng.
