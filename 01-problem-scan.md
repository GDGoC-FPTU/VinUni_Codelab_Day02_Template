# 01 — Problem Scan & Quick-Assess
> **Lab 02: AI Product Scoping — Vin Smart Future**  
> Deliverable I1 · Individual · Phase 1 (SCAN) + Phase 2 (QUICK-ASSESS)

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

Dùng **4 Lenses** quét qua vận hành của các công ty thành viên Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công các phản hồi khẩn cấp từ tài xế về sự cố hết pin hoặc va chạm thực địa (mất 12–15 phút/lượt). Bottleneck nằm ở bước tra cứu trạm sạc trống và soạn tin nhắn chỉ dẫn. |
| 2 | **VinFast** | Lặp lại | So khớp hóa đơn sạc điện hằng tuần từ hàng nghìn trụ sạc liên kết đối tác với hóa đơn thực tế gửi về hệ thống tài chính — nhân viên kế toán làm thủ công trên Excel, mất 2–3 ngày/tuần. |
| 3 | **Vinhomes** | AI-upgrade | Hệ thống phân loại và điều hướng tự động các phản hồi/khiếu nại của cư dân (mất điện, hỏng thang máy, tiếng ồn) gửi qua App Vinhomes Resident — CSKH phản hồi rập khuôn, mất 12 giờ/ticket. |
| 4 | **Vinmec** | Pain từ người khác | Bác sĩ mất 20–30 phút/bệnh nhân để viết tóm tắt hồ sơ xuất viện thủ công; bác sĩ phàn nàn về quá tải giấy tờ, dễ bỏ sót thông tin thuốc quan trọng. |
| 5 | **Xanh SM** | Pain từ người khác | Tài xế phàn nàn: hệ thống gợi ý điểm đón khách không chính xác vào giờ cao điểm do không đọc được ghi chú tiếng Việt tự do của khách ("đón trước cổng trường, có biển đỏ"). |
| 6 | **Vinpearl** | Tốn thời gian | Quản lý khách sạn Vinpearl đọc thủ công hàng trăm review trên Booking.com / Agoda để tìm phàn nàn khẩn cấp (phòng bẩn, điều hoà hỏng) — không có hệ thống cảnh báo tự động. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

**Top 3 lựa chọn từ danh sách SCAN: #1 (Xanh SM Sự cố pin), #3 (Vinhomes CSKH), #4 (Vinmec Discharge Summary).**

---

## Card #1 — Xanh SM: Xử lý sự cố hết pin thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM báo sự cố hết pin / sạc sắp cạn  │
│ giữa đường — cần điều phối viên tìm trạm sạc gần + soạn   │
│ tin nhắn chỉ dẫn hoặc gọi xe cứu hộ pin di động.           │
│ Công ty thành viên: [x] Xanh SM (GSM)                      │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│   - Tài xế (chờ đợi, không đón khách được, mất thu nhập)  │
│   - Điều phối viên (phải xử lý 5 bước thủ công, quá tải)  │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Tài xế gọi tổng đài điều vận báo hết/sắp hết pin      │
│   → 2. Dispatcher tra cứu định vị xe trên bản đồ nội bộ   │
│   → 3. Tra thủ công trạm sạc VinFast còn trụ trống gần nhất│
│   → 4. Soạn tin nhắn chỉ dẫn đường + gửi qua App tài xế   │
│   → 5. Nếu pin < 5%: gọi thêm đội xe cứu hộ pin di động   │
│                                                             │
│ Bước nào tốn nhất? Bước 3–4 (⏱ ~10 phút/lượt)             │
│ AI hỗ trợ ở bước nào? Bước 2-3-4                           │
│  (Auto-pull GPS → Tìm trạm trống → Draft SMS chỉ dẫn)     │
│                                                             │
│ Đo thành công (Metric có số)?                               │
│   Giảm thời gian xử lý từ 15 phút → dưới 3 phút.          │
│   Tỉ lệ chỉ dẫn đúng trạm/loại cổng sạc đạt ≥ 98%.       │
│                                                             │
│ Quick Architecture: [x] LLM Feature                        │
│  (Không cần Agent tự trị: quy trình có cấu trúc cố định;  │
│   rủi ro điều phối sai trạm → xe cạn pin giữa đường)       │
└─────────────────────────────────────────────────────────────┘
```

---

## Card #2 — Vinhomes: Phân loại & Điều hướng phản ánh cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Cư dân gửi khiếu nại qua App Vinhomes Resident; │
│ nhân viên CSKH phân loại thủ công và chuyển đến đúng bộ   │
│ phận (điện, nước, thang máy, an ninh) theo từng tòa nhà.  │
│ Công ty thành viên: [x] Vinhomes                           │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│   - Cư dân (phàn nàn phải chờ 12+ giờ mới có phản hồi)   │
│   - Nhân viên CSKH (đọc và phân loại thủ công ~200 ticket │
│     mỗi ngày trên toàn hệ thống)                           │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi mô tả sự cố qua App (văn bản tự do)       │
│   → 2. CSKH đọc từng ticket, phân loại theo loại sự cố    │
│   → 3. Forward đến đúng bộ phận kỹ thuật từng tòa         │
│   → 4. Bộ phận kỹ thuật xác nhận tiếp nhận + xử lý       │
│                                                             │
│ Bước nào tốn nhất? Bước 2 (⏱ ~3 phút/ticket × 200 = 10h) │
│ AI hỗ trợ ở bước nào? Bước 1→2 (Auto-classify + route)   │
│                                                             │
│ Đo thành công (Metric có số)?                               │
│   Giảm thời gian phân loại từ 3 phút → dưới 10 giây.     │
│   Tỉ lệ phân loại đúng bộ phận đạt ≥ 92%.                │
│                                                             │
│ Quick Architecture: [x] Rule + LLM Feature                 │
│  (Rule-based router cho 5 loại sự cố phổ biến;            │
│   LLM cho các mô tả mơ hồ không khớp rule cứng)           │
└─────────────────────────────────────────────────────────────┘
```

---

## Card #3 — Vinmec: Soạn thảo tóm tắt hồ sơ xuất viện

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Bác sĩ Vinmec mất 20–30 phút/bệnh nhân để đọc  │
│ bệnh án điện tử, kết quả xét nghiệm, ghi chú điều dưỡng  │
│ và viết tóm tắt xuất viện thủ công bằng ngôn ngữ dễ hiểu │
│ cho bệnh nhân.                                             │
│ Công ty thành viên: [x] Vinmec                             │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│   - Bác sĩ (quá tải giấy tờ, ít thời gian khám bệnh)     │
│   - Bệnh nhân (tóm tắt xuất viện khó đọc, thiếu nhất quán)│
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Bác sĩ đọc toàn bộ bệnh án điện tử (EMR)             │
│   → 2. Tổng hợp kết quả xét nghiệm + chẩn đoán            │
│   → 3. Viết tay tóm tắt xuất viện bằng tiếng Việt         │
│   → 4. Ký duyệt + đưa cho bệnh nhân khi xuất viện         │
│                                                             │
│ Bước nào tốn nhất? Bước 1–3 (⏱ ~25 phút/bệnh nhân)       │
│ AI hỗ trợ ở bước nào? Bước 1→3 (Trích xuất EMR → Draft)  │
│                                                             │
│ Đo thành công (Metric có số)?                               │
│   Giảm thời gian soạn từ 25 phút → dưới 5 phút.          │
│   Bác sĩ chỉ cần review + ký thay vì viết từ đầu.        │
│                                                             │
│ Quick Architecture: [x] LLM Feature                        │
│  (Bắt buộc Human-in-the-loop: bác sĩ phải phê duyệt bản │
│   nháp trước khi đưa cho bệnh nhân — không auto-send)     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Quyết định lựa chọn để Deep-Dive:

**Nhóm chọn Card #1 — Xanh SM Sự cố hết pin thực địa** để thực hiện Phase 3 (DEEP-DIVE).

**Lý do loại bỏ các thẻ khác:**
- **Card #2 (Vinhomes CSKH):** Quy trình phân loại có thể giải quyết phần lớn bằng rule-based classifier trước, cần gom thêm dữ liệu ticket để fine-tune. Rủi ro sai sót liên quan đến tranh chấp pháp lý căn hộ.
- **Card #3 (Vinmec Discharge Summary):** Rủi ro y tế cực kỳ cao nếu LLM bỏ sót thông tin thuốc hoặc chẩn đoán — cần kiểm định lâm sàng nghiêm ngặt hơn trước khi triển khai.
