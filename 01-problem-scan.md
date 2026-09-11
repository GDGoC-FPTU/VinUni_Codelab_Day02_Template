# 01 — Problem Scan & Quick Cards (Cá nhân)

**Học viên:** Nguyễn Văn An
**Mảng kinh doanh:** Xanh SM (GSM) — Vận hành xe taxi/xe máy điện thông minh

---

# 🔍 Phase 1 — SCAN: Danh sách bài toán

| #   | Subsidiary | Lens               | Mô tả ngắn bài toán                                                                                                                                                                                                                                                    |
| --- | ---------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Xanh SM    | Tốn thời gian      | Nhân viên CSKH xử lý khiếu nại "tài xế đi vòng / lộ trình không tối ưu": phải tự tay mở lại lịch sử GPS chuyến đi, so sánh với route ngắn nhất trên Google Maps để xác định đúng/sai trước khi trả lời khách (mất 10-15 phút/ticket, ~120 ticket/ngày toàn thành phố). |
| 2   | Xanh SM    | Lặp lại            | Đối soát doanh thu cuối ca: kế toán ca trực đối chiếu thủ công giữa số cuốc + số tiền ghi trên app tài xế với số liệu thanh toán (tiền mặt, QR, ví điện tử) trên hệ thống trung tâm để phát hiện chênh lệch.                                                           |
| 3   | Xanh SM    | Pain từ người khác | Tài xế phàn nàn việc phân bổ cuốc xe theo khu vực không công bằng vào giờ thấp điểm — điều phối viên chia cuốc thủ công theo cảm tính vì không có bảng theo dõi mật độ tài xế/khu vực theo thời gian thực.                                                             |
| 4   | Xanh SM    | AI có thể tốt hơn  | Chatbot CSKH hiện tại trả lời rập khuôn (kịch bản cố định) cho các câu hỏi về chính sách hủy chuyến, hoàn tiền, phí chờ — khách phải chuyển tiếp qua tổng đài viên cho hầu hết câu hỏi có ngữ cảnh cụ thể.                                                             |
| 5   | Xanh SM    | Tốn thời gian      | Quản lý khu vực mỗi sáng phải đọc lại toàn bộ log sự cố kỹ thuật (xe hỏng, va chạm nhẹ, xe hết pin dọc đường) từ tối hôm trước để tổng hợp báo cáo gửi cấp trên — hiện làm thủ công trên Excel, mất ~45 phút/ca.                                                       |
| 6   | Xanh SM    | Lặp lại            | Khi khách khiếu nại giá cước "tính sai", tổng đài viên phải tự đối chiếu km thực tế theo GPS với km hệ thống tính phí cho từng chuyến — tra cứu và giải trình bằng tay.                                                                                                |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

## Card #1 — Xử lý khiếu nại "lộ trình không tối ưu"

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán: Khách khiếu nại tài xế "đi vòng", CSKH phải tự    │
│ tra lại lộ trình GPS và so sánh với route tối ưu.           │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Nhân viên CSKH (quá tải ticket), khách hàng    │
│ (chờ phản hồi lâu, mất niềm tin)                             │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                         │
│   1. Nhận ticket khiếu nại từ App/Hotline                   │
│   → 2. Tra cứu lộ trình GPS thực tế của chuyến               │
│   → 3. So sánh thủ công với route ngắn nhất (Google Maps)   │
│   → 4. Soạn phản hồi giải thích/đền bù gửi khách             │
│                                                             │
│ Bước nào tốn nhất? Bước 2-3 (⏱ 10 phút/ticket)               │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3               │
│ (Tự động pull GPS log → so sánh route → tính % lệch)         │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian xử lý ticket từ 12 phút ──> dưới 3 phút.      │
│                                                             │
│ Quick Architecture: [x] LLM Feature (so sánh + draft phản hồi)│
└─────────────────────────────────────────────────────────────┘
```

## Card #2 — Đối soát doanh thu cuối ca

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán: Kế toán ca trực đối chiếu thủ công số cuốc/doanh  │
│ thu giữa app tài xế và hệ thống thanh toán trung tâm.       │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Kế toán ca trực (làm việc lặp lại cuối mỗi ca) │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                         │
│   1. Export báo cáo cuốc xe từ app tài xế                    │
│   → 2. Export báo cáo thanh toán từ hệ thống trung tâm       │
│   → 3. So khớp thủ công từng dòng trên Excel                 │
│   → 4. Đánh dấu và báo cáo các dòng lệch số                  │
│                                                             │
│ Bước nào tốn nhất? Bước 3 (⏱ 30 phút/ca/khu vực)             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3                 │
│ (Auto-match 2 bảng dữ liệu, flag các dòng chênh lệch bất thường)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm thời gian đối soát từ 30 phút ──> dưới 5 phút/ca.       │
│                                                             │
│ Quick Architecture: [x] Rule / State-Machine                 │
└─────────────────────────────────────────────────────────────┘
```

## Card #3 — Chatbot CSKH chính sách hủy chuyến/hoàn tiền

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán: Chatbot CSKH trả lời rập khuôn, không xử lý được  │
│ các câu hỏi có ngữ cảnh cụ thể về hủy chuyến/hoàn tiền.     │
│ Công ty thành viên: [x] Xanh SM (GSM)                       │
│                                                             │
│ Ai đang đau? Khách hàng (chờ chuyển tiếp tổng đài viên),    │
│ Tổng đài viên (quá tải câu hỏi đơn giản lặp lại)             │
│                                                             │
│ Workflow thủ công hiện tại (4 bước):                         │
│   1. Khách hỏi chatbot theo ngữ cảnh cụ thể                  │
│   → 2. Chatbot không nhận diện được intent → chuyển tổng đài │
│   → 3. Tổng đài viên tra cứu chính sách áp dụng cho case     │
│   → 4. Trả lời và xử lý hoàn tiền (nếu đủ điều kiện)         │
│                                                             │
│ Bước nào tốn nhất? Bước 2-3 (⏱ 8 phút/case, tắc nghẽn hàng đợi)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1-3                │
│ (LLM đọc hiểu ngữ cảnh, tra cứu chính sách, trả lời trực tiếp)│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                        │
│ Giảm tỉ lệ chuyển tổng đài viên từ 70% ──> dưới 30% case.    │
│                                                             │
│ Quick Architecture: [x] LLM Feature (RAG trên chính sách)     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Đề xuất lựa chọn cho Deep-Dive (nhóm sẽ thảo luận và chốt)

Cá nhân tôi đề xuất **Card #1 (Khiếu nại lộ trình không tối ưu)** vì:

- Ảnh hưởng trực tiếp đến trải nghiệm khách hàng và uy tín thương hiệu.
- Có dữ liệu GPS sẵn có để làm cơ sở so sánh (khả thi kỹ thuật cao).
- Rủi ro khi AI sai thấp hơn các bài toán tài chính (Card #2) hay pháp lý — phù hợp để bắt đầu với LLM Feature có HITL.
