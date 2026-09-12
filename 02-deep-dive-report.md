# 02 — Deep-Dive Report: Xanh SM Battery-Critical Dispatch
> **Lab 02: AI Product Scoping — Vin Smart Future**  
> Deliverable G1–G4 · Group · Phase 3 (DEEP-DIVE) + Phase 5 (EVALUATE)  
> **Bài toán được chọn:** Xanh SM — Xử lý sự cố hết pin thực địa (Dispatcher Co-pilot)

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping

Quy trình xử lý sự cố hết pin thực địa hiện tại của điều phối viên Xanh SM:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3  🔴   │     │ Bước 4  🔴   │
│ Nhận cuộc    │     │ Tra cứu định │     │ Tra cứu trạm │     │ Soạn văn bản │
│ gọi sự cố   │ ──→ │ vị GPS xe   │ ──→ │ sạc VinFast  │ ──→ │ hướng dẫn   │
│ từ tài xế   │     │ trên bản đồ  │     │ còn trụ trống│     │ gửi App tài  │
│              │     │ nội bộ       │     │ & phù hợp    │     │ xế (tiếng Vn)│
│ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │
│ ⏱ 2 phút    │     │ ⏱ 2 phút    │     │ ⏱ 5 phút 🔴 │     │ ⏱ 5 phút 🔴 │
│ In: Điện thoại│    │ In: Biển số  │     │ In: Toạ độ  │     │ In: Raw data │
│ Out: Log sự  │     │ Out: Toạ độ  │     │ Out: Địa chỉ │     │ Out: SMS/App │
│ cố           │     │ GPS          │     │ trạm sạc     │     │ message      │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5       │
                                                               │ Nếu pin<5%: │
                                                               │ Gọi xe cứu  │
                                                               │ hộ pin di   │
                                                               │ động         │
                                                               │ Ai: Dispatch │
                                                               │ ⏱ 1 phút    │
                                                               └──────────────┘

🔴 = Bottlenecks (Bước 3 & 4)
🔄 Handoff: Tài xế → Tổng đài → Dispatcher → App tài xế
⏱ Tổng thời gian xử lý thủ công: ~15 phút/lượt
📊 Quy mô: ~80 sự cố pin/ngày tại Hà Nội → ~20 giờ công lãng phí/ngày
```

**Điểm nghẽn cổ chai (Bottleneck) nổi bật:**
- **Bước 3** (5 phút): Dispatcher phải mở Dashboard trạm sạc riêng biệt, tra thủ công trụ còn trống + đúng loại cổng sạc (CCS2/GBT) phù hợp với model xe (VF5/VFe34/VF8/VF9).
- **Bước 4** (5 phút): Soạn tin nhắn chỉ dẫn đường đi bằng tiếng Việt thân thiện — thông tin lấy từ nhiều nguồn khác nhau, cần tổng hợp thủ công.

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Field | Nội dung chi tiết |
|-------|-------------------|
| **1. Actor / Operator** | Điều phối viên (Dispatcher) thuộc Trung tâm Điều vận Xanh SM — vận hành ca 24/7, mỗi ca ~5 dispatcher chịu trách nhiệm toàn bộ đội xe tại Hà Nội. |
| **2. Current Workflow** | Khi tài xế báo hết/sắp hết pin qua điện thoại, Dispatcher: (1) tra định vị GPS xe trên bản đồ nội bộ; (2) mở Dashboard trạm sạc VinFast để tìm trụ trống gần nhất đúng cổng sạc; (3) soạn tin nhắn chỉ dẫn đường đi bằng tiếng Việt gửi qua App tài xế; (4) nếu pin dưới 5%: gọi thêm đội xe cứu hộ pin di động. 5 bước, hoàn toàn thủ công, mất 15 phút/lượt. |
| **3. Bottleneck** | Bước 3 & 4 (chiếm 10/15 phút): Tra cứu thủ công trụ sạc trống phù hợp model xe và soạn thảo tin nhắn hướng dẫn đường đi thân thiện bằng tiếng Việt. Đây là tác vụ lặp lại hoàn toàn — cấu trúc cố định nhưng tốn sức người. |
| **4. Business Impact** | ~80 sự cố pin/ngày tại Hà Nội → lãng phí ~20 giờ công dispatcher/ngày. Tài xế chờ 15 phút không đón được khách → rò rỉ doanh thu ước tính ~15% per incident. Tỉ lệ khách hủy chuyến tăng khi tài xế không phản hồi do đang chờ hướng dẫn. |
| **5. Success Metric** | 1. **Efficiency:** Giảm tổng thời gian xử lý sự cố từ 15 phút → dưới 3 phút (Giảm 80%). 2. **Quality:** Tỉ lệ hướng dẫn đúng địa điểm & đúng loại cổng sạc phù hợp đạt ≥ 98%. 3. **Safety:** 100% trường hợp pin < 5% phải kích hoạt dispatch xe cứu hộ di động, không đề xuất trạm > 5 km. |
| **6. Operational Boundary** | **AI ĐƯỢC PHÉP:** Truy xuất API định vị xe, API trạm sạc VinFast trống, soạn bản nháp tin nhắn hướng dẫn có tag `[DRAFT_ONLY]`. **TUYỆT ĐỐI CẤM:** (a) Tự động gửi tin nhắn đến tài xế mà không có Dispatcher phê duyệt (bắt buộc HITL); (b) Đề xuất trạm sạc > 5 km khi pin < 5% — phải dispatch xe cứu hộ di động; (c) Đề xuất trạm sạc không đúng loại cổng sạc của model xe. |

---

## 3.3. Future-State Flow & AI Fit

**AI Fit Matrix:**

| Loại giải pháp | Phù hợp? | Lý do |
|----------------|----------|-------|
| **Rule / State-Machine** | ⚠️ Một phần | Có thể xử lý logic lọc trạm sạc (loại cổng, khoảng cách), nhưng không thể soạn thảo tin nhắn ngôn ngữ tự nhiên thân thiện. |
| **LLM Feature** | ✅ **Lựa chọn chính** | Đủ để: (1) Tổng hợp dữ liệu đa nguồn (GPS + trạm sạc + model xe), (2) Soạn tin nhắn tiếng Việt thân thiện theo context. Quy trình có cấu trúc cố định → không cần Agent tự trị. |
| **Agentic Loop** | ❌ Quá mức cần thiết | Rủi ro quá cao: Agent tự trị có thể gửi tin nhắn sai đến tài xế, làm xe hết pin giữa đường. Cần Human-in-the-loop bắt buộc. |

**Quyết định:** Chọn **LLM Feature** với Human-in-the-loop bắt buộc.

**Future-State Flow (Quy trình tương lai):**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận cuộc   │     │ 🔵 Auto-pull │     │ 🔵 AI Draft  │     │ 🟢 Dispatch  │
│ gọi sự cố   │ ──→ │ GPS xe +     │ ──→ │ SMS hướng   │ ──→ │ 1-click phê  │
│ từ tài xế   │     │ Trạm trống   │     │ dẫn [DRAFT_  │     │ duyệt & gửi │
│              │     │ + Model xe   │     │ ONLY] tiếng  │     │ qua App      │
│              │     │              │     │ Việt         │     │ tài xế       │
│ Ai: Tài xế  │     │ Ai: 🔵 System│     │ Ai: 🔵 LLM  │     │ Ai: 🟢 Human │
│ ⏱ 2 phút    │     │ ⏱ <5 giây   │     │ ⏱ <10 giây  │     │ ⏱ <30 giây  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                             ┌────────────────────────────────────────┘
                             │
                             ▼ ↩️ Fallback:
                    Nếu AI draft lỗi / không tự tin (low-confidence),
                    Dispatcher tự viết tay như quy trình cũ.
                    Nếu pin < 5%: Hệ thống tự động trigger
                    dispatch_mobile_charger, KHÔNG đề xuất trạm > 5km.

🔵 = AI Step (LLM/System tự động)
🟢 = Human Step (Human-in-the-loop: Dispatcher phê duyệt bắt buộc)
↩️ = Fallback (Dự phòng khi LLM thất bại)

⏱ Tổng thời gian mục tiêu: < 3 phút/lượt (giảm 80% so với hiện tại)
```

---

# 🏁 Phase 5 — EVALUATE

## AI Readiness Checklist

| # | Tiêu chí | Trạng thái | Ghi chú |
|---|----------|-----------|---------|
| 1 | Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? | ✅ **Có** | Xanh SM có logs sự cố pin hàng ngày (~80 records/ngày), dữ liệu GPS xe theo thời gian thực, API trạm sạc VinFast. |
| 2 | Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? | ✅ **Có** | Dispatcher phê duyệt bắt buộc trước khi gửi (`[DRAFT_ONLY]`). Nếu AI sai → Fallback thủ công như cũ. Quy tắc pin < 5% → mobile charger được hard-code. |
| 3 | Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? | ✅ **Có** | Dispatcher đã phàn nàn về quá tải → sẵn sàng thử nghiệm. Cần training ngắn về cách review bản nháp AI. |

**Tổng đánh giá: 3/3 tiêu chí ĐẠT.**

---

## Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future

**[x] ✅ GO (Bắt đầu xây dựng Prototype)**

### Justification (Lý giải quyết định):

**Bằng chứng kỹ thuật ủng hộ GO:**

1. **Bài toán rõ ràng, có cấu trúc:** Input (GPS xe + % pin + model xe) và Output (tin nhắn hướng dẫn tiếng Việt) đều xác định rõ — phù hợp LLM Feature đơn giản, không cần Agent phức tạp.

2. **Dữ liệu sẵn có:** Logs sự cố pin, API định vị xe, API trạm sạc VinFast đều đang hoạt động. Không cần đầu tư thêm cơ sở hạ tầng dữ liệu.

3. **Ranh giới an toàn kiểm soát được:** Hai quy tắc cứng (`[DRAFT_ONLY]` bắt buộc + pin < 5% → mobile charger) có thể enforce qua System Prompt và code validation. Rủi ro khi AI sai được Dispatcher chặn lại trước khi gửi đến tài xế.

4. **ROI rõ ràng:** 80 sự cố/ngày × 12 phút tiết kiệm/lượt = ~16 giờ công dispatcher/ngày → tương đương 2 FTE tiết kiệm. Chi phí triển khai LLM API thấp hơn nhiều so với chi phí nhân sự.

5. **Scope hẹp, rủi ro thấp:** Bắt đầu với pilot tại 1 trung tâm điều vận (Hà Nội), đo metrics trong 2 tuần, mở rộng sau khi đạt ngưỡng 98% accuracy.

**Scope triển khai Prototype:**
- Tuần 1–2: Xây dựng + test System Prompt với Gemini 2.5 Flash trên dữ liệu giả lập.
- Tuần 3–4: Pilot với 1 dispatcher thực tế, ghi log 100 sự cố đầu tiên.
- Tuần 5: Đánh giá metrics, quyết định scale-up.
