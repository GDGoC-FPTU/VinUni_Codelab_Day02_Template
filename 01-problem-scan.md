# Phase 1 & Phase 2: AI Product Scoping (Vin Smart Future)

- **Học viên:** Nguyễn Văn Tùng (nguyenvantung011204@gmail.com)
- **Đơn vị:** Vin Smart Future — Tập đoàn Vingroup
- **Chủ đề lựa chọn:** Trợ lý AI Hỗ trợ Soạn thảo Ticket Leo thang Cảnh báo An ninh Mạng từ VinSOC Tier 1 lên VinSOC Tier 2 (Hệ thống Y tế Vinmec)

---

## 🔍 Phase 1 — SCAN (Khảo sát qua 4 Lenses)

Áp dụng 4 Lenses để tìm kiếm các bài toán vận hành thực tế tại các công ty thành viên Vingroup:

### 📝 Danh sách bài toán tìm được:

| # | Đơn vị thành viên | Lens | Mô tả ngắn bài toán thực tế |
|---|---|---|---|
| 1 | **Vinmec (VinSOC)** | **Tốn thời gian & Pain** | Khi phát hiện cảnh báo an ninh thật (True Positive) trên hệ thống bệnh viện (HIS/PACS), nhân viên VinSOC Tier 1 phải copy log thủ công, tra cứu IP/mã độc và tự viết văn bản mô tả để tạo ticket gửi lên Tier 2 Incident Response. Mỗi ticket mất khoảng 15-16 phút, chiếm phần lớn thời gian ca trực. |
| 2 | **VinFast** | **Lặp lại** | Kỹ sư vận hành trạm sạc phải lọc thủ công hàng nghìn bản ghi log sạc xe điện mỗi ngày để phân biệt giữa lỗi phần mềm sạc thực sự với trường hợp tài xế tự rút súng sạc sớm. |
| 3 | **Xanh SM (GSM)** | **Pain từ người khác** | Đội vận hành phải kiểm tra thủ công dữ liệu GPS và tốc độ di chuyển của tài xế khi có nghi vấn gian lận cuốc xe ảo (GPS spoofing) để trục lợi chính sách thưởng, tốn nhiều thời gian đối soát. |
| 4 | **Vinhomes** | **Tốn thời gian** | Nhân viên ban quản lý phải đọc và phân loại bằng tay hàng trăm phản ánh của cư dân mỗi ngày gửi qua ứng dụng Vinhomes Resident để chuyển cho đúng bộ phận kỹ thuật hoặc an ninh xử lý. |
| 5 | **Vinpearl** | **AI có thể tốt hơn** | Nhân viên chăm sóc khách hàng phải trả lời lặp đi lặp lại các câu hỏi về combo vé, giờ mở cửa các khu vui chơi VinWonders và tra cứu thủ công tình trạng phòng trống trên hệ thống. |

---

## 🃏 Phase 2 — QUICK-ASSESS (3 Quick Problem Cards)

Chọn 3 bài toán tiềm năng nhất để điền thẻ đánh giá nhanh:

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1 (CHỌN LÀM BÀI TOÁN CHÍNH)             │
│                                                             │
│ Bài toán (1 câu): Hỗ trợ chuyên viên VinSOC Tier 1 trích    │
│ xuất IoC, làm sạch dữ liệu mật và soạn nháp ticket leo thang│
│ sự cố lên Tier 2 bảo vệ hệ thống y tế Vinmec.               │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec (VinSOC)  [ ] Khác           │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│ - Chuyên viên trực ca VinSOC Tier 1 (quá tải gõ ticket).     │
│ - Đội VinSOC Tier 2 IR (nhận ticket thiếu log, thiếu IoC).  │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Nhận alert ──> 2. Xem tiến trình ──> 3. Tra cứu IoC    │
│   ──> 4. Gõ ticket trên Jira ──> 5. Bàn giao sang Tier 2    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                            │
│ Bước 4 (Soạn ticket: 6 phút) & Bước 3 (Tra cứu IoC: 4 phút).│
│ Tổng cộng mất khoảng ~16 phút/ticket.                       │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│ - Dùng Regex tự động che mật khẩu và mã bệnh nhân PID.      │
│ - Dùng LLM tóm tắt log, gợi ý kỹ thuật MITRE ATT&CK và      │
│   soạn sẵn bản nháp ticket chuẩn hóa.                       │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ - Giảm thời gian làm ticket từ 16 phút xuống <= 3.5 phút.   │
│ - Tỷ lệ ticket đạt chuẩn ngay lần đầu >= 95%.               │
│ - 100% dữ liệu mật và mã bệnh nhân được che giấu tự động.   │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
│ Ghi chú: Chỉ sinh bản nháp (draft_only: True), con người    │
│ duyệt 100%, không cho AI tự động ngắt mạng máy chủ bệnh viện│
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tự động gom và tóm tắt thông tin bối cảnh │
│ từ các nguồn Threat Intelligence khi phát hiện mã băm lạ    │
│ nhắm vào máy chủ VinFast và Vinmec.                         │
│                                                             │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (VinSOC)          │
│                                                             │
│ Ai đang đau (Actor)? Chuyên viên phân tích an ninh VinSOC.  │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Lấy IP/Hash lạ ──> 2. Mở VirusTotal, AlienVault OTX    │
│   ──> 3. Đọc bài phân tích bằng tiếng Anh ──> 4. Ghi chú lại│
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                            │
│ Bước 2 & 3: Mở nhiều tab tra cứu và đọc báo cáo phân tán    │
│ (mất khoảng 10-15 phút cho mỗi chỉ số IoC lạ).              │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│ Gọi API lấy thông tin danh tiếng và dùng LLM tóm tắt nhanh  │
│ mối liên hệ với các nhóm tấn công APT đã biết.              │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Giảm thời gian tra cứu từ 15 phút xuống dưới 2 phút/IoC.    │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Phân tích log tọa độ GPS và cảm biến pin  │
│ để phát hiện các trường hợp tạo cuốc xe ảo của tài xế XanhSM│
│                                                             │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Đội vận hành & phòng chống gian lận.   │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Nhận báo cáo nghi vấn ──> 2. Xuất dữ liệu GPS & cuốc   │
│   ──> 3. Kiểm tra độ lệch tọa độ ──> 4. Kết luận xử lý     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                            │
│ Bước 2 & 3: Đối chiếu thủ công chuỗi thời gian di chuyển    │
│ (mất khoảng 20-25 phút cho mỗi trường hợp khiếu nại).       │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                       │
│ Phân tích chuỗi tọa độ để nhận diện các bước nhảy GPS bất   │
│ thường và tự động tóm tắt bằng chứng nghi vấn.              │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ Rút ngắn thời gian xác minh từ 25 phút xuống dưới 3 phút.   │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

