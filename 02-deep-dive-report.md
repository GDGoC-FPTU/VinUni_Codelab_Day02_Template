# 02 — Deep-Dive Report (Nhóm)

**Nhóm:** [Nguyễn Văn An]
**Bài toán chọn Deep-Dive:** Xanh SM — Xử lý khiếu nại "tài xế đi vòng / lộ trình không tối ưu"
**Nguồn gốc:** Card #1 trong `01-problem-scan.md`

---

## 3.1. Current-State Workflow

Quy trình xử lý khiếu nại lộ trình hiện tại của nhân viên CSKH Xanh SM:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận ticket  │     │ Tra cứu lộ   │     │ So sánh thủ  │     │ Soạn phản    │
│ khiếu nại    │ ──→ │ trình GPS    │ ──→ │ công với     │ ──→ │ hồi gửi khách│
│              │     │ thực tế      │     │ route ngắn   │     │              │
│              │     │              │     │ nhất (GG Map)│     │              │
│ Ai: CSKH     │     │ Ai: CSKH     │     │ Ai: CSKH     │     │ Ai: CSKH     │
│ ⏱ 2 phút     │     │ ⏱ 5 phút 🔴  │     │ ⏱ 5 phút 🔴  │     │ ⏱ 3 phút     │
│ In: Ticket   │     │ In: Mã chuyến│     │ In: Toạ độ   │     │ In: % lệch   │
│ App/Hotline  │     │ Out: Toạ độ  │     │ lộ trình     │     │ Out: Tin nhắn│
│ Out: Log     │     │ lộ trình     │     │ Out: % lệch  │     │ phản hồi     │
│ khiếu nại    │     │ thực tế      │     │ ước tính     │     │              │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                          Nếu % lệch > 15%       ▼
                                                          🔄 Handoff ──→ ┌──────────────┐
                                                                        │ Bước 5       │
                                                                        │ Chuyển hồ sơ │
                                                                        │ cho Trưởng ca│
                                                                        │ duyệt hoàn   │
                                                                        │ tiền         │
                                                                        │ Ai: Trưởng ca│
                                                                        │ ⏱ ~1 ngày    │
                                                                        │ (xử lý theo  │
                                                                        │ batch)       │
                                                                        └──────────────┘

🔴 = Bottleneck   🔄 = Handoff (chuyển giao giữa CSKH và Trưởng ca)
⏱ Tổng thời gian xử lý thủ công (không tính escalation): 15 phút/ticket.
⏱ Nếu có escalation hoàn tiền: cộng thêm tới 1 ngày chờ duyệt.
```

---

## 3.2. Problem Statement (6-field)

| Field                       | Nội dung                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Actor / Operator**     | Nhân viên CSKH (Customer Service) thuộc Trung tâm Chăm sóc Khách hàng Xanh SM, và Trưởng ca khi cần duyệt hoàn tiền.                                                                                                                                                                                                                                                                                                                              |
| **2. Current Workflow**     | Khi khách khiếu nại tài xế đi vòng, CSKH tra lại lộ trình GPS thực tế của chuyến trên hệ thống nội bộ, mở Google Maps để so sánh thủ công với route ngắn nhất, ước lượng % lệch bằng mắt/tính tay, rồi soạn tin nhắn phản hồi. Nếu % lệch có vẻ lớn, hồ sơ được chuyển tay cho Trưởng ca duyệt hoàn tiền (xử lý theo batch cuối ngày). 4-5 bước, hoàn toàn thủ công, mất 15 phút/ticket (chưa tính thời gian chờ duyệt hoàn tiền).                |
| **3. Bottleneck**           | Bước 2 & 3 (mất 10 phút): Tra cứu lộ trình GPS thủ công và so sánh bằng tay với route tham chiếu trên Google Maps — không có công cụ tự động tính % lệch, dễ sai số theo cảm tính từng nhân viên.                                                                                                                                                                                                                                                 |
| **4. Business Impact**      | Trung bình ~120 ticket khiếu nại lộ trình/ngày tại Hà Nội. Tổng thời gian xử lý thủ công ~30 giờ làm việc CSKH/ngày. Do đánh giá % lệch không nhất quán giữa các nhân viên, tỉ lệ khách khiếu nại lần 2 vì "trả lời không thoả đáng" ước tính ~20%, ảnh hưởng đến điểm hài lòng khách hàng (CSAT) và tăng tải cho Trưởng ca duyệt hoàn tiền.                                                                                                      |
| **5. Success Metric**       | 1. Giảm thời gian xử lý ticket từ 15 phút xuống dưới 3 phút (Efficiency).<br>2. Độ chính xác tính % lệch route khớp với số liệu GPS thực tế đạt ≥ 98% (Quality).<br>3. Giảm tỉ lệ khách khiếu nại lần 2 từ 20% xuống dưới 10% (Customer Satisfaction).                                                                                                                                                                                            |
| **6. Operational Boundary** | AI được phép: truy xuất log GPS chuyến đi, tự động tính % lệch so với route tham chiếu, soạn nháp phản hồi khách và đề xuất mức hoàn tiền tham khảo khi lệch > 15%. **CẤM:** AI không được tự động gửi phản hồi cho khách mà không có CSKH phê duyệt (Bắt buộc HITL); không được tự động phê duyệt/chuyển tiền hoàn — chỉ đề xuất, Trưởng ca vẫn phải duyệt; không được dùng ngôn từ quy kết tài xế gian lận/cố tình trong bất kỳ trường hợp nào. |

---

## 3.3. Future-State Flow & AI Fit

- **AI Fit:** Chọn **LLM Feature** (không chọn Rule thuần vì cần AI đọc hiểu và diễn giải ngữ cảnh khiếu nại bằng ngôn ngữ tự nhiên; không chọn Agentic Loop vì quy trình có phạm vi hẹp, rủi ro tài chính khi tự động phê duyệt hoàn tiền sai cần được kiểm soát chặt bằng con người).
- **Quy trình tương lai (Future-State):**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ 🔵 Bước 2    │     │ 🔵 Bước 3    │     │ 🟢 Bước 4    │
│ Nhận ticket  │ ──→ │ Auto-pull GPS│ ──→ │ AI tính % lệch│──→ │ CSKH review  │
│ khiếu nại    │     │ log & route  │     │ + draft phản │     │ & click duyệt│
│              │     │ tham chiếu   │     │ hồi/đề xuất  │     │ gửi khách    │
│              │     │              │     │ hoàn tiền    │     │              │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                    Nếu đề xuất hoàn tiền (>15%)   ▼
                                                    🔄 Handoff ──→ ┌──────────────┐
                                                                  │ 🟢 Bước 5    │
                                                                  │ Trưởng ca    │
                                                                  │ duyệt hoàn   │
                                                                  │ tiền cuối    │
                                                                  └──────────────┘

↩️ Fallback: Nếu dữ liệu GPS bị thiếu/lỗi hoặc AI không tự tin (confidence thấp),
   hệ thống trả về "cần xử lý thủ công" và CSKH quay lại quy trình cũ 4 bước.
```

---

## Phase 5 — EVALUATE

### AI Readiness Checklist:

- [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? — Có, log GPS chuyến đi đã được lưu trữ sẵn trong hệ thống điều vận.
- [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? — Có: CSKH luôn duyệt trước khi gửi (Bước 4); Trưởng ca luôn duyệt hoàn tiền cuối cùng (Bước 5); có fallback về quy trình thủ công khi dữ liệu thiếu.
- [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? — Có, đã trao đổi sơ bộ với leader CSKH, họ ủng hộ vì giảm tải công việc lặp lại.

### Quyết định cuối cùng:

**[x] GO (Bắt đầu xây dựng Prototype)** — với scope hẹp: chỉ tự động hoá bước tính % lệch route và soạn nháp phản hồi; KHÔNG tự động hoá việc phê duyệt hoàn tiền.

**Justification:**

> Bài toán có metric rõ ràng (% lệch route có thể tính bằng dữ liệu GPS sẵn có), rủi ro tài chính được kiểm soát chặt qua 2 lớp HITL (CSKH duyệt tin nhắn, Trưởng ca duyệt hoàn tiền), và giải pháp LLM Feature đơn giản (không cần Agent tự trị) đã đủ để giải quyết bottleneck chính là bước so sánh route thủ công. Kết quả stress-test trong `starter-code/prompt_prototype.py` cho thấy ranh giới an toàn ([DRAFT_ONLY], ngưỡng 15%, cấm ngôn từ buộc tội) đứng vững trước 3 kịch bản tấn công prompt khác nhau — đủ cơ sở để tiến hành xây dựng prototype ở quy mô nhỏ trước khi mở rộng.
