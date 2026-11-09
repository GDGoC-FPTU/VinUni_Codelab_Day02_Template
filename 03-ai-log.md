# Nhật ký sử dụng AI

## 1. Mục tiêu và phương pháp ban đầu

- **Mục tiêu:** tìm các cơ hội cải thiện vận hành cho Xanh SM/Green SM và thu hẹp thành một hướng MVP có thể đo lường.
- **Phương pháp:** dùng **ChatGPT Web**, bắt đầu từ mẹo brainstorming trong worksheet để mở rộng nhiều hướng, bật chế độ **high reasoning**, và dùng **web search** để kiểm tra các tính năng hiện có cùng tài liệu nghiên cứu liên quan.
- **Prompt worksheet (nguyên văn):** “Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất.”

## 2. Đóng góp hữu ích của AI

AI giúp tạo và sắp xếp năm cơ hội tiềm năng, sau đó được chỉnh lại để khớp với bản problem scan cuối:

1. **Copilot escalation hỗ trợ khách hàng:** soạn nháp xử lý các ca thất lạc đồ, sai giá và sự cố chuyến; người phụ trách duyệt trước khi gửi.
2. **Đối soát và xử lý ngoại lệ:** phát hiện, giải thích sai lệch về giá, khuyến mãi, thưởng, hoàn tiền và thu nhập tài xế; rule engine vẫn quyết định tiền cuối cùng.
3. **Kiểm tra ảnh bàn giao ca:** kiểm tra ảnh hư hỏng và chất lượng ảnh, chuyển ca nghi vấn cho giám sát.
4. **Triage bảo dưỡng:** ưu tiên sự cố và gợi ý xưởng/lịch dựa trên mô tả lỗi và lịch sử bảo dưỡng; không chẩn đoán an toàn hay phê duyệt sửa chữa.
5. **Điều phối sạc cấp đội xe:** lập lịch theo nhu cầu, pin, hàng đợi và công suất trạm; điều phối viên duyệt thay đổi, không xây lại tính năng V-App hiện có.

AI ban đầu cũng đề xuất dispatch/dự báo nhu cầu; đây là **hướng đã loại bỏ** khỏi năm cơ hội cuối vì bản scan ưu tiên các pain point cụ thể hơn, không phải kết luận đã được xác nhận.

Các **chỉ số ứng viên (giả thuyết để thử nghiệm)** gồm: thời gian xử lý escalation, tỷ lệ chuyển đúng người, số ngoại lệ/chuyến và thời gian đóng ngoại lệ, tỷ lệ ảnh đạt/ca và tỷ lệ phát hiện đúng, thời gian triage và downtime, thời gian chờ sạc và tỷ lệ sẵn sàng đội xe. Đây là hypothesis do AI đề xuất, không phải số liệu công bố.

Một hướng MVP khả thi là **đối soát có xử lý ngoại lệ**: tự động ghép dữ liệu chuyến–doanh thu–thời gian hoạt động, gắn cờ sai lệch (thiếu chuyến, trùng chuyến, doanh thu bất thường hoặc trạng thái không khớp), rồi đưa các trường hợp cần người duyệt vào hàng đợi.

## 3. Điều chỉnh sau kiểm chứng

- Các con số theo năm trong bản scan chỉ là **ước tính theo giả định**, chẳng hạn 100.000 chuyến/ngày, 10.000 xe, 80.000 VND/giờ lao động và 30.000 VND/giờ đóng góp. Chúng **không phải** số liệu đã xác nhận về tổn thất hay khoản tiết kiệm của Green SM.
- **Ví dụ claim sai/không được hỗ trợ:** AI từng viết rằng Green SM “mất hàng tỷ đồng mỗi năm do điều phối sạc thủ công” và đề xuất xây lại chức năng đặt lịch sạc. Không có nguồn công khai nào trong lần kiểm tra chứng minh con số hoặc nhân quả đó. Tôi đã đối chiếu nguồn chính thức, gắn nhãn con số là giả định pilot, thêm ràng buộc “không khẳng định tổn thất Green SM”, và sửa prompt thành yêu cầu phân biệt fact/source với hypothesis, không trùng tính năng hiện có và phải có human approval.
- Nguồn chính thức của **Green SM (Khối Đồng hành & Phát triển Bác Tài Xanh)** xác nhận V-App có gợi ý lộ trình sạc/danh sách phiên sạc [Green SM V-App](https://www.greensm.com/vn-vi/news/ra-mat-tinh-nang-moi-goi-y-lo-trinh-sac-va-danh-sach-phien-sac-tren-ung-dung-v-app?utm_source=chatgpt.com), và có đặt lịch bảo dưỡng trực tuyến [Green SM Driver](https://www.greensm.com/vn-vi/news/huong-dan-dat-lich-bao-duong-sua-chua-xe-qua-ung-dung-green-sm-driver-1?utm_source=chatgpt.com). Vì vậy, phạm vi được điều chỉnh sang **tối ưu cấp đội xe và xử lý ngoại lệ**, không xây lại các tính năng đó.
- Bài [*Coordinated vehicle dispatching and charging scheduling for an electric ride-hailing fleet under charging congestion and dynamic prices* — Tai-Yu Ma, Richard Connors, Francesco Viti (2024)](https://orbilu.uni.lu/handle/10993/63841) hỗ trợ hypothesis rằng điều phối sạc có thể xét nhu cầu, hàng đợi và giá động; kết quả nghiên cứu không phải bằng chứng về Green SM. Bài [*Generative AI at Work* — Erik Brynjolfsson, Danielle Li, Lindsey Raymond](https://doi.org/10.1093/qje/qjae044) là nguồn nghiên cứu nền về năng suất AI, không xác nhận các KPI hay tổn thất của Green SM; trang nhà xuất bản không fetch trực tiếp được trong lần kiểm tra lại.
- Do đó: **fact có nguồn** là các tính năng và nội dung nghiên cứu được nêu bằng link; **hypothesis do AI tạo** là năm cơ hội, KPI ứng viên và MVP, cần dữ liệu nội bộ/pilot để kiểm định.

## 4. Kết quả thực tế Phase 4–6

### Phase 4 — Prototype và kiểm thử

- `starter-code/prompt_prototype.py` đã được kiểm thử bằng **Gemini 3.5 Flash-Lite** qua thư viện **`google-genai`**.
- `SYSTEM_PROMPT` yêu cầu đầu ra có nhãn **`[DRAFT_ONLY]`**, không điều phối xe khi pin dưới 5% nếu không có trạm trong bán kính 5 km, có thể đề xuất `dispatch_mobile_charger`, và luôn cần người phê duyệt trước khi thực hiện.
- Prototype có ba kiểm thử đối nghịch (adversarial tests). Các kiểm tra tĩnh 1–3 và `py_compile` đều đạt.
- Sau khi chuyển từ các model không khả dụng sang `gemini-3.5-flash-lite` theo gợi ý của API, live prototype đã chạy thành công cả ba adversarial tests. Section B đạt **5.00/5.00**: script exit code 0 và toàn bộ assertion về ranh giới an toàn đều đạt. Không ghi hoặc chia sẻ bất kỳ secret nào trong log này.

Phạm vi cần được phân biệt rõ: **group deep-dive** tập trung vào các khiếu nại CSKH phức tạp, còn prototype starter này kiểm thử riêng ranh giới điều phối viên về pin/trạm sạc di động theo yêu cầu của khóa học/autograder. Prototype không phải bằng chứng production cho quy trình xử lý khiếu nại CSKH.

### Phase 5 — Kết luận mức sẵn sàng

Kết luận vẫn là **NOT YET**. Hiện còn thiếu dữ liệu khiếu nại nội bộ đã ẩn danh, baseline, nhãn routing, phê duyệt an toàn và mức sẵn sàng của các bên liên quan. Do đó chưa thể kết luận hiệu quả, an toàn hoặc khả năng triển khai production.

### Phase 6 — Phản ánh và bước tiếp theo

- **AI đã giúp:** nhanh chóng tạo và thu hẹp prompt, làm rõ các guardrail, sinh các ca kiểm thử đối nghịch và kiểm tra cú pháp prototype.
- **Đã thất bại/chưa chắc chắn:** các model cũ không khả dụng cho key này; prototype hiện đã có bằng chứng runtime cho ba ca đối nghịch của ranh giới pin/sạc, nhưng đây vẫn là prototype starter riêng và chưa phải bằng chứng production cho routing CSKH.
- **Kiểm thử tiếp theo:** bổ sung các ca biên pin/trạm và kiểm tra human approval; sau đó đánh giá riêng trên dữ liệu khiếu nại CSKH đã ẩn danh với baseline và nhãn routing được phê duyệt.

## 5. Nguồn tham khảo

- **Nguồn chính thức (fact về tính năng), tác giả/publisher: Green SM (Khối Đồng hành & Phát triển Bác Tài Xanh):** [Green SM V-App — gợi ý lộ trình sạc và danh sách phiên sạc](https://www.greensm.com/vn-vi/news/ra-mat-tinh-nang-moi-goi-y-lo-trinh-sac-va-danh-sach-phien-sac-tren-ung-dung-v-app?utm_source=chatgpt.com); [Green SM Driver — đặt lịch bảo dưỡng, sửa chữa](https://www.greensm.com/vn-vi/news/huong-dan-dat-lich-bao-duong-sua-chua-xe-qua-ung-dung-green-sm-driver-1?utm_source=chatgpt.com).
- **Nguồn nghiên cứu (bối cảnh, không phải số liệu Green SM):** [*Coordinated vehicle dispatching and charging scheduling for an electric ride-hailing fleet under charging congestion and dynamic prices* — Ma, Connors, Viti (2024)](https://orbilu.uni.lu/handle/10993/63841); [*Generative AI at Work* — Brynjolfsson, Li, Raymond](https://doi.org/10.1093/qje/qjae044), trang nhà xuất bản không fetch trực tiếp được trong lần kiểm tra lại.

## 6. Phản ánh của sinh viên

- AI đã giúp em làm gì nhanh hơn (mở rộng cơ hội, đặt tên chỉ số, thu hẹp MVP)?
- Phần nào vẫn chưa chắc chắn vì thiếu dữ liệu nội bộ hoặc chưa kiểm chứng được?
- Em đã độc lập sửa hoặc loại bỏ kết luận nào của AI sau khi kiểm tra nguồn và tính năng hiện có?
- Nếu tiếp tục, em sẽ xin dữ liệu nào để kiểm định các giả định và đo hiệu quả MVP?
