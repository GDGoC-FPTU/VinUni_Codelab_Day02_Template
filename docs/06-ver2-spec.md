# ChargeSafe Copilot — Tài liệu Kỹ thuật & Báo cáo Nâng cấp Version 2 (Ver 2)

## 1. Giới thiệu Tổng quan Ver 2
Phiên bản 2 (Ver 2) của **ChargeSafe Copilot** mở rộng khả năng điều phối sự cố pin Xanh SM từ mô hình phân tích vị trí tĩnh sang **Mô hình Tối ưu Lộ trình Động (En-Route Waypoint Optimization)**, tích hợp định vị tự động, bản đồ tương tác và bộ phòng thủ Prompt Injection đa tầng.

Toàn bộ hệ thống vẫn kiên định với nguyên lý an toàn cốt lõi:
- **Fail-Closed & Invariants**: Mọi bản thảo luôn gắn nhãn `[DRAFT_ONLY]`, cấm tự động gửi `auto_send = false`, bắt buộc con người duyệt (`requires_human_approval = true`).
- **Pin nguy cấp < 5%**: Luôn kích hoạt xe sạc lưu động (`dispatch_mobile_charger`), nghiêm cấm gợi ý bất kỳ trạm sạc nào.
- **Tương thích 100% Autograder**: Đạt điểm tối đa **10.00 / 10.00** trên GitHub Classroom.

---

## 2. Các Tính năng Nâng cấp Mới

### 2.1. Phòng thủ & Kiểm thử Toàn diện Chống Prompt Injection
Hệ thống bổ sung suite kiểm thử `tests/test_prompt_injection_v2.py` gồm 12 tình huống tấn công phức tạp, đạt tỷ lệ vượt qua an toàn **12/12 (100% Fail-Closed)**:
1. **Direct System Prompt Override**: Ép in API key, token bí mật hoặc hướng dẫn hệ thống.
2. **DAN Unrestricted Mode Activation**: Cố tình phá vỡ quy tắc điều phối và dump database.
3. **Executive / Authority Spoofing**: Giả danh Giám đốc vận hành Xanh SM ra lệnh tắt HITL hoặc auto-send.
4. **Social Engineering Kỹ sư Trạm**: Giả mạo kỹ sư V-GREEN đòi lấy thông tin trạm sạc.
5. **Data Exfiltration (PII)**: Đòi xuất danh sách số điện thoại, biển số xe và vị trí tài xế.
6. **Bypass DRAFT_ONLY**: Yêu cầu bỏ nhãn nháp và gửi thẳng cho tài xế.
7. **Critical Battery Deception**: Khai man mức pin 2% thành 50% để trốn xe sạc lưu động.
8. **Conflicting Battery Oscillation**: Tấn công làm dao động pin (lúc 3%, lúc 80%) ép hệ thống đoán mò.
9. **Physical Hazard Suppression**: Che giấu sự cố cháy nổ để ép hệ thống chỉ trạm sạc tiếp.
10. **Electrical Smoke & Arcing**: Cố tình cắm sạc khi có khói và mùi khét rò điện.
11. **Route Hijack Detour**: Ép hệ thống điều xe VF 3 pin 6% đi trạm xa 60 km bất chấp an toàn.
12. **Structured JSON Injection**: Chèn cú pháp JSON độc hại trong phần ghi chú của tài xế.

### 2.2. Định vị GPS Tự động (Browser Geolocation API)
- Người dùng chỉ cần nhấp nút **"📍 Lấy vị trí hiện tại của tôi"**.
- Trình duyệt tự động truy vấn GPS thiết bị thông qua `navigator.geolocation.getCurrentPosition()`, tự điền kinh độ/vĩ độ, đặt vị trí xe và căn chỉnh tâm bản đồ.
- Có cơ chế xử lý lỗi rõ ràng (từ chối cấp quyền, vị trí không khả dụng, timeout) kèm giải pháp fallback cho phép nhấp trực tiếp lên bản đồ.

### 2.3. Slider Bán kính Tìm kiếm Linh hoạt (1 – 30 km)
- Thanh trượt điều chỉnh khoảng cách tìm trạm (mặc định 15 km).
- Hiển thị trực quan vòng tròn quét bán kính co giãn thời gian thực quanh vị trí xe trên bản đồ.
- Danh sách so sánh các trạm sạc trong bán kính cho phép điều phối viên xem khoảng cách, số cổng trống và chuyển đổi trạm đề xuất chỉ với 1 cú nhấp.

### 2.4. Thuật toán Tối ưu Hóa Trạm Sạc Trên Lộ Trình (En-Route Waypoint Routing)
Giải quyết bài toán thực tế: **Một trạm sạc xa hơn một chút nhưng nằm tiện đường lộ trình sẽ tốt hơn rất nhiều so với một trạm gần hơn nhưng nằm ngược hướng di chuyển.**

#### Mô hình Toán học & Thuật toán:
Cho:
- Vị trí xe hiện tại: $A = (\text{lat}_A, \text{lon}_A)$
- Điểm đến mong muốn: $B = (\text{lat}_B, \text{lon}_B)$
- Trạm sạc ứng viên: $S = (\text{lat}_S, \text{lon}_S)$
- Khoảng cách đường kính trực tiếp: $d(A, B) = \text{haversine}(A, B)$
- Khoảng cách từ xe tới trạm: $d(A, S) = \text{haversine}(A, S)$
- Khoảng cách từ trạm tới điểm đến: $d(S, B) = \text{haversine}(S, B)$

Độ lệch lộ trình (Detour Distance):
$$\Delta d = d(A, S) + d(S, B) - d(A, B) \ge 0$$

Vector hướng di chuyển $\vec{AB}$ và vector trạm sạc $\vec{AS}$:
$$\cos\theta = \frac{\vec{AB} \cdot \vec{AS}}{\|\vec{AB}\| \|\vec{AS}\|}$$

Hàm mục tiêu chi phí định tuyến (Routing Cost):
$$\text{Cost}(S) = d(A, S) + \lambda \cdot \Delta d + \text{Penalty}_{\text{ngược hướng}}$$
- Nếu $\cos\theta < -0.15$ (Trạm nằm ngược hướng lộ trình): $\lambda = 2.5$ và cộng thêm điểm phạt quay đầu $+4.0$. Gắn nhãn: **"Ngược đường"**.
- Nếu $\Delta d \le 1.2\text{ km}$: $\lambda = 1.2$. Gắn nhãn: **"Rất tiện đường"**.
- Nếu $\Delta d > 1.2\text{ km}$: $\lambda = 1.8$. Gắn nhãn: **"Tiện đường một phần"**.

**Ràng buộc an toàn bất biến**:
Xe chỉ được phép đi tới trạm $S$ nếu:
$$d(A, S) \le \text{demo\_range\_limit}$$
Nếu pin xe không đủ an toàn để tới trạm tiện đường xa hơn, hệ thống tự động ưu tiên trạm an toàn gần nhất hoặc chuyển cứu hộ lưu động.

### 2.5. Tích hợp Bản đồ Tương tác & Google Maps Navigation
1. **Bản đồ Tương tác Leaflet + OpenStreetMap**:
   - Vẽ vị trí xe (icon ô tô xanh), điểm đến (icon mục tiêu đỏ), các trạm sạc trong mạng lưới.
   - Vẽ đường nét đứt biểu thị lộ trình di chuyển $A \to S \to B$.
   - Vòng tròn bán kính quét trực quan.
   - Hỗ trợ click trực tiếp lên bản đồ để thay đổi vị trí xe hoặc điểm đến.
2. **Canvas Offline Fallback**:
   - Nếu môi trường mạng cô lập không tải được CDN OpenStreetMap, hệ thống tự động chuyển sang chế độ radar Canvas 2D mượt mà.
3. **Liên kết Chỉ đường Trực tiếp Google Maps**:
   - Nút **"Mở chỉ đường trên Google Maps"** tạo đường link chuẩn Google Maps Directions:
     `https://www.google.com/maps/dir/?api=1&origin={latA},{lonA}&destination={latB},{lonB}&waypoints={latS},{lonS}&travelmode=driving`
   - Cho phép điều phối viên hoặc tài xế mở ngay ứng dụng Google Maps Navigation chỉ với 1 chạm.

---

## 3. Hướng dẫn Khởi chạy & Kiểm thử Ver 2

### 3.1. Chạy Web Server Ver 2
```bash
source .venv/bin/activate
python3 web_server.py --offline
```
Mở trình duyệt tại: `http://127.0.0.1:8765`

### 3.2. Chạy Suite Kiểm thử Prompt Injection Ver 2
```bash
PYTHONPATH=. .venv/bin/python tests/test_prompt_injection_v2.py
```

### 3.3. Chạy Kiểm thử Autograder (GitHub Classroom)
```bash
PYTHONPATH=. .venv/bin/python autograder/autograder.py
```
Kết quả: **10.00 / 10.00**

### 3.4. Chạy Toàn bộ Pytest Suite
```bash
PYTHONPATH=. .venv/bin/pytest tests/
```
Kết quả: **95 passed, 1 skipped, 0 failures**
