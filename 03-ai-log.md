# 03 — AI Log & Reflection

## 1. Mục tiêu sử dụng AI

Trong quá trình thực hiện Lab 02, AI được sử dụng như một **thought-partner** để brainstorm, phản biện và stress-test ý tưởng. AI không được coi là nguồn dữ liệu vận hành nội bộ của Vingroup.

---

## 2. AI đã giúp gì?

### Brainstorm

AI hỗ trợ mở rộng danh sách các pain point theo 4 lenses:

- Repetitive
- Time-consuming
- AI-upgrade
- Stakeholder Pain

Từ đó nhóm có thể tạo danh sách use case rồi chọn các bài toán phù hợp hơn với tiêu chí Problem First, AI Second.

### Stress-test

AI được yêu cầu đóng vai trò CFO/Trưởng phòng Vận hành để phản biện:

- metric có cơ sở hay chưa;
- bài toán có thực sự cần AI không;
- rule-based có thể giải quyết không;
- operational boundary có đủ chặt không.

### Thiết kế prototype

AI hỗ trợ xây dựng system prompt, JSON schema và adversarial test cases cho prototype.

---

## 3. AI có thể sai ở đâu?

Một rủi ro rõ ràng là AI có thể **tạo ra số liệu vận hành nghe có vẻ hợp lý nhưng không có nguồn xác minh**.

Ví dụ, các con số như volume ticket, thời gian xử lý hoặc tỷ lệ tiết kiệm nếu được AI đề xuất chỉ nên xem là giả định để xây dựng prototype.

Do đó, trong bài làm này các con số giả định được ghi rõ là **assumption**, không trình bày như dữ liệu nội bộ thực tế.

---

## 4. Tôi đã sửa như thế nào?

Tôi áp dụng ba nguyên tắc:

1. Không biến số liệu do AI brainstorm thành fact.
2. Tách rõ `Assumption` và `Evidence`.
3. Với metric production, yêu cầu phải có dataset/log thực tế trước khi kết luận.

Ngoài ra, tôi không chọn Agent chỉ vì nó phức tạp hơn. Với use case phân loại ticket, LLM Feature kết hợp Rule-based routing phù hợp hơn.

---

## 5. Reflection

Điểm quan trọng nhất tôi học được là AI Product Scoping không bắt đầu bằng câu hỏi “dùng model nào?”, mà bắt đầu bằng:

**Problem → Workflow → Bottleneck → Metric → Boundary → AI Fit.**

AI rất hữu ích trong việc mở rộng góc nhìn và phản biện, nhưng người làm sản phẩm vẫn phải chịu trách nhiệm kiểm chứng giả định, xác định ranh giới và quyết định Go/Not Yet/No-Go.

Sau buổi lab, tôi hiểu rõ hơn sự khác biệt giữa một ý tưởng “có thể dùng AI” và một bài toán “đáng để xây dựng thành sản phẩm AI”.
