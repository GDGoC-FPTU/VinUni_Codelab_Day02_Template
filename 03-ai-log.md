<<<<<<< HEAD
# 📝 Phase 6 — REFLECTION (Cá nhân)


### 1. Công việc đã thực hiện
- Sử dụng AI để phân tích, rà soát lỗi và lên kế hoạch sửa đổi các file mã nguồn.
- Yêu cầu AI hỗ trợ hoàn thiện các báo cáo, tài liệu phân tích.
- Đặt câu hỏi để giải quyết các vướng mắc về logic lập trình và cách triển khai các công nghệ cụ thể trong bài.

### 2. Ưu điểm và lợi ích nhận được
- **Tốc độ:** AI giúp tiết kiệm đáng kể thời gian tìm kiếm lỗi (debug) và tra cứu cú pháp, đưa ra các gợi ý sửa lỗi gần như ngay lập tức.
- **Củng cố kiến thức:** Các lời giải thích đi kèm mã nguồn của AI rất chi tiết và dễ hiểu, giúp tôi nhận ra những lỗ hổng trong tư duy lập trình của mình.
- **Nâng cao hiệu suất:** AI hỗ trợ thực hiện những công việc lặp đi lặp lại hoặc cần định dạng tốn thời gian (như viết báo cáo Markdown) một cách gọn gàng và chuyên nghiệp.

### 3. Thách thức và khó khăn
- **Ngữ cảnh:** Đôi lúc AI chưa nắm bắt được toàn bộ ngữ cảnh phức tạp của cả dự án nếu câu lệnh (prompt) đưa ra quá ngắn gọn hoặc chung chung.
- **Tính chính xác:** Một số đoạn code do AI sinh ra cần được tinh chỉnh lại mới có thể chạy đúng trên môi trường thực tế, đòi hỏi phải luôn có bước kiểm chứng (verify).

### 4. Bài học rút ra (Takeaways)
- **Kỹ năng Prompting:** Cần rèn luyện cách đặt câu hỏi rõ ràng, chia nhỏ vấn đề lớn thành các yêu cầu nhỏ hơn để AI xử lý hiệu quả nhất.
- **Tư duy phản biện:** Không nên phụ thuộc hoàn toàn vào AI. Cần luôn giữ vai trò là người kiểm duyệt, đọc hiểu và đánh giá lại các đoạn code hay nội dung mà AI tạo ra trước khi sử dụng.
- **Công cụ học tập:** AI nên được coi là một người bạn "pair-programming", giúp bản thân học hỏi cách tư duy giải quyết vấn đề thay vì chỉ đơn thuần là công cụ "giải bài hộ".
=======
# 03 — AI Log & Reflection

## AI được dùng như thế nào

Tôi dùng AI để cấu trúc bài toán predictive maintenance: tách deterministic safety policy, mô hình chuỗi thời gian và lớp giải thích. AI cũng giúp tạo red-team cases về telemetry thiếu, dữ liệu ngoài phân phối và yêu cầu can thiệp xe trái quyền.

## AI hỗ trợ tốt

1. Biến ý tưởng “dự đoán lỗi” thành pipeline: data quality → rule override → risk model → evidence → human review → feedback.
2. Chỉ ra predictive maintenance không chỉ là LLM: tín hiệu chính là telemetry/DTC theo thời gian và nhãn outcome từ xưởng.
3. Làm rõ ranh giới: không tự xóa lỗi, điều khiển xe, khẳng định xe an toàn hoặc tự đặt lịch.

## Sai lệch/hallucination cần tránh

Nguồn công khai cho thấy VinFast có kết nối, theo dõi, cảnh báo và chẩn đoán từ xa; chúng không chứng minh dữ liệu training, schema, độ phủ xe, chất lượng nhãn hay KPI nội bộ. AI cũng dễ nhầm anomaly score là nguyên nhân gốc hoặc quyết định an toàn.

## Cách tôi điều chỉnh prompt và quy trình

- Mục tiêu metric là mục tiêu pilot, không phải fact.
- Model chỉ trả risk triage/draft dựa trên evidence đã cung cấp và luôn yêu cầu người duyệt.
- Policy an toàn/DTC cao override ML/LLM; data stale hoặc out-of-distribution chuyển `needs_human_review`.
- Tách train/test theo thời gian và xe, so với baseline rule, theo dõi drift trước retrain.

## Bài học

Ở vehicle health, dữ liệu, nhãn và rollback quan trọng hơn câu trả lời trôi chảy. LLM chỉ nên giải thích kết quả đã qua policy/model kiểm soát; kỹ thuật viên mới chẩn đoán và phê duyệt quyết định cuối.
>>>>>>> e7eabe7bddd44bf8100dba65595b10552b6e4c07
