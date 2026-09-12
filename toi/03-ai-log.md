# 03 — AI Log & Reflection
## Lab 02 — AI Product Scoping

> **Lưu ý:** Đây là bản draft có cấu trúc. Những phần đánh dấu `TODO` cần được chỉnh theo đúng trải nghiệm thật của cá nhân trước khi nộp. Không nên nộp nguyên văn nếu không phản ánh đúng quá trình bạn đã làm.

---

## 1. Tôi đã dùng AI ở những bước nào?

### Brainstorm / Scoping
AI được dùng để:
- phản biện xem bài toán smart parking có thật sự cần LLM hay không;
- bóc tách current-state workflow;
- tách pain của tài xế khỏi pain của operations;
- gợi ý metric có thể đo được.

### AI-Fit
Điểm hữu ích nhất là việc tách:
- **LLM** cho natural-language intake và explanation;
- **rule/optimization** cho hard filter, scoring và routing;
- **state machine** cho hold/spot status.

Điều này giúp tránh việc dùng Agentic Loop chỉ vì muốn có “AI”.

### Safety / Boundary
AI hỗ trợ liệt kê các boundary:
- không tự cấp accessible spot;
- không bịa spot ID;
- không override occupied/held state;
- không hứa hold quá TTL;
- chống prompt injection.

### Technical architecture
AI được dùng như thought-partner để kiểm tra việc giữ MVP nhỏ:
- single FastAPI process;
- simulator bằng `asyncio.Task`;
- SQLite mặc định;
- không Redis/Celery;
- chạy được khi không có API key.

---

## 2. AI đã giúp gì tốt?

### Điểm 1 — Buộc tôi phân biệt “AI problem” và “optimization problem”
Trước khi chốt kiến trúc, bài toán rất dễ bị gọi chung là “AI Parking”. Sau khi phân tích, tôi nhận ra phần quyết định ô đỗ không nên giao cho LLM. Đây là phần cần deterministic algorithm vì có hard constraints và cần test được.

### Điểm 2 — Làm rõ Operational Boundary
Việc viết boundary thành các câu cấm cụ thể giúp prototype có tiêu chí pass/fail rõ hơn thay vì chỉ đánh giá bằng cảm giác.

### Điểm 3 — Chuyển ý tưởng thành metric
Thay vì chỉ nói “giúp tài xế đỗ nhanh hơn”, bài toán được chuyển thành:
- giảm barrier → parked ≥40%;
- top-1 acceptance ≥70%;
- hard-constraint violation = 0%.

---

## 3. AI đã sai / chưa đủ ở đâu?

> TODO: Viết ít nhất 2 tình huống thật trong buổi lab.

Gợi ý cách viết:

### Tình huống A
**AI đề xuất:** `TODO`

**Vấn đề:** `TODO`

**Tôi sửa thành:** `TODO`

**Bài học:** Không lấy output AI làm fact nếu chưa có dữ liệu thực tế.

### Tình huống B
**AI đề xuất:** `TODO`

**Vấn đề:** `TODO`

**Tôi sửa thành:** `TODO`

**Bài học:** Cần giữ scope theo thời gian lab và rubric.

---

## 4. Tôi đã kiểm chứng output AI như thế nào?

- So sánh với current workflow đã mô tả.
- Đánh dấu các số liệu thời gian hiện tại là **assumption cần validate**, không biến thành fact.
- Đưa hard constraints ra khỏi LLM.
- Thiết kế fallback khi LLM không hoạt động.
- Chuẩn bị adversarial test để kiểm tra boundary.

> TODO: Sau khi chạy prototype, thêm số lượng test pass/fail thật.

---

## 5. Một quyết định tôi không giao cho AI

Tôi không để LLM tự chọn parking spot.

Lý do:
- spot state là dữ liệu có cấu trúc;
- permit/EV/size là hard constraints;
- route là graph problem;
- recommendation phải có breakdown và reproducible;
- output sai có thể vi phạm boundary.

Quyết định cuối cùng được thiết kế theo pipeline:

```text
LLM parse
   ↓
Deterministic filter/score/route
   ↓
LLM explain
   ↓
Human chooses
```

---

## 6. Điều tôi sẽ làm khác nếu có thêm thời gian

> TODO: Chọn 2–3 mục đúng với trải nghiệm thật.

Gợi ý:
- đo 30 xe thực tế ở peak/off-peak;
- lấy log barrier → parked;
- kiểm thử sensor/camera occupancy accuracy;
- chạy baseline `nearest free`;
- chạy 20–30 golden scenarios;
- chạy adversarial prompt suite;
- test với 8–10 người dùng.

---

## 7. Reflection ngắn

> TODO — 4–6 câu bằng lời của bạn.

Khung tham khảo:

“Điểm tôi học được rõ nhất trong lab là `...`. Ban đầu tôi nghĩ `...`, nhưng sau khi scoping tôi thay đổi thành `...`. AI hữu ích nhất khi `...`, nhưng tôi không thể tin AI ở phần `...` vì `...`. Nếu triển khai tiếp, việc đầu tiên tôi sẽ kiểm chứng là `...`.”
