# Lab 02 — Problem Scan & Quick Assess

## Vin Smart Future — Use Case Xanh SM

**Vai trò:** AI Product Engineer, Vin Smart Future
**Doanh nghiệp được lựa chọn:** Xanh SM (GSM)
**Vấn đề được chọn để phân tích sâu:** AI hỗ trợ xử lý các sự cố về pin/sạc xe điện ngoài hiện trường

> **Lưu ý về dữ liệu:** Các số liệu vận hành được đánh dấu là giả định chỉ là các giả thuyết phục vụ việc xác định phạm vi bài toán và cần được kiểm chứng bằng log vận hành thực tế của GSM trước khi đưa vào production.

---

# Phase 1 — SCAN

Sử dụng bốn góc nhìn (lenses) trong worksheet, các cơ hội vận hành sau đây đã được xác định.

| # | Công ty  | Lens             | Vấn đề / Điểm nghẽn                                                                                                                        |
| - | -------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | Xanh SM  | Repetitive       | Định tuyến lại hoặc phân công lại chuyến taxi khi tài xế báo thay đổi địa điểm đón hoặc điều kiện tuyến đường.                             |
| 2 | Xanh SM  | Time-consuming   | Điều phối viên (dispatcher) phải xử lý thủ công các sự cố khẩn cấp liên quan đến pin/sạc xe điện do tài xế báo cáo ngoài hiện trường.      |
| 3 | VinFast  | Repetitive       | Đối soát thủ công dữ liệu phiên sạc từ các nhà cung cấp trạm sạc đối tác với dữ liệu thanh toán.                                           |
| 4 | Vinhomes | AI-upgrade       | Khiếu nại của cư dân được phân loại và chuyển đến đội ngũ quản lý tòa nhà phù hợp một cách thủ công.                                       |
| 5 | VinFast  | AI-upgrade       | Khách hàng mô tả các vấn đề của xe bằng ngôn ngữ tiếng Việt tự nhiên, khiến nhân viên phải xác định danh mục sự cố kỹ thuật ban đầu.       |
| 6 | Xanh SM  | Stakeholder Pain | Nhân viên phải xem xét thủ công các cuộc gọi hủy chuyến và ghi chú của tài xế để xác định các nguyên nhân lặp lại dẫn đến việc hủy chuyến. |

## Ưu tiên ban đầu

Vấn đề **#2** được lựa chọn là ứng viên mạnh nhất vì nó kết hợp:

* Một điểm nghẽn vận hành rõ ràng.
* Một quy trình có tính lặp lại.
* Một mục tiêu rõ ràng và có thể đo lường về thời gian xử lý.
* Một use case LLM tự nhiên cho việc soạn thảo tin nhắn cho dispatcher.
* Một quy tắc an toàn mang tính xác định (deterministic) cho các tình huống pin ở mức nghiêm trọng.
* Một điểm kiểm soát rõ ràng theo mô hình **Human-in-the-loop**.
* Có phương án fallback an toàn về quy trình xử lý thủ công hiện tại.

---

# Phase 2 — QUICK-ASSESS

## Quick Problem Card #1 — Xanh SM: Hỗ trợ xử lý sự cố pin xe điện

### Vấn đề

Các tài xế báo tình trạng pin yếu hoặc sự cố sạc cần dispatcher phải tự thu thập thông tin về xe, kiểm tra các lựa chọn trạm sạc gần đó và chuẩn bị hướng dẫn xử lý.

### Công ty

**Xanh SM (GSM)**

### Actor

* Dispatcher của Xanh SM
* Tài xế với vai trò là người vận hành ngoài hiện trường đang gặp sự cố

### Quy trình thủ công hiện tại

1. Tài xế báo cáo sự cố pin/sạc.
2. Dispatcher kiểm tra thông tin nhận dạng xe và vị trí.
3. Dispatcher kiểm tra các lựa chọn trạm sạc gần đó.
4. Dispatcher kiểm tra mức độ nghiêm trọng của tình trạng pin và chuẩn bị hướng dẫn.
5. Dispatcher gửi phản hồi hoặc thực hiện escalation.

### Điểm nghẽn chính

Bước 3–4 được dự kiến là phần tiêu tốn nhiều thời gian nhất của dispatcher.

**Giả định để xác định phạm vi:** khoảng **10 phút trong tổng số 15 phút xử lý** được dành cho việc tra cứu thông tin và chuẩn bị phản hồi. Điều này phải được kiểm chứng bằng log sự cố thực tế.

### Điểm AI tham gia

* **LLM:** tóm tắt sự cố và soạn thảo phản hồi ngắn gọn.
* **Rule engine:** thực thi các ràng buộc an toàn, chẳng hạn như ngưỡng pin ở mức nghiêm trọng.
* **API/hệ thống vận hành hiện có:** cung cấp dữ liệu đáng tin cậy về xe, vị trí và trạm sạc.

### Các chỉ số thành công

1. Giảm thời gian xử lý trung bình từ mức giả định **15 phút xuống dưới 3 phút**.
2. Đảm bảo **100% trường hợp pin ở mức nghiêm trọng tuân thủ quy tắc an toàn đã xác định** trong tập dữ liệu kiểm thử prototype.
3. Mục tiêu **≥98% hoàn thiện hợp lệ các trường dữ liệu của bản nháp (draft-field completion)** trên một tập đánh giá được kiểm soát.

### Kiến trúc sơ bộ

**Tính năng Rule + LLM**

Quyết định liên quan đến an toàn không nên chỉ phụ thuộc vào LLM. Các rule mang tính xác định nên xử lý các ngưỡng quan trọng, trong khi LLM được sử dụng để hiểu ngôn ngữ và soạn thảo phản hồi.

---

## Quick Problem Card #2 — Vinhomes: Định tuyến khiếu nại của cư dân

### Vấn đề

Các khiếu nại của cư dân như đèn bị hỏng, vấn đề về nước, tiếng ồn hoặc sự cố cơ sở vật chất được phân loại và chuyển đến đội ngũ quản lý tòa nhà phù hợp một cách thủ công.

### Công ty

**Vinhomes**

### Actor

* Nhân viên chăm sóc khách hàng (Customer-service agent)
* Nhân viên quản lý tòa nhà

### Quy trình hiện tại

1. Cư dân gửi khiếu nại.
2. Nhân viên CS đọc nội dung.
3. Nhân viên xác định danh mục và mức độ ưu tiên.
4. Nhân viên tìm đội ngũ chịu trách nhiệm.
5. Nhân viên chuyển ticket.

### Điểm nghẽn chính

Đọc thủ công, phân loại và định tuyến.

**Giả định để xác định phạm vi:** 5–8 phút cho mỗi ticket tùy theo độ phức tạp.

### Điểm AI tham gia

LLM thực hiện phân loại và trích xuất thông tin.

### Các chỉ số thành công

* Giảm ít nhất **60% thời gian phân loại thủ công**.
* Đạt **≥95% độ chính xác phân loại** trên tập dữ liệu kiểm thử đã được gán nhãn.
* **100% trường hợp có độ tin cậy thấp được chuyển sang con người kiểm tra.**

### Kiến trúc sơ bộ

**Tính năng LLM + định tuyến dựa trên rule**

---

## Quick Problem Card #3 — VinFast: Phân loại vấn đề xe do khách hàng báo cáo

### Vấn đề

Khách hàng mô tả các vấn đề của xe bằng ngôn ngữ tiếng Việt không chính thức, khiến nhân viên phải tự diễn giải mô tả và gán một danh mục sự cố ban đầu.

### Công ty

**VinFast**

### Actor

* Nhân viên chăm sóc khách hàng
* Cố vấn dịch vụ kỹ thuật

### Quy trình hiện tại

1. Khách hàng báo cáo vấn đề của xe.
2. Nhân viên đọc mô tả bằng ngôn ngữ tự nhiên.
3. Nhân viên đặt các câu hỏi bổ sung.
4. Nhân viên gán danh mục sự cố ban đầu.
5. Nhân viên chuyển case đến đội ngũ kỹ thuật phù hợp.

### Điểm nghẽn chính

Hiểu các mô tả tiếng Việt không chính thức, không đầy đủ và có tính mơ hồ.

### Điểm AI tham gia

LLM dùng để trích xuất thông tin và phân loại ban đầu.

### Các chỉ số thành công

* Giảm thời gian phân loại ban đầu từ mức giả định **8 phút xuống dưới 2 phút**.
* Đạt **≥95% độ chính xác phân loại** trên tập dữ liệu đã được gán nhãn.
* Yêu cầu con người kiểm tra đối với **tất cả các trường hợp liên quan đến an toàn hoặc có độ tin cậy thấp**.

### Kiến trúc sơ bộ

**Tính năng LLM**

---

# Lựa chọn của nhóm

## Vấn đề được lựa chọn

**Xanh SM — AI hỗ trợ xử lý các sự cố pin/sạc xe điện ngoài hiện trường**

### Tại sao vấn đề này được lựa chọn

1. Quy trình hiện tại có một điểm nghẽn vận hành rõ ràng.
2. Vấn đề xảy ra lặp lại và do đó có thể tạo ra các lợi ích hiệu suất có thể đo lường.
3. Vai trò của AI có thể được giới hạn trong việc tổng hợp thông tin và tạo bản nháp phản hồi.
4. Các quyết định liên quan đến an toàn có thể tiếp tục được xử lý bằng rule xác định và có sự kiểm soát của con người.
5. Quy trình thủ công hiện tại cung cấp một phương án fallback thực tế.
6. Vấn đề đã có prototype prompt kỹ thuật và các bài kiểm thử adversarial.

### Tại sao hai vấn đề còn lại không được lựa chọn

**Vinhomes — Định tuyến khiếu nại:** có giá trị và khả thi, nhưng chủ yếu là bài toán phân loại/định tuyến và ít liên quan trực tiếp hơn đến prototype an toàn dành cho dispatcher mà nhóm đã có.

**VinFast — Phân loại vấn đề xe:** có tiềm năng mang lại giá trị, nhưng các tác động về kỹ thuật và an toàn đòi hỏi một knowledge base đã được kiểm chứng lớn hơn cùng với quá trình review kỹ thuật chuyên sâu hơn trước khi triển khai.

---

# Nguyên tắc xác định phạm vi

Dự án **không nhằm mục đích tạo ra một dispatcher tự động (autonomous dispatcher).**

AI nên:

* hiểu nội dung sự cố;
* sử dụng dữ liệu vận hành đáng tin cậy được cung cấp bởi các hệ thống hiện có;
* áp dụng các quy tắc an toàn mang tính xác định;
* chuẩn bị bản nháp phản hồi;
* yêu cầu con người phê duyệt trước khi thực hiện bất kỳ giao tiếp bên ngoài hoặc hành động vận hành nào.

AI **không được**:

* tự ý gửi tin nhắn;
* tự điều phối xe;
* tuyên bố rằng một hành động đã được thực hiện;
* tự tạo hoặc bịa ra thông tin vận hành.
