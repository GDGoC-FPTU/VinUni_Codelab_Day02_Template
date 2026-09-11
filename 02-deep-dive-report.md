# 📋 Báo Cáo Phân Tích Sâu (Deep-Dive Report) — Vin Smart Future

**Dự án:** Trợ lý Điều phối Thông minh Xử lý Sự cố Sạc Pin Thực địa (Xanh SM Smart Dispatcher Co-pilot)  
**Tác giả:** Huy — AI Product Engineer, Vin Smart Future  
**Đơn vị thụ hưởng:** Khối Vận Hành Xanh SM (GSM — Vingroup)  

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow (Quy trình vận hành hiện tại)

Quy trình xử lý thủ công hiện tại khi tài xế Xanh SM gọi điện về tổng đài báo sự cố pin yếu/hết pin giữa đường:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Tiếp nhận    │     │ Tra cứu định │     │ Tra cứu trạm │     │ Soạn tin nhắn│
│ cuộc gọi     │ ──> │ vị GPS xe   │ ──> │ sạc VinFast  │ ──> │ hướng dẫn    │
│              │     │              │     │ còn trụ trống│     │ gửi tài xế   │
│ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │     │ Ai: Dispatch │
│ ⏱ 2 phút     │     │ ⏱ 2 phút     │     │ ⏱ 5 phút 🔴  │     │ ⏱ 5 phút 🔴  │
│ In: Điện thoại│     │ In: Biển số  │     │ In: Vị trí GPS│     │ In: Địa chỉ  │
│ Out: Log sự cố│     │ Out: Toạ độ  │     │ Out: Trạm sạc│     │ Out: SMS/App │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                       │
                                                                       ▼
                                                                ┌──────────────┐
                                                                │ Bước 5       │
                                                                │ Điều xe cứu  │
                                                                │ hộ (nếu cần) │
                                                                │ Ai: Dispatch │
                                                                │ ⏱ 1 phút     │
                                                                │ In: Pin < 5% │
                                                                │ Out: Lệnh xe │
                                                                └──────────────┘
🔴 = Điểm nghẽn cổ chai (Bottleneck)
⏱ Tổng thời gian xử lý trung bình: 15 phút/lượt.
🔄 Handoffs: 3 lần chuyển giao giữa hệ thống thoại tổng đài, bản đồ định vị GPS, và CMS trạm sạc VinFast.
```

---

## 3.2. Problem Statement (6-Field Standard) — Vin Smart Future

| Trường thông tin | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | **Điều phối viên (Dispatcher)** tại Trung tâm Vận hành Điều xe Xanh SM (Hà Nội, TP.HCM). |
| **2. Current Workflow** | Khi tài xế gọi báo cạn pin hoặc trạm sạc tắc nghẽn, điều phối viên chuyển qua lại giữa 3 màn hình (CMS tổng đài, bản đồ GPS xe, dashboard trụ sạc VinFast), tìm trụ sạc trống có đầu sạc tương thích (CCS2), tự gõ tin nhắn chỉ đường gửi qua SMS/App tài xế, hoặc gọi đội xe cứu hộ pin lưu động nếu pin dưới 5%. Quy trình 5 bước thủ công mất trung bình 15 phút/lượt. |
| **3. Bottleneck** | **Bước 3 & Bước 4 (Chiếm 10 phút / 67% thời gian):** Tra cứu thủ công trạm sạc trống có cổng sạc phù hợp với dòng xe (VF5/VF e34/VF8) trong bán kính khả thi và soạn thảo văn bản chỉ dẫn đường đi chi tiết kèm cảnh báo an toàn. |
| **4. Business Impact** | Toàn hệ thống Xanh SM ghi nhận ~80-100 cuộc gọi sự cố pin mỗi ngày trong giờ cao điểm. Gây lãng phí hơn **20 giờ làm việc/ngày** của đội ngũ điều phối; xe nằm chờ gây ách tắc giao thông, giảm tỉ lệ hoàn thành chuyến 12-15%, khiến tài xế ức chế và khách hàng hủy cuốc. |
| **5. Success Metric** | 1. **Thời gian (Efficiency):** Giảm thời gian xử lý sự cố từ **15 phút xuống dưới 3 phút/lượt** (giảm 80%).<br>2. **Độ chính xác (Quality):** Đạt **≥ 98%** tỉ lệ chỉ dẫn đúng loại cổng sạc và trạm sạc còn trụ trống thực tế.<br>3. **An toàn (Safety Zero Defect):** **0%** trường hợp xe pin < 5% bị hướng dẫn đi xa > 5km dẫn đến chết máy giữa đường. |
| **6. Operational Boundary** | **Được phép:** Tự động tổng hợp dữ liệu GPS và API trạm sạc trống; tự động soạn bản nháp (draft) tin nhắn chỉ đường; tự động đề xuất lệnh điều xe cứu hộ khi pin dưới ngưỡng an toàn.<br>**NGHIÊM CẤM:** AI **không được tự ý gửi tin nhắn trực tiếp** cho tài xế mà chưa qua phê duyệt của điều phối viên (bắt buộc Human-in-the-loop); **không được gợi ý trạm sạc cách xa > 5km** khi pin xe báo dưới 5%. |

---

## 3.3. Future-State Flow & AI Fit

### Phân tích AI-Fit Matrix (Lựa chọn công nghệ):
* **Rule / State-Machine:** Thích hợp để check điều kiện cứng (`pin < 5%` hoặc khoảng cách trạm sạc), nhưng không thể sinh ra văn bản chỉ đường thân thiện, linh hoạt theo tình hình giao thông thực tế cho tài xế.
* **Agentic Loop tự trị hoàn toàn:** Rủi ro an toàn giao thông rất cao nếu mô hình gặp lỗi ảo giác (hallucination) tự động điều xe sai chỗ hoặc điều xe chết máy trên cầu vượt/cao tốc.
* **Lựa chọn tối ưu: LLM Feature (Co-pilot với Human-in-the-loop):**
  - Kết hợp Rule-based Guardrails (kiểm soát pin và bán kính) với LLM (tổng hợp thông tin và soạn thảo văn bản nháp mang thẻ `[DRAFT_ONLY]`).
  - Con người (Dispatcher) giữ vai trò phê duyệt cuối cùng (Final approval gatekeeper).

### Quy trình tương lai (Future-State Flow):

```text
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ Bước 1          │       │ Bước 2          │       │ Bước 3          │       │ Bước 4          │
│ Nhận cuộc gọi / │ ────> │ 🔵 Auto-pull     │ ────> │ 🔵 AI Draft      │ ────> │ 🟢 Dispatcher   │
│ Driver click App│       │ GPS & Trạm sạc  │       │ Hướng dẫn / Lệnh│       │ Review & Click  │
│                 │       │ (Rule Pipeline) │       │ [DRAFT_ONLY]    │       │ Phát lệnh / Gửi │
└─────────────────┘       └─────────────────┘       └─────────────────┘       └─────────────────┘
                                                                                       │
                                                                                       ▼
                                                                                ↩️ Fallback Mechanism:
                                                                                Nếu LLM timeout (>5s)
                                                                                hoặc output sai format,
                                                                                hệ thống bật template mẫu
                                                                                hoặc Dispatcher gõ tay.
```

---

# 🏁 Phase 5 — EVALUATE (Đánh giá độ sẵn sàng & Quyết định)

### AI Readiness Checklist:
1. **Dữ liệu mẫu/Logs sạch:** ✅ **ĐẠT.** Hệ thống xe điện thông minh VinFast và GSM đã có sẵn API telemetry GPS, trạng thái SoC (State of Charge) pin theo thời gian thực và API mạng lưới trạm sạc V-GREEN.
2. **Kiểm soát rủi ro (HITL & Fallback):** ✅ **ĐẠT.** Toàn bộ khuyến nghị AI đều bắt đầu bằng thẻ `[DRAFT_ONLY]`, hiển thị trên màn hình điều vận để nhân viên bấm "Duyệt" hoặc chỉnh sửa nhanh trước khi gửi. Hệ thống có fallback về tin nhắn mẫu khi ngắt kết nối mạng.
3. **Mức độ sẵn sàng của Stakeholders:** ✅ **ĐẠT.** Ban Điều hành Xanh SM rất ủng hộ vì giải pháp giúp giảm tải trực tiếp cho nhân viên tổng đài và cải thiện SLA phục vụ tài xế.

### Quyết định của Ban Giám Đốc Vin Smart Future:
# 👉 **QUYẾT ĐỊNH: [GO] (Tiến hành xây dựng Prototype & Triển khai thử nghiệm)**

### Lý giải chi tiết (Justification):
* **Lợi ích kinh tế vượt trội:** Tiết kiệm ~15 giờ làm việc của điều phối viên mỗi ngày, giảm thời gian giải tỏa xe chết pin từ 15 phút xuống 3 phút, tăng doanh thu vận hành của đội xe thêm ước tính 1.2 tỷ VND/tháng trên toàn quốc.
* **Chi phí & Độ phức tạp thấp:** Mô hình chỉ cần tận dụng **Gemini 2.5 Flash** với chi phí inference cực thấp (< 0.0001$/lần gọi), thời gian phản hồi dưới 1 giây, dễ dàng tích hợp qua API vào Dashboard vận hành hiện tại.
* **Ranh giới an toàn tuyệt đối:** Đã xây dựng và kiểm thử thành công cơ chế bảo vệ ranh giới tại `starter-code/prompt_prototype.py`, bảo đảm loại trừ 100% nguy cơ rò rỉ rủi ro an toàn thực địa.
