# AI Log

## Phase 1 — Scan Problem

### Prompt 01 — Identify Operational Problems

Tôi là AI Engineer tại Vin Smart Future (Vingroup). Hãy tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho các công ty thành viên của Vingroup, ưu tiên các quy trình thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất.

Với mỗi bài toán, hãy xác định:
- Công ty thành viên
- Quy trình nghiệp vụ
- Actor đang gặp pain point
- Công việc thủ công hiện tại
- Điểm nghẽn vận hành
- AI có thể can thiệp ở đâu
- Metric có thể dùng để đo hiệu quả
- Ước tính tổn thất dựa trên benchmark đáng tin cậy

Không tự bịa số liệu nội bộ. Phân biệt rõ giữa dữ liệu thực tế, benchmark ngành và giả định để xây dựng POC.

### Prompt 02 — Shortlist Problems

Từ danh sách bài toán đã tìm được, hãy chọn Top 5 bài toán có:
1. Business impact rõ ràng
2. Workflow thủ công có thể xác định được
3. Có metric định lượng
4. Có khả năng triển khai AI thực tế
5. Có khả năng mở rộng thành sản phẩm/dịch vụ

Ưu tiên các bài toán mà AI tạo ra giá trị vượt trội so với automation hoặc rule-based thông thường.

### Prompt 03 — Build Problem Cards

Với Top 3 bài toán được chọn, hãy hoàn thiện Quick Problem Card gồm:
- Bài toán
- Công ty thành viên
- Actor
- Workflow thủ công 3-5 bước
- Bước tốn thời gian/lỗi nhất
- AI intervention point
- Metric có số
- Quick Architecture

Không tự bịa baseline nội bộ nếu chưa có dữ liệu. Nếu cần giả định để xây dựng POC, đánh dấu rõ đó là assumption.

---

## Phase 5 — Evaluate

### Prompt 04 — Critical Evaluation

Đóng vai CFO và Trưởng phòng Vận hành cực kỳ khắt khe. Hãy đánh giá Quick Problem Card đã chọn theo 3 khía cạnh:

1. Logic của bài toán
2. Tính hợp lệ của metric
3. AI có thực sự cần thiết hay Rule-based/automation thông thường đã đủ tốt?

Chỉ ra các giả định ngầm, dữ liệu còn thiếu và những điểm có thể khiến dự án AI không tạo ra ROI.

### Prompt 05 — AI Readiness

Đánh giá bài toán theo AI Readiness Checklist:

1. Có dữ liệu mẫu/logs sạch để test hay chưa?
2. Rủi ro khi AI sai có kiểm soát được bằng HITL hoặc fallback hay không?
3. Stakeholders có khả năng thay đổi workflow hiện tại hay không?

Sau đó đưa ra một trong ba quyết định:
- GO
- NOT YET
- NO-GO

Quyết định phải dựa trên business value, technical feasibility, data readiness và chi phí triển khai.

### Prompt 06 — Final Evaluation

Với Quick Problem Card:

> Vinhomes — Điều phối work order bảo trì-sửa chữa từ cư dân chưa tối ưu, gây gán sai kỹ thuật viên và chậm SLA.

Hãy hoàn thiện Phase 5 — EVALUATE theo đúng format:

- AI Readiness Checklist
- Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future
- Justification

Đặc biệt kiểm tra liệu LLM có thực sự tạo ra incremental value hay không.

Nếu phần matching skill + workload + location có thể giải quyết bằng Rule-based, không được mặc định sử dụng AI.

AI chỉ nên được đề xuất ở phần free-text classification nếu có bằng chứng rằng nó tốt hơn structured input hoặc rule-based approach.

### Final Decision

GO — Bắt đầu Prototype với scope hẹp.

Prototype tập trung vào:

Cư dân gửi mô tả sự cố
→ AI chuẩn hóa/phân loại free-text
→ Rule-based engine lọc và rank KTV theo skill + workload + location
→ Nhân viên trực xác nhận
→ Tạo work order.

Decision Gate:

"LLM có giúp giảm đáng kể thời gian và lỗi phân loại free-text so với Rule-based/structured input hay không?"

Nếu không, loại bỏ LLM và triển khai Rule-based solution.