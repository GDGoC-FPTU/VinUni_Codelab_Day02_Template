# Lab 02 — AI Log & Reflection

> **Họ tên:** [V]
> **Mã sinh viên:** [2A202602895]
> **Nhóm:** []
> **Ngày:** [11/9/2026]
>
> Đây là nhật ký cá nhân. Tôi cần bổ sung hoặc chỉnh lại những chi tiết chỉ mình tôi biết trước khi nộp.

## 1. Mục tiêu sử dụng AI

Trong Lab 02, tôi sử dụng AI như một thought-partner để:

- Hiểu thứ tự các phase và tiêu chí của từng deliverable.
- Brainstorm các bài toán/bottleneck cho VinFast và Vinmec.
- Chuyển ý tưởng thành bảng SCAN và Quick Problem Cards.
- Phản biện metric, operational boundary và lựa chọn kiến trúc AI.
- Kiểm tra cấu trúc file và refactor nhẹ prompt prototype.

AI không được xem là nguồn sự thật tuyệt đối. Tôi vẫn phải kiểm tra lại quy trình, số liệu, rủi ro và quyết định cuối cùng.

## 2. Các prompt chính đã sử dụng

### Prompt 1 — Hiểu yêu cầu lab

Tôi yêu cầu AI đọc yêu cầu lab và giải thích thứ tự thực hiện, các file cần nộp và cách phân biệt phần cá nhân với phần nhóm.

**AI hỗ trợ:** AI tách lab thành các phase SCAN, QUICK-ASSESS, DEEP-DIVE, PROTOTYPE và EVALUATE; đồng thời giải thích branch cá nhân và branch main.

**Kết quả tôi sử dụng:** Tôi tạo được checklist công việc và biết rằng bốn deliverable Markdown/ảnh phải xuất hiện ở main, còn code prototype được chấm trên branch cá nhân.

### Prompt 2 — Brainstorm bài toán

Tôi yêu cầu AI đề xuất 3 bài toán liên quan đến VinFast và 2 bài toán liên quan đến Vinmec để điền vào Phase 1.

**AI hỗ trợ:** AI gợi ý các bài toán liên quan đến phân loại yêu cầu dịch vụ, điều phối cứu hộ và phân loại lịch khám.

**Cách tôi kiểm tra:** Tôi yêu cầu các ý tưởng dựa trên quy trình công khai, sau đó kiểm tra các trang chính thức của VinFast và Vinmec về đặt lịch, dịch vụ cứu hộ và quy trình tiếp nhận bệnh nhân.

### Prompt 3 — Tạo Quick Problem Cards

Tôi yêu cầu AI chuyển ba ý tưởng thành Quick Problem Cards có actor, workflow, bottleneck, thời gian, metric và kiến trúc.

**AI hỗ trợ:** AI tạo workflow 5 bước cho mỗi card và đề xuất metric có số.

**Điểm tôi phải thận trọng:** Các số như 10–20 phút/yêu cầu hoặc 90% độ chính xác là mục tiêu/ước tính scoping, không phải số liệu nội bộ. Tôi ghi rõ cần kiểm chứng thay vì trình bày chúng như sự thật.

### Prompt 4 — Tạo và chỉnh sửa tài liệu

Tôi yêu cầu AI tạo template cho 01-problem-scan.md và 02-deep-dive-report.md, sau đó điền Phase 2 vào file.

**AI hỗ trợ:** AI tạo cấu trúc Markdown, bảng và checklist giúp tôi không bỏ sót các trường bắt buộc của rubric.

**Cách tôi kiểm tra:** Tôi kiểm tra file có đủ số lượng card, 6-field, checklist và đường dẫn đến sơ đồ/code.

### Prompt 5 — Refactor prompt prototype

Tôi yêu cầu AI refactor nhẹ starter-code/prompt_prototype.py nhưng giữ toàn bộ comment, tên hàm và tên parameter.

**AI hỗ trợ:** AI phát hiện file có hai khối code nối tiếp nhau, khiến block main đầu tiên có thể kết thúc chương trình trước khi chạy phần implementation phía sau. AI gom lại thành một module duy nhất.

**Cách tôi kiểm tra:** Tôi chạy Python compile, git diff --check và các check tĩnh của autograder cho SYSTEM_PROMPT, Gemini SDK và ADVERSARIAL_TESTS.

## 3. Một điểm AI có nguy cơ sai hoặc gây nhầm lẫn

Ban đầu, ví dụ lab và starter code sử dụng action dispatch_mobile_charger. Tuy nhiên, khi kiểm tra thông tin chính thức, tôi thấy VinFast đã công bố chuyển sang cứu hộ bằng xe kéo RSA cho trường hợp xe hết pin từ ngày 06/06/2025.

Điều này cho thấy ví dụ trong starter code có thể là boundary giả lập cho bài lab, không nhất thiết là quy trình production hiện hành. Tôi đã điều chỉnh báo cáo để:

- Dùng RSA khi mô tả quy trình hiện hành của VinFast.
- Giữ dispatch_mobile_charger trong phần prototype vì đây là action được starter code yêu cầu.
- Ghi rõ action này là placeholder giáo dục và cần thay bằng action production sau khi xác nhận với bộ phận vận hành.

## 4. Những giới hạn tôi đã đặt cho AI

Tôi đặt các giới hạn sau trong phạm vi bài toán:

1. AI chỉ trích xuất thông tin, phân loại và tạo bản nháp.
2. AI không tự điều xe, tự gọi cứu hộ hoặc tự gửi tin nhắn.
3. AI không tự bịa vị trí, lộ trình, ETA hoặc tình trạng đội cứu hộ.
4. Mọi hành động vận hành phải có Human-in-the-loop.
5. Nếu dữ liệu thiếu, mâu thuẫn hoặc AI không chắc chắn, case phải chuyển về nhân viên xử lý thủ công.
6. Với nội dung y tế, AI không được chẩn đoán, kê đơn hoặc quyết định điều trị.

## 5. Kết quả và phần chưa hoàn tất

AI giúp tôi hoàn thiện được cấu trúc ba file báo cáo và làm rõ ranh giới giữa LLM Feature với Rule/State Machine. Tôi cũng hiểu rằng một prototype tốt không chỉ cần prompt mà còn cần metric, HITL, fallback, audit log và bộ test có ground truth.

Trong workspace hiện tại chưa có GEMINI_API_KEY nên tôi chưa thể xác nhận kết quả chạy Gemini live của các adversarial tests. Trước khi nộp, tôi cần:

- Thiết lập API key trong terminal nhưng không đưa key vào Git.
- Chạy starter-code/prompt_prototype.py.
- Ghi kết quả Pass/Fail thực tế vào 02-deep-dive-report.md.
- Kiểm tra output có bắt đầu bằng [DRAFT_ONLY] và xử lý đúng trường hợp pin dưới 5% hay không.

## 6. Bài học cá nhân

Bài học lớn nhất của tôi là phải bắt đầu từ problem và workflow, sau đó mới chọn AI. Không nên chọn Agent chỉ vì nó phức tạp hơn. Với bài toán điều phối cứu hộ, LLM chỉ nên xử lý phần ngôn ngữ và chuẩn hóa dữ liệu; các điều kiện an toàn cần được kiểm soát bằng Rule và nhân viên vận hành.

Tôi cũng nhận ra rằng AI có thể tạo ra một báo cáo nghe hợp lý nhưng vẫn chứa số liệu chưa được chứng minh. Vì vậy, tôi cần phân biệt rõ giữa nguồn chính thức, quan sát thực tế, giả định scoping và metric mục tiêu.
