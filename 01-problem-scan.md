# 01 — Problem Scan (Cá nhân)

> Vin Smart Future — AI Product Scoping Lab

---

## 🔍 Phase 1 — SCAN

### 📝 List bài toán của tôi:

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | VinFast | Lặp lại (Repetitive) | Nhân viên đọc và gắn nhãn mức độ nghiêm trọng cho từng phản hồi/khiếu nại lỗi xe gửi qua hotline/app trước khi chuyển kỹ thuật xử lý. |
| 2 | Xanh SM | Pain từ người khác (Stakeholder Pain) | Phát hiện gian lận cuốc xe ảo (fake trip) — nhân viên soát xét thủ công các cuốc có pattern bất thường, gây thất thoát doanh thu và ảnh hưởng tài xế chân chính. |
| 3 | Xanh SM | AI-upgrade | AI hỗ trợ chung cho tổng đài hỗ trợ tài xế, tiếp nhận và phân luồng mọi yêu cầu vào 2 nhóm case riêng biệt: (a) case khẩn cấp (an toàn/tai nạn) cần phân loại & ưu tiên xử lý ngay, và (b) yêu cầu huỷ cuốc thông thường cần xử lý theo quy trình riêng — hiện cả hai đều do nhân viên trực xử lý thủ công chung một hàng đợi. |
| 4 | Vinpearl/VinWonders | AI-upgrade | Dự báo lượng khách theo ngày/giờ để điều phối nhân sự tại điểm soát vé — hiện dựa vào kinh nghiệm cá nhân của quản lý ca. |
| 5 | Vinpearl/VinWonders | AI-upgrade | Trả lời câu hỏi thường gặp (đa ngôn ngữ) của khách quốc tế về giờ mở cửa, giá vé combo đang bị chậm/không nhất quán. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Top 3 lựa chọn từ danh sách SCAN: **#1 (VinFast – Phân loại phản hồi lỗi xe), #2 (Xanh SM – Fake trip), #3 (Xanh SM – AI hỗ trợ tổng đài tài xế: gồm 2 nhóm case Khẩn cấp & Huỷ cuốc).**

### Quick Problem Card #1 — VinFast: Phân loại phản hồi lỗi xe

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                        │
│                                                               │
│ Bài toán: Nhân viên tiếp nhận khiếu nại phải đọc và phân      │
│ loại thủ công từng phản hồi lỗi xe trước khi chuyển kỹ thuật.│
│ Công ty thành viên: [x] VinFast                              │
│                                                               │
│ Ai đang đau (Actor)? Nhân viên CSKH/tiếp nhận khiếu nại tại  │
│ trung tâm dịch vụ; Kỹ thuật viên chờ ticket được phân loại   │
│ đúng để xử lý kịp thời.                                      │
│                                                               │
│ Workflow thủ công hiện tại (4 bước):                         │
│   1. Khách gửi phản hồi qua hotline/app ──> 2. Nhân viên đọc │
│   và đánh giá mức độ nghiêm trọng ──> 3. Gắn nhãn loại lỗi   │
│   (pin/phanh/phần mềm...) ──> 4. Chuyển ticket cho bộ phận   │
│   kỹ thuật phù hợp                                           │
│                                                               │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ ~6 phút/ticket, │
│ dễ đánh giá sai mức độ ưu tiên khi số lượng ticket lớn)      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3 (tự động đọc, │
│ phân loại mức độ nghiêm trọng + loại lỗi, đề xuất bộ phận    │
│ nhận xử lý)                                                  │
│                                                               │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian phân loại từ 6 phút ──> dưới 1 phút/ticket, │
│   độ chính xác gắn nhãn đạt ≥ 90%                            │
│                                                               │
│ Quick Architecture: [ ] No AI  [x] LLM  [ ] Rule  [ ] Agent  │
└─────────────────────────────────────────────────────────────┘
```

### Quick Problem Card #2 — Xanh SM: Phát hiện gian lận cuốc xe ảo (fake trip)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                        │
│                                                               │
│ Bài toán: Đội vận hành phải rà soát thủ công các cuốc xe có  │
│ dấu hiệu gian lận (fake trip) trong khối lượng dữ liệu lớn.  │
│ Công ty thành viên: [x] Xanh SM                              │
│                                                               │
│ Ai đang đau (Actor)? Nhân viên đội chống gian lận/vận hành;  │
│ Tài xế chân chính bị ảnh hưởng uy tín/thu nhập nếu xử lý sai.│
│                                                               │
│ Workflow thủ công hiện tại (4 bước):                         │
│   1. Hệ thống ghi nhận cuốc xe hoàn thành ──> 2. Nhân viên   │
│   lọc/rà soát thủ công các cuốc có dấu hiệu bất thường ──>   │
│   3. Đối chiếu GPS, thời gian, giá cước từng cuốc ──> 4. Ra  │
│   quyết định treo/khóa tài khoản nếu xác định gian lận       │
│                                                               │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ ~10 phút/cuốc   │
│ nghi vấn, khối lượng cuốc lớn nên dễ bỏ sót)                 │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3 (tự động lọc  │
│ pattern bất thường + tóm tắt bằng chứng để nhân viên duyệt)  │
│                                                               │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Giảm thời gian rà soát từ 10 phút ──> dưới 2 phút/cuốc     │
│   nghi vấn, tăng tỉ lệ phát hiện đúng gian lận lên ≥ 85%     │
│                                                               │
│ Quick Architecture: [ ] No AI  [x] LLM  [ ] Rule  [ ] Agent  │
└─────────────────────────────────────────────────────────────┘
```

### Quick Problem Card #3 — Xanh SM: AI hỗ trợ tổng đài tài xế (2 nhóm case: Khẩn cấp & Huỷ cuốc)

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                        │
│                                                               │
│ Bài toán: Tổng đài hỗ trợ tài xế xử lý chung một hàng đợi    │
│ cho mọi loại yêu cầu, trong đó có 2 nhóm case tách biệt về   │
│ bản chất: (a) Case khẩn cấp (an toàn/tai nạn), (b) Yêu cầu   │
│ huỷ cuốc thông thường — hoàn toàn xử lý thủ công.            │
│ Công ty thành viên: [x] Xanh SM                              │
│                                                               │
│ Ai đang đau (Actor)? Nhân viên trực tổng đài hỗ trợ tài xế;  │
│ Tài xế gặp sự cố khẩn cấp phải chờ đợi lâu vì xếp hàng FIFO  │
│ chung với các yêu cầu huỷ cuốc thông thường.                 │
│                                                               │
│ Workflow thủ công hiện tại (4 bước):                         │
│   1. Tài xế gửi yêu cầu vào kênh hỗ trợ chung ──> 2. Nhân    │
│   viên đọc lần lượt theo thứ tự đến (FIFO) ──> 3. Xác định   │
│   case thuộc nhóm nào: (a) Khẩn cấp hay (b) Huỷ cuốc ──>     │
│   4a. Nếu khẩn cấp: escalate ưu tiên ngay / 4b. Nếu huỷ cuốc:│
│   xử lý theo quy trình riêng (cập nhật hệ thống, hoàn phí...)│
│                                                               │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3 (⏱ case khẩn cấp   │
│ có thể trễ 5-10 phút nếu đến sau nhiều yêu cầu huỷ cuốc)     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3 (tự động phân │
│ loại case vào đúng nhóm (a)/(b), đẩy case khẩn cấp lên đầu   │
│ hàng đợi, đồng thời tự xử lý case huỷ cuốc theo policy rõ    │
│ ràng thuộc nhóm (b))                                         │
│                                                               │
│ Đo thành công bằng gì (Metric có số)?                        │
│   Nhóm (a) Khẩn cấp: giảm thời gian phát hiện + escalate từ  │
│   ~7 phút ──> dưới 30 giây.                                  │
│   Nhóm (b) Huỷ cuốc: tự động xử lý ≥70% case không cần con   │
│   người can thiệp trực tiếp.                                 │
│                                                               │
│ Quick Architecture: [ ] No AI  [ ] LLM  [ ] Rule  [x] Agent  │
└─────────────────────────────────────────────────────────────┘
```
