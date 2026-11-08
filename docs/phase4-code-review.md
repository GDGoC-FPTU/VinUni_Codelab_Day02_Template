# Phase 4 — Đối chiếu starter code với scope Vinmec sau khám

**Trạng thái:** Ghi chép khảo sát starter và SDK trước khi triển khai, chưa chạy Gemini cho scope này. Khi bàn giao, dùng [đặc tả demo tối giản](phase4-proposal.md) làm nguồn quyết định mới nhất; các gợi ý Pydantic hoặc diễn giải tự nhiên trong ghi chép khảo sát không phải yêu cầu triển khai.

**Nguồn yêu cầu:** [Worksheet — Phase 1–4](../01-worksheet.md), [glossary](../GLOSSARY.md), [quyết định về chatbot và bàn giao bác sĩ](adr/0001-approved-aftercare-chatbot-and-doctor-handoff.md).

## 1. Starter hiện có gì?

- [starter-code/prompt_prototype.py](../starter-code/prompt_prototype.py) vẫn là ví dụ điều vận Xanh SM: pin dưới 5%, trạm sạc quá 5 km và điều xe sạc di động.
- `SYSTEM_PROMPT` còn TODO; `evaluate_prompt(user_input: str) -> str` chưa gọi API và còn `raise NotImplementedError`.
- Hai adversarial tests cùng hai nhánh kiểm tra đầu ra đều phục vụ ví dụ taxi. Kiểm tra từ khóa chưa chứng minh nội dung trả lời đúng hoặc giữ được boundary của Vinmec.
- Starter yêu cầu từ khóa `[DRAFT_ONLY]` cho mọi đầu ra. Với scope đã chốt, bản chuẩn bị cho bác sĩ cần duyệt, còn câu giải thích trong nguồn và boundary đã duyệt được phép trả cho bệnh nhân. Hai trạng thái này cần được phân biệt rõ trong output.
- Worksheet yêu cầu ít nhất **3 adversarial inputs**, dù docstring starter chỉ nhắc ít nhất 2; lấy yêu cầu worksheet làm mốc.

## 2. Nội dung Phase 4 cần chuyển sang Vinmec

| Thành phần | Hướng thay thế theo Phase 3 | Bằng chứng cần thu |
|---|---|---|
| System prompt | Vai trò sau khám; bác sĩ cung cấp chỉ định sơ bộ, nguồn và boundary; bệnh nhân không có quyền sửa các thông tin đã duyệt. | Lưu phiên bản prompt dùng trong lần thử. |
| Dự thảo cho bác sĩ | AI tổ chức chỉ định đã được cung cấp thành bản nháp để bác sĩ xem xét; không tự chọn thuốc hoặc tạo liệu trình mới. | Trạng thái chờ duyệt; chưa có quyền dùng như chỉ định đã duyệt. |
| Giải thích cho bệnh nhân | Chỉ giải thích kế hoạch và kiến thức bệnh lý trong nguồn bác sĩ đã duyệt. | Nội dung, nguồn tham chiếu và kết quả kiểm tra đầu ra. |
| Vượt boundary | Thiếu căn cứ, nguồn mâu thuẫn, triệu chứng mới hoặc yêu cầu đổi chỉ định chuyển bác sĩ. | Yêu cầu tham vấn có câu hỏi, tóm tắt liên quan, lý do và trạng thái chờ. |
| Handoff | Bản lab mô phỏng hàng đợi và thông báo; không tuyên bố bác sĩ đã nhận hoặc trả lời khi chưa có xác nhận. | Phân biệt tạo yêu cầu, chờ tiếp nhận và trả lời; ghi rõ thông báo mô phỏng. |
| Fallback | Lỗi API, JSON không hợp lệ, nguồn không hợp lệ hoặc nội dung chưa đủ căn cứ giữ lại câu trả lời chưa đạt và chuyển xử lý thủ công. | Ghi lỗi và kết quả không đạt; không đổi tên lỗi thành một ca Gemini thành công. |
| Bộ thử | Có câu hỏi bình thường và tối thiểu 3 tấn công: vượt boundary / đổi chỉ định, bỏ duyệt hoặc giả mạo quyền, truy cập thông tin bệnh nhân khác; bổ sung ca thiếu nguồn và lỗi kỹ thuật. | Expected outcome, actual outcome và kiểm tra riêng từng ca. |

Không dùng bệnh án thật hoặc coi tài liệu mô phỏng là tài liệu đã được bác sĩ Vinmec xác nhận. Luồng khẩn cần quy trình chuyên môn đã duyệt; bản lab chưa có quy trình đó, nên không tự đặt ngưỡng triệu chứng hay hứa thực hiện điều phối thật.

## 3. SDK và mô hình — các dữ kiện đã kiểm tra

- Google khuyến nghị SDK `google-genai`, thay cho thư viện legacy `google-generativeai`. [Tài liệu thư viện](https://ai.google.dev/gemini-api/docs/libraries).
- SDK vẫn hỗ trợ `client.models.generate_content(...)`, system instruction và JSON schema. Có thể giữ cách gọi phù hợp starter, sử dụng schema đơn giản và kiểm tra lại JSON trả về bằng Pydantic. [SDK — cấu hình](https://github.com/googleapis/python-genai#system-instructions-and-other-configs), [SDK — JSON schema](https://github.com/googleapis/python-genai#json-response-schema).
- Structured output kiểm soát cấu trúc, không chứng minh nội dung đúng chuyên môn hoặc bám đúng nguồn; cần kiểm tra giá trị và nội dung riêng. [Structured outputs](https://ai.google.dev/gemini-api/docs/structured-output).
- Tài liệu Google được đọc trong phiên ghi `gemini-2.5-flash` là deprecated, quyền truy cập giới hạn cho người dùng hiện hữu; thông báo định tuyến tự động sang model khác có hiệu lực từ 01/12/2026. Cần cho phép cấu hình model và ghi rõ model được yêu cầu / thông tin model thực tế nếu API cung cấp; quyền truy cập tài khoản chưa được thử. [Models](https://ai.google.dev/gemini-api/docs/models), [Deprecations](https://ai.google.dev/gemini-api/docs/deprecations).
- SDK nhận `GEMINI_API_KEY` hoặc `GOOGLE_API_KEY`. Code cần nêu rõ cách chọn key nếu cả hai được cấu hình và không ghi giá trị key vào log. [API-key configuration](https://ai.google.dev/gemini-api/docs/api-key).

## 4. Môi trường và giới hạn autograder

- Python mặc định đã kiểm tra: **3.12.2**. Chưa tìm thấy `.venv` cho repo; chưa có `google-genai`, `pydantic`, `pytest` trong môi trường Python đã kiểm tra.
- Chưa có `GEMINI_API_KEY` hoặc `GOOGLE_API_KEY` trong môi trường process dùng để kiểm tra. Chưa gọi API; không thu thập hoặc ghi giá trị bí mật.
- [Autograder gốc](../autograder/autograder.py) tìm prototype tại `extras/prompt_prototype.py`, rồi `starter-code/prompt_prototype.py`, rồi file ở root; không dùng bản trong `solution`.
- Grader yêu cầu ít nhất hai trong các từ khóa `draft_only`, `5%`, `dispatch_mobile_charger` trong prompt. Vì vậy, prompt Vinmec đúng scope có thể không đạt phần chấm từ khóa taxi. Không thêm quy tắc taxi chỉ để vượt kiểm tra này.
- Grader còn kiểm tra source của `evaluate_prompt`, cấu trúc `ADVERSARIAL_TESTS`, chạy script trong 30 giây và đếm chữ `Passed` / `Failed`. Đây không phải kiểm định tính đúng chuyên môn hoặc hành vi giữ nguồn.
- Lúc import module không được tự gọi mạng hoặc đòi key. Cần phân biệt kết quả test logic offline với hành vi Gemini thật; một hệ thống chặn được đầu ra lỗi không đồng nghĩa bản thân model đã tuân thủ prompt.

## 5. Các quyết định đã chốt với người làm bài

- **Hai luồng tối giản:** AI tổ chức dự thảo cho bác sĩ duyệt; chatbot giải thích cho bệnh nhân và bàn giao nội dung vượt boundary.
- **Chỉ Gemini thật:** Không xây dựng chế độ offline hoặc dùng phản hồi mô hình giả để tính điểm. Thiếu key thì báo chưa chạy; kiểm tra cấu trúc tĩnh không được coi là kết quả hành vi Gemini.
- **JSON cục bộ:** Lưu hàng đợi mô phỏng và bằng chứng chạy thử, đồng thời hiển thị tóm tắt trên terminal.
- **Autograder Vinmec:** Điều chỉnh grader cục bộ theo scope Vinmec; thay kiểm tra từ khóa taxi và đếm chữ Passed / Failed bằng kiểm tra phù hợp. Đây chưa phải grader được giảng viên xác nhận.
- **Cấu hình:** Đã tạo `.env` trong repo với trường key trống và model cấu hình được; file được Git bỏ qua. Prototype mới cần nạp file này; starter hiện tại chưa có bước nạp `.env`.

Đặc tả triển khai để xác nhận hiểu đúng nằm tại [bản Phase 4](phase4-proposal.md); quyết định về nguồn bằng chứng nằm tại [ADR 0002](adr/0002-live-gemini-and-vinmec-evaluation.md).

Phase 4 có thể cung cấp bằng chứng về cấu trúc đầu ra, xử lý lỗi, tạo yêu cầu và hành vi trên bộ thử. Các mục tiêu **≤7 phút**, **≥95% nội dung** và **bệnh nhân nhắc lại đúng ≥4/5 ý** vẫn cần phép đo và đánh giá tương ứng; không suy ra đã đạt chỉ từ việc script chạy thành công.
