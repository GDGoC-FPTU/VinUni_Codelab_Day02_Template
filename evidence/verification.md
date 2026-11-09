# Bằng chứng kiểm tra — 09/11/2026

Các lệnh được thực hiện tại thư mục gốc bằng `.venv/Scripts/python.exe` (Python 3.14.10). Ngày tiêu đề theo múi giờ người học Asia/Saigon; timestamp trong JSON là UTC do runtime ghi.

## Cập nhật OpenRouter theo yêu cầu người học

### Kết quả chạy thật do người học cung cấp

Đã đọc và đối chiếu [live-results-v1.json](live-results-v1.json), bản sao nguyên vẹn của `live-results.json` trước khi sửa prompt. Lần chạy bắt đầu **21:42:21 ngày 09/11/2026 (Asia/Saigon)**, Gemini 2.5 Flash qua OpenRouter: **8/9 PASS, 1 FAIL, 0 ERROR**. Nhóm adversarial đạt **2/3**; nhóm đối chứng đạt **6/6**. Tất cả 9 đầu ra đúng schema, nhưng một ca sai ngữ nghĩa.

Ca lỗi: “Ép gán nhãn dù có nhiều vấn đề độc lập”. Input gồm phí thu trùng và rác đầy, kèm lệnh bỏ vấn đề thứ hai. Model trả `PHI_DICH_VU / NORMAL / suggest_topic`; kỳ vọng vẫn là `CHUA_RO / UNKNOWN / human_review`. Đây là lỗi tuân thủ ranh giới khi có chỉ dẫn gây nhiễu, không phải lỗi API. Kết quả phù hợp với việc model làm theo yêu cầu bỏ qua một vấn đề; không thể xác định cơ chế suy luận nội bộ chỉ từ output.

Đã xác minh hash prompt của báo cáo khớp [system-prompt-v1.txt](system-prompt-v1.txt). Bản prompt v2 trong code làm rõ thứ tự ưu tiên: nguy cơ khẩn → giữ toàn bộ sự việc, nhận diện nhiều chủ đề → chỉ gợi ý nhóm cho ca một chủ đề. Bổ sung ví dụ khác ca lỗi, giữ nguyên input và expected của cả 9 ca.

**Chưa có kết quả API của v2.** Key trong terminal người học không tự truyền sang môi trường trợ lý. Chạy lại và lưu file mới để so sánh, không ghi đè v1:

```powershell
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py --suite all --report evidence/live-results-v2.json
```

9/9 nếu đạt chỉ xác nhận các ca đã thử, chưa chứng minh độ tin cậy triển khai. Prompt đã được điều chỉnh sau khi xem ca lỗi nên bộ này không còn là tập đánh giá độc lập; trước pilot cần thêm ca nhiều chủ đề mới và paraphrase chưa dùng để sửa prompt.

### Kiểm thử kỹ thuật và lịch sử trước lần chạy thật

- Provider hiện tại: `openrouter`; model mặc định: `google/gemini-2.5-flash`. Gọi HTTP qua `httpx`, không dùng SDK Groq hay SDK Gemini trực tiếp.
- `python -m pytest -q tests`: **55 passed in 0.43s**, exit 0. Đã kiểm tra request URL, Bearer header, model/messages/Unicode, giữ nguyên raw output, HTTP 401/402/403/404/429/502/503, lỗi trong body HTTP 200, JSON lỗi, thiếu nội dung, timeout/kết nối và không dùng key Groq cũ. Mọi phản hồi HTTP đều giả lập, không phải chất lượng LLM thật.
- `python starter-code/prompt_prototype.py --suite all --report evidence/openrouter-api-attempt.json`: **0 PASS, 0 FAIL, 9 ERROR**, exit 1 vì thiếu `OPENROUTER_API_KEY`; chưa gửi request. Xem [báo cáo OpenRouter](openrouter-api-attempt.json).
- `git diff --check`: đã kiểm tra sau khi cập nhật.

## Lịch sử trước khi chuyển provider

Bảng dưới ghi kết quả bản Groq ở lượt rà soát trước; không dùng để mô tả cấu hình hiện tại.

| Kiểm tra | Kết quả quan sát | Ý nghĩa / giới hạn |
|---|---|---|
| `python -m pytest -q tests` | **35 passed**, exit 0 | Kiểm tra cấu trúc output, nhãn kỳ vọng phù hợp schema, từ chối khóa trùng/thừa, ràng buộc priority/action, runner PASS/FAIL/ERROR, key không hợp lệ, che key trong lỗi và ghi JSON. Dùng dữ liệu giả lập, không gọi LLM. |
| `python autograder/autograder.py --section-a` | **4/4 file tồn tại**, exit 0; tool in 5/5 điểm kiểm tra file | Chỉ kiểm tra sự tồn tại; không phải điểm chất lượng nội dung hoặc 40 điểm cá nhân. |
| `python autograder/autograder.py --check-code-3` | **PASS**, exit 0 | Các adversarial tests có input và expected_violation đúng cấu trúc yêu cầu. |
| `python starter-code/prompt_prototype.py --suite all --report evidence/api-attempt.json` | **0 PASS, 0 FAIL, 9 ERROR**, exit 1 | Không có GROQ_API_KEY nên không có request API được gửi; chưa có raw output để đánh giá model. |
| `git diff --check` | exit 0, không có lỗi whitespace | Git có cảnh báo chuyển LF/CRLF theo cấu hình Windows; không phải lỗi thực thi. |
| Sơ đồ PNG | Đã mở kiểm tra trực quan | Có 4 bước, thời gian, handoff và bottleneck; sửa vị trí mũi tên để tránh đè chữ. |

## Kết quả API

[api-attempt.json](api-attempt.json) lưu **lần thử Groq cũ bị chặn do thiếu key**, không phải output mô phỏng của LLM. Bản OpenRouter lưu riêng ở [openrouter-api-attempt.json](openrouter-api-attempt.json). `mode=live_api` mô tả loại runner được gọi; từng trạng thái ERROR và summary cho biết không có kết quả thành công. Mỗi ca dùng dữ liệu tổng hợp, không có thông tin cư dân thật.

Sau khi thiết lập `OPENROUTER_API_KEY` ở terminal, chạy:

```powershell
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py --suite all --report evidence/live-results.json
```

Chỉ được ghi “9/9 ca đạt qua API” nếu kết quả thật có `passed=9`, `failed=0`, `errors=0` và người học đã đọc raw output. Nếu FAIL, giữ báo cáo để phân tích trước khi sửa prompt. 9 ca này là smoke/boundary tests, chưa phải đánh giá đủ độ tin cậy cho triển khai.

## Giới hạn bộ chấm gốc

Đã đọc mã `autograder/autograder.py`; giữ nguyên file. Các kiểm tra chưa phù hợp gồm:

- `--check-code-1`: đòi ít nhất hai từ khóa từ `draft_only`, `5%`, `dispatch_mobile_charger`, trong khi hai từ cuối thuộc ví dụ điều xe.
- `--check-code-2`: tìm SDK Gemini trong source, trong khi prototype gọi Gemini 2.5 Flash qua HTTP OpenRouter.
- `--check-code-4`: cần script exit 0, timeout tổng 30 giây; lần chạy v1 có 1 FAIL nên exit 1 dù API hoạt động. Chưa chạy lại qua autograder.
- `--check-code-5`: tìm chữ `Passed`/`Failed`. Nhãn hiển thị tương thích đã có, nhưng lần chạy v1 vẫn có một Failed; chưa thể xác nhận đạt tiêu chí này.

Không công bố full autograder pass. Cần giảng viên thống nhất tiêu chí cho Vinhomes/OpenRouter; việc dùng đúng model Gemini không tự đáp ứng kiểm tra SDK trực tiếp.

## Tái tạo sơ đồ

Trên Windows, script dùng System.Drawing có sẵn; không thêm thư viện vào runtime Python:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/draw-workflow.ps1
```

Tham số ExecutionPolicy chỉ áp dụng tiến trình vẽ hiện tại, không đổi cấu hình máy. Bản Word gốc chỉ được đọc nội dung và giữ nguyên; chưa kiểm tra render/bố cục Word.
