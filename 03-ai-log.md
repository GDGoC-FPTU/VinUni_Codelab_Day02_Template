# Phản ánh quá trình sử dụng AI như trợ lý đồng hành

Trong quá trình thực hiện bài toán tìm kiếm và tối ưu một quy trình vận hành bằng AI cho Vinmec, tôi sử dụng ChatGPT như một trợ lý đồng hành để phân tích vấn đề, xây dựng quy trình Current-State, xác định bottleneck và đề xuất Future-State Flow. Tôi không sử dụng AI như một công cụ đưa ra đáp án cuối cùng, mà liên tục kiểm tra, phản biện và điều chỉnh kết quả do AI tạo ra.

## 1. AI đã hỗ trợ tôi như thế nào?

Đầu tiên, tôi sử dụng ChatGPT để brainstorming các pain point có thể ứng dụng AI trong hoạt động của Vinmec. AI đề xuất nhiều quy trình khác nhau và giúp tôi thu hẹp phạm vi vào bài toán **tóm tắt hồ sơ bệnh án và chuẩn bị thông tin trước khi bác sĩ khám**.

Sau khi chọn bài toán, AI giúp tôi xây dựng **Quick Problem Card**, bao gồm Actor, Current Workflow, Bottleneck, Business Impact, Success Metric và Operational Boundary.

AI cũng hỗ trợ tôi mô hình hóa quy trình hiện tại. Ví dụ, quy trình được chia thành các bước:

> Mở hồ sơ → đọc lịch sử khám → kiểm tra xét nghiệm/CĐHA → kiểm tra thuốc → tự tổng hợp thông tin → bắt đầu khám.

Qua quá trình này, tôi nhận ra bottleneck không đơn giản là "bác sĩ phải đọc hồ sơ", mà nằm ở việc **bác sĩ phải tự tổng hợp một lượng lớn thông tin từ nhiều nguồn trước khi có thể bắt đầu tư vấn**.

Tiếp theo, AI giúp tôi thiết kế Future-State Flow với ba thành phần chính:

* 🔵 AI Step: LLM đọc và tạo Clinical Summary.
* 🟢 Human-in-the-loop: Bác sĩ review và xác nhận kết quả.
* ↩️ Fallback: Khi AI không đủ tin cậy, bác sĩ quay lại hồ sơ gốc và xử lý thủ công.

Nhờ vậy, tôi xác định bài toán này phù hợp nhất với **LLM Feature**, thay vì Agentic Loop.

## 2. AI đã trả lời sai hoặc có nguy cơ hallucination ở đâu?

Một vấn đề quan trọng tôi nhận ra là AI có xu hướng **đưa ra những con số rất cụ thể dù chưa có dữ liệu thực tế**.

Ví dụ, khi phân tích Current-State Workflow, AI đưa ra các khoảng thời gian như:

* Đọc lịch sử khám: 3–7 phút.
* Kiểm tra xét nghiệm/CĐHA: 2–5 phút.
* Kiểm tra thuốc: 1–3 phút.
* Tổng thời gian: khoảng 12–25 phút/lượt.

Những con số này có thể hữu ích để xây dựng một workflow mẫu trong workshop, nhưng nếu trình bày chúng như số liệu thực tế của Vinmec thì sẽ trở thành một dạng hallucination hoặc ít nhất là **unsupported assumption**.

Tôi nhận ra rằng AI không thể tự biết chính xác một bác sĩ Vinmec mất bao nhiêu phút để chuẩn bị hồ sơ nếu không có dữ liệu time-study thực tế.

Tương tự, các metric như "giảm 50% thời gian" hoặc "95% thông tin được tóm tắt chính xác" cũng không nên được coi là kết quả đã chứng minh. Đây chỉ nên được xem là **target để kiểm chứng trong PoC**.

## 3. Tôi đã sửa prompt như thế nào?

Sau khi nhận ra vấn đề trên, tôi thay đổi cách đặt câu hỏi cho AI. Thay vì yêu cầu AI đưa ra một câu trả lời hoàn chỉnh ngay lập tức, tôi yêu cầu AI:

> "Nếu không có số liệu thực tế, hãy ghi rõ đây là assumption/ước tính dùng cho workshop và không được trình bày như số liệu đã được Vinmec xác nhận."

Tôi cũng chia bài toán thành từng bước nhỏ:

1. Xác định Actor.
2. Mô tả Current-State.
3. Xác định Bottleneck.
4. Xác định Business Impact.
5. Đặt Success Metric.
6. Xác định Operational Boundary.
7. Thiết kế Future-State.
8. Xác định AI Step, Human Step và Fallback.

Cách làm này giúp tôi dễ kiểm tra từng phần hơn thay vì tin toàn bộ câu trả lời của AI.

## 4. Tôi đã thiết lập ranh giới cho AI như thế nào?

Đối với bài toán y tế, tôi xác định ranh giới rất rõ.

AI **được phép**:

* Đọc dữ liệu bệnh án được cấp quyền.
* Trích xuất thông tin quan trọng.
* Tóm tắt lịch sử khám.
* Tóm tắt xét nghiệm, chẩn đoán hình ảnh và thuốc.
* Tạo Clinical Summary để hỗ trợ bác sĩ.

AI **không được phép**:

* Tự chẩn đoán bệnh.
* Tự kê thuốc.
* Tự thay đổi phác đồ điều trị.
* Tự đưa ra quyết định y khoa cuối cùng.
* Tự động thay đổi hồ sơ bệnh án mà không có kiểm duyệt.

Điểm kiểm soát quan trọng nhất là **Human-in-the-loop**: bác sĩ phải review và xác nhận Clinical Summary trước khi sử dụng nó trong quá trình khám.

Ngoài ra, tôi thiết kế một cơ chế **Fallback**. Nếu AI gặp lỗi, dữ liệu không đầy đủ hoặc kết quả không đủ tin cậy, hệ thống không cố gắng "đoán" mà quay trở lại quy trình truyền thống để bác sĩ xem hồ sơ gốc.

## 5. Bài học rút ra

Qua quá trình làm việc, tôi nhận ra rằng sử dụng AI hiệu quả không phải là hỏi một câu prompt thật dài rồi lấy nguyên kết quả. AI nên được xem như một **trợ lý đồng hành**.

AI rất mạnh trong việc:

* Brainstorming.
* Phân rã vấn đề.
* Mô hình hóa workflow.
* Đề xuất các hướng giải pháp.
* Phát hiện những khía cạnh mà người dùng có thể chưa nghĩ tới.
* Chuyển ý tưởng thành cấu trúc rõ ràng.

Tuy nhiên, con người vẫn phải chịu trách nhiệm về **tính đúng đắn của dữ liệu, các giả định, phạm vi áp dụng và quyết định cuối cùng**.

Đặc biệt với những lĩnh vực có rủi ro cao như y tế, tôi cho rằng nguyên tắc quan trọng nhất là:

> **AI hỗ trợ con người ra quyết định, không thay thế con người ra quyết định.**

Qua bài tập này, tôi không chỉ học được cách sử dụng ChatGPT để tạo nội dung nhanh hơn mà còn học được cách **phản biện output của AI, nhận diện hallucination, phân biệt fact với assumption và thiết lập operational boundary** trước khi đưa AI vào một quy trình thực tế.
