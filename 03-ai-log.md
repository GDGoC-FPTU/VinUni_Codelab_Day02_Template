# AI Log & Reflection — Xanh SM Intelligent Dispatcher

## 1. Mục tiêu và phạm vi

Tôi sử dụng AI như công cụ hỗ trợ phân tích và phản biện trong vai trò AI Engineer tại Vin Smart Future. Bài toán được chọn là **điều phối lại chuyến khi tài xế hủy hoặc không nhận cuốc**.

Mục tiêu sử dụng AI:

- Xác định pain point vận hành.
- Cấu trúc hóa actor, workflow, bottleneck và metric.
- Thiết kế prototype có HITL, audit log và fallback.

AI không được sử dụng để thay thế quyết định vận hành của điều phối viên.

## 2. Kết quả AI hỗ trợ

AI hỗ trợ brainstorming theo bốn lens: repetitive, time-consuming, AI-upgrade và stakeholder pain. Kết quả là năm giả thuyết gồm phân loại khiếu nại, điều phối lại chuyến, đối soát doanh thu, xử lý điểm đón sai và lập lịch sạc/bảo trì.

Sau khi so sánh, tôi chọn bài toán điều phối lại chuyến vì có bottleneck rõ, tần suất lặp lại cao và metric định lượng được. AI hỗ trợ xây dựng Quick Problem Card và mô tả current-state/future-state workflow.

Qua phân tích, tôi xác định kiến trúc phù hợp là **Rule/State Machine kết hợp Agent giới hạn**:

- Rule lọc tài xế không đủ điều kiện và tính điểm ứng viên.
- Agent hỗ trợ tìm ứng viên, tạo bản nháp lời mời và theo dõi trạng thái.
- Điều phối viên phê duyệt trước khi gửi lời mời hoặc thay đổi chuyến.

## 3. Sai lệch và nguy cơ hallucination

### 3.1. Số liệu không có nguồn xác minh

AI đề xuất các số liệu như 1.000 sự cố/ngày, 5 phút xử lý/sự cố, 3-7 phút chờ phát sinh và giảm 20% tỷ lệ hủy. AI không có quyền truy cập dữ liệu nội bộ, vì vậy các số liệu này không thể xem là số liệu thực tế.

Tôi chuyển chúng thành **ước tính scoping** và yêu cầu xác minh bằng log chuyến, timestamp, GPS/ETA, thời gian xử lý và tỷ lệ hủy. Các giá trị này chỉ được dùng làm baseline giả định và ngưỡng thử nghiệm pilot.

### 3.2. Lạm dụng LLM/Agent

AI ban đầu có xu hướng đề xuất Agent hoặc LLM cho việc chọn tài xế. Đây là lựa chọn không cần thiết vì vị trí, ETA, trạng thái, loại xe và điều kiện vận hành là dữ liệu có cấu trúc, có thể xử lý bằng Rule/State Machine.

Tôi tách bài toán thành hai lớp: Rule xử lý quyết định có tính ràng buộc; Agent chỉ thực hiện chuỗi tác vụ giới hạn. LLM chỉ là tùy chọn cho việc tạo bản nháp tin nhắn.

### 3.3. Vượt operational boundary

Prompt có thể khiến mô hình đề xuất tự gửi lời mời, tự hủy chuyến, sửa giá hoặc cam kết bồi thường nếu chỉ tối ưu thời gian xử lý. Đây là rủi ro đối với khách hàng, tài xế và SLA.

## 4. Điều chỉnh prompt và kiểm soát

Tôi điều chỉnh prompt theo các trường sau:

1. **Role:** Dispatcher co-pilot; không phải người ra quyết định cuối cùng.
2. **Input:** Chỉ sử dụng dữ liệu chuyến và tài xế được cấp quyền.
3. **Allowed actions:** Lọc, xếp hạng, giải thích và tạo bản nháp.
4. **Forbidden actions:** Không phạt tài xế, hủy chuyến, sửa giá, cam kết bồi thường hoặc tự gửi hành động nhạy cảm.
5. **Output:** Trả về ứng viên, lý do, ETA, confidence và trạng thái cần duyệt.
6. **Fallback:** Chuyển sang điều phối thủ công khi dữ liệu lỗi, không có ứng viên hoặc confidence dưới 0,85.
7. **Audit:** Ghi nhận input chính, policy version, đề xuất và quyết định cuối cùng.

Tôi sử dụng adversarial test để kiểm tra hai tình huống: yêu cầu bỏ qua phê duyệt và yêu cầu thực hiện hành động ngoài quyền hạn. Ngoài ra, tôi yêu cầu AI đóng vai CFO/Trưởng phòng Vận hành để phản biện chi phí, metric và khả năng thay thế bằng Rule-based.

## 5. Kết luận

AI phù hợp để hỗ trợ brainstorming, cấu trúc hóa vấn đề và phản biện thiết kế. AI không thay thế việc xác minh dữ liệu hoặc trách nhiệm vận hành. Tôi phải phân biệt rõ fact và assumption, kiểm tra nguồn số liệu và chọn kiến trúc đơn giản nhất đáp ứng yêu cầu.

Quyết định là **GO có điều kiện cho prototype nội bộ**. Prototype phải dùng dữ liệu đã làm sạch, có baseline, pilot ở phạm vi nhỏ và HITL bắt buộc. Nếu dữ liệu không đạt chất lượng hoặc metric không cải thiện, dự án chuyển sang **NOT YET** để bổ sung dữ liệu và điều chỉnh policy.
