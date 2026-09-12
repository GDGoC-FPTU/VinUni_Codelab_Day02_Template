##  Current
[Cư dân]                [NV trực BQL]              [KTV]                [Hệ thống]
   │                          │                       │                      │
   ▼                          │                       │                      │
①Gửi yêu cầu qua app/hotline  │                       │                      │
   (mô tả tự do, đôi khi kèm  │                       │                      │
    ảnh)                      │                       │                      │
   │──────🔄 Handoff─────────>│                       │                      │
   │                          ▼                       │                      │
   │                    ②Đọc & phân loại sự cố         │                      │
   │                    (điện/nước/khóa/thang máy...) │                      │
   │                    🔴 BOTTLENECK #1               │                      │
   │                    ⏱ 2-3 phút/ticket              │                      │
   │                    (mô tả mơ hồ → đọc lại,        │                      │
   │                     hỏi lại cư dân qua điện thoại)│                      │
   │                          │                       │                      │
   │                          ▼                       │                      │
   │                    ③Tra bảng phân công thủ công   │                      │
   │                    (Excel/bảng giấy: ai đang rảnh,│                      │
   │                     ai đúng chuyên môn, ai gần)   │                      │
   │                    🔴 BOTTLENECK #2 (nặng nhất)   │                      │
   │                    ⏱ 2-3 phút/ticket              │                      │
   │                    → tỷ lệ gán sai chuyên môn      │                      │
   │                      15-20%                       │                      │
   │                          │──────🔄 Handoff───────>│                      │
   │                          │    (gọi điện/nhắn Zalo)│                      │
   │                          │                       ▼                      │
   │                          │                 ④KTV xác nhận nhận việc       │
   │                          │                 (đôi khi từ chối vì sai      │
   │                          │                  chuyên môn hoặc đang bận    │
   │                          │                  → quay lại bước ③)          │
   │                          │                 🔴 rework loop nếu từ chối   │
   │                          │                       │                      │
   │                          │<─────🔄 Handoff────────│                      │
   │                          ▼                       │                      │
   │                    ⑤Cập nhật trạng thái ticket    │                      │
   │                    thủ công trên hệ thống         │                      │
   │                    ⏱ 1 phút                       │                      │
   │                          │───────────────────────────────🔄 Handoff───>│
   │                          │                       │              (Log hệ │
   │                          │                       │              thống)  │
   │<─────────────────────────┴───────────────────────┴──────────────────────┘
   ⑥Cư dân nhận thông báo KTV đang xử lý

   ## Future
  [Cư dân]                    [Hệ thống AI-Rule Hybrid]              [NV trực BQL]           [KTV]
   │                                 │                                  │                    │
   ▼                                 │                                  │                    │
①Gửi yêu cầu (ưu tiên dropdown       │                                  │                    │
  structured; free-text là fallback)│                                  │                    │
   │────────────🔄──────────────────>│                                  │                    │
   │                                 ▼                                  │                    │
   │                    🔵 AI Step: NLP classify category                │                    │
   │                    (chỉ chạy khi input là free-text)                │                    │
   │                    Confidence ≥ 80%? ──Yes──┐                       │                    │
   │                                 │            │                      │                    │
   │                              No │            ▼                      │                    │
   │                                 │      🔵 AI Step: Rule engine       │                    │
   │                                 │      match KTV (skill+workload+   │                    │
   │                                 │      khoảng cách) → top 2-3 gợi ý │                    │
   │                                 ▼                                  │                    │
   │                    ↩️ FALLBACK: Route thẳng cho                     │                    │
   │                    NV trực xử lý thủ công 100%                     │                    │
   │                    (case an toàn-nhạy cảm luôn                     │                    │
   │                     vào nhánh này, bất kể confidence)               │                    │
   │                                 │                                  │                    │
   │                                 └──────────🔄────────────────────>│                    │
   │                                                            🟢 Human Step (HITL):         │
   │                                                            NV xem gợi ý, xác nhận         │
   │                                                            hoặc chọn lại KTV               │
   │                                                            (1 click, không gõ tay)         │
   │                                                                    │                    │
   │                                                                    │────🔄─────────────>│
   │                                                                    │                    ▼
   │                                                                    │              🟢 Human Step:
   │                                                                    │              KTV nhận/từ chối
   │                                                                    │              (nếu từ chối →
   │                                                                    │              ↩️ fallback quay
   │                                                                    │              lại rule engine
   │                                                                    │              với KTV đã loại trừ)
   │                                                                    │<────🔄─────────────│
   │                                                                    ▼                    │
   │                                                          Hệ thống tự động cập nhật        │
   │                                                          trạng thái ticket (không cần      │
   │                                                          NV gõ tay)                        │
   │<───────────────────────────────🔄──────────────────────────────────────────────────────┘
   ⑥Cư dân nhận thông báo real-time