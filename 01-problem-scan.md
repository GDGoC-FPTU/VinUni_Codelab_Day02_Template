# Lab 02 — Problem Scan & Quick Assessment

**Người thực hiện:** Lưu Văn Việt Đức  
**Tên nhóm:** Simple - Tech  
**Email:** luuvanvietduc@gmail.com  
**Ngày cập nhật:** 07/11/2026  
**Phạm vi đóng góp:** Bài làm cá nhân của Lưu Văn Việt Đức; chưa thay thế báo cáo tổng hợp của nhóm.

## 1. Phạm vi khảo sát

VinFast — Quy trình tiếp nhận nhu cầu sửa chữa xe.

Các pain point hiện là giả thuyết cần xác nhận với nhân viên nghiệp vụ.

## 2. Phase 1 — Bảng scan 5 vấn đề

**Phạm vi khảo sát:** Tiếp nhận mô tả hiện tượng của xe, thu thập thông tin bổ sung và hoàn thiện phiếu tiếp nhận dịch vụ.

**Trạng thái:** Các vấn đề dưới đây là **giả thuyết cần kiểm chứng**, chưa phải kết luận về quy trình nội bộ VinFast. Chưa có số liệu xác nhận về tần suất, thời gian xử lý hoặc tỷ lệ sai sót.

| # | Subsidiary | Lens | Mô tả bài toán ứng viên |
|---|---|---|---|
| **1** | **VinFast — Dịch vụ hậu mãi** | **Pain từ người dùng/nhân viên — Stakeholder Pain** | **Mô tả hiện tượng thiếu thông tin cần thiết.** Khách chỉ ghi nội dung ngắn như “điều hòa không mát”, chưa cung cấp thời điểm bắt đầu, tần suất hoặc điều kiện xuất hiện. Cố vấn dịch vụ cần xác định và hỏi bổ sung trước khi hoàn thiện phiếu, có thể làm phát sinh nhiều lượt trao đổi. |
| **2** | **VinFast — Dịch vụ hậu mãi** | **Tốn thời gian — Time-consuming** | **Nhiều hiện tượng và yêu cầu được trình bày lẫn trong một đoạn dài.** Khách kể đồng thời về điều hòa, tiếng kêu và nhu cầu bảo dưỡng. Cố vấn cần đọc, tách từng nội dung và lập danh sách yêu cầu kiểm tra, có nguy cơ bỏ sót một phần nhu cầu của khách. |
| **3** | **VinFast — Dịch vụ hậu mãi** | **AI có thể hỗ trợ tốt hơn — AI-upgrade** | **Cách diễn đạt đời thường chưa rõ nghĩa hoặc khó ghi nhận thống nhất.** Những mô tả như “xe bị ì”, “kêu cụp cụp” hoặc “máy lạnh yếu” cần được làm rõ và chuyển thành câu mô tả dễ hiểu, đồng thời giữ nguyên ý khách và tránh suy diễn thành chẩn đoán kỹ thuật. |
| **4** | **VinFast — Dịch vụ hậu mãi** | **Lặp lại — Repetitive** | **Thông tin cùng một trường không nhất quán giữa biểu mẫu và phần mô tả.** Ví dụ, số kilomet trên biểu mẫu khác số kilomet khách ghi trong nội dung trao đổi. Cố vấn cần đối chiếu, phát hiện khác biệt và xác nhận thông tin đúng trước khi sử dụng. |
| **5** | **VinFast — Dịch vụ hậu mãi** | **Pain từ người dùng/nhân viên — Stakeholder Pain** | **Thông tin đã thu thập có nguy cơ bị mất khi tổng hợp và bàn giao.** Khi chuyển nội dung trao đổi sang phiếu tiếp nhận, điều kiện xuất hiện hiện tượng hoặc yêu cầu cụ thể của khách có thể bị lược bỏ. Người nhận bàn giao cần hỏi lại hoặc tra cứu nội dung gốc để làm rõ. |

**Phân biệt phạm vi của 5 bài toán**

| Bài toán | Câu hỏi trọng tâm |
|---|---|
| **1 — Độ đầy đủ** | Khách **chưa cung cấp** thông tin nào cần thiết? |
| **2 — Tách nội dung** | Trong mô tả, khách **đã nêu những hiện tượng và yêu cầu nào**? |
| **3 — Độ rõ nghĩa** | Cách diễn đạt nào **cần hỏi rõ và ghi nhận lại**, không suy diễn? |
| **4 — Tính nhất quán** | Những thông tin nào **khác nhau và cần xác nhận**? |
| **5 — Chất lượng bàn giao** | Thông tin **đã thu thập** có được giữ đầy đủ trong phiếu bàn giao không? |

**Nội dung cần kiểm chứng tiếp**

- Mỗi vấn đề có thực sự xuất hiện trong quy trình tiếp nhận không?

- Tần suất và ảnh hưởng của từng vấn đề như thế nào?

- Biểu mẫu, ứng dụng hoặc quy trình hiện có đã xử lý đến đâu?

- Có thể thu thập tình huống mẫu và đo thời gian, chất lượng để đánh giá không?

## 3. Phase 2 — Ba Quick Problem Cards

### Card 1 — Scan #1: Phát hiện thông tin còn thiếu

**Người đề xuất:** Lưu Văn Việt Đức  

**Đơn vị:** VinFast — Dịch vụ hậu mãi  

**Bài toán Scan:** #1 — Mô tả hiện tượng thiếu thông tin cần thiết.

| Thành phần | Nội dung |
|---|---|
| **Bài toán — một câu** | Khi mô tả của khách chưa đủ thông tin, cố vấn dịch vụ cần xác định nội dung còn thiếu và trao đổi bổ sung trước khi hoàn thiện phiếu tiếp nhận. |
| **Actor** | Cố vấn dịch vụ tiếp nhận yêu cầu; khách hàng cung cấp thông tin. |
| **Workflow hiện tại — cần xác minh** | 1. Khách gửi mô tả → 2. Cố vấn đọc và kiểm tra → 3. Xác định thông tin thiếu → 4. Hỏi khách và ghi nhận bổ sung → 5. Hoàn thiện phiếu tiếp nhận. |
| **Bottleneck dự kiến** | Bước 3–4: xác định câu hỏi phù hợp và thu thập thông tin còn thiếu. **Thời gian/lượt: chưa đo.** |
| **Tác động cần kiểm chứng** | Tăng số lượt trao đổi và thời gian hoàn thiện phiếu; có thể vẫn bỏ sót thông tin sau khi hỏi. |
| **Điểm AI hỗ trợ** | Đối chiếu mô tả với checklist đã được người phụ trách nghiệp vụ xác nhận; liệt kê thông tin thiếu và đề xuất câu hỏi, tránh hỏi lại nội dung khách đã cung cấp. |
| **Metric đề xuất** | Trên bộ thử ít nhất **20 tình huống mô phỏng**: phát hiện đúng ít nhất **90%** mục thông tin thiếu theo đáp án chuẩn; giảm ít nhất **30%** thời gian thao tác chủ động để hoàn thiện phiếu, tính cả kiểm tra và chỉnh sửa, so với cách làm đối chứng. |
| **Quick Architecture** | **Workflow có LLM + Human Review.** Rule kiểm tra trường bắt buộc; LLM đọc nội dung tự do và đề xuất câu hỏi theo ngữ cảnh. |
| **Boundary & Fallback** | Không tự điền thông tin khách chưa cung cấp, không suy diễn nguyên nhân hỏng. Cố vấn duyệt câu hỏi; khi AI không xác định được, cố vấn trực tiếp hỏi và ghi nhận. |

**Ví dụ mô phỏng**

Khách: **“Điều hòa xe không mát.”**

Đầu ra mong muốn: ghi nhận đúng hiện tượng và đề xuất hỏi về thời điểm bắt đầu, tần suất, điều kiện xuất hiện theo checklist. Không kết luận **“xe thiếu gas”**.

**Future-State — phác thảo**

Khách gửi mô tả → AI đề xuất thông tin cần bổ sung → cố vấn duyệt câu hỏi → khách bổ sung → cố vấn xác nhận phiếu.

### Card 2 — Scan #2: Tách nhiều hiện tượng và yêu cầu

**Người đề xuất:** Lưu Văn Việt Đức  

**Đơn vị:** VinFast — Dịch vụ hậu mãi  

**Bài toán Scan:** #2 — Nhiều hiện tượng và yêu cầu nằm lẫn trong một đoạn mô tả.

| Thành phần | Nội dung |
|---|---|
| **Bài toán — một câu** | Khi khách trình bày nhiều hiện tượng và yêu cầu trong một đoạn dài, cố vấn dịch vụ cần tách từng nội dung để lập phiếu tiếp nhận đầy đủ, tránh bỏ sót hoặc gộp sai ý. |
| **Actor** | Cố vấn dịch vụ đọc và tổng hợp nội dung; nhân viên nhận bàn giao sử dụng phiếu. |
| **Workflow hiện tại — cần xác minh** | 1. Khách gửi mô tả → 2. Cố vấn đọc toàn bộ → 3. Tách các hiện tượng và yêu cầu → 4. Ghi từng nội dung vào phiếu → 5. Đối chiếu với mô tả gốc và xác nhận. |
| **Bottleneck dự kiến** | Bước 3–4: phân tách, tổng hợp và ghi lại nội dung. **Thời gian/lượt: chưa đo.** |
| **Tác động cần kiểm chứng** | Tốn công đọc lại; có nguy cơ bỏ sót yêu cầu hoặc gắn nhầm điều kiện xuất hiện với một hiện tượng khác. |
| **Điểm AI hỗ trợ** | Trích xuất danh sách hiện tượng và yêu cầu; giữ điều kiện xuất hiện đi cùng đúng hiện tượng; gắn mỗi mục với đoạn văn bản nguồn để người dùng kiểm tra. |
| **Metric đề xuất** | Trên bộ thử ít nhất **20 tình huống mô phỏng**: **Precision và Recall đều ≥95%** khi trích xuất các mục theo đáp án chuẩn; giảm ít nhất **30%** thời gian thao tác chủ động để lập và kiểm tra danh sách so với cách làm đối chứng. |
| **Quick Architecture** | **LLM Feature trong Workflow có Human Review.** Đầu ra có cấu trúc và trích đoạn nguồn; cố vấn xác nhận trước khi dùng. |
| **Boundary & Fallback** | Không biến hiện tượng thành chẩn đoán, không thêm yêu cầu sửa chữa. Nội dung mơ hồ phải đánh dấu cần xác nhận; cố vấn sửa trực tiếp nếu bản trích xuất sai. |

**Ví dụ mô phỏng**

Khách: **“Điều hòa lạnh yếu, bánh trước thỉnh thoảng kêu khi qua gờ, tiện kiểm tra giúp gạt mưa vì gạt không sạch.”**

Đầu ra mong muốn gồm **3 nội dung riêng**:

1. Điều hòa lạnh yếu.

2. Tiếng kêu ở bánh trước, thỉnh thoảng xuất hiện khi qua gờ.

3. Khách yêu cầu kiểm tra gạt mưa vì gạt không sạch.

Không tự kết luận bộ phận nào hỏng hoặc cần thay thế.

**Future-State — phác thảo**

Khách gửi mô tả → AI tách nội dung kèm đoạn nguồn → cố vấn đối chiếu và chỉnh sửa → xác nhận với khách khi cần → hoàn thiện phiếu.

### Card 3 — Scan #4: Phát hiện thông tin không nhất quán

**Người đề xuất:** Lưu Văn Việt Đức  

**Đơn vị:** VinFast — Dịch vụ hậu mãi  

**Bài toán Scan:** #4 — Thông tin cùng một trường không nhất quán giữa các phần của yêu cầu.

| Thành phần | Nội dung |
|---|---|
| **Bài toán — một câu** | Khi biểu mẫu và phần mô tả chứa các giá trị khác nhau cho cùng một thông tin, cố vấn dịch vụ cần phát hiện và xác nhận lại trước khi sử dụng để lập phiếu tiếp nhận. |
| **Actor** | Cố vấn dịch vụ kiểm tra thông tin; khách hàng xác nhận giá trị đúng. |
| **Workflow hiện tại — cần xác minh** | 1. Nhận biểu mẫu và mô tả → 2. Đối chiếu các thông tin liên quan → 3. Đánh dấu điểm khác biệt → 4. Hỏi khách xác nhận → 5. Cập nhật phiếu và lưu nội dung xác nhận. |
| **Bottleneck dự kiến** | Bước 2–3: tìm các giá trị cần so sánh và xác định khác biệt có thực sự cần hỏi lại không. **Thời gian/lượt: chưa đo.** |
| **Tác động cần kiểm chứng** | Có nguy cơ sử dụng sai thông tin hoặc phải chỉnh sửa phiếu sau khi bàn giao. |
| **Điểm hỗ trợ tự động hóa** | Trích xuất giá trị kèm nguồn và ngữ cảnh; so sánh theo từng trường; hiển thị điểm khác biệt và tạo câu hỏi xác nhận. |
| **Metric đề xuất** | Trên bộ thử ít nhất **20 tình huống mô phỏng**: phát hiện ít nhất **95%** trường hợp không nhất quán theo đáp án chuẩn; tỷ lệ cảnh báo nhầm **≤10%**; **0 trường hợp** tự chọn hoặc sửa giá trị khi chưa được xác nhận. |
| **Quick Architecture** | **Ưu tiên Rule; bổ sung LLM khi cần đọc mô tả tự do.** Rule so sánh dữ liệu đã chuẩn hóa; LLM hỗ trợ trích xuất ngữ cảnh và soạn câu hỏi. Cần so sánh với phương án chỉ dùng Rule để đánh giá giá trị tăng thêm. |
| **Boundary & Fallback** | Không tự xác định bên nào đúng, không ghi đè dữ liệu gốc. Không coi hai giá trị ở hai thời điểm khác nhau là mâu thuẫn một cách máy móc. Trường hợp chưa rõ chuyển cố vấn xác minh. |

**Ví dụ mô phỏng**

- Biểu mẫu: số kilomet hiện tại **12.000 km**.

- Mô tả: **“Xe hiện đi được 21.000 km.”**

Đầu ra mong muốn: hiển thị hai giá trị cùng nguồn và hỏi khách xác nhận số kilomet hiện tại. Không tự lấy giá trị lớn hơn hoặc giá trị trong biểu mẫu làm đáp án đúng.

**Future-State — phác thảo**

Nhận yêu cầu → hệ thống trích xuất và so sánh thông tin → cố vấn kiểm tra cảnh báo → khách xác nhận → cố vấn cập nhật phiếu, giữ dấu vết xác nhận.

## 4. Lựa chọn để phân tích sâu

Bài toán được lựa chọn: phát hiện thông tin còn thiếu trong mô tả

nhu cầu sửa chữa và hỗ trợ tạo bản nháp phiếu tiếp nhận.

### 4.1. Lý do chọn Card 1 / Scan #1

- **Phạm vi hẹp, đầu ra kiểm tra được:** Có thể bắt đầu với bốn nhóm thông tin: hiện tượng, thời điểm bắt đầu, tần suất và điều kiện xuất hiện. Mỗi nhận định cần có căn cứ từ đầu vào.
- **Có thể thử nghiệm bằng dữ liệu giả lập:** Đã chuẩn bị 20 tình huống để kiểm tra phát hiện thông tin thiếu, phân biệt chưa biết/không áp dụng, xử lý mâu thuẫn và chống yêu cầu vượt ranh giới.
- **Có phương án đối chứng rõ ràng:** So sánh LLM với biểu mẫu có hướng dẫn và Rule + checklist trên cùng dữ liệu; không mặc định LLM tốt hơn.
- **Quyền quyết định được giữ ở con người:** Cố vấn duyệt câu hỏi và phiếu; không cho mô hình chẩn đoán, báo giá, quyết định sửa chữa hoặc xác nhận lịch.
- **Có thể đo chất lượng và công sức:** Đo khả năng phát hiện thông tin thiếu cùng thời gian nhân viên đọc, hỏi, sửa và hoàn thiện phiếu.

### 4.2. Vì sao chưa chọn hai card còn lại để prototype?

| Card | Lý do chưa chọn trong vòng đầu |
|---|---|
| **Card 2 / Scan #2 — Tách nhiều nội dung** | Cần đáp án chi tiết ở mức từng hiện tượng, yêu cầu và điều kiện đi kèm. Phạm vi trích xuất nhiều mục làm việc đánh giá phức tạp hơn; có thể mở rộng sau khi kiểm chứng luồng một hiện tượng. |
| **Card 3 / Scan #4 — Tính nhất quán** | Nhiều tình huống so sánh giá trị đã có cấu trúc có thể giải quyết bằng Rule. Cần chứng minh phần đọc ngôn ngữ tự do tạo thêm giá trị trước khi chọn LLM. |

### 4.3. Ranh giới giữa ba card và prototype đã làm

Prototype hiện tập trung vào **Card 1**. Khả năng đánh dấu mâu thuẫn trong một số ca kiểm thử là ranh giới hỗ trợ cho việc hỏi lại, **chưa phải kiểm chứng toàn bộ Card 3** như đối chiếu kilomet từ nhiều nguồn. Prototype cũng chưa triển khai đầy đủ chức năng tách nhiều hiện tượng của Card 2.

Bộ 20 tình huống hiện có phục vụ Card 1. Các cỡ bộ thử và mục tiêu số trong Card 2–3 là đề xuất cho thử nghiệm riêng trong tương lai, không phải kết quả của bộ dữ liệu hiện tại.

## 5. Tài liệu liên quan

- [Báo cáo deep-dive, thiết kế prototype và đánh giá](02-deep-dive-report.md).
- [Nhật ký sử dụng AI và phản tư cá nhân](03-ai-log.md).
- [Mã nguồn prototype](starter-code/prompt_prototype.py).
- [Bộ dữ liệu giả lập và đáp án tham chiếu](vinfast_intake/README.md).
- [Worksheet hướng dẫn bài lab](01-worksheet.md).

**Lưu ý :** Các workflow và tác động trong file này là giả thuyết scoping, chưa được xác nhận bằng phỏng vấn hay quan sát nghiệp vụ. Nguồn công khai và giới hạn của bằng chứng được trình bày tại mục 1 của báo cáo deep-dive.
