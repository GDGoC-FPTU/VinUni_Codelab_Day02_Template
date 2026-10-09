# 🔍 Phase 1 — SCAN

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vinhomes | Lặp lại (Repetitive) | Phân loại hàng ngàn yêu cầu hỗ trợ (bảo trì, khiếu nại, dịch vụ) từ cư dân trên app Vinhomes Resident mỗi ngày và gán cho đúng phòng ban xử lý. |
| 2 | Vinmec | Tốn thời gian (Time-consuming) | Bác sĩ mất nhiều thời gian đọc, tổng hợp hồ sơ bệnh án cũ và các kết quả xét nghiệm rời rạc để đưa ra tóm tắt tình trạng bệnh nhân trong các ca hội chẩn/chuyển ca. |
| 3 | VinFast | Stakeholder Pain | Kỹ thuật viên bảo hành tại xưởng mất nhiều thời gian tra cứu hàng ngàn trang tài liệu HDSD và sơ đồ mạch điện phức tạp để tìm cách xử lý các mã lỗi (DTC) hiếm gặp trên xe EV. |
| 4 | Vinpearl | AI-upgrade | Khách hàng hỏi về lịch trình vui chơi, giá vé, hoặc yêu cầu tư vấn tour qua fanpage/chatbot hiện tại chỉ nhận được các câu trả lời rập khuôn theo kịch bản (rule-based) gây nhàm chán và tỷ lệ drop-off cao. |
| 5 | Xanh SM | Lặp lại (Repetitive) | CSKH phải nghe/đọc và tóm tắt lại các báo cáo sự cố từ tài xế (xe hỏng, khách hủy chuyến, tai nạn nhẹ) để nhập lên hệ thống quản lý Jira/CRM. |

---

# 🃏 Phase 2 — QUICK-ASSESS

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây.

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1 - VINHOMES                            │
│                                                             │
│ Bài toán: Phân loại và dự thảo phản hồi tự động cho các yêu │
│ cầu/khiếu nại của cư dân trên app.                          │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên CSKH (Ban quản lý Vinhomes). │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Đọc ticket ──> 2. Xác định loại lỗi (điện/nước/an ninh)│
│   ──> 3. Soạn phản hồi ──> 4. Assign cho kỹ thuật viên.     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 8-10 phút)   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Đọc ticket, tự động   │
│ phân loại (Tag) và dự thảo sẵn câu trả lời.                 │
│                                                             │
│ Đo thành công bằng gì? Giảm thời gian xử lý ticket từ       │
│ 10 phút xuống < 2 phút/ticket. Độ chính xác phân loại > 90%.│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2 - VINMEC                              │
│                                                             │
│ Bài toán: Tự động tổng hợp và trích xuất thông tin quan     │
│ trọng từ hồ sơ bệnh án đa nguồn của bệnh nhân.              │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Bác sĩ chuyên khoa, Điều dưỡng trưởng. │
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Mở HIS ──> 2. Đọc từng phiếu xét nghiệm/khám cũ ──>    │
│   3. Ghi chú tay tóm tắt ──> 4. Viết báo cáo hội chẩn.      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 15-20 phút)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Trích xuất Entity (chỉ│
│ số bất thường, bệnh nền) và tạo đoạn tóm tắt bệnh sử ngắn.  │
│                                                             │
│ Đo thành công bằng gì? Tiết kiệm 10 phút/bệnh nhân. Không   │
│ bỏ sót (Recall = 100%) các bệnh nền nghiêm trọng (Dị ứng).  │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3 - VINFAST                             │
│                                                             │
│ Bài toán: Trợ lý AI tra cứu mã lỗi (DTC) và quy trình sửa   │
│ chữa từ tài liệu kỹ thuật dành cho xưởng dịch vụ.           │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)? Kỹ thuật viên (KTV) sửa chữa tại xưởng.│
│                                                             │
│ Workflow thủ công hiện tại:                                 │
│   1. Đọc mã lỗi từ máy Scan ──> 2. Mở file PDF HDSD ──>     │
│   3. Ctrl+F tìm mã lỗi ──> 4. Đọc quy trình xử lý.          │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3 (⏱ 10-30 phút)  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Tìm kiếm semantic và  │
│ tổng hợp trực tiếp các bước sửa chữa từ kho tài liệu.       │
│                                                             │
│ Đo thành công bằng gì? Giảm thời gian tra cứu từ 20 phút    │
│ xuống < 1 phút. Cung cấp chính xác trang tài liệu tham chiếu│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘
```
