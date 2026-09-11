<!-- ========================================================================== -->
<!-- THÔNG TIN NHÓM & DANH SÁCH THÀNH VIÊN                                      -->
<!-- Tên nhóm: safe-drive                                                       -->
<!-- Danh sách thành viên:                                                      -->
<!-- 1. Nguyễn Đức Phát - nguyenducphat.edu@gmail.com                           -->
<!-- 2. Đỗ Thành Đạt - dothanhdat10x@gmail.com                                  -->
<!-- 3. Nguyễn Ngọc Minh - nnminh433@gmail.com                                  -->
<!-- 4. Phạm Quang Đạt - phamqdat99@gmail.com                                   -->
<!-- 5. Lâm Hoàng Phúc - lamhoangphuc2003st@gmail.com                           -->
<!-- 6. Chử Trần Phương Nam - tranphuongnam932004@gmail.com                     -->
<!-- ========================================================================== -->

# 01 — Problem Scan & Quick Problem Cards (Vin Smart Future)

**Đơn vị:** Vin Smart Future (Vingroup)  
**Nhóm thực hiện:** safe-drive  
**Vai trò:** AI Product Engineer  

---

## 🏛️ Bối cảnh thực địa tại Vin Smart Future
Vin Smart Future là đầu mối công nghệ tập trung cho toàn bộ hệ sinh thái Vingroup. Với vai trò là Kỹ sư Sản phẩm AI (AI Product Engineer), chúng tôi tiến hành khảo sát hoạt động vận hành tại các đơn vị thành viên: VinFast, Xanh SM (GSM), Vinhomes, Vinmec và Vinpearl nhằm nhận diện các điểm nghẽn (bottlenecks) có thể giải quyết hiệu quả bằng trí tuệ nhân tạo.

---

# 🔍 Phase 1 — SCAN: Bảng Quét Cơ Hội Qua 4 Lenses

Chúng tôi áp dụng **4 Lenses** (Lặp lại, Tốn thời gian, AI-upgrade, Pain từ người khác) để quét qua các quy trình vận hành:

| # | Subsidiary | Lens | Mô tả ngắn bài toán & Điểm nghẽn thực tế |
|:---:|:---|:---|:---|
| **1** | **Xanh SM (GSM)** | **Tốn thời gian** | **Xử lý khẩn cấp sự cố pin thực địa:** Tài xế gọi báo xe sắp cạn pin hoặc lỗi sạc. Điều phối viên (Dispatcher) phải mở nhiều màn hình tra cứu GPS, tìm trụ sạc VinFast còn trống và gõ tin nhắn chỉ đường thủ công (mất 12–15 phút/lượt). |
| **2** | **Vinhomes** | **AI-upgrade** | **Phân loại & định tuyến phản ánh cư dân:** App Vinhomes Resident nhận hàng nghìn phản ánh mỗi ngày (ồn ào, mất nước, hỏng đèn). Nhân viên CSKH đọc và chuyển tiếp thủ công, phản hồi rập khuôn mất từ 6–12 tiếng. |
| **3** | **VinFast** | **Lặp lại** | **Đối soát hóa đơn trụ sạc đối tác:** Hằng tuần bộ phận tài chính phải đối chiếu thủ công hàng chục nghìn phiên sạc liên kết từ các đối tác trạm sạc bên ngoài với hệ thống core billing của VinFast. |
| **4** | **Xanh SM (GSM)** | **Pain từ người khác** | **Phân tích nguyên nhân hủy cuốc giờ cao điểm:** Tài xế và khách hàng phàn nàn vì cuốc xe bị hủy nhiều. Hiện phải nghe lại ghi âm tổng đài và đọc ghi chú tài xế thủ công để tổng hợp pattern nguyên nhân. |
| **5** | **Vinmec** | **Pain từ người khác** | **Soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary):** Bác sĩ mất 20–30 phút/bệnh nhân để tổng hợp các kết quả xét nghiệm, chẩn đoán thành văn bản dễ hiểu cho người bệnh, gây quá tải giờ trực. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Từ danh sách trên, chúng tôi chọn ra **Top 3 bài toán khả thi nhất** để lập thẻ đánh giá nhanh:

---

### 📇 QUICK PROBLEM CARD #1 — Xanh SM: Xử lý sự cố pin thực địa

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                       │
│                                                                             │
│ Bài toán: Hỗ trợ điều phối viên phản ứng nhanh khi tài xế taxi điện Xanh SM │
│ báo cáo cạn kiệt pin hoặc gặp sự cố sạc giữa đường.                         │
│ Công ty thành viên: [x] Xanh SM (GSM)                                       │
│                                                                             │
│ Ai đang đau (Actor)? Điều phối viên (quá tải), Tài xế taxi (hoang mang).    │
│                                                                             │
│ Workflow thủ công hiện tại (5 bước):                                        │
│   1. Nhận cuộc gọi khẩn ──> 2. Tra cứu toạ độ GPS xe                        │
│   ──> 3. Tra cứu trạm sạc VinFast trống ──> 4. Soạn tin nhắn chỉ dẫn/cứu hộ │
│   ──> 5. Gửi tài xế và gọi cứu hộ nếu pin < 5%                             │
│                                                                             │
│ Bước nào tốn nhất? Bước 3 & 4 (⏱ 10-12 phút/lượt).                          │
│ AI nhảy vào hỗ trợ ở bước nào? Bước 3 & 4 (Tự động hóa đối chiếu và draft   │
│ tin nhắn định tuyến kèm kiểm tra ranh giới an toàn pin < 5%).               │
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                       │
│ - Giảm thời gian xử lý sự cố từ 15 phút ──> dưới 3 phút/lượt.               │
│ - Tỉ lệ chỉ đúng trạm sạc tương thích cổng xe đạt >= 98%.                   │
│                                                                             │
│ Quick Architecture: [x] LLM Feature (Co-pilot sinh draft + HITL phê duyệt)  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 QUICK PROBLEM CARD #2 — Vinhomes: Trợ lý phân loại phản ánh cư dân

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                       │
│                                                                             │
│ Bài toán: Tự động phân loại, trích xuất độ khẩn cấp và định tuyến ý kiến    │
│ phản ánh của cư dân trên App Vinhomes Resident đến đúng ban quản lý tòa nhà.│
│ Công ty thành viên: [x] Vinhomes                                            │
│                                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH Vinhomes, Cư dân khu đô thị.            │
│                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                        │
│   1. Cư dân gửi ticket ──> 2. Nhân viên đọc & phân loại thủ công            │
│   ──> 3. Chuyển ticket về kỹ thuật/vệ sinh tòa nhà ──> 4. Phản hồi cư dân   │
│                                                                             │
│ Bước nào tốn nhất? Bước 2 & 3 (⏱ 30-45 phút/ticket, tồn đọng 12 tiếng).    │
│ AI nhảy vào hỗ trợ ở bước nào? Bước 2 & 3 (Phân loại intent + trích xuất    │
│ tòa nhà + gợi ý mức độ khẩn cấp P1/P2/P3).                                  │
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                       │
│ - Giảm thời gian định tuyến từ 4 tiếng ──> dưới 30 giây.                    │
│ - Độ chính xác phân loại phòng ban đạt >= 92%.                              │
│                                                                             │
│ Quick Architecture: [x] LLM Feature (Phân loại văn bản + trích xuất thực thể)│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 QUICK PROBLEM CARD #3 — VinFast: Đối soát hóa đơn sạc điện đối tác

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                       │
│                                                                             │
│ Bài toán: So khớp và phát hiện bất thường trong dữ liệu phiên sạc giữa các  │
│ đối tác trạm sạc bên ngoài và dữ liệu viễn thông xe VinFast hằng tuần.      │
│ Công ty thành viên: [x] VinFast                                             │
│                                                                             │
│ Ai đang đau (Actor)? Chuyên viên kế toán & đối soát tài chính VinFast.       │
│                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                        │
│   1. Xuất file Excel đối tác ──> 2. Vlookup với database nội bộ             │
│   ──> 3. Lọc các dòng lệch số kWh/tiền ──> 4. Gửi email yêu cầu giải trình   │
│                                                                             │
│ Bước nào tốn nhất? Bước 2 & 3 (⏱ 3 ngày công/tuần).                         │
│ AI nhảy vào hỗ trợ ở bước nào? Bước 3 (Phát hiện gian lận và lệch số liệu). │
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                       │
│ - Giảm thời gian xử lý từ 3 ngày ──> dưới 2 giờ.                            │
│ - Tỉ lệ nhận diện sai lệch bất thường đạt 100%.                             │
│                                                                             │
│ Quick Architecture: [x] Rule-based / Data Pipeline (Không cần LLM)          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Quyết Định Lựa Chọn Bài Toán Của Nhóm

Nhóm thống nhất lựa chọn **Card #1: Xanh SM — Xử lý sự cố pin thực địa** để thực hiện Deep-Dive vì các lý do chiến lược sau:
1. **Tác động trực tiếp tới vận hành thời gian thực (Real-time Business Impact):** Sự cố hết pin ảnh hưởng ngay lập tức tới an toàn giao thông, trải nghiệm khách hàng và doanh thu cuốc xe của Xanh SM.
2. **Tính AI-Fit rõ nét:** Bài toán đòi hỏi vừa xử lý dữ liệu có cấu trúc (toạ độ GPS, % pin, trạm sạc) vừa cần xử lý ngôn ngữ tự nhiên (soạn tin nhắn hỗ trợ tài xế thân thiện, chuẩn chỉ), rất phù hợp với mô hình **LLM Feature (Co-pilot)**.
3. **Ranh giới an toàn (Operational Boundaries) khắt khe:** Có bài toán ranh giới sinh tử rõ ràng (pin dưới 5% không được điều đi xa > 5km, bắt buộc duyệt `[DRAFT_ONLY]`), hoàn hảo cho việc xây dựng và kiểm thử kỹ thuật Prompt Prototype.
4. **Lý do loại trừ Card #2 & #3:**
   * *Card #2 (Vinhomes):* Rủi ro tranh chấp pháp lý và khiếu nại của cư dân cần thu thập thêm dữ liệu gán nhãn lịch sử.
   * *Card #3 (VinFast):* Bản chất là bài toán so khớp bảng dữ liệu dạng số, giải quyết bằng SQL / Python Rule-based script sẽ chính xác 100% và tiết kiệm hơn nhiều so với việc dùng LLM.
