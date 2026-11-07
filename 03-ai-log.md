# Lab 02 — AI Log & Personal Reflection

**Người thực hiện:** Lưu Văn Việt Đức  
**Tên nhóm:** Simple - Tech  
**Email:** luuvanvietduc@gmail.com  
**Ngày tổng hợp:** 07/11/2026  
**Đề tài:** VinFast — Chuẩn hóa mô tả nhu cầu sửa chữa thành phiếu tiếp nhận dịch vụ.  
**Phạm vi đóng góp:** Nhật ký và phản tư cá nhân; chỉ ghi các hoạt động đã thực hiện trong quá trình làm bài.

## 1. Tôi sử dụng AI để làm gì?

Tôi dùng ChatGPT làm người cùng thảo luận: đọc yêu cầu lab, phản biện phạm vi, hỗ trợ xây dựng workflow, thiết kế thử nghiệm, hỗ trợ viết code và tổng hợp tài liệu. Tôi dùng Gemini API làm mô hình thực thi trong prompt prototype. Hai vai trò này được phân biệt: đề xuất của ChatGPT không phải kết quả kiểm thử của Gemini.

| Công cụ | Mục đích | Việc tôi chịu trách nhiệm |
|---|---|---|
| ChatGPT | Brainstorm, phản biện, hỗ trợ thiết kế prompt/code, kiểm tra output và tổng hợp báo cáo | Chọn phạm vi, đối chiếu worksheet, kiểm tra bằng chứng, chỉnh lại nội dung và hỗ trợ đưa ra quyết định sử dụng |
| Gemini API qua `google-genai` | Nhận mô tả giả lập, trích xuất thông tin và trả JSON theo prompt | Chạy thử, lưu log, kiểm tra đầu ra, phân biệt ca đạt với ca chưa có phản hồi |
| Nguồn công khai của VinFast | Đối chiếu bối cảnh nhập mô tả và đặt dịch vụ | Không suy ra quy trình nội bộ hoặc pain point từ thông tin công khai một cách thiếu căn cứ |

AI hỗ trợ soạn tài liệu, nhưng chưa có nhân viên nghiệp vụ xác nhận checklist, dữ liệu tham chiếu hay các giả thuyết vận hành. 

## 2. Nhật ký tương tác tiêu biểu

Các yêu cầu trong bảng được tóm tắt theo nội dung trao đổi, không phải toàn bộ lịch sử chat hoặc bản chép nguyên văn từng prompt. Thứ tự là trình tự công việc, không gán thời điểm cụ thể .

| Bước | Yêu cầu / mục đích của tôi | AI đã hỗ trợ | Tôi kiểm tra hoặc điều chỉnh |
|---|---|---|---|
| 1. Hiểu bài lab | Đọc README, worksheet và làm rõ cách nộp bài | Giải thích các phase, sản phẩm đầu ra và quy trình branch | Đối chiếu lại worksheet; dùng tên và số phase trong worksheet thay vì dựa vào một cách phân chia không thống nhất |
| 2. Tìm đề tài | Xem xét bài toán đối chiếu hóa đơn sạc và nghi ngờ thông tin “làm thủ công trên Excel” | Gợi ý hướng tìm bằng chứng và các đề tài khác | Không sử dụng giả định về công cụ nội bộ làm sự thật; chuyển sang đề tài tiếp nhận nhu cầu sửa chữa |
| 3. Thu hẹp phạm vi scan | Giữ chủ đề VinFast thay vì mở lại sang nhiều công ty | Đề xuất các pain point và quick cards | Yêu cầu cả năm vấn đề cùng nằm trong phạm vi tiếp nhận sửa chữa; chọn Scan #1, #2, #4 |
| 4. Chọn deep-dive | Chọn vấn đề có thể làm prototype trong lab | Hỗ trợ so sánh các card và xác định phạm vi | Tập trung vào phát hiện thông tin thiếu; chưa mở rộng thành hệ thống tiếp nhận toàn diện hoặc chẩn đoán xe |
| 5. Thiết kế workflow và metric | Mô tả trước/sau, ranh giới và cách đo | Hỗ trợ vẽ workflow, Problem Statement và mục tiêu thử nghiệm | Giữ các số 90% và 30% là mục tiêu đề xuất; không gọi đó là kết quả hoặc baseline thực tế |
| 6. Chuẩn bị dữ liệu | Cần mô tả đầu vào để thử nghiệm | Hỗ trợ tạo 20 ca giả lập và đáp án tham chiếu | Phân biệt dữ liệu giả lập với dữ liệu khách hàng; dùng đáp án để đối chiếu sau khi chạy |
| 7. Tích hợp code | Tích hợp prototype gọi Gemini 3.8 | Hỗ trợ viết code schema và kiểm tra đầu ra | Kiểm tra cấu trúc hàm, cấu hình model |
| 8. Kiểm thử ranh giới | Ngăn thêm triệu chứng, chẩn đoán và giả duyệt/đặt lịch | Soạn ba ca adversarial và ranh giới prompt | Giữ trạng thái nháp, nhân viên duyệt; xem cả ngữ nghĩa đầu ra, không chỉ tìm từ khóa |
| 9. Xử lý lỗi chạy | Phân biệt lỗi model, API và dữ liệu | Hỗ trợ đọc lỗi 404, 503, 504 và đề xuất cấu hình | Thay model theo phản hồi 404; bổ sung timeout/retry có giới hạn; |
| 10. Đánh giá và tổng hợp | Tổng hợp kết quả và hoàn thiện báo cáo | Hỗ trợ tóm tắt phản hồi và soạn bản nháp đánh giá | Chỉ ghi nhận phản hồi đã có; giữ các ca còn lại là chưa kiểm chứng; chọn NOT YET cho bước phát triển tiếp |

## 3. AI trả lời lệch hoặc có nguy cơ khiến tôi kết luận sai ở đâu?

### 3.1. Đề xuất lệch phạm vi

Trong quá trình brainstorm, có lúc đề xuất mở sang các công ty khác trong khi tôi đã chọn chủ đề VinFast. Tôi nhắc lại rằng năm vấn đề phải cùng thuộc quy trình tiếp nhận nhu cầu sửa chữa. Sau điều chỉnh, bảng scan phân biệt năm góc: độ đầy đủ, tách nội dung, độ rõ nghĩa, tính nhất quán và chất lượng bàn giao.

Bài học: trước khi yêu cầu brainstorm cần ghi rõ đơn vị, actor, điểm bắt đầu/kết thúc workflow và những phần nằm ngoài phạm vi.

### 3.2. Bối cảnh hợp lý không đồng nghĩa với sự thật nghiệp vụ

Nhận định như “hiện đang làm thủ công trên Excel”, số phút xử lý hay mức tổn thất cần có căn cứ. Tôi đã đặt câu hỏi về tính chính xác của giả định ban đầu. Với đề tài mới, báo cáo chỉ dùng nguồn công khai để xác nhận có điểm nhập mô tả; không kết luận VinFast chưa có hỗ trợ nội bộ.

Đây là điểm cần kiểm soát khi dùng AI: một lời giải thích nghe hợp lý có thể bị viết thành khẳng định nếu không yêu cầu chỉ rõ nguồn, giả định và dữ liệu còn thiếu. Tôi chưa có bằng chứng để khẳng định mức độ pain point, chi phí hay hiệu quả tại VinFast.

### 3.3. Đề xuất code chưa khớp cấu trúc tôi cần

Một số phương án trước chưa khớp mong muốn tích hợp vào starter hoặc gây khó theo dõi vị trí hàm. Tôi yêu cầu giữ cấu trúc ban đầu, đặc biệt hàm `evaluate_prompt(user_input: str) -> str`, rồi thay logic nghiệp vụ sang VinFast.

Tôi cũng làm rõ rằng ví dụ Xanh SM trong starter không phải nghiệp vụ của đề tài cá nhân. Không giữ hành vi điều phối xe sạc chỉ để phù hợp với từ khóa của một bài mẫu. Yêu cầu kỹ thuật và ranh giới được điều chỉnh theo bài toán VinFast đã chọn.

### 3.4. Nội dung cũ bị đặt nhầm vào Phase 4

Bản báo cáo đang soạn từng dùng phần nghiên cứu nguồn công khai cho mục Phase 4 và còn câu “chưa chạy qua mô hình”, dù tôi đã có phản hồi Gemini. Khi tổng hợp, nội dung nghiên cứu được chuyển về phần căn cứ; Phase 4 được cập nhật thành mã nguồn, dữ liệu, schema, ca tấn công và kết quả thực tế.

Bài học: khi tiến độ thay đổi cần rà lại tài liệu, không chỉ nối thêm đoạn mới vào bản cũ.

### 3.5. Dễ nhầm kết quả dự đoán với bằng chứng

Do mất thời gian vì lỗi dịch vụ, tôi từng muốn bỏ qua lỗi API và coi các ca chưa chạy là chạy bình thường theo dự đoán. Tuy nhiên, kết quả kỳ vọng không thể thay cho phản hồi mô hình. Bản đánh giá cuối giữ hai phần riêng: đã quan sát và chưa kiểm chứng.

Các lỗi 503/504 là lỗi dịch vụ, không phải hallucination. Ngược lại, JSON hợp lệ cũng chưa chứng minh nội dung đúng nghiệp vụ. Vì thế tôi không ghi 20/20 ca đạt hoặc 3/3 ca adversarial đạt.

## 4. Tôi đã điều chỉnh prompt và ranh giới như thế nào?

| Nội dung | Thiết kế được sử dụng | Lý do |
|---|---|---|
| Vai trò | Trợ lý hỗ trợ cố vấn lập phiếu nháp | Tránh mô hình tự đóng vai kỹ thuật viên chẩn đoán hoặc người có quyền xác nhận |
| Phạm vi đầu vào | Mô tả và thông tin xe giả lập; checklist bốn trường | Tạo phạm vi có thể kiểm tra trong lab |
| Trạng thái thông tin | Phân biệt `provided`, `missing`, `unknown`, `not_applicable`, `conflicting`, `unclear` | Không coi mọi ô trống đều là thiếu; không hỏi lại điều khách nói không biết |
| Căn cứ | Mỗi nhận định có trích đoạn `evidence` từ đầu vào | Giúp nhân viên đối chiếu; vẫn cần đọc ngữ cảnh |
| Câu hỏi | Chỉ đề xuất cho trường thiếu, chưa rõ hoặc mâu thuẫn | Hạn chế hỏi thừa và không tự điền câu trả lời |
| Triệu chứng | Không thêm dữ kiện chỉ vì khách yêu cầu ghi cho được ưu tiên | Ngăn tạo hồ sơ sai |
| Chẩn đoán | Không biến triệu chứng hay yêu cầu của khách thành kết luận hỏng/thay phụ tùng | Giữ quyết định kỹ thuật cho người có trách nhiệm |
| Nháp và duyệt | `draft_summary` bắt đầu bằng `[DRAFT_ONLY]`; hai cờ `draft_only` và `requires_human_review` là `true` | Giữ đầu ra ở trạng thái chờ nhân viên kiểm tra |
| Hành động nghiệp vụ | Không tự gửi, giả duyệt, xác nhận lịch, giá hay bảo hành | Prototype chưa có thẩm quyền hoặc tích hợp nghiệp vụ |
| Lỗi và không chắc chắn | Ghi nhận lỗi; thiết kế fallback sang nhân viên dùng checklist | Không dùng đầu ra lỗi hoặc tạo kết quả giả |

Response toàn bộ là JSON; nhãn `[DRAFT_ONLY]` nằm ở đầu trường `draft_summary`, không nằm trước dấu `{`. Đây là điều chỉnh định dạng của prototype VinFast so với ví dụ văn bản trong starter.

Các trường hợp mơ hồ/mâu thuẫn có thể yêu cầu người làm rõ riêng. Dù `human_resolution_required=false`, đầu ra vẫn cần nhân viên duyệt vì `requires_human_review=true`.

## 5. Bằng chứng và những gì chưa chứng minh được

### 5.1. Kết quả đã quan sát

- Dry-run đọc và hiển thị đủ 20 đầu vào.
- VF-01, VF-02, VF-03 nhận được JSON, qua kiểm tra cơ học và khi đọc thủ công thấy nhận diện được triệu chứng cùng ba trường thiếu.
- Một lượt VF-18 không đưa “mùi khét” thành triệu chứng thật, giữ trạng thái nháp và ghi lưu ý về yêu cầu bịa dữ kiện.
- Có bốn ID duy nhất đã được rà phản hồi, từ hai lượt chạy khác nhau; chưa phải một lượt đánh giá đầy đủ toàn bộ bộ thử.

| Bằng chứng | Đường dẫn trong repo |
|---|---|
| VF-01–03 | [responses.jsonl](results/vinfast_intake/20261107_191845_915767fd/responses.jsonl) |
| Lượt có VF-18 | [responses.jsonl](results/vinfast_intake/20261107_191022_9efed991/responses.jsonl) |
| Mã nguồn | [prompt_prototype.py](starter-code/prompt_prototype.py) |
| Dữ liệu giả lập | [README dữ liệu](vinfast_intake/README.md) |
| Báo cáo đánh giá | [02-deep-dive-report.md](02-deep-dive-report.md) |

### 5.2. Những gì chưa được chứng minh

Chưa có phản hồi đầy đủ cho hai ca adversarial còn lại hoặc toàn bộ các nhóm dữ liệu. Chưa đo Recall trên toàn bộ bộ thử, công sức tiết kiệm, tỷ lệ hỏi thừa hay chi phí API. Chưa phỏng vấn stakeholder và chưa có baseline nghiệp vụ.

`mechanical_checks_ok` không xác nhận toàn bộ ý nghĩa nội dung hoặc độ vững của ranh giới. “Không thấy lỗi trong các phản hồi đã đọc” không có nghĩa không thể có lỗi ở đầu vào khác.

Model chạy thực tế là `gemini-3.8-flash`; model `gemini-2.5-flash` trong starter trả lỗi 404 với tài khoản đang thử. Thay model là điều chỉnh môi trường, không phải chứng cứ chất lượng. Các log lỗi dịch vụ được tách khỏi đánh giá nội dung.

## 6. Phase 6 — Phản tư cá nhân

### 6.1. Tôi học được gì về cách xác định bài toán?

Ban đầu, tôi chọn một chủ đề khá rộng là hỗ trợ tiếp nhận nhu cầu sửa chữa xe. Khi liệt kê năm vấn đề và chọn ba card, tôi thấy cần thu hẹp vào một tác vụ có đầu vào, đầu ra và cách đo rõ ràng. Phạm vi đầu tiên là phát hiện thông tin cần làm rõ và tạo bản nháp để cố vấn xem xét.

Tôi cũng học cách phân biệt giả định với bằng chứng. Việc nhân viên có thể phải hỏi lại nhiều lần là giả thuyết cần kiểm chứng. Tôi không thể gọi đó là vấn đề nghiêm trọng hoặc gán tổn thất chỉ vì AI giải thích nghe hợp lý.

### 6.2. Tôi hiểu thêm điều gì về vai trò và giới hạn của AI?

AI có thể hỗ trợ đọc cách diễn đạt đa dạng và chuyển thông tin sang cấu trúc thống nhất. Tuy nhiên, một phiếu có vẻ đầy đủ vẫn có thể sai nếu mô hình suy diễn thêm chi tiết. Vì vậy, thiếu thông tin phải được thể hiện rõ thay vì tự điền cho đủ.

Tôi giữ AI ở vai trò đề xuất. Cố vấn dịch vụ kiểm tra câu hỏi và phiếu; khách xác nhận dữ kiện; kỹ thuật viên kết luận nguyên nhân và phương án sửa chữa. Thiết kế này giúp xác định rõ trách nhiệm, nhưng vẫn cần kiểm chứng việc duyệt có hiệu quả hay không.

### 6.3. Prototype đã thay đổi suy nghĩ của tôi thế nào?

Các ca chạy thành công cho thấy tác vụ cốt lõi có thể thực hiện được trong những tình huống đơn giản. Tôi cũng nhận ra có ba mức đánh giá khác nhau: gọi API được, trả đúng cấu trúc và trả đúng nội dung nghiệp vụ. Chỉ đạt hai mức đầu chưa đủ để quyết định sử dụng thực tế.

Việc dịch vụ lỗi làm tôi muốn kết thúc thử nghiệm sớm. Qua đó, tôi thấy báo cáo nên ghi đúng giới hạn thay vì biến kết quả dự đoán thành thành tích. Tôi có thể dừng xử lý lỗi hạ tầng trong phạm vi thời gian lab và vẫn đưa ra quyết định có căn cứ, nếu giữ rõ phần nào chưa được thử.

### 6.4. Hạn chế lớn nhất của bài làm hiện tại là gì?

Dữ liệu hoàn toàn giả lập, checklist và đáp án chưa được người hiểu nghiệp vụ xác nhận. Các phản hồi được đọc còn ít và chưa đại diện cho mọi tình huống. Tôi chưa có số thời gian nhân viên xử lý hoặc bằng chứng stakeholder muốn thay đổi workflow.

Do đó, tôi chọn **NOT YET** cho bước phát triển tiếp hoặc pilot nghiệp vụ. Đây không phải kết luận ý tưởng không khả thi; tôi cần thêm bằng chứng để so sánh với biểu mẫu và Rule + checklist.

### 6.5. Nếu tiếp tục, tôi sẽ ưu tiên điều gì?

Tôi sẽ ưu tiên xác nhận với cố vấn dịch vụ xem thông tin nào thực sự cần hỏi cho từng nhóm yêu cầu. Tiếp theo là đo baseline, hoàn tất bộ thử và rà các ca không biết, không áp dụng, mâu thuẫn hoặc cố tình yêu cầu vượt phạm vi.

Tôi sẽ so sánh thời gian hoàn thành phiếu khi dùng checklist và khi có AI, tính cả thời gian đọc, sửa và fallback. Nếu AI không tạo ra lợi ích rõ ràng sau khi tính toàn bộ công sức và chi phí, tôi sẽ ưu tiên phương án đơn giản hơn.

## 7. Nguyên tắc sử dụng AI tôi rút ra

1. Ghi rõ phạm vi và yêu cầu bằng chứng ngay từ đầu.
2. Xem đề xuất của AI là bản nháp cần kiểm tra, đặc biệt với sự thật nghiệp vụ và con số.
3. Tách mục tiêu, kết quả kỳ vọng và kết quả thực tế.
4. Không coi JSON hợp lệ là đủ; luôn đọc nội dung và kiểm tra căn cứ.
5. Dùng giải pháp đơn giản làm phương án đối chứng, không mặc định cần Agent hoặc LLM.
6. Khi không đủ bằng chứng, ghi nhận điều còn thiếu và quyết định bước tiếp theo phù hợp.

## 8. Tài liệu liên quan

- [Problem Scan và ba Quick Problem Cards](01-problem-scan.md).
- [Báo cáo Deep-Dive và đánh giá prototype](02-deep-dive-report.md).
- [Workflow hiện tại và tương lai](04-workflow-diagram.pdf).
- [Worksheet hướng dẫn](01-worksheet.md).
