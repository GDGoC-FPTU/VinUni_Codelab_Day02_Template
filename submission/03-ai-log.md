# 03 — Nhật ký tương tác AI & Reflection

> Lab 02 — AI Product Scoping (Vin Smart Future)

## 1. AI được dùng như thế nào?

Trong quá trình làm bài, tôi sử dụng AI như một **thought-partner** để:

- brainstorm các pain point có thể xuất hiện trong vận hành Vingroup;
- stress-test Problem Card;
- so sánh Rule-based, LLM Feature và Agentic Loop;
- kiểm tra xem metric, boundary và fallback có hợp lý hay chưa;
- gợi ý các adversarial input để kiểm tra ranh giới của prototype;
- phân biệt **thông tin có nguồn** với **giả định scoping**.

Tôi không dùng nội dung AI sinh ra như bằng chứng về tình hình vận hành thực tế của Vinhomes.

### Nguồn được dùng trong quá trình suy luận

- `01-worksheet.md`: yêu cầu và rubric của Lab.
- `02-deliverable-example.md`: ví dụ chuẩn để tham chiếu cấu trúc/độ sâu, không phải bằng chứng về Vinhomes.
- `03-inspiration-kit.md`: use case được đề xuất cho Vinhomes.
- **Vinhomes Annual Report 2024**: xác nhận bối cảnh và quy mô của Vinhomes Resident.
- **Vinhomes Investor Presentation 3Q2020**: bằng chứng lịch sử về “in-app support requests”.
- **Trang Vinhomes về Vinhomes Resident**: hỗ trợ nhận định rằng ứng dụng đóng vai trò kết nối cư dân với Ban Quản lý và các bộ phận vận hành.

---

## 2. AI đã giúp gì?

AI đặc biệt hữu ích khi phản biện assumption và ép problem statement phải cụ thể hơn.

Ví dụ, ban đầu có thể dễ rơi vào mô tả chung chung như:

> “Dùng AI để tự động hóa việc xử lý khiếu nại cư dân.”

Qua quá trình stress-test, bài toán được thu hẹp thành:

> **Phân loại intent + trích xuất thông tin + đề xuất queue + soạn draft, với HITL bắt buộc cho case nhạy cảm hoặc không chắc chắn.**

AI cũng giúp chỉ ra rằng Agentic Loop không cần thiết khi workflow đã tương đối cố định.

### Giá trị của nguồn bên ngoài

Việc kiểm tra nguồn công khai giúp xác nhận rằng **Vinhomes Resident thực sự là một nền tảng cư dân quy mô lớn**, thay vì chỉ giả định đây là một app tồn tại trong bối cảnh bài lab. Vinhomes báo cáo khoảng 130.000 tài khoản trong Annual Report 2024; một tài liệu trước đó ghi nhận hơn 22.000 yêu cầu hỗ trợ trong ứng dụng. Những dữ liệu này giúp củng cố **bối cảnh**, nhưng không cung cấp baseline 2026 cho bài toán triage được đề xuất. Vì vậy tôi không dùng chúng để suy ra thời gian xử lý hay routing accuracy.

---

## 3. AI có thể sai hoặc gây hiểu nhầm ở đâu?

### Vấn đề 1 — Con số vận hành

AI có thể dễ dàng đề xuất các số liệu trông rất hợp lý như:

- 6–8 phút/ticket;
- 95% routing accuracy;
- 20–30% ticket cần re-route.

Những con số này **không có trong bộ tài liệu được cung cấp và cũng không xuất hiện trong các nguồn công khai tôi sử dụng cho case này**. Vì vậy tôi không coi chúng là facts.

Tôi chuyển chúng thành **[GIẢ ĐỊNH]** hoặc **target metric**, đồng thời ghi rõ rằng phải thay bằng dữ liệu thực tế trước pilot.

### Vấn đề 2 — Đồng nhất “AI có thể làm” với “AI được phép làm”

AI có thể đề xuất tự động gửi phản hồi hoặc xử lý trực tiếp ticket, nhưng điều đó không phù hợp với operational boundary của bài toán.

Vì vậy phạm vi được giới hạn thành:

- classify;
- extract;
- recommend;
- draft.

Các quyết định có tác động đáng kể vẫn thuộc về con người.

### Vấn đề 3 — Bị cuốn theo worked example

Worked Example của Lab rất hữu ích để hiểu tiêu chuẩn output, nhưng nếu sao chép gần nguyên ví dụ Xanh SM thì bài làm không còn thể hiện quá trình scoping độc lập.

Do đó tôi dùng một use case khác có trong Inspiration Kit: **Vinhomes — Phân loại & Điều hướng phản ánh cư dân**.

---

## 4. Tôi đã sửa gì sau khi review output của AI?

### Thay đổi A — Metric

Thay vì trình bày KPI như một sự thật đã được xác minh, tôi tách thành:

- **target metric:** thành công nên được đo bằng gì;
- **baseline assumption:** con số tạm dùng trong scope/prototype;
- **evidence requirement:** dữ liệu cần đo trước production/pilot.

### Thay đổi B — Kiến trúc

Tôi loại bỏ ý tưởng Agent tự trị vì workflow đã có cấu trúc tương đối rõ.

Kiến trúc cuối cùng là:

> **Rule / policy checks + LLM Feature + HITL + manual fallback**

### Thay đổi C — Operational Boundary

Tôi xác định rõ AI không được:

- tự phê duyệt khoản phí;
- đưa ra kết luận pháp lý;
- thay đổi dữ liệu cư dân;
- tự gửi thông điệp ra bên ngoài.

Case nhạy cảm hoặc confidence thấp phải quay về hàng đợi xử lý thủ công/HITL.

### Thay đổi D — Gắn nhãn mức độ bằng chứng

Tôi bổ sung ba trạng thái vào các tài liệu:

- **Nguồn xác nhận:** có tài liệu chính thức hỗ trợ.
- **Mô hình scoping:** nhóm đề xuất để mô tả workflow/solution.
- **[GIẢ ĐỊNH]:** số liệu hoặc giả thuyết chưa được xác minh.

Điều này giúp tránh việc một con số được AI đề xuất vô tình trở thành “fact” trong bài nộp.

---

## 5. Reflection

Bài học lớn nhất là AI hữu ích khi đóng vai trò **mở rộng và stress-test tư duy**, nhưng không nên được xem là nguồn bằng chứng về cách một doanh nghiệp thực tế đang vận hành.

Giá trị lớn nhất của quá trình AI-assisted nằm ở việc phát hiện khoảng trống:

> **“Điều gì thực sự được hỗ trợ bởi tài liệu nguồn, và điều gì chỉ là giả định của chúng ta?”**

Đối với bài lab này, kiểm tra nguồn còn cho thấy một điểm quan trọng: có thể chứng minh **bối cảnh và sự tồn tại của kênh Vinhomes Resident**, nhưng không thể từ đó suy ra workflow triage hiện tại hoặc KPI 2026. Vì vậy quyết định cuối cùng **NOT YET** trong Deep-Dive phản ánh đúng mức độ bằng chứng hiện có.

---

## 6. Trạng thái prototype

File Python đi kèm được chuẩn bị để kiểm tra:

- system prompt nghiêm ngặt;
- structured JSON output;
- operational boundary;
- các adversarial input.

Việc chạy thử Gemini thực tế yêu cầu có `GEMINI_API_KEY`. Khi chưa có key, tôi **không ghi nhận một kết quả giả là kết quả chạy thật**.

---

# Danh mục nguồn tham chiếu

1. **Nguồn nội bộ Lab — `01-worksheet.md`**: quy trình Lab và yêu cầu reflection.
2. **Nguồn nội bộ Lab — `02-deliverable-example.md`**: worked example để tham chiếu chất lượng, không phải bằng chứng cho Vinhomes case.
3. **Nguồn nội bộ Lab — `03-inspiration-kit.md`**: use case Vinhomes và nguyên tắc Problem First, AI Second.
4. **Vinhomes Annual Report 2024**: thông tin quy mô Vinhomes Resident. https://gcp-cdn.vinhomes.vn/cms-data/VIE_Vinhomes%20AR%202024_250411_compressed.pdf
5. **Vinhomes Investor Presentation 3Q2020**: hơn 22.000 in-app support requests trong giai đoạn được báo cáo. https://gcp-cdn.vinhomes.vn/cms-data/2020-10-29-VHM-3Q20-Earnings-Presensentation-vUP.pdf
6. **Vinhomes — “Những lá thư cảm ơn…”**: vai trò kết nối cư dân với Ban Quản lý và các nhóm vận hành. https://vinhomes.vn/vi/nhung-la-thu-cam-on-tu-cu-dan-va-dich-vu-tu-trai-tim-vinhomes
