# 🔍 Phase 1 — SCAN & Phase 2 — QUICK-ASSESS
**Học viên:** Phùng Quốc Việt  
**Đơn vị:** Vin Smart Future (Vingroup)  
**Mảng đề tài lựa chọn:** Khối Dịch Vụ & Trợ Lý Xe Điện Thông Minh (VinFast & Xanh SM)

---

# 🔍 Phase 1 — SCAN: Bảng Quét Cơ Hội Tối Ưu Hóa Bằng AI (4 Lenses)

Sử dụng 4 lăng kính (Repetitive, Time-consuming, AI-upgrade, Stakeholder Pain) để quét qua các hoạt động vận hành tại các công ty thành viên Vingroup:

| # | Đơn vị thành viên | Lăng kính (Lens) | Mô tả chi tiết bài toán & Điểm nghẽn vận hành |
|---|---|---|---|
| **1** | **VinFast & Xanh SM** | **Pain từ người khác & Tốn thời gian** | **Tài xế xe điện khó tìm trạm sạc trống phù hợp nhất theo dung lượng pin còn lại và tình trạng thực tế:** Tài xế mở app xem danh sách nhưng không rõ trụ trống, lái xe đến nơi mới biết hết trụ hoặc phải xếp hàng chờ 30-45 phút, sau đó lại phải loay hoay tìm trạm khác. |
| **2** | **Xanh SM (GSM)** | **Lặp lại** | **So khớp và điều phối cứu hộ khi xe taxi điện cạn pin khẩn cấp (< 5%):** Điều phối viên phải kiểm tra thủ công mức pin, định vị GPS, tìm trụ sạc VinFast còn trống phù hợp cổng sạc hoặc điều xe sạc pin lưu động (Mobile Charging Vehicle). |
| **3** | **Vinhomes** | **Pain từ người khác** | **Phân loại khẩn cấp & Điều phối phản ánh cư dân trên App Vinhomes Resident:** Hàng trăm phản ánh mỗi ngày (mất nước, kẹt thang máy, ồn ào, báo cháy). Helpdesk mất 10–15 phút/ticket để phân cấp độ ưu tiên (P1 khẩn cấp vs P4 thường), dễ chậm trễ cứu hộ. |
| **4** | **Vinmec** | **Tốn thời gian** | **Tự động hóa soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary):** Bác sĩ điều trị mất 25–30 phút/bệnh nhân tổng hợp từ hàng chục kết quả xét nghiệm, phẫu thuật, đơn thuốc để viết bản tóm tắt dặn dò dễ hiểu cho bệnh nhân. |
| **5** | **Vinpearl** | **AI-upgrade** | **Quét và phản hồi khiếu nại review tiêu cực thời gian thực (Guest Sentiment Shield):** Rà soát review 1–2 sao từ Google Maps, Agoda, Booking.com để cảnh báo khủng hoảng truyền thông và draft văn bản phản hồi cá nhân hóa kèm đề xuất bồi thường. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

---

### 📇 QUICK PROBLEM CARD #1

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                                  │
│                                                                                        │
│ Bài toán (1 câu): Chatbot thông minh hỗ trợ cố vấn dịch vụ phân loại mã lỗi xe điện     │
│ VinFast từ mô tả tự nhiên của khách hàng.                                              │
│                                                                                        │
│ Công ty thành viên: [x] VinFast   [ ] Xanh SM   [ ] Vinhomes   [ ] Vinmec   [ ] Khác   │
│                                                                                        │
│ Ai đang đau (Actor)? Cố vấn dịch vụ (Service Advisor) tại các Xưởng Dịch Vụ VinFast.  │
│                                                                                        │
│ Workflow thủ công hiện tại (4 bước):                                                   │
│   1. Nhận cuộc gọi / ghi chú mô tả sự cố bằng tiếng Việt từ khách                      │
│   → 2. Tra cứu sổ tay kỹ thuật và mã lỗi DTC                                           │
│   → 3. Kiểm tra lịch trống của cầu nâng và thợ chuyên trách                            │
│   → 4. Soạn thảo văn bản báo giá và xác nhận lịch hẹn gửi khách                        │
│                                                                                        │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (⏱ 15 phút/lượt)                               │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Trích xuất triệu chứng và mapping mã lỗi DTC.     │
│                                                                                        │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian tiếp nhận từ 20 min ──> dưới 3 min│
│                                                                                        │
│ Quick Architecture: [x] LLM Feature                                                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 QUICK PROBLEM CARD #2

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                                  │
│                                                                                        │
│ Bài toán (1 câu): Phân loại mức độ khẩn cấp và tự động điều phối phản ánh cư dân trên  │
│ App Vinhomes Resident đến đúng bộ phận phụ trách (Cơ điện, Vệ sinh, An ninh).          │
│                                                                                        │
│ Công ty thành viên: [ ] VinFast   [ ] Xanh SM   [x] Vinhomes   [ ] Vinmec   [ ] Khác   │
│                                                                                        │
│ Ai đang đau (Actor)? Nhân viên trực Tổng đài / Helpdesk Ban Quản Lý Khu Đô Thị.        │
│                                                                                        │
│ Workflow thủ công hiện tại (4 bước):                                                   │
│   1. Đọc tin nhắn phản ánh của cư dân gửi về App Vinhomes Resident                     │
│   → 2. Xác minh thông tin căn hộ, tòa nhà và tính chất khiếu nại                       │
│   → 3. Đánh giá thủ công mức độ khẩn cấp (P1: Khẩn cấp/cháy nổ/kẹt thang vs P4: Thường)│
│   → 4. Tạo ticket trên phần mềm quản lý và gọi điện phân công tổ kỹ thuật tòa nhà      │
│                                                                                        │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 10 phút/ticket, dễ sót sự cố P1)       │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 và 4 (Phân loại & gán ticket tự động) │
│                                                                                        │
│ Đo thành công bằng gì (Metric có số)?                                                  │
│   - Giảm thời gian phản hồi ban đầu từ 15 phút ──> dưới 30 giây.                       │
│   - 100% sự cố khẩn cấp P1 được kích hoạt cảnh báo tức thì đến đội an ninh.           │
│                                                                                        │
│ Quick Architecture: [x] LLM Feature                                                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 QUICK PROBLEM CARD #3 (LỰA CHỌN CHÍNH CỦA TÔI — ĐỀ TÀI THỰC HIỆN CODE)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Tài xế xe điện khó tìm trạm sạc trống phù │
│ hợp nhất theo dung lượng pin còn lại và tình trạng thực tế  │
│ Công ty thành viên: [x] VinFast   [ ] Xanh SM   [ ] Vinhomes│
│                     [ ] Vinmec    [ ] Khác (Ghi rõ)________ │
│                                                             │
│ Ai đang đau (Actor)? Tài xế VinFast & Tài xế Xanh SM        │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Xe sắp hết pin, tài xế mở app bản đồ tìm trạm sạc ──>   │
│   2. Xem danh sách các trạm gần nhưng không rõ trụ trống ──>│
│   3. Lái xe đến nơi mới phát hiện hết trụ sạc hoặc đang chờ dài──>│
│   4. Tiếp tục phải tìm đường sang trạm sạc khác             │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 30 phút/lượt)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Dự báo lượng pin tiêu │
│ hao, quét trạng thái thời gian thực của cổng sạc và gợi ý   │
│ lộ trình tối ưu có sẵn trụ trống.                           │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   VD: "Giảm thời gian chờ đợi tại trạm sạc từ 30 min ──> 0 min"│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết Định Lựa Chọn Của Nhóm:
Nhóm thống nhất chọn bài toán **"Quick Problem Card #3: Tài xế xe điện khó tìm trạm sạc trống phù hợp nhất theo dung lượng pin còn lại và tình trạng thực tế"** làm bài toán trọng tâm để thực hiện Deep-Dive phân tích chi tiết và lập trình bản mẫu (Prompt Prototype) vì:
1. **Giải quyết đúng nỗi đau lớn nhất:** Xóa bỏ hoàn toàn tình trạng tài xế phải di chuyển lòng vòng hoặc xếp hàng chờ đợi 30 phút tại trạm sạc đang quá tải.
2. **Giá trị kinh tế & vận hành vượt bậc:** Đối với tài xế taxi Xanh SM, tiết kiệm 30 phút chờ sạc tương đương tăng thêm 2 cuốc xe/ngày, tối ưu hóa doanh thu đội xe; đối với người dùng cá nhân VinFast, giúp xóa bỏ triệt để rào cản tâm lý "lo ngại cạn pin".
3. **Tính khả thi và ranh giới an toàn rõ ràng:** Kết hợp giữa cơ chế Agentic loop quét trạng thái thời gian thực của trụ sạc, dự báo tiêu hao pin và ranh giới an toàn tuyệt đối khi pin ở ngưỡng nguy cấp (< 5% thì lập tức kích hoạt xe sạc pin lưu động).
