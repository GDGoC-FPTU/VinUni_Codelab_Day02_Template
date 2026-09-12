# 🏗️ Báo Cáo Phân Tích Sâu (Deep-Dive Report) — Vin Smart Future
**Đơn vị:** Vin Smart Future (Khối Công Nghệ Tập Đoàn Vingroup)  
**Dự án:** Trợ Lý AI Tối Ưu Hóa & Điều Hướng Trạm Sạc Trống Cho Xe Điện (VinFast & Xanh SM Smart Charging Agent)  
**Tác giả:** Phùng Quốc Việt (AI Product Engineer)  
**Đối tác Vận hành:** Khối Hạ Tầng Trạm Sạc VinFast & Đội Xe Xanh SM (GSM)

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow Mapping (Quy Trình Thủ Công Hiện Tại)

Hiện tại, khi tài xế xe điện VinFast hoặc tài xế taxi Xanh SM nhận thấy xe sắp hết pin và cần sạc, quy trình diễn ra qua 4 bước:

```text
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Bước 1          │     │ Bước 2          │     │ Bước 3          │     │ Bước 4          │
│ Xe sắp hết pin, │     │ Xem danh sách   │     │ Lái xe đến nơi  │     │ Tiếp tục phải   │
│ tài xế mở app   │ ──→ │ các trạm gần    │ ──→ │ mới phát hiện   │ ──→ │ tìm đường sang  │
│ bản đồ tìm trạm │     │ nhưng không rõ  │     │ hết trụ sạc     │     │ trạm sạc khác   │
│                 │     │ trụ trống       │     │ hoặc chờ dài 🔴 │     │                 │
│ Actor: Tài xế   │     │ Actor: Tài xế   │     │ Actor: Tài xế   │     │ Actor: Tài xế   │
│ ⏱ 2 phút        │     │ ⏱ 5 phút 🔴     │     │ ⏱ 30 phút 🔴    │     │ ⏱ 10 phút       │
│ In: Cảnh báo pin│     │ In: Vị trí GPS  │     │ In: Trạm đã đầy │     │ In: Tìm trạm mới│
│ Out: Chọn bừa   │     │ Out: List trạm  │     │ Out: Xếp hàng   │     │ Out: Di chuyển  │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘

🔴 = Điểm nghẽn cổ chai (Bottlenecks)
⏱ Bước tốn thời gian và gây ức chế nhất: Bước 2 & 3 (Tổng thời gian lãng phí: 35 – 45 phút/lượt).
⚠️ Hậu quả nghiêm trọng: Xe hết trụ sạc phải xếp hàng 30 phút, hoặc pin cạn kiệt không đủ chạy sang trạm thứ hai.
```

---

## 3.2. Problem Statement (6-field) — Tiêu Chuẩn Vin Smart Future

| Trường thông tin | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Tài xế xe điện VinFast (VF5, VF6, VF8, VF9) và Tài xế taxi Xanh SM (GSM). |
| **2. Current Workflow** | Khi xe sắp hết pin, tài xế mở app bản đồ xem danh sách các trạm sạc gần nhưng không biết chính xác trạm nào đang có trụ sạc trống phù hợp với cổng sạc của xe. Tài xế lái xe đến nơi mới phát hiện hết trụ sạc hoặc đang có hàng dài xe chờ sạc, buộc phải chờ 30 phút hoặc tiếp tục tìm đường sang trạm khác. |
| **3. Bottleneck** | **Bước 2 & 3 (30 phút/lượt):** Ứng dụng bản đồ tĩnh không có cơ chế dự báo mức tiêu hao pin thực tế theo địa hình/tắc đường và không cập nhật trạng thái trụ sạc theo thời gian thực (real-time availability), dẫn đến việc tài xế lao vào các trạm sạc đang quá tải hoặc hết chỗ. |
| **4. Business Impact** | Mỗi lượt chờ đợi 30 phút làm giảm từ 1 đến 2 cuốc xe/ngày của mỗi tài xế Xanh SM, gây thất thoát doanh thu ước tính ~12-15% trên toàn đội xe. Đồng thời gây nghẽn cục bộ tại các trạm sạc lớn trong khu đô thị Vinhomes và trung tâm thương mại Vincom. |
| **5. Success Metric** | 1. **Hiệu suất (Efficiency):** Giảm thời gian chờ đợi tại trạm sạc từ **30 phút ──> 0 phút** (xe đến nơi có sẵn trụ sạc trống dành riêng hoặc được điều hướng đón đầu chính xác).<br>2. **Độ chính xác (Quality):** Tỷ lệ gợi ý đúng trạm còn trụ sạc trống tương thích cổng CCS2 đạt tối thiểu **98%**.<br>3. **An toàn tuyệt đối (Safety):** 100% trường hợp pin dưới 5% được cảnh báo nguy cấp, ngăn chặn việc di chuyển xa > 5km và kích hoạt xe sạc pin lưu động (Mobile Charger). |
| **6. Operational Boundary (Ranh giới vận hành)** | **ĐƯỢC PHÉP:** Đọc dữ liệu GPS, mức % pin xe, tra cứu trạng thái thời gian thực của các trụ sạc VinFast, dự báo mức tiêu hao pin và đề xuất lộ trình tối ưu.<br>🛑 **TUYỆT ĐỐI CẤM (Safety Boundaries):**<br>- Mọi văn bản xuất ra bắt buộc phải mang tiền tố `[DRAFT_ONLY]` để tài xế duyệt xác nhận trước khi điều hướng.<br>- Nếu dung lượng pin dưới 5% (`battery < 5%`), TUYỆT ĐỐI KHÔNG được gợi ý trạm sạc cách xa trên 5km vì xe có nguy cơ chết máy giữa đường. BẮT BUỘC lập tức kích hoạt hành động điều xe sạc lưu động: `{"action": "dispatch_mobile_charger", "reason": "<lý do an toàn>"}`.<br>- TUYỆT ĐỐI KHÔNG điều hướng tài xế vào trạm sạc đang có 0 trụ trống (hết chỗ) hoặc trạm đang bảo trì. |

---

## 3.3. Future-State Flow & AI Fit

### 📊 Đánh Giá Độ Tương Thích AI (AI-Fit Assessment)
* **Rule-based thuần túy:** Chỉ tìm trạm gần nhất theo bán kính đường thẳng mà không tính được độ tiêu hao pin động và luồng xe đang đổ về trạm sạc.
* ➔ **LỰA CHỌN TỐI ƯU:** **AI Agent (Agentic Loop kết hợp LLM Feature & Real-time Sensor API):** Agent tự động truy vấn API trạng thái trụ sạc VinFast thời gian thực, tính toán dung lượng pin tiêu hao và đưa ra quyết định điều hướng thông minh.

### 🔄 Sơ Đồ Quy Trình Tương Lai Tích Hợp AI (Future-State Flow)

```text
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Bước 1          │     │ Bước 2          │     │ Bước 3          │     │ Bước 4          │
│ Tài xế yêu cầu  │     │ 🔵 AI Agent     │     │ 🟢 Tài xế       │     │ Xe đến trạm     │
│ tìm trạm sạc    │ ──→ │ Quét thời gian  │ ──→ │ Nhìn đề xuất    │ ──→ │ cắm sạc ngay    │
│ qua giọng nói   │     │ thực trụ trống  │     │ [DRAFT_ONLY] &  │     │ không phải chờ  │
│ ⏱ 3 giây        │     │ & dự báo pin    │     │ bấm xác nhận    │     │ ⏱ 0 phút chờ!   │
│                 │     │ ⏱ 2 giây        │     │ ⏱ 3 giây        │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
                                                       │
                          ┌────────────────────────────┴────────────────────────────┐
                          ▼                                                         ▼
                  [Trường hợp Bình thường - Pin >= 5%]                       [Trường hợp Nguy cấp - Pin < 5%]
                  Đề xuất trạm sạc có sẵn trụ trống 100%,                   CẤM điều hướng trạm xa > 5km.
                  thời gian chờ sạc = 0 phút.                               Kích hoạt ngay xe cứu hộ pin:
                                                                            `{"action": "dispatch_mobile_charger"}`

                  ↩️ Fallback Plan:
                  Nếu mất kết nối dữ liệu viễn thông (mất sóng 4G/5G),
                  hệ thống tự động chuyển sang chế độ Rule-based offline dẫn đường
                  đến trạm sạc có quy mô lớn nhất (Hub sạc > 20 trụ) gần nhất.
```

---

# 🏁 Phase 5 — EVALUATE: Đánh Giá Khả Thi & Quyết Định Đầu Tư

### ✅ Bảng Kiểm Tra Độ Sẵn Sàng (AI Readiness Checklist)
1. **[x] Dữ liệu mẫu & Logs sạch:** Nền tảng IoT trạm sạc VinFast đã hỗ trợ giao thức OCPP truyền trạng thái trụ sạc (Trống / Đang sạc / Lỗi) thời gian thực lên hệ sinh thái đám mây.
2. **[x] Rủi ro sai sót nằm trong tầm kiểm soát:** Gắn nhãn `[DRAFT_ONLY]`, tài xế xác nhận mới chuyển lệnh điều hướng. Cơ chế pin < 5% chốt cứng logic điều xe sạc lưu động.
3. **[x] Stakeholders sẵn sàng chuyển đổi:** Cả tài xế Xanh SM và người dùng VinFast đều rất hào hứng vì giải quyết trực tiếp nỗi đau chờ đợi 30 phút tại trạm sạc.

---

### 🏆 Quyết Định Cuối Cùng Của Ban Giám Đốc Vin Smart Future:
**[x] GO (Bắt đầu xây dựng Prototype kỹ thuật với scope hẹp)**

### 📝 Lý giải quyết định (Justification):
1. **Loại bỏ lãng phí thời gian:** Đưa thời gian chờ sạc từ 30 phút về **0 phút**, nâng cao trực tiếp chỉ số hài lòng khách hàng và doanh thu cuốc xe của Xanh SM.
2. **Cân bằng tải mạng lưới:** Tránh dồn xe vào các trạm sạc đang đông, phân bổ thông minh sang các trạm sạc vệ tinh lân cận.
3. **An toàn pin tuyệt đối:** Ngăn chặn triệt để tình trạng xe cạn pin trên đường thông qua ranh giới an toàn kích hoạt xe sạc lưu động.
