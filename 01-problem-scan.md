# 01-problem-scan.md — Phase 1 (SCAN) & Phase 2 (QUICK-ASSESS)

**Đơn vị:** Vin Smart Future (Tập đoàn Vingroup)  
**Khối kinh doanh tập trung:** **GSM — Xanh SM (Vận hành Taxi & Xe máy điện thông minh)**  
**Dự án:** AI Product Scoping & Boundary Engineering  
**Học viên / Kỹ sư:** Nhóm Kỹ sư AI Vin Smart Future  

---

## 🔍 Phase 1 — SCAN: Bảng Quét Cơ Hội Tối Ưu Vận Hành Xanh SM (GSM)

Áp dụng **4 Lenses tìm bài toán AI** (Lặp lại, Tốn thời gian, AI có thể tốt hơn, Pain từ người khác) quét qua toàn bộ chuỗi vận hành thực địa của **Xanh SM (GSM)**:

| # | Đơn vị thành viên | Lens áp dụng | Tên bài toán / Nghiệp vụ thủ công | Mô tả ngắn & Bottleneck quan sát |
|---|---|---|---|---|
| **1** | **Xanh SM (GSM)** | **Tốn thời gian** | Xử lý sự cố sạc pin & cạn kiệt pin thực địa | Khi tài xế báo pin yếu/nguy cơ chết máy giữa đường, điều phối viên mất 15 phút mở nhiều màn hình đối chiếu GPS, kiểm tra trụ sạc VinFast còn trống phù hợp chuẩn xe (VF5/VF8/e34) và gõ tin nhắn hướng dẫn thủ công. |
| **2** | **Xanh SM (GSM)** | **Pain từ người khác** | Phân tích ghi âm cuộc gọi hủy cuốc & chống gian lận đi ngoài | Tỷ lệ hủy cuốc 15–25% giờ cao điểm; nhiều tài xế gọi điện năn nỉ khách hủy cuốc trên app để chở tiền mặt trốn chiết khấu; đội ngũ QA/QC chỉ nghe audit được <2% cuộc gọi, báo cáo trễ 7 ngày. |
| **3** | **Xanh SM (GSM)** | **AI-upgrade** | Điều vận điểm đón thông minh (Smart Pickup Dispatching) | Khách định vị sai sảnh tòa nhà (đặc biệt tại Vinhomes, khu đô thị lớn); tài xế và khách nhắn tin qua lại tìm nhau mất 5–10 phút; AI có thể phân tích tin nhắn và bản đồ để đề xuất điểm đón tối ưu, tránh đường cấm dừng đỗ. |
| **4** | **Xanh SM (GSM)** | **Lặp lại** | Tái phân bổ cuốc & kiểm tra pin khi khách đổi điểm đến | Khách yêu cầu đổi lộ trình hoặc đi xa hơn lộ trình ban đầu; điều phối viên phải tính toán thủ công xem dung lượng pin hiện tại của xe có đủ đến đích an toàn hay cần điều xe khác thay thế. |
| **5** | **Xanh SM (GSM)** | **AI-upgrade** | Phân loại & xử lý khiếu nại đánh giá 1–3 sao sau chuyến đi | Mỗi ngày có hàng nghìn đánh giá tiêu cực (xe có mùi, tài xế bấm còi nhiều, đi sai đường); CSKH mất 10–12 tiếng đọc từng đánh giá để phân loại lỗi và soạn phản hồi xin lỗi khách hàng. |
| **6** | **Xanh SM (GSM)** | **Lặp lại** | Điều phối lịch sạc đêm phân tán cho đội xe Taxi Xanh | Hàng vạn xe taxi điện cần sạc qua đêm; điều phối viên phải lên lịch thủ công cho từng tổ xe để tránh tập trung quá đông gây nghẽn trụ sạc VinFast và tối ưu giá điện giờ thấp điểm. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Dành riêng cho Xanh SM)

Chọn lọc Top 3 bài toán cấp bách nhất từ danh sách SCAN của **Xanh SM**:

---

### 🪪 Thẻ Bài Toán #1: Xanh SM — Xử Lý Sự Cố Pin Xe Điện & Điều Hướng Trạm Sạc (Selected for Deep-Dive)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                   │
│                                                                         │
│ Bài toán: Co-pilot hỗ trợ điều phối viên phản hồi khẩn cấp và điều      │
│           hướng trạm sạc cho tài xế Xanh SM gặp sự cố pin yếu.          │
│ Công ty thành viên: [x] Xanh SM (GSM)                                   │
│                                                                         │
│ Ai đang đau? Tài xế (sợ chết máy giữa đường), Điều phối viên (quá tải)  │
│                                                                         │
│ Workflow thủ công hiện tại (5 bước):                                    │
│   1. Tài xế gọi hotline điều phối báo pin yếu / sắp hết                 │
│   ──> 2. Điều phối viên tra cứu tọa độ GPS của xe trên bản đồ          │
│   ──> 3. Mở tab trụ sạc VinFast tra cứu trạm trống tương thích xe       │
│   ──> 4. Gõ tay tin nhắn chỉ đường gửi qua Driver App                   │
│   ──> 5. Nếu pin xe < 5%, liên hệ điều xe sạc cứu hộ di động            │
│                                                                         │
│ Bước nào tốn thời gian nhất? Bước 3 & 4 (⏱ 10–12 phút/lượt)             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4                        │
│ (Tự động pull vị trí ──> Tìm trạm phù hợp ──> Draft tin [DRAFT_ONLY])   │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ • Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút (giảm 80%).     │
│ • 0 trường hợp xe < 5% pin bị chỉ dẫn đi trạm xa > 5km.                 │
│ • 100% tin nhắn draft có thẻ [DRAFT_ONLY] cho con người duyệt.          │
│                                                                         │
│ Quick Architecture: [x] LLM Feature (Co-pilot sinh Draft tin nhắn + Rule)│
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 🪪 Thẻ Bài Toán #2: Xanh SM — Phân Tích Ghi Âm Cuộc Gọi Hủy Chuyến & Chống Gian Lận Đi Ngoài

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                   │
│                                                                         │
│ Bài toán: Tự động phân tích hội thoại cuộc gọi & ghi chú của tài xế khi │
│           hủy cuốc để bóc tách 10 lý do thực tế và phát hiện chở ngoài. │
│ Công ty thành viên: [x] Xanh SM (GSM)                                   │
│                                                                         │
│ Ai đang đau? Ban Vận hành (rò rỉ doanh thu), Đội kiểm soát QA/QC        │
│                                                                         │
│ Workflow thủ công hiện tại (4 bước):                                    │
│   1. Cuốc xe bị hủy, hệ thống lưu file ghi âm và note tài xế           │
│   ──> 2. QA auditor chọn mẫu ngẫu nhiên 1-2% tổng số cuốc hủy           │
│   ──> 3. QA nghe từng file audio và đối chiếu tọa độ xe (3-5 phút)      │
│   ──> 4. Gõ tay mã phân loại lý do vào bảng tính Excel                 │
│                                                                         │
│ Bước nào tốn thời gian nhất? Bước 3 & 4 (⏱ 5–7 phút/lượt, độ phủ < 2%)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4                        │
│ (Speech-to-Text + LLM Multimodal phân loại 10 nhóm lý do tự động)       │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ • Tăng độ phủ audit từ 2% ──> 100% cuốc hủy có ghi âm.                 │
│ • Rút ngắn thời gian phân tích từ 5 phút ──> dưới 15 giây/cuốc.         │
│ • Phát hiện tài xế xúi khách hủy đi ngoài đạt độ chính xác F1 >= 92%.   │
│                                                                         │
│ Quick Architecture: [x] LLM Feature (Multimodal Pipeline / Batch Engine)│
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 🪪 Thẻ Bài Toán #3: Xanh SM — Điều Vận Điểm Đón Thông Minh (Smart Pickup Dispatching)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                   │
│                                                                         │
│ Bài toán: Phân tích tin nhắn trao đổi giữa tài xế - khách và vị trí GPS │
│           để tự động gợi ý điểm đón thuận tiện nhất, tránh tắc đường.   │
│ Công ty thành viên: [x] Xanh SM (GSM)                                   │
│                                                                         │
│ Ai đang đau? Khách hàng (đứng chờ lâu), Tài xế (bị phạt vì dừng sai chỗ)│
│                                                                         │
│ Workflow thủ công hiện tại (4 bước):                                    │
│   1. Khách đặt xe, ghim vị trí theo định vị GPS điện thoại              │
│   ──> 2. Tài xế đến gần nhưng không thấy khách, gọi/nhắn tin hỏi sảnh   │
│   ──> 3. Khách mô tả vị trí đứng bằng ngôn ngữ tự nhiên (mất 3-5 phút)  │
│   ──> 4. Tài xế phải đi lòng vòng quay đầu xe tìm khách                 │
│                                                                         │
│ Bước nào tốn thời gian nhất? Bước 2 & 3 (⏱ 4–6 phút/cuốc xe)            │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 & 3                        │
│ (Trích xuất landmark từ tin nhắn ──> Đối chiếu bản đồ ──> Gợi ý sảnh)   │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                   │
│ • Giảm thời gian đón khách (Pickup Time) từ 7 phút ──> dưới 3 phút.     │
│ • Giảm 50% số lượng cuộc gọi hỏi đường giữa tài xế và khách hàng.       │
│                                                                         │
│ Quick Architecture: [x] LLM Feature (NLP Landmark Extraction & Mapping) │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Quyết định Lựa chọn Bài toán cho Deep-Dive của Xanh SM

* **Bài toán được lựa chọn:** **Quick Problem Card #1 — Xanh SM Xử lý sự cố pin xe điện & điều hướng trạm sạc thực địa**.
* **Lý do lựa chọn:**
  1. **Trực tiếp giải quyết bài toán sống còn của vận hành xe điện:** Tình trạng xe cạn kiệt pin giữa đường ảnh hưởng trực tiếp đến an toàn giao thông, SLA phục vụ của Xanh SM và hạ tầng trạm sạc VinFast.
  2. **Ranh giới vận hành rõ ràng (Operational Boundary):** Cần thiết lập ranh giới an toàn nghiêm ngặt (pin < 5% cấm điều hướng trạm xa > 5km, bắt buộc điều xe sạc cứu hộ; tin nhắn chỉ dẫn bắt buộc có thẻ `[DRAFT_ONLY]` để điều phối viên duyệt).
  3. **Khớp 100% với nguyên mẫu kỹ thuật (Prompt Prototype):** Cho phép kiểm thử tự động ranh giới an toàn trên Gemini 2.5 Flash ngay tại `starter-code/prompt_prototype.py`.
