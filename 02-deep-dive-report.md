# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)
**Vẽ quy trình hiện tại lên bảng/giấy A3.** Sử dụng các ký hiệu:
* 🔴 **Bottleneck:** Bước gây tắc nghẽn, tốn thời gian, hoặc sai sót nhiều nhất.
* 🔄 **Handoff:** Điểm chuyển giao thông tin giữa người và hệ thống, hoặc giữa các bộ phận.
* Ghi rõ thời gian vận hành trung bình: **Tổng cộng = khoảng 5 phút/lượt**.

### Bài toán được chọn: Điều phối lại chuyến khi tài xế hủy hoặc không nhận cuốc

**Current-State Workflow:**

`Hệ thống ghi nhận hủy/timeout` → 🔄 `Điều phối viên nhận cảnh báo` → `Kiểm tra vị trí và trạng thái tài xế trên màn hình` → 🔴 `Tìm, gọi hoặc nhắn lần lượt cho tài xế thay thế (khoảng 3 phút)` → 🔄 `Tài xế xác nhận nhận chuyến` → `Điều phối viên cập nhật chuyến và báo khách`.

| Bước | Người/hệ thống | Thời gian ước tính | Rủi ro hoặc điểm nghẽn |
|---|---|---:|---|
| Ghi nhận chuyến bị hủy hoặc timeout | Hệ thống | Dưới 10 giây | Dữ liệu trạng thái có thể chậm cập nhật |
| Tiếp nhận và kiểm tra chuyến | Điều phối viên | 30 giây | 🔄 Handoff từ hệ thống sang người |
| Tìm tài xế phù hợp | Điều phối viên | 1-2 phút | Phải xem nhiều tiêu chí cùng lúc |
| Liên hệ tài xế thay thế | Điều phối viên và tài xế | 2-3 phút | 🔴 Không bắt máy, từ chối hoặc nhận chuyến khác |
| Cập nhật chuyến và thông báo khách | Điều phối viên/hệ thống | 30 giây | 🔄 Có thể cập nhật chậm hoặc sai trạng thái |

**Tổng cộng:** khoảng **5 phút/lượt**, chưa tính thời gian chờ tài xế phản hồi. Với giả định 1.000 sự cố/ngày, thời gian xử lý thủ công khoảng 83 giờ/ngày. Các số liệu này là baseline giả định và cần được xác nhận bằng log vận hành.

## 3.2. Problem Statement (6-field) & Metrics (15 min)
Điền đầy đủ 6 trường thông tin của bài toán:

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Ai đang thực hiện tác vụ hằng ngày? |
| **2. Current Workflow** | Mô tả tóm tắt quy trình thủ công hiện tại và công cụ sử dụng. |
| **3. Bottleneck** | Bước nào chậm, lỗi, hoặc cần xử lý ngôn ngữ tự động nhiều nhất? |
| **4. Business Impact** | Tổn thất thực tế đo bằng thời gian, chi phí, hoặc SLA của Vingroup. |
| **5. Success Metric** | AI giải quyết được thì đạt ngưỡng số mấy? (Ví dụ: *"85% vé được phân loại dưới 10s"*). |
| **6. Operational Boundary** | AI được phép làm gì, TUYỆT ĐỐI không được làm gì, điểm nào cần duyệt? |

| Field | Nội dung phân tích |
|---|---|
| **1. Actor / Operator** | Điều phối viên Xanh SM là người theo dõi chuyến bị hủy, tìm tài xế thay thế, liên hệ và cập nhật chuyến. Khách hàng cần được thông báo nhanh; tài xế được mời nhận chuyến thay thế. |
| **2. Current Workflow** | Khi tài xế hủy hoặc không phản hồi, hệ thống tạo cảnh báo. Điều phối viên kiểm tra vị trí, trạng thái online, loại xe và lịch chuyến của các tài xế gần đó; sau đó gọi/nhắn từng người, chọn người đồng ý, cập nhật chuyến trên hệ thống và thông báo cho khách. Quy trình mất khoảng 5 phút/lượt và thường sử dụng màn hình điều phối, bản đồ, điện thoại hoặc công cụ nhắn tin nội bộ. |
| **3. Bottleneck** | 🔴 Tìm và liên hệ tài xế thay thế là bottleneck. Điều phối viên phải tổng hợp nhiều tiêu chí theo cách thủ công, trong khi tài xế có thể không bắt máy, từ chối hoặc nhận chuyến khác. |
| **4. Business Impact** | Với giả định 1.000 sự cố/ngày, 5 phút xử lý mỗi sự cố tạo khoảng 83 giờ công/ngày. Khách có thể chờ thêm 3-7 phút, làm tăng nguy cơ hủy chuyến, giảm trải nghiệm và ảnh hưởng SLA. Đây là ước tính scoping, cần đối chiếu với log chuyến, thời gian phản hồi và tỷ lệ hủy thực tế. |
| **5. Success Metric** | (a) Giảm thời gian tìm tài xế từ 5 phút xuống dưới 1 phút; (b) tối thiểu 85% đề xuất đầu tiên được điều phối viên chấp nhận; (c) giảm thời gian chờ phát sinh xuống dưới 2 phút; (d) giảm tỷ lệ chuyến bị hủy hoàn toàn ít nhất 20% so với baseline; (e) 100% quyết định cuối cùng có log người hoặc hệ thống thực hiện. |
| **6. Operational Boundary** | AI được phép đọc dữ liệu chuyến và tài xế đã được cấp quyền, xếp hạng tài xế đủ điều kiện, giải thích lý do đề xuất và soạn lời mời nhận chuyến. AI tuyệt đối không được tự ý phạt tài xế, hủy chuyến, thay đổi giá, cam kết bồi thường hoặc điều phối xe không đủ điều kiện. Điều phối viên phải duyệt trước khi gửi lời mời hoặc thay đổi chuyến. Các ca có dữ liệu GPS lỗi, sự cố an toàn, khiếu nại nghiêm trọng hoặc độ tin cậy thấp phải chuyển sang xử lý thủ công. |

## 3.3. Future-State Flow & AI Fit (25 min)
* **Xác định mức AI Fit (AI-Fit Matrix):** Giải pháp thuộc nhóm nào? [x] Rule / State-Machine [ ] LLM Feature [x] Agentic Loop có giới hạn.
* **Vẽ Future-State Flow:** Đánh dấu rõ:
  * 🔵 **AI Step:** Bước Rule/ranking hoặc tác vụ AI được kiểm soát.
  * 🟢 **Human Step (HITL):** Bước con người phê duyệt/review (Human-in-the-loop).
  * ↩️ **Fallback:** Kế hoạch dự phòng khi LLM trả về kết quả lỗi hoặc không tự tin.

### AI-Fit và Future-State Flow

**AI-Fit Matrix:** [x] Rule / State-Machine  [ ] LLM Feature  [x] Agentic Loop có giới hạn

Phần xếp hạng tài xế nên dùng rule/state-machine và điểm số xác định, vì vị trí, trạng thái, loại xe và điều kiện đủ tư cách là dữ liệu có cấu trúc. Agentic loop chỉ được dùng trong phạm vi hẹp để thực hiện chuỗi tác vụ tìm ứng viên, tạo lời mời và chờ trạng thái; không được tự đưa ra quyết định kinh doanh ngoài các công cụ được cấp quyền. LLM không cần thiết cho quyết định điều phối lõi, nhưng có thể hỗ trợ tạo bản nháp tin nhắn nếu cần ngôn ngữ tự nhiên.

**Future-State Workflow:**

1. Hệ thống phát hiện chuyến bị hủy/timeout và tạo event.
2. Bộ lọc Rule loại bỏ tài xế offline, đang bận, không đúng loại xe, quá xa hoặc không đủ điều kiện vận hành.
3. 🔵 **AI Step:** Bộ xếp hạng tính điểm các tài xế còn lại theo khoảng cách, ETA, hướng di chuyển, trạng thái và xác suất nhận cuốc; hệ thống trả về tối đa 3 ứng viên cùng lý do và độ tin cậy.
4. 🔵 **AI Step:** Agent giới hạn tạo bản nháp lời mời nhận chuyến, không gửi trực tiếp.
5. 🟢 **Human Step (HITL):** Điều phối viên kiểm tra ứng viên, lý do đề xuất, ETA và bản nháp; phê duyệt một ứng viên hoặc chọn xử lý thủ công.
6. Hệ thống gửi lời mời cho tài xế được duyệt và chờ phản hồi trong thời hạn cấu hình.
7. Nếu tài xế chấp nhận, hệ thống cập nhật chuyến, ghi audit log và gửi thông báo cho khách.
8. ↩️ **Fallback:** Nếu tài xế từ chối/hết thời gian, không có ứng viên hợp lệ, dữ liệu GPS lỗi hoặc độ tin cậy dưới ngưỡng 0,85, hệ thống dừng tự động và chuyển lại điều phối viên theo quy trình hiện tại.

**Kiểm soát an toàn:** Mọi đề xuất phải kèm lý do, thời điểm, dữ liệu đầu vào chính và phiên bản policy. Không cho phép agent tự gọi các công cụ phạt tài xế, hủy chuyến, sửa giá hoặc gửi cam kết tới khách.

---

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:
1. [x] **Dữ liệu mẫu/logs:** Có thể bắt đầu với log chuyến bị hủy, vị trí/ETA, trạng thái tài xế, loại xe, lịch sử nhận cuốc và thời gian xử lý. Cần làm sạch, gắn nhãn kết quả điều phối và xác nhận quyền sử dụng dữ liệu trước khi test.
2. [x] **Rủi ro được kiểm soát:** Có Rule filter, ngưỡng confidence, HITL bắt buộc, audit log và fallback về điều phối thủ công. Không tự động thay đổi giá, phạt tài xế hoặc gửi cam kết cho khách.
3. [ ] **Stakeholders sẵn sàng:** Cần pilot với một nhóm điều phối viên và một khu vực nhỏ để đo tỷ lệ chấp nhận đề xuất, tránh làm gián đoạn SLA hiện tại.

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
**GO có điều kiện cho prototype nội bộ, không phải triển khai tự động toàn bộ.** Bài toán có tần suất lặp lại cao, bottleneck rõ ràng và metric đo được: thời gian xử lý, thời gian chờ phát sinh, tỷ lệ chấp nhận đề xuất và tỷ lệ hủy chuyến. Rule/state-machine có thể xử lý các điều kiện bắt buộc; agent chỉ hỗ trợ chuỗi tác vụ có giới hạn và luôn có HITL. Vì vậy, rủi ro có thể kiểm soát với chi phí thử nghiệm thấp hơn so với tự động hóa hoàn toàn.

Trước khi mở rộng, nhóm phải xác nhận baseline từ log thật, kiểm tra chất lượng GPS/ETA, đo tác động lên SLA và thử nghiệm A/B hoặc pilot ở một khu vực nhỏ. Nếu dữ liệu không đủ sạch, tỷ lệ đề xuất đúng dưới 85% hoặc thời gian chờ không giảm, quyết định phải chuyển về **NOT YET** để bổ sung dữ liệu và điều chỉnh policy.

---
