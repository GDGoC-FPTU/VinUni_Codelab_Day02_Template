# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.0. Quyết định lựa chọn bài toán
Nhóm đã chọn bài toán **#2 — Xanh SM: Tài xế gặp khó khăn khi tìm điểm đón khách chính xác tại các khu vực đông người** để thực hiện Deep-Dive.

### Lý do lựa chọn
* Đây là bài toán có **tác động trực tiếp đến trải nghiệm khách hàng** và độ tin cậy của dịch vụ taxi điện.
* Quy trình hiện tại còn **thủ công và có nhiều điểm chậm**, dễ gây chậm trễ ở giờ cao điểm.
* Bài toán này phù hợp để dùng **LLM Feature**: đề xuất điểm đón tối ưu, tạo tin nhắn hướng dẫn ngắn gọn và dễ hiểu cho khách, đồng thời vẫn có người phê duyệt cuối cùng.

---

## 3.1. Current-State Workflow Mapping (25 min)
**Quy trình hiện tại của Xanh SM khi tài xế và khách cần xác định điểm đón phù hợp:**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận vị trí   │     │ Tài xế tìm    │     │ Kiểm tra     │     │ Gửi vị trí   │
│ khách cần đón│ ──→ │ điểm đón     │ ──→ │ lưu lượng,   │ ──→ │ cho khách,   │
│              │     │ phù hợp ở     │     │ chỗ đỗ, an   │     │ điều chỉnh   │
│ Ai: Tài xế    │     │ khu vực đông  │     │ toàn, thời   │     │ nếu cần      │
│ ⏱ 2 phút     │     │ người         │     │ tiết          │     │ ⏱ 3 phút    │
│ In: Vị trí   │     │ Ai: Tài xế    │     │ Ai: Tài xế    │     │ In: Điểm đón │
│ Out: Yêu cầu │     │ ⏱ 5 phút 🔴 │     │ ⏱ 5 phút 🔴 │     │ Out: Chỉ dẫn│
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                      │
                                                      ▼
                                               ┌──────────────┐
                                               │ Bước 5       │
                                               │ Khách không  │
                                               │ tìm thấy điểm│
                                               │ đón sẽ gọi   │
                                               │ lại hoặc hủy │
                                               │ Ai: Khách/Tài │
                                               │ xế            │
                                               │ ⏱ 2-5 phút  │
                                               └──────────────┘
```

### Ghi chú quá trình:
* 🔴 **Bottleneck:** Bước 2-3 (tìm điểm đón phù hợp và kiểm tra điều kiện thực địa) là nơi mất nhiều thời gian nhất.
* 🔄 **Handoff:** Từ tài xế sang khách, và từ khách sang tài xế khi vị trí không phù hợp.
* **Tổng thời gian vận hành trung bình:** khoảng **10-15 phút/lượt** trong giờ cao điểm.

---

## 3.2. Problem Statement (6-field) & Metrics (15 min)

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | **Tài xế Xanh SM** đang thực hiện việc xác định điểm đón khách trong các khu vực đông người như trung tâm thương mại, sân bay, bệnh viện. Bên cạnh đó, **khách hàng** là người chịu tác động trực tiếp khi không tìm thấy điểm đón đúng vị trí. |
| **2. Current Workflow** | Tài xế nhận vị trí khách, tự tìm điểm đón gần nhất ở khu vực đó, kiểm tra lưu lượng giao thông, chỗ đỗ và yếu tố an toàn, sau đó gửi vị trí cho khách. Nếu khách không tìm thấy điểm đón hoặc chỗ đỗ không phù hợp, tài xế phải điều chỉnh lại thủ công. |
| **3. Bottleneck** | Bước **tìm điểm đón tối ưu** và **kiểm tra điều kiện thực tế** tại khu vực đông người là bước chậm nhất. Tài xế phải suy nghĩ theo kiểu thủ công, mất thời gian và dễ nhầm vị trí, đặc biệt vào giờ cao điểm hoặc nơi có không gian hạn chế. |
| **4. Business Impact** | Mỗi lượt điểm đón sai gây khách phải chờ thêm, gọi lại hoặc hủy cuốc. Tại giờ cao điểm, số lượng sự cố này tăng và làm giảm trải nghiệm dịch vụ, đồng thời ảnh hưởng đến hiệu suất điều phối và doanh thu của Xanh SM. |
| **5. Success Metric** | 1. Giảm số lần khách chờ quá 5 phút từ **30% xuống dưới 10%**.<br>2. Tăng tỷ lệ điểm đón chính xác lên **95%+**.<br>3. Giảm thời gian xác định điểm đón từ **10 phút xuống dưới 3 phút/lượt**. |
| **6. Operational Boundary** | AI được phép **đề xuất điểm đón phù hợp nhất, ngắn gọn và dễ hiểu** dựa trên vị trí khách, lưu lượng giao thông, điều kiện thực địa và dữ liệu lịch sử. AI **không được tự động gửi vị trí cho khách mà không có phê duyệt** từ tài xế hoặc hệ thống. Trường hợp không chắc chắn, AI phải chuyển về quy trình cũ và yêu cầu người dùng xác nhận. |

---

## 3.3. Future-State Flow & AI Fit (25 min)

### AI Fit lựa chọn
**LLM Feature** là lựa chọn phù hợp nhất.

**Lý do:**
* Bài toán này có cấu trúc rõ ràng nhưng cần **xử lý ngôn ngữ và suy luận theo ngữ cảnh**, ví dụ: “điểm đón dễ nhận diện”, “an toàn”, “không gây tắc đường”, “đúng vị trí gần khách nhất”.
* Đề xuất điểm đón không cần AI tự hành toàn bộ; chỉ cần AI **gợi ý trong khung đã định nghĩa** và để con người phê duyệt.
* Điều này giữ được độ an toàn nhưng vẫn nâng tốc độ xử lý đáng kể.

### Future-State Flow

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Nhận vị trí  │ ──→ │ 🔵 AI gợi ý  │ ──→ │ 🟢 Tài xế     │ ──→ │ Gửi cho     │
│ khách cần    │     │ điểm đón tốt│     │ xem xét,     │     │ khách /      │
│ đón          │     │ nhất dựa trên│     │ phê duyệt    │     │ điều chỉnh   │
│              │     │ vị trí, lưu  │     │ hoặc chỉnh   │     │ nếu cần      │
│ Ai: Tài xế    │     │ lượng, an    │     │ lại trước khi│     │ Ai: Tài xế    │
│              │     │ toàn, lịch sử│     │ gửi đi       │     │              │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu AI không chắc chắn,
                                                               tài xế tiếp tục tìm điểm đón
                                                               thủ công như hiện tại.
```

### Vai trò của AI trong flow mới
* **🔵 AI Step:** Phân tích vị trí khách, đề xuất 2-3 điểm đón ưu tiên, dựa trên yếu tố an toàn, gần đơn vị khách, và tiện lợi truy cập.
* **🟢 Human Step (HITL):** Tài xế đánh giá và phê duyệt điểm đón trước khi gửi cho khách.
* **↩️ Fallback:** Nếu hệ thống không đủ dữ liệu hoặc kết quả AI có độ tin cậy thấp, quay lại quy trình thủ công cũ.

---

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)?
3. [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Trì hoãn để chuẩn bị thêm.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> Bài toán Xanh SM về điểm đón khách là một ví dụ rất phù hợp cho AI vì nó có tác động rõ ràng đến trải nghiệm người dùng, có thể đo lường bằng metric số, và có thể được giải quyết bằng một prototype nhẹ với độ phức tạp vừa phải. Cấu trúc quy trình hiện tại khá rõ, nên việc xây dựng LLM Feature không yêu cầu nền tảng quá lớn. Ngoài ra, đặt thêm bước phê duyệt của tài xế giúp giảm rủi ro khi AI sai, nên khả năng triển khai thực tế là cao. Từ góc độ chi phí, bài toán này có thể bắt đầu với scope hẹp: chỉ đề xuất điểm đón và sinh gợi ý nhắn tin, không cần tự động hóa toàn bộ hệ thống. Vì vậy, quyết định là **GO** với phiên bản prototype đầu tiên.
