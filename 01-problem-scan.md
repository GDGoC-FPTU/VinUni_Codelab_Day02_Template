# Lab 02 — Quét cơ hội và Quick Problem Cards

**Đề tài chọn:** Trợ lý soạn nháp xử lý sự cố pin cho điều phối viên Xanh SM.

Đây là bài tập mô phỏng, không phải khảo sát hay mô tả hệ thống nội bộ đã xác minh của doanh nghiệp. Tất cả thời gian, sản lượng và mục tiêu là **giả định để lập kế hoạch**, chưa phải kết quả đo. Ngưỡng pin là quy định của lab, không phải hướng dẫn vận hành xe thực tế.

## 1. SCAN — 5 cơ hội qua 4 góc nhìn

| # | Đơn vị | Góc nhìn | Bài toán và người bị ảnh hưởng |
|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Điều phối viên phải đọc báo cáo pin yếu, xác minh vị trí và soạn phản hồi thủ công; tài xế chờ hướng xử lý. |
| 2 | Vinhomes | Lặp lại | Nhân viên tiếp nhận phân loại và chuyển phản ánh mất nước, hỏng đèn, tiếng ồn tới bộ phận xử lý. |
| 3 | Xanh SM | Pain từ người khác | Nhân viên chất lượng khó tổng hợp lý do hủy chuyến từ ghi chú tự do; tài xế và khách có thể phải giải thích lại. |
| 4 | Vinpearl | AI có thể tốt hơn | CSKH cần soạn phản hồi đánh giá phù hợp từng tình huống thay cho câu trả lời rập khuôn. |
| 5 | VinFast | Lặp lại | Nhân viên đối soát kiểm tra bản ghi sạc với hóa đơn; ưu tiên thử rule đối chiếu mã, ngày và số tiền trước LLM. |

## 2. Card 1 — Xanh SM: xử lý sự cố pin

- **Bài toán:** Rút ngắn thời gian soạn đề xuất xử lý báo cáo pin yếu, giữ quyền quyết định ở điều phối viên.
- **Actor:** Điều phối viên; tài xế và đội cứu hộ chịu ảnh hưởng.
- **Quy trình mô phỏng:** Nhận báo cáo (2 phút) → xác minh GPS và pin (2 phút) → tra cứu lựa chọn hỗ trợ (5 phút) → soạn phương án (5 phút) → chuyển người có thẩm quyền/đội hỗ trợ (1 phút). Tổng **15 phút/lượt**.
- **Bottleneck:** Tra cứu và soạn phương án, tổng **10 phút/lượt**.
- **AI hỗ trợ:** Đọc tin nhắn, nêu thông tin còn thiếu, soạn đề xuất có cấu trúc. Người vận hành kiểm tra dữ liệu nghiệp vụ.
- **Metric mục tiêu:** ≥85% ca mô phỏng đủ dữ liệu được xử lý đến chuyển giao trong **≤5 phút**, riêng soạn nháp **≤1 phút**; chưa phải SLA đã kiểm chứng.
- **Kiến trúc:** Rule kiểm tra đầu ra + LLM feature, không dùng agent tự thực thi.
- **Ranh giới:** `[DRAFT_ONLY]`, người duyệt bắt buộc; pin <5% đề xuất `dispatch_mobile_charger`; không tự gửi tin/điều xe.

## 3. Card 2 — Vinhomes: phân loại phản ánh cư dân

- **Bài toán:** Giảm thao tác đọc và chuyển phản ánh tới bộ phận phụ trách.
- **Actor:** Nhân viên tiếp nhận và ban quản lý; cư dân chờ phản hồi.
- **Quy trình giả định:** Tiếp nhận (1 phút) → phân loại (3 phút) → tìm bộ phận (2 phút) → soạn xác nhận (2 phút). Tổng **8 phút/lượt**.
- **Bottleneck:** Phân loại và tìm bộ phận, **5 phút/lượt**.
- **AI hỗ trợ:** Đề xuất nhãn và nội dung xác nhận, nhân viên duyệt trước khi chuyển.
- **Metric mục tiêu:** ≥90% phân loại đúng trên 50 phản ánh do con người gán nhãn; thời gian trung vị ≤4 phút. Chưa có tập dữ liệu thật.
- **Kiến trúc:** Rule cho từ khóa rõ ràng; LLM cho mô tả tự do hoặc đa vấn đề.
- **Ranh giới:** Không quyết định mức phí, tranh chấp hoặc bồi thường; chuyển người phụ trách khi mơ hồ.

## 4. Card 3 — Xanh SM: tổng hợp lý do hủy chuyến

- **Bài toán:** Gom nhóm lý do từ ghi chú để nhân viên chất lượng phát hiện vấn đề lặp lại.
- **Actor:** Nhân viên chất lượng; tài xế và khách là bên phản ánh.
- **Quy trình giả định cho 100 ghi chú:** Xuất dữ liệu (10 phút) → đọc, gán nhãn (60 phút) → tổng hợp (20 phút) → review (10 phút). Tổng **100 phút/lô**.
- **Bottleneck:** Đọc và gán nhãn, **60 phút/lô**.
- **AI hỗ trợ:** Gợi ý nhóm nguyên nhân, dẫn mã ghi chú làm bằng chứng.
- **Metric mục tiêu:** ≥85% nhãn khớp nhãn người review; xử lý một lô ≤40 phút. Chưa kiểm chứng.
- **Kiến trúc:** LLM feature theo lô, bộ nhãn cố định và nhóm “chưa rõ”.
- **Ranh giới:** Không suy diễn lỗi cá nhân hay tự phạt tài xế; ẩn định danh trước khi gửi mô hình.

## 5. Lựa chọn và phản biện

Chọn **Card 1** vì phạm vi hẹp, có ranh giới kiểm tra được và phù hợp starter code/autograder. Card 2 cần danh mục bộ phận và quy trình chuyển tuyến đã xác nhận; Card 3 cần tập ghi chú đã gán nhãn. Đây không phải bằng chứng rằng hai ý tưởng đó kém giá trị hơn.

Ba điểm yếu cần kiểm chứng: (1) baseline 15 phút chưa được đo; (2) chưa có dữ liệu GPS/trạm tin cậy nên prototype không tự chọn trạm; (3) ngưỡng pin và lựa chọn cứu hộ có thể xử lý bằng rule nếu đầu vào có cấu trúc. Giá trị cần kiểm chứng của LLM là hiểu tin nhắn tự do và soạn nháp. Nếu form + mẫu tin đạt cùng chất lượng với chi phí thấp hơn, ưu tiên giải pháp đó.
