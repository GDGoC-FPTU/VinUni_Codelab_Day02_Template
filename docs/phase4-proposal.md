# Phase 4 — Demo LLM Vinmec sau khám

**Trạng thái:** Đã chốt theo vòng phản biện thứ hai, sẵn sàng bàn giao cho agent triển khai. Phiên này chỉ sửa tài liệu, không viết hoặc chạy code.

## 1. Mục tiêu và giới hạn

Demo kiểm tra ý tưởng: LLM chọn các đoạn phù hợp từ dữ liệu đã duyệt; chương trình ghép nguyên văn và chuyển yêu cầu ngoài phạm vi cho bác sĩ theo mô phỏng.

- Hai luồng thử riêng: tổ chức dự thảo cho bác sĩ và trả lời bệnh nhân.
- Hai fixture chưa duyệt / đã duyệt được chuẩn bị sẵn. Không có CLI duyệt, không kiểm thử chuyển trạng thái phê duyệt đầu-cuối.
- Thuốc, hoạt động, bệnh nhân và kiến thức đều mang mã DEMO, không có hướng dẫn y khoa thật.
- Chỉ Gemini thật; mỗi ca live gọi một lần. Ba ca kiểm soát trước API không được tính là Gemini đã đạt. Không có chế độ offline hoặc phản hồi mô hình giả.
- Demo terminal, không làm giao diện, database, đăng nhập, thông báo thật, tìm kiếm web, agent tự trị hoặc hệ thống vận hành bệnh viện.

## 2. Việc agent nhận bàn giao cần làm

1. Đọc Phase 3 trong [worksheet](../01-worksheet.md) và fixture bên dưới; giữ các quyết định chuyên môn của bác sĩ ngoài quyền LLM.
2. Sửa [prototype](../starter-code/prompt_prototype.py) thành một script nhỏ dùng `google-genai`, `python-dotenv` và `json` của Python. Không cần mô hình dữ liệu hoặc framework bổ sung; schema JSON có thể khai báo bằng dictionary.
3. Sửa [autograder](../autograder/autograder.py) cho Vinmec; giữ các flag cũ và phần kiểm tra file nộp bài. Bỏ rule taxi và cách đếm chữ Passed / Failed.
4. Cập nhật phụ thuộc cần thiết, bỏ qua output sinh ra trong Git và ghi Phase 4 vào worksheet bằng kết quả thực tế. Giữ Phase 1–3, 5–6 và nội dung người dùng đã sửa; chỉ cập nhật câu trạng thái cần thiết.
5. Kiểm tra cú pháp/import, rồi chạy grader `--section-b` một lần khi đủ cấu hình. Không tự commit/push. Nếu thiếu key, giao lại code cùng trạng thái chưa chạy Gemini.

## 3. Hợp đồng tối thiểu

### Đầu vào và nguồn tin cậy

Giữ cách gọi `evaluate_prompt(user_input: str) -> str`; thêm keyword-only `mode="patient_chat"`, `case_id="DEMO_APPROVED"`. Mode chỉ nhận `doctor_draft` hoặc `patient_chat`; case ID lấy từ fixture của chương trình. Sai mode/case là lỗi cấu hình, không gọi API. Lời bệnh nhân không thay được mode, ca, nguồn hoặc phê duyệt.

Hàm trả **chuỗi JSON thô của Gemini**, không trả kết quả fallback giả làm đầu ra mô hình. Runner kiểm tra trước API, parse và render sau API. Guard chặn trước API được runner ghi riêng, không tạo raw model response.

### JSON của LLM

Chỉ có ba trường bắt buộc: `action` (string), `segment_ids` (list string không lặp), `reason` (string không rỗng). Từ chối trường thừa, sai kiểu và ID ngoài fixture được phép dùng.

| Action | Điều kiện | ID được chọn |
|---|---|---|
| DRAFT_FOR_REVIEW | Chỉ luồng bác sĩ; bản nháp vẫn chờ duyệt | Không rỗng, thuộc chỉ định sơ bộ được cung cấp |
| ANSWER | Chỉ luồng bệnh nhân, fixture đã duyệt | Không rỗng, thuộc đoạn đã duyệt của đúng ca |
| ESCALATE | Cần bác sĩ làm rõ, có yêu cầu đổi chỉ định hoặc triệu chứng mới | Rỗng |
| BLOCKED | Yêu cầu thông tin bệnh nhân khác hoặc quyền không được phép | Rỗng |

Chương trình tạo `app_text` bằng cách ghép nguyên văn các đoạn theo thứ tự ID, ngăn bằng hai newline. Bản nháp thêm nhãn `[DRAFT_ONLY]` ở phần hiển thị, không thêm trước JSON API. Không hiển thị `reason` của LLM như lời tư vấn; các thông báo chặn/bàn giao dùng câu cố định. Nhánh `URGENT` chỉ do guard của kịch bản DEMO tạo, không phải kết luận cấp cứu của LLM.

### Fixture và bộ thử

Dùng nguyên văn [fixture và expected outcomes](phase4-demo-fixtures.md). System prompt không chứa expected action hoặc expected IDs của từng câu hỏi. Expected chỉ dùng trong runner/grader sau khi có đầu ra.

Có 10 ca: 7 ca gọi Gemini và 3 ca guard. Một lần/case, không chọn lọc lần chạy đẹp. Chỉ kiểm tra lựa chọn đoạn và luồng trên bộ câu hỏi hữu hạn; không suy ra năng lực giải thích y khoa hoặc độ ổn định.

## 4. Chạy, lưu kết quả và lỗi

- Nạp `.env` ở root, không override biến process đã có. Ưu tiên `GEMINI_API_KEY`, rồi `GOOGLE_API_KEY`, truyền key tường minh cho SDK. Không in hoặc ghi key, headers hay nội dung `.env`.
- Model mặc định `gemini-2.5-flash`, cho phép `GEMINI_MODEL` override tường minh. Nếu không truy cập được thì báo lỗi, không tự chuyển model. Ghi model yêu cầu và model thực tế nếu API cung cấp.
- Không gọi mạng hoặc đòi key lúc import. Mỗi ca live gọi `generate_content` một lần, timeout 30 giây, không tự retry. Lỗi dịch vụ dừng lượt chạy; JSON/action/ID không hợp lệ là ca kiểm tra không đạt nhưng tiếp tục ca sau.
- Preflight key và SDK trước khi chạy suite; nếu thiếu, cả 10 ca đều NOT_RUN, kể cả guard. Việc kiểm tra cú pháp/import vẫn có thể làm riêng.
- Mỗi lượt có thư mục mới `outputs/phase4/<run_id>/`, gồm `results.json` và `doctor_queue.json`. Có thể thêm `--output-dir` để grader chỉ định thư mục mới, không ghi đè bằng chứng cũ.
- `results.json` ghi run ID, thời điểm, model, phiên bản/hash prompt và fixture, trạng thái thực thi; mỗi ca có expected, `api_called`, raw response hoặc null, model action/IDs hoặc null, kết quả kiểm tra model, app action/text và kết quả guard/bàn giao. Raw và expected không được đưa vào thông báo bệnh nhân.
- Model check dùng `PASS`, `FAIL`, `NOT_APPLICABLE`, `NOT_RUN`. Ca guard thành công có model=`NOT_APPLICABLE`, guard=`PASS`; ca chưa thực hiện có model=`NOT_RUN`. Không đưa ba guard vào mẫu số pass của bảy ca live.
- Patient `ESCALATE` tạo hàng đợi `pending`; `URGENT` tạo mục riêng `urgent_demo`. Ghi đúng ca, câu hỏi, lý do và tóm tắt từ dữ liệu tin cậy. `BLOCKED` không tạo hàng đợi; dự thảo bác sĩ không tạo yêu cầu tự gửi cho chính bác sĩ.
- Nếu model trả sai schema/action/ID, không hiển thị nội dung lỗi. Patient được chuyển xử lý thủ công, có queue mô phỏng; model vẫn `FAIL` dù ứng dụng chặn thành công. Lỗi ở luồng bác sĩ chỉ báo cần người soạn kiểm tra, không tạo queue bệnh nhân.
- Chỉ thông báo đã ghi nhận sau khi lưu queue thành công. Nếu ghi file thất bại, báo chưa ghi nhận; dùng chuỗi fallback `DEMO_CONTACT: kênh liên hệ mô phỏng, không gửi thông báo thật.` Không dựng số điện thoại. Nếu không lưu được báo cáo, ghi lỗi ngắn lên stderr và dừng; grader không dùng báo cáo cũ.

Mã thoát prototype: **0** khi hoàn thành và mọi kiểm tra tự động đạt; **1** khi hoàn thành nhưng có ca không đạt; **2** khi thiếu cấu hình hoặc chạy chưa hoàn tất vì lỗi API/ghi file. Thiếu key ghi `NOT_RUN`, không gọi API hoặc tính điểm hành vi; không yêu cầu gửi key trong chat.

## 5. Grader và điều kiện hoàn thành

Giữ 5 mục code, mỗi mục 1 điểm cục bộ: (1) prompt/schema/domain, (2) hàm gọi Gemini và cấu hình, (3) bộ 10 ca có 3 adversarial, (4) hoàn thành thực thi live, (5) kết quả tự động trên bộ thử. Phần kiểm tra file tài liệu giữ nguyên; không tạo file rỗng để lấy điểm.

- Một invocation `--section-b` gọi suite tối đa một lần, timeout toàn suite 10 phút, đọc JSON của đúng lần chạy đó. Giữ hành vi exit 0/1 của grader: 0 khi tất cả tiêu chí được yêu cầu đạt, 1 khi có mục không đạt/chưa chạy.
- Mục 4 có thể đạt khi prototype exit 0 **hoặc 1** nếu cả 7 ca live đã có phản hồi và cả 3 guard đã được kiểm tra, báo cáo lưu đầy đủ. Mục 5 chỉ đạt khi cả 7 model checks và 3 guard checks đều đạt, queue/hiển thị đúng. Model sai thì mục 5 không đạt, kể cả fallback đã bảo vệ được phần hiển thị.
- Thiếu key/lỗi dịch vụ không được điểm live của mục 4–5; mục tĩnh được báo riêng. Grader đánh giá lựa chọn ID và luồng theo fixture, không xác nhận đúng chuyên môn hoặc nguồn thực sự đã được bác sĩ duyệt.
- Cú pháp/import là kiểm tra code, không phải chế độ phản hồi offline. Không giả lập lỗi API để ghi thành bằng chứng Gemini.
- Agent giao lại file đã sửa, lệnh chạy, đường dẫn JSON và kết quả trung thực. Nếu chưa chạy được API phải nêu rõ; lỗi boundary thật giữ nguyên để báo cáo, không sửa expected chỉ để pass.

Các mục tiêu Phase 3 **≤7 phút**, **≥95% nội dung** và **teach-back ≥4/5** chưa được đo trong demo này. Không tự kết luận GO ở Phase 5.
