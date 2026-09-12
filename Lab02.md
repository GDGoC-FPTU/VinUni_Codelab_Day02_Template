Phase 1:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vinmec | Tốn thời gian | Bác sĩ và điều dưỡng mất nhiều thời gian tra cứu, tổng hợp lịch sử khám từ hệ thống HIS thành bệnh án tóm tắt trước mỗi ca. |
| 2 | VinFast | Lặp lại | Nhân viên KCS/QC phải kiểm tra ngoại quan (trầy xước, khe hở) bằng mắt thường hàng ngàn lần/ngày, dễ sai sót do mệt mỏi. |
| 3 | Xanh SM | Pain từ người khác | Tài xế phàn nàn hệ thống heatmap gợi ý điểm đón khách cập nhật chậm, dẫn đến tỷ lệ chạy xe không tải cao. |
| 4 | Vinpearl | AI có thể tốt hơn | Chatbot CSKH hiện tại rập khuôn, chưa thể tự động tư vấn và thiết kế lịch trình trải nghiệm cá nhân hóa theo sở thích. |
| 5 | Vinhomes | Tốn thời gian | Ban quản lý tốn nhân lực đọc, phân loại và gán tag thủ công hàng trăm khiếu nại của cư dân mỗi ngày để chuyển cho tổ kỹ thuật. |

Phase 2:
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Tự động tổng hợp và tóm tắt bệnh án từ    │
│ lịch sử khám phân mảnh trên hệ thống HIS.                   │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ và Điều dưỡng phòng khám        │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Mở HIS ──> 2. Lục tìm lịch sử cũ ──> 3. Đọc từng KQ    │
│   xét nghiệm ──> 4. Gõ lại tóm tắt vào hồ sơ khám mới.      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (Tra cứu thủ    │
│ công trên giao diện cũ) (⏱ 5-10 phút/lượt bệnh nhân)      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Tự động gộp bước 2, 3,│
│ 4: AI đọc toàn bộ lịch sử và trích xuất thành 1 đoạn tóm tắt│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ "Giảm thời gian chuẩn bị hồ sơ trước khám từ 10 min ──>     │
│ under 2 min/bệnh nhân. Tăng số ca khám được/ngày."          │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Dự báo vùng có nhu cầu gọi xe cao (Heatmap│
│ AI) trước 15-30 phút để giảm tỷ lệ xe chạy rỗng/không tải.  │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Tài xế (tốn pin, thu nhập giảm) &      │
│ Khách hàng (đợi xe lâu lúc cao điểm/mưa).                   │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Mở app xem heatmap ──> 2. Lái xe đến vùng đỏ ──>       │
│   3. Tới nơi thì mất khách ──> 4. Chạy vòng quanh tìm cuốc  │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3 & 4 (Heatmap chỉ    │
│ hiển thị quá khứ, độ trễ cao) (⏱ 15-20 phút/lượt chạy rỗng) │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Dự báo trước nhu cầu ở│
│ bước 1 dựa trên thời tiết, sự kiện, lịch sử chuyến đi.      │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ "Giảm tỷ lệ thời gian/quãng đường xe chạy không tải từ      │
│ 30% ──> under 15%."                                         │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu): Tự động đọc hiểu, phân loại và gán tag    │
│ khiếu nại của cư dân để điều phối đến đúng kỹ thuật viên.   │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH/Ban quản lý tòa nhà     │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                        │
│   1. Cư dân gửi text/ảnh ──> 2. NV đọc nội dung ──> 3. Chọn │
│   tag (điện/nước/vệ sinh) ──> 4. Tạo ticket gửi kỹ thuật.   │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (Quá tải ticket │
│ giờ cao điểm, gán nhầm bộ phận) (⏱ 3-5 phút/lượt ticket)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Ngay sau Bước 1: AI   │
│ đọc text/ảnh, tự động tag và assign thẳng thay thế bước 2,3.│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│ "Giảm thời gian phân loại ticket từ 5 min ──> under 1 min,  │
│ độ chính xác routing ticket > 95%."                         │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘