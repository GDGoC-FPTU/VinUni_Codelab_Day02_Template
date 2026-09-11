# 04 — Workflow Diagram (Current-State)
**Bài toán:** Xanh SM — Xử lý khiếu nại "tài xế đi vòng / lộ trình không tối ưu"

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

> Bản vẽ trực quan (hình ảnh) tương ứng: xem `04-workflow-diagram.png`.