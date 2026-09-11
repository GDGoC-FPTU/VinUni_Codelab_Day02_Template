# Problem Scan — VinUni Canteen & Smart Operations

## Phase 1 — Scan bằng 4 Lenses

Các số liệu thời gian dưới đây là giả định scoping và cần được xác lập bằng quan sát thực tế.

| # | Đơn vị | Lens | Bài toán vận hành |
|---:|---|---|---|
| 1 | VinUni Canteen | Tốn thời gian | Sinh viên phải xếp hàng mua vé rồi xếp hàng lần hai tại quầy cơm vào giờ trưa. |
| 2 | VinUni Canteen | Lặp lại | Thu ngân thu tiền/phát vé và nhân viên quầy cơm kiểm tra/thu vé cho từng suất. |
| 3 | VinUni Canteen | AI có thể tốt hơn | Menu chưa tận dụng món đã lưu và lịch sử mua để hỗ trợ đặt lại hoặc khám phá món mới. |
| 4 | Vinhomes | AI có thể tốt hơn | Thiết bị tòa nhà có nguy cơ vận hành theo lịch cố định thay vì theo nhu cầu thực tế. |
| 5 | Vinhomes | Stakeholder Pain | Bảo vệ phải quan sát nhiều camera nên có nguy cơ phát hiện chậm sự kiện bất thường. |

## Phase 2 — Quick Problem Cards

### Card 1 — Pre-order và gợi ý món tại căn-tin VinUni

| Trường | Nội dung |
|---|---|
| **Bài toán** | Sinh viên phải mua vé rồi xếp hàng lần hai để nhận cơm, trong khi chưa có đặt trước, lưu món quen hoặc gợi ý món mới phù hợp. |
| **Actor** | Sinh viên, thu ngân, nhân viên quầy cơm và quản lý căn-tin. |
| **Workflow** | Xem món → xếp hàng mua vé → thanh toán/nhận vé → xếp hàng quầy cơm → đưa vé/chọn món → nhận suất. |
| **Bottleneck** | Hai hàng chờ, ước tính tổng 10–20 phút vào giờ cao điểm; cần đo baseline trong ít nhất 5 ngày học. |
| **AI hỗ trợ** | Dùng menu còn hàng, lịch sử đơn và món đã lưu để gợi ý tối đa 3 món; hiểu yêu cầu tự nhiên và tạo giỏ hàng nháp. |
| **Metric** | Nhận đơn pre-order dưới 5 phút; ≥70% đơn giờ cao điểm qua app/QR; ≥30% dùng đặt lại; đơn sai dưới 2%. |
| **Architecture** | Rule/State-machine cho giá, tồn kho, thanh toán, QR; LLM Feature cho gợi ý và đơn nháp. |
| **Boundary** | AI không tự đặt, tự trừ tiền, đổi giá, hoàn tiền hoặc đảm bảo dị ứng; người dùng luôn xác nhận. |

### Card 2 — Giám sát camera an ninh Vinhomes

| Trường | Nội dung |
|---|---|
| **Bài toán** | Bảo vệ phải theo dõi đồng thời nhiều camera nên có nguy cơ bỏ sót hoặc phát hiện chậm các sự kiện đã định nghĩa. |
| **Actor** | Nhân viên giám sát, đội tuần tra, ban quản lý, cư dân và khách. |
| **Workflow** | Camera truyền hình → bảo vệ quan sát → phát hiện nghi ngờ → tua lại/đối chiếu → gọi tuần tra xác minh. |
| **Bottleneck** | Quan sát liên tục nhiều luồng; thời gian phát hiện/xác minh giả định 5–15 phút/sự kiện. |
| **AI hỗ trợ** | AI Vision phát hiện xe đỗ sai vùng, vật thể bỏ quên hoặc mật độ người vượt ngưỡng và gửi clip cho bảo vệ. |
| **Metric** | Recall ≥85%; cảnh báo dưới 60 giây; false-positive dưới 15%; 100% cảnh báo mức cao được người xác minh. |
| **Architecture** | AI Vision kết hợp rule-based cho ngưỡng và tuyến cảnh báo. |
| **Boundary** | AI không kết luận tội phạm, không tự phạt và không tự khóa/mở cổng. |

### Card 3 — Bảo trì dự báo thiết bị Vinhomes

| Trường | Nội dung |
|---|---|
| **Bài toán** | Đội kỹ thuật có nguy cơ chỉ phát hiện lỗi khi thang máy, điều hòa, bơm hoặc máy phát đã bất thường hay dừng hẳn. |
| **Actor** | Kỹ thuật viên, quản lý tòa nhà, cư dân và khách sử dụng dịch vụ. |
| **Workflow** | Thiết bị vận hành → phát sinh lỗi/người dùng báo → tạo ticket → kỹ thuật viên kiểm tra → tra lịch sử → sửa/đặt phụ tùng. |
| **Bottleneck** | Phát hiện muộn và chẩn đoán thủ công; giả định 30–120 phút để khoanh vùng một sự cố. |
| **AI hỗ trợ** | ML phân tích nhiệt độ, rung, điện năng, chu kỳ hoạt động và lịch sử lỗi để chấm điểm rủi ro, cảnh báo kiểm tra sớm. |
| **Metric** | Phát hiện trước ≥70% lỗi mục tiêu từ 24–72 giờ; giảm 20% downtime ngoài kế hoạch; giảm 15% ca sửa khẩn. |
| **Architecture** | Predictive ML kết hợp rule cảnh báo; không cần LLM/Agent cho dự báo lõi. |
| **Boundary** | AI chỉ xếp hạng rủi ro; kỹ thuật viên duyệt trước khi dừng thiết bị hoặc thay linh kiện. |

## Quyết định chọn bài toán

Chọn **Card 1 — Pre-order và gợi ý món tại căn-tin VinUni** để deep-dive vì actor và workflow rõ, có thể pilot ở một quầy, tác động đo được và rủi ro được giới hạn bằng xác nhận thanh toán. Hai card Vinhomes cần dữ liệu camera/cảm biến và quy trình an toàn phức tạp hơn.
