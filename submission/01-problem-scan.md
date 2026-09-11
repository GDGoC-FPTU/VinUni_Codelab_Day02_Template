# 01 — Quét bài toán & Thẻ bài toán nhanh

> Lab 02 — AI Product Scoping (Vin Smart Future)
>
> **Giả định làm việc:** Đây là bản nộp cá nhân dự kiến để nhóm review. Các con số vận hành có nhãn **[GIẢ ĐỊNH]** là giả thuyết phục vụ scoping và phải được thay thế bằng dữ liệu quan sát/log trước khi đưa ra quyết định triển khai thực tế.
>
> **Nguyên tắc bằng chứng:** Các ý tưởng bài toán được lấy từ worksheet/Inspiration Kit của Lab; thông tin về hệ sinh thái Vinhomes Resident được đối chiếu thêm với tài liệu công khai chính thức của Vinhomes. Những điểm chưa có số liệu nội bộ được ghi rõ là giả định hoặc mục tiêu đo lường.

---

## Phase 1 — SCAN

| # | Công ty thành viên | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | **Vinhomes** | Lặp lại | Tự động phân loại phản ánh/khiếu nại từ App Vinhomes Resident và chuyển đúng ban/tòa nhà phụ trách. |
| 2 | **VinFast** | AI có thể tốt hơn | Phân loại mô tả lỗi xe bằng tiếng Việt thành nhóm lỗi kỹ thuật ban đầu để hỗ trợ kỹ sư/CSKH. |
| 3 | **VinFast** | Lặp lại | Đối chiếu dữ liệu sạc điện từ nhiều trạm/đối tác với hóa đơn tài chính hằng tuần. |
| 4 | **Vinmec** | Tốn thời gian | Soạn thảo tóm tắt hồ sơ xuất viện từ bệnh án điện tử, kết quả xét nghiệm và ghi chú bác sĩ. |
| 5 | **VinUni** | Lặp lại | Phân tích lỗi code của bài lab và soạn thảo phản hồi sư phạm cho sinh viên sau khi autograder phát hiện lỗi. |

### Cơ sở lựa chọn ý tưởng

Các bài toán trên được chọn dựa trên **4 Lenses** trong worksheet và các use case có sẵn trong **Inspiration Kit**. Inspiration Kit nhấn mạnh nguyên tắc **“Problem First, AI Second”** và yêu cầu ranh giới vận hành nghiêm ngặt ở các miền nhạy cảm như y tế và an toàn xe. [Nguồn nội bộ Lab: `01-worksheet.md`, Phase 1; `03-inspiration-kit.md`, mục “Lưu ý khi chọn bài toán”.]

Bài toán Vinhomes được ưu tiên vì chính Inspiration Kit nêu rõ use case **“Phân loại & Điều hướng phản ánh cư dân”**: tự động phân loại các khiếu nại như mất nước, hỏng đèn, ồn ào và đưa đến đúng ban quản lý/tòa nhà. [Nguồn nội bộ Lab: `03-inspiration-kit.md`, mục 2 — Vinhomes & Vinpearl.]

### Bằng chứng công khai hỗ trợ bối cảnh

Vinhomes công bố Vinhomes Resident là một nền tảng phục vụ nhu cầu cư dân và cung cấp nhiều dịch vụ số. Báo cáo thường niên 2024 của Vinhomes cho biết ứng dụng có khoảng **130.000 tài khoản**, hơn **86% số căn hộ** đã sử dụng và tỷ lệ hoạt động hàng tháng lên tới **97%**. Đây là bằng chứng cho thấy Vinhomes Resident là một kênh vận hành có quy mô đáng kể; các số liệu này **không phải dữ liệu nội bộ hiện tại của bài lab** và không được dùng để suy ra volume ticket 2026. [Nguồn: Vinhomes Annual Report 2024.]

Một tài liệu công bố trước đó của Vinhomes cũng ghi nhận **hơn 22.000 yêu cầu hỗ trợ trong ứng dụng** trong giai đoạn được báo cáo. Con số này chỉ được dùng để chứng minh rằng “support requests” là một dạng tương tác đã từng tồn tại trên kênh ứng dụng; không dùng làm baseline hiện tại. [Nguồn: Vinhomes Investor Presentation 3Q2020.]

---

# Phase 2 — QUICK-ASSESS

## Thẻ bài toán nhanh #1 — Vinhomes: Phân loại & Điều hướng phản ánh cư dân

**Bài toán (1 câu):** Phản ánh của cư dân gửi qua App cần được phân loại và chuyển đúng nhóm/bộ phận xử lý nhanh hơn, thay vì CSKH phải đọc và điều hướng thủ công.

**Công ty thành viên:** Vinhomes

**Ai đang gặp vấn đề (Actor):**
- CSKH/điều phối viên tiếp nhận phản ánh.
- Ban quản lý tòa nhà nhận ticket sai nhóm hoặc thiếu thông tin.
- Cư dân phải chờ lâu nếu ticket bị chuyển vòng.

**Quy trình hiện tại (mô hình hóa để scoping, chưa phải workflow nội bộ đã xác minh):**
1. Cư dân gửi phản ánh qua App.
2. CSKH đọc nội dung.
3. CSKH xác định loại vấn đề.
4. CSKH xác định tòa nhà/nhóm phụ trách.
5. CSKH chuyển ticket và soạn phản hồi ban đầu.

**Bước tốn thời gian/lỗi nhất:** Bước 3–4 — phân loại + điều hướng.
- **[GIẢ ĐỊNH]** 4–6 phút/ticket trong baseline giả định.
- **[GIẢ ĐỊNH]** 20–30% ticket có nguy cơ cần điều hướng lại do thiếu thông tin hoặc phân loại không thống nhất.

**AI có thể hỗ trợ ở:** Bước 3–5.
- Phân loại intent/category.
- Trích xuất thông tin chính.
- Đề xuất nhóm nhận ticket.
- Soạn thảo phản hồi ban đầu.

**Chỉ số thành công đề xuất:**
- Giảm median thời gian triage từ **[GIẢ ĐỊNH] 6 phút → <2 phút/ticket**.
- Đạt **≥95% độ chính xác điều hướng** trên tập test đã có nhãn.
- **100%** ticket thuộc nhóm nhạy cảm (pháp lý, thanh toán, tranh chấp) phải qua HITL.

**Kiến trúc nhanh:** **Tính năng LLM + routing dựa trên Rule**

> **Nguồn/độ tin cậy:** Use case được nêu trực tiếp trong Inspiration Kit; kênh Vinhomes Resident được Vinhomes xác nhận là nền tảng phục vụ cư dân. Workflow, thời gian và accuracy target trong card là **thiết kế scoping của nhóm**, không phải số liệu Vinhomes đã công bố. [Nguồn: `03-inspiration-kit.md`; Vinhomes Annual Report 2024.]

---

## Thẻ bài toán nhanh #2 — VinFast: Phân loại lỗi xe từ mô tả tiếng Việt

**Bài toán (1 câu):** Khách hàng mô tả triệu chứng xe bằng ngôn ngữ tự nhiên; hệ thống hỗ trợ phân loại nhóm lỗi kỹ thuật ban đầu cho CSKH/kỹ sư.

**Công ty thành viên:** VinFast

**Ai đang gặp vấn đề (Actor):** CSKH, kỹ thuật viên tiếp nhận yêu cầu.

**Quy trình hiện tại (mô hình hóa):**
1. Khách mô tả triệu chứng.
2. Nhân viên đọc/chuyển ngữ nếu cần.
3. Tìm mã lỗi/nhóm lỗi gần nhất trong tài liệu.
4. Ghi ticket.
5. Chuyển kỹ thuật viên.

**Bottleneck:** Bước 3 — tra cứu và chuẩn hóa mô tả.

**Chỉ số đề xuất:**
- **[GIẢ ĐỊNH]** giảm thời gian triage từ 8 → <3 phút.
- Top-3 technical category recall ≥90% trên tập đánh giá nội bộ.

**Ranh giới vận hành:** AI chỉ phân loại/soạn thảo; không được đưa ra chẩn đoán an toàn hoặc yêu cầu người dùng tự sửa hệ thống điện/ắc quy.

**Kiến trúc nhanh:** **Tính năng LLM + retrieval/rules**

> **Nguồn:** Use case này có trong Inspiration Kit. Quy trình, target metric và safety boundary là thiết kế scoping của nhóm, chưa phải quy trình kỹ thuật đã được xác minh từ VinFast. [Nguồn nội bộ Lab: `03-inspiration-kit.md`.]

---

## Thẻ bài toán nhanh #3 — VinUni: Phân tích lỗi code và soạn phản hồi lab

**Bài toán (1 câu):** Sau khi autograder phát hiện lỗi, hệ thống dùng LLM để soạn thảo phản hồi sư phạm thay vì giảng viên phải viết lại các lỗi tương tự.

**Công ty thành viên:** VinUni

**Ai đang gặp vấn đề (Actor):** Trợ giảng / giảng viên.

**Quy trình hiện tại (mô hình hóa):**
1. Autograder chạy test.
2. Trợ giảng đọc output/log.
3. Trợ giảng xác định loại lỗi.
4. Trợ giảng viết phản hồi.
5. Sinh viên nhận phản hồi.

**Bottleneck:** Bước 3–4, đặc biệt với lỗi lặp lại.

**Chỉ số đề xuất:**
- **[GIẢ ĐỊNH]** giảm thời gian viết phản hồi từ 5 → <1,5 phút/bài.
- ≥90% feedback đạt checklist chất lượng nội bộ.

**Ranh giới vận hành:** AI không được thay điểm, không được đưa đáp án hoàn chỉnh cho bài đang đánh giá, và phải giữ nguyên bằng chứng từ autograder.

**Kiến trúc nhanh:** **Tính năng LLM**

> **Nguồn:** Use case này có trong Inspiration Kit. Quy trình, target metric và boundary là thiết kế scoping của nhóm. [Nguồn nội bộ Lab: `03-inspiration-kit.md`.]

---

# Danh sách rút gọn đề xuất

| Card | Giá trị | Rủi ro | Độ phù hợp với AI | Nhận xét |
|---|---|---|---|---|
| #1 Vinhomes routing | Cao | Thấp–Trung bình | Cao | Scope rõ, HITL dễ thiết kế, metric đo được |
| #2 VinFast symptom classification | Cao | Cao | Trung bình–Cao | Giá trị tốt nhưng safety boundary nghiêm ngặt |
| #3 VinUni lab feedback | Trung bình | Thấp | Cao | Dễ prototype, nhưng business impact nhỏ hơn |

**Đề xuất chọn Card #1 — Vinhomes Phân loại & Điều hướng phản ánh cư dân** để thực hiện Deep-Dive.

### Lý do

1. Bài toán là workflow có cấu trúc, nên không cần Agent tự trị.
2. AI có thể tạo giá trị ở classification/extraction/drafting, nhưng quyết định cuối vẫn do con người.
3. Có thể thiết kế fallback rõ ràng theo rule-based hoặc xử lý thủ công.
4. Rủi ro thấp hơn so với use case y tế hoặc an toàn xe.
5. Có thể prototype hoàn toàn bằng structured output mà chưa cần tích hợp hệ thống production.

> **Lưu ý:** Bộ tài liệu lab không có dữ liệu nội bộ của Vinhomes. Vì vậy các thời gian, volume và accuracy nêu trên là **giả thuyết/baseline giả định hoặc target metric**, không phải số liệu thực tế đã xác minh.

---

# Danh mục nguồn tham chiếu

1. **Nguồn nội bộ Lab — `01-worksheet.md`**: 4 Lenses, Quick Problem Card, tiêu chí Deep-Dive, AI Fit, HITL và Fallback.
2. **Nguồn nội bộ Lab — `03-inspiration-kit.md`**: danh sách use case Vinhomes/VinFast/Vinmec/VinUni và use case “Phân loại & Điều hướng phản ánh cư dân”.
3. **Vinhomes Annual Report 2024**: thông tin về quy mô sử dụng Vinhomes Resident (khoảng 130.000 tài khoản; >86% căn hộ sử dụng; ~97% active monthly). https://gcp-cdn.vinhomes.vn/cms-data/VIE_Vinhomes%20AR%202024_250411_compressed.pdf
4. **Vinhomes Investor Presentation 3Q2020**: ghi nhận hơn 22.000 in-app support requests trong giai đoạn được báo cáo. https://gcp-cdn.vinhomes.vn/cms-data/2020-10-29-VHM-3Q20-Earnings-Presensentation-vUP.pdf
5. **Vinhomes — “Những lá thư cảm ơn…”**: mô tả Vinhomes Resident như cầu nối giữa cư dân và Ban Quản lý, đồng thời nêu các nhóm vận hành như CSKH, Kỹ thuật, An ninh, House Keeping. https://vinhomes.vn/vi/nhung-la-thu-cam-on-tu-cu-dan-va-dich-vu-tu-trai-tim-vinhomes
