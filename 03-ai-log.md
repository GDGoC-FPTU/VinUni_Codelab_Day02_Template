# NHẬT KÝ TƯƠNG TÁC Ai

### 1. Vai trò của AI trong quá trình thực hiện

Trong quá trình xây dựng đề tài, em sử dụng ChatGPT làm trợ lý đồng hành để hỗ trợ phân tích bài toán, hỏi đáp cho đề tài của mình.

AI đã hỗ trợ em ở một số công việc chính:

- Phân tích: Hỗ trợ xác định khó khăn của nhân viên CSKH và Manager khi phải đọc, phân loại và tổng hợp số lượng lớn review từ Booking.com, Agoda và Google Maps.
- Xác định điểm nghẽn: Giúp nhận diện các công đoạn tiêu tốn nhiều thời gian, đặc biệt là đọc, phân tích và tổng hợp review thủ công.
- Thiết kế giải pháp: Đề xuất sử dụng LLM kết hợp NLP và Rule-based Classification để phân tích cảm xúc, trích xuất vấn đề, xác định mức độ nghiêm trọng và phân loại bộ phận phụ trách.
- Xây dựng Prompt:Hỗ trợ thiết kế systempront, xác định các nguyên tắc như không tự ý phản hồi khách hàng, không bịa đặt dữ liệu, phát hiện khiếu nại nghiêm trọng và yêu cầu con người phê duyệt trước khi thực hiện hành động.

### 2. Những trường hợp AI trả lời sai hoặc chưa chính xác

Trong quá trình tương tác, em nhận thấy AI không phải lúc nào cũng hiểu chính xác yêu cầu và bối cảnh đã thống nhất.

Trường hợp 1: AI thiết kế sai quy trình vận hành
Khi yêu cầu tạo Current-State Workflow, AI ban đầu tạo ra một quy trình xử lý review tiêu cực khác với quy trình nhóm em đã dựng đưa lên. Sơ đồ xuất hiện các bước điều tra, xử lý vấn đề và phản hồi khách hàng, trong khi quy trình thực tế của đề tài chỉ gồm 5 bước:

1. Thu thập review từ các nền tảng.
2. Đọc và phân tích từng review.
3. Xác định vấn đề và mức độ lỗi.
4. Tổng hợp báo cáo.
5. Manager phân công bộ phận xử lý.
   AI đã tự suy diễn thêm các công đoạn và thay đổi thời gian xử lý, khiến hình ảnh không còn phản ánh đúng nội dung đã thống nhất.

Cách khắc phục: em cung cấp lại sơ đồ quy trình bằng văn bản, ghi rõ từng bước, người phụ trách, thời gian, đầu vào, đầu ra và vị trí các điểm nghẽn. Sau đó yêu cầu AI tạo lại hình ảnh dựa chính xác trên sơ đồ này.

### 3. Điều chỉnh Prompt và thiết lập ranh giới cho AI

Sau khi nhận thấy những hạn chế trên, em xác định cần đưa ra các quy tắc rõ ràng thay vì chỉ yêu cầu AI phân tích review một cách chung chung.
Em xây dựng các nguyên tắc cho Prompt Prototype như sau:
cung cấp thêm thông tin chính xác, yêu cầu không tự ý sáng tạo, không trảloiwf lam man,..

### 4. Bài học kinh nghiệm

Qua quá trình tương tác, em nhận thấy AI có thể giúp tăng tốc độ phân tích, hỗ trợ tư duy và giảm công việc thủ công. Tuy nhiên, kết quả AI tạo ra không mặc nhiên chính xác.

Một số bài học quan trọng:

1. Prompt càng rõ ràng, kết quả càng dễ kiểm soát: Cần mô tả cụ thể vai trò, đầu vào, đầu ra, giới hạn và tiêu chí đánh giá.
2. Không nên tin tưởng tuyệt đối vào kết quả AI: Các kết quả quan trọng, cần được con người kiểm tra.

### 5. Kết luận

Qua quá trình làm việc với ChatGPT và thử nghiệm Gemini API, em hiểu rõ hơn cách sử dụng AI như một trợ lý đồng hành trong quá trình phân tích và xây dựng giải pháp.

AI giúp em tiết kiệm thời gian, hệ thống hóa ý tưởng và xây dựng bản thiết kế ban đầu. Tuy nhiên, em vẫn phải chủ động kiểm tra, điều chỉnh yêu cầu và xác định ranh giới hoạt động của AI để tránh những kết quả sai lệch.

Đối với đề tài Vinpearl, em cho rằng mô hình phù hợp nhất ở giai đoạn đầu là AI hỗ trợ phân tích và cảnh báo, kết hợp với cơ chế Human-in-the-loop. Đây là cách tiếp cận giúp tận dụng khả năng xử lý ngôn ngữ của AI nhưng vẫn đảm bảo con người kiểm soát các quyết định quan trọng trong vận hành khách sạn.
