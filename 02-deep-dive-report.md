# 02 — Deep-Dive Report: Xanh SM Intelligent Charging Incident Copilot

## 1. Current-State Workflow

| Bước | Người thực hiện | Hoạt động | Input/Output | Thời gian |
|---:|---|---|---|---:|
| 1 | Điều phối viên | Nhận cuộc gọi và ghi log sự cố | Input: cuộc gọi; Output: mã xe, tình trạng pin | 2 phút |
| 2 | Điều phối viên | Tra cứu vị trí GPS của xe | Input: mã xe; Output: tọa độ | 2 phút |
| 3 | Điều phối viên | Tìm trạm còn chỗ, đúng loại xe/cổng sạc | Input: tọa độ, model, pin; Output: danh sách trạm | 5 phút |
| 4 | Điều phối viên | Viết hướng dẫn đường đi và gửi qua ứng dụng | Input: trạm được chọn; Output: tin nhắn | 5 phút |
| 5 | Điều phối viên | Gọi đội cứu hộ nếu pin quá thấp | Input: mức pin và đánh giá an toàn; Output: yêu cầu cứu hộ | 1 phút |

**Tổng thời gian thủ công: 15 phút/lượt.** Bottleneck chính là bước 3 và 4 vì phải chuyển đổi giữa nhiều hệ thống và dễ chọn sai trạm hoặc mất thời gian soạn tin.

## 2. Problem Statement — 6 fields

| Field | Nội dung |
|---|---|
| Actor / Operator | Điều phối viên tại Trung tâm Điều vận Xanh SM; tài xế là người cung cấp thông tin hiện trường. |
| Current Workflow | Điều phối viên nhận cuộc gọi, tra GPS, kiểm tra trạm sạc, soạn tin hướng dẫn và gọi cứu hộ nếu cần. Quy trình dùng điện thoại, bản đồ nội bộ và dashboard trạm sạc. |
| Bottleneck | Tra cứu thủ công trạm phù hợp và soạn tin nhắn; hai bước này chiếm khoảng 10 phút trong tổng 15 phút. |
| Business Impact | Giả định baseline có khoảng 80 sự cố/ngày; tương đương khoảng 20 giờ công điều vận/ngày. Xe nằm chờ làm giảm năng lực nhận chuyến và tăng áp lực cho tài xế. Các con số cần được xác minh bằng log thật trước khi triển khai. |
| Success Metric | Giảm thời gian xử lý trung vị từ 15 xuống dưới 3 phút; độ chính xác trạm tương thích đạt ít nhất 98%; 0 tin nhắn được gửi tự động khi chưa có phê duyệt. |
| Operational Boundary | AI chỉ được đọc dữ liệu được cấp quyền và tạo draft. AI không được gửi tin, điều xe, đoán dữ liệu thiếu, hoặc đề xuất trạm không tương thích. Nếu pin dưới 5% và trạm xa hơn 5 km, phải đề xuất `dispatch_mobile_charger`. Mọi hành động cần điều phối viên duyệt. |

## 3. AI Fit

Giải pháp phù hợp nhất là **LLM Feature kết hợp Rule/State Machine**, không phải Agent tự trị. Rule kiểm tra ngưỡng pin, khoảng cách và tương thích; LLM chỉ diễn đạt hướng dẫn và lý do dưới dạng draft. Agent tự trị bị loại vì sai một bước có thể khiến xe cạn pin hoặc làm gián đoạn vận hành.

## 4. Future-State Flow

1. Điều phối viên nhận sự cố và xác nhận mã xe.
2. Hệ thống tự lấy GPS, model xe, mức pin và dữ liệu trạm được phép truy cập.
3. Rule kiểm tra dữ liệu bắt buộc, ngưỡng pin, khoảng cách và connector.
4. Gemini tạo JSON draft bắt đầu bằng `[DRAFT_ONLY]`.
5. Điều phối viên xem lý do, trạm/xe cứu hộ và nhấn duyệt.
6. Chỉ sau khi duyệt, hệ thống hiện tại của Xanh SM mới gửi hướng dẫn hoặc tạo yêu cầu cứu hộ.

### Human-in-the-loop

Điều phối viên là người duyệt cuối cùng. Không có đường tắt cho yêu cầu “gửi ngay”, kể cả khi người dùng cố gắng bỏ qua tag `[DRAFT_ONLY]`.

### Fallback

- Thiếu GPS, mức pin, model xe hoặc dữ liệu connector: trả `request_human_review`.
- Gemini lỗi, timeout hoặc trả JSON không hợp lệ: dùng response an toàn cục bộ và yêu cầu người duyệt.
- Pin dưới 5% và trạm xa hơn 5 km: không đưa trạm đó vào draft; trả `dispatch_mobile_charger`.
- Nếu dispatcher không tin kết quả: quay lại quy trình thủ công hiện tại.

## 5. AI Readiness Checklist

| Tiêu chí | Đánh giá | Bằng chứng / Việc cần làm |
|---|---|---|
| Có dữ liệu mẫu/log sạch để test? | NOT YET | Cần lấy log sự cố đã ẩn danh, GPS, pin, model và connector để lập baseline. |
| Rủi ro có được kiểm soát? | YES, có điều kiện | Có Rule, HITL, fallback và giới hạn 5%/5 km; phải kiểm thử thêm với dữ liệu thật. |
| Stakeholder sẵn sàng thay đổi? | Cần xác nhận | Chạy pilot với nhóm dispatcher và đo thời gian xử lý trước/sau. |

## 6. Quyết định

**NOT YET — cần tích lũy dữ liệu và xác lập baseline trước khi triển khai pilot.**

Prototype prompt đủ rõ để bắt đầu kiểm thử kỹ thuật trong môi trường sandbox, nhưng chưa nên chuyển sang production khi chưa xác minh tỷ lệ sự cố, dữ liệu trạm theo thời gian thực và độ chính xác 98%. Sau khi có log đã ẩn danh, có thể thực hiện pilot hẹp với HITL bắt buộc.

