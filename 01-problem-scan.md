# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân — Huy)

Bối cảnh: **Huy** — AI Product Engineer tại **Vin Smart Future (Vingroup)**.
Dưới đây là bảng phân tích 6 cơ hội tối ưu hóa vận hành thông qua **4 Lenses** tại các công ty thành viên Vingroup.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **Xanh SM** | Tốn thời gian | Điều phối viên xử lý thủ công các báo cáo khẩn cấp từ tài xế về sự cố cạn kiệt pin thực địa hoặc trạm sạc quá tải (mất 15-20 phút/lượt). |
| 2 | **VinFast** | Lặp lại | Đối chiếu và so khớp hóa đơn sạc điện giữa trạm nội bộ và các trạm sạc đối tác công cộng hằng tuần (mất 3 ngày làm việc thủ công của kế toán). |
| 3 | **Vinhomes** | AI-upgrade | Phân loại và định tuyến thông minh phản ánh/khiếu nại của cư dân trên App Vinhomes Resident (hiện tại CSKH phản hồi rập khuôn, mất 12-24 giờ). |
| 4 | **Vinmec** | Pain từ người khác | Bác sĩ mất 20-30 phút/bệnh nhân để soạn thảo tóm tắt bệnh án xuất viện và hướng dẫn sử dụng thuốc, gây chậm trễ thủ tục ra viện và áp lực lớn cho đội ngũ y tế. |
| 5 | **Xanh SM** | Lặp lại | Tự động phân bổ lại chuyến đi khi khách hàng đổi lộ trình hoặc điểm đến giữa chừng nhằm tối ưu cước phí và tuyến đường tài xế. |
| 6 | **Vinpearl** | AI-upgrade | Trợ lý số CSKH đa ngôn ngữ hỗ trợ giải đáp thắc mắc và đặt dịch vụ vui chơi, vé cáp treo theo thời gian thực cho khách quốc tế tại VinWonders. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân — Huy)

Chọn top 3 bài toán từ danh sách trên: **#1 (Xanh SM Sự cố sạc pin), #2 (VinFast Đối chiếu hóa đơn), #3 (Vinhomes CSKH Resident App)**.

## Quick Problem Card #1: Xanh SM — Xử lý sự cố sạc pin & điều phối cứu hộ thực địa

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Tài xế Xanh SM gặp sự cố hết pin/pin yếu khẩn cấp │
│ giữa đường cần hướng dẫn trạm sạc gần nhất hoặc gọi cứu hộ. │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Tài xế (bị kẹt, mất khách), Điều phối viên     │
│ (Dispatcher bị quá tải xử lý cuộc gọi).                     │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Nhận cuộc gọi khẩn từ tài xế báo pin yếu               │
│   ──> 2. Tra cứu thủ công toạ độ GPS xe trên bản đồ         │
│   ──> 3. Tra cứu trạm sạc VinFast còn trụ trống phù hợp     │
│   ──> 4. Soạn tin nhắn SMS/In-App chỉ đường gửi tài xế      │
│   ──> 5. Điều phối xe sạc pin di động cứu hộ nếu pin < 5%   │
│                                                             │
│ Bước nào tốn thời gian nhất? Bước 3 & 4 (⏱ 10-12 phút/lượt)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4            │
│ (Auto-pull vị trí & trạm trống -> AI draft tin chỉ dẫn)     │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ 1. Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút.   │
│ 2. Tỉ lệ điều phối chính xác trạm sạc phù hợp cổng sạc >=98%│
│                                                             │
│ Quick Architecture: [x] LLM Feature (Co-pilot hỗ trợ soạn)   │
└─────────────────────────────────────────────────────────────┘
```

---

## Quick Problem Card #2: VinFast — Tự động đối chiếu dữ liệu trạm sạc đối tác

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Đối chiếu số liệu điện năng tiêu thụ và doanh thu  │
│ giữa hệ thống telemetry VinFast và trạm sạc đối tác bên thứ 3│
│ Công ty thành viên: [x] VinFast                             │
│                                                             │
│ Ai đang đau? Chuyên viên tài chính kế toán trạm sạc.        │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Xuất file Excel log sạc từ hệ thống trụ VinFast        │
│   ──> 2. Tải bảng đối chiếu CDR từ đối tác hạ tầng          │
│   ──> 3. Dò tìm lệnh sạc lệch số kWh bằng hàm VLOOKUP       │
│   ──> 4. Viết email giải trình các giao dịch bất thường     │
│                                                             │
│ Bước nào tốn thời gian nhất? Bước 3 (⏱ 3 ngày/tuần)          │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3 & 4            │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Rút ngắn chu kỳ đối soát từ 72 giờ ──> dưới 30 phút.        │
│                                                             │
│ Quick Architecture: [x] Rule / Automation (Data Pipeline)   │
└─────────────────────────────────────────────────────────────┘
```

---

## Quick Problem Card #3: Vinhomes — Phân loại & định tuyến phản ánh cư dân

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Phân loại hàng nghìn phản ánh của cư dân trên App  │
│ Vinhomes Resident về an ninh, vệ sinh, sửa chữa kỹ thuật.   │
│ Công ty thành viên: [x] Vinhomes                            │
│                                                             │
│ Ai đang đau? Nhân viên Ban Quản lý tòa nhà và cư dân chờ đợi│
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Tiếp nhận ticket phản ánh trên CMS quản lý             │
│   ──> 2. Nhân viên đọc thủ công nội dung phản ánh           │
│   ──> 3. Gán tag phòng ban xử lý (Kỹ thuật/Lễ tân/An ninh)  │
│   ──> 4. Soạn phản hồi ban đầu xác nhận tiếp nhận           │
│                                                             │
│ Bước nào tốn thời gian nhất? Bước 2 & 3 (⏱ 15 phút/ticket)   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 & 4         │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Tăng tỉ lệ định tuyến tự động đúng ban chuyên trách >= 95%   │
│                                                             │
│ Quick Architecture: [x] LLM Feature (Classifier & Routing)  │
└─────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết định lựa chọn bài toán Deep-Dive của cá nhân & nhóm:
Chúng tôi quyết định chọn **"Quick Problem Card #1 — Xanh SM Xử lý sự cố sạc pin & điều phối cứu hộ thực địa"** làm trọng tâm phân tích sâu.

## Lý do lựa chọn:
1. **Tác động trực tiếp tới vận hành thời gian thực (Real-time Operations):** Taxi điện Xanh SM là mảng kinh doanh đang phát triển thần tốc. Việc giải quyết sự cố hết pin nhanh chóng giúp bảo vệ doanh thu, giảm thời gian chết (downtime) của xe và nâng cao trải nghiệm của tài xế.
2. **Ranh giới an toàn rõ ràng (Strict Safety Boundaries):** Tác vụ có sự kết hợp hoàn hảo giữa công nghệ AI (soạn thảo linh hoạt theo ngữ cảnh) và ranh giới vật lý bắt buộc (nghiêm cấm xe pin < 5% chạy đường xa, bắt buộc điều xe cứu hộ pin).
3. **Tại sao loại trừ Card #2 và #3?**
   - **Card #2 (VinFast):** Bài toán đối soát kế toán chủ yếu dựa trên logic toán học và dữ liệu bảng có cấu trúc; giải pháp Rule-based / Data Pipeline thông thường phù hợp và tiết kiệm hơn LLM.
   - **Card #3 (Vinhomes):** Xử lý phản ánh cư dân liên quan đến nhiều chính sách nhạy cảm về pháp lý và phí dịch vụ; rủi ro ảo giác (hallucination) cần nhiều thời gian chuẩn bị dữ liệu nội bộ trước khi áp dụng.
