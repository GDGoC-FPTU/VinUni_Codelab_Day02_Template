# Deep-Dive Report — Trợ lý lập phương án sạc cho tài xế VinFast

**Bài toán chọn:** Card #2 trong [01-problem-scan.md](01-problem-scan.md), lấy từ top 3 gồm #2 (VinFast), #4 (Vinhomes), #5 (Vinpearl).

**Phạm vi bản đầu tiên:** ô tô điện VinFast, chuyến đi liên tỉnh tại Việt Nam, trạm sạc V-GREEN.

**Quy ước số liệu:** số có nguồn báo chí được ghi rõ. Số đánh dấu *(giả định)* chỉ dùng để lập khung đo, chưa phải dữ liệu nội bộ của VinFast.

**Vì sao chọn #2:** phần lớn quyết định dựa trên dữ liệu có cấu trúc nên kiểm tra được bằng rule, và thiệt hại khi sai rất cụ thể (đến trạm không dùng được hoặc không đủ pin để đến trạm), nên ranh giới vận hành rõ ràng. Lý do loại #4 và #5 nằm ở cuối [01-problem-scan.md](01-problem-scan.md).

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow

Sơ đồ đầy đủ: [04-workflow-diagram.png](04-workflow-diagram.png)

| Bước | Việc | Ai / Công cụ | Input → Output | ⏱ *(giả định)* | Ký hiệu |
|---|---|---|---|---:|---|
| 1 | Xem % pin và quãng đường còn lại | Tài xế / màn hình xe | Trạng thái xe → số liệu nhớ trong đầu | 1 phút | 🔄 Handoff: số liệu xe được mang sang app bằng tay |
| 2 | Tìm các trạm dọc tuyến | Tài xế / app, bản đồ | Điểm đến → danh sách trạm | 3 phút | |
| 3 | So từng trạm: loại cổng, công suất, trụ trống | Tài xế / app, bản đồ | Danh sách trạm → 2-3 trạm khả thi | 5 phút | 🔴 Bottleneck |
| 4 | Tự tính pin khi đến trạm và thời gian sạc | Tài xế / tính nhẩm | Trạm khả thi → trạm được chọn | 3 phút | 🔴 Bottleneck |
| 5 | Đến nơi hết trụ thì tìm lại trạm khác | Tài xế / app, bản đồ | Trạm kín → trạm mới | 4 phút | 🔴 Bottleneck |
| 6 | Gọi tổng đài nhờ tra cứu | Tài xế → Tổng đài | Câu hỏi → chỉ dẫn qua điện thoại | 5 phút | 🔄 Handoff: tài xế sang nhân viên |

**Tổng cộng *(giả định)*: 12 phút/lượt nếu trạm còn trụ (bước 1-4); 21 phút/lượt nếu hết trụ và phải gọi tổng đài (bước 1-6).**

**Vì sao các bước 3-5 là điểm nghẽn:** từng thông tin có thể tra được, nhưng tài xế phải tự ghép nhiều yếu tố cùng lúc. Tình trạng trụ còn thay đổi giữa lúc lập kế hoạch và lúc đến nơi. Báo chí ghi nhận nhiều điểm sạc ở Hà Nội kín chỗ vào giờ cao điểm.

## 3.2. Problem Statement (6-field)

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Người dùng chính: tài xế/chủ ô tô điện VinFast trên chuyến đi liên tỉnh. Người vận hành: nhân viên tổng đài xử lý cuộc gọi hỏi trạm sạc. |
| **2. Current Workflow** | Tài xế xem mức pin trên xe, tìm trạm trên app hoặc bản đồ, so loại cổng, công suất và trụ trống, tự tính pin khi đến trạm và thời gian sạc. Nếu đến nơi hết trụ thì tìm lại hoặc gọi tổng đài. Khoảng 12-21 phút/lượt *(giả định)*. |
| **3. Bottleneck** | Bước 3-5: ghép tầm pin, loại cổng, công suất và tình trạng trụ thành một quyết định, rồi phải làm lại khi trạm đã kín. |
| **4. Business Impact** | **Bối cảnh công khai:** V-GREEN có khoảng 150.000 cổng sạc cho ô tô và xe máy điện theo báo chí; một số điểm ở Hà Nội thường xuyên kín giờ cao điểm. **Chưa có số nội bộ** về số lượt lập kế hoạch, số cuộc gọi tổng đài hay tỉ lệ đến nơi hết trụ. Công thức cần đo: `số lượt/ngày × phút tiết kiệm`. Ví dụ minh họa *(giả định)*: 1.000 lượt/ngày × 12 phút ≈ 200 giờ tài xế/ngày. |
| **5. Success Metric** | 1. Thời gian có phương án sạc: từ baseline đo được xuống **dưới 1 phút**.<br>2. Phương án đúng loại cổng và trong tầm pin có dự phòng: **100%** trên bộ 200 kịch bản test.<br>3. Đến nơi hết trụ mà không được báo trước: **giảm 50%** so với baseline.<br>4. Cuộc gọi tổng đài hỏi trạm sạc: **giảm 30%** so với baseline.<br>5. Phản hồi p95: **dưới 5 giây**. |
| **6. Operational Boundary** | **AI được phép:** hiểu yêu cầu của tài xế, đọc dữ liệu xe và trạm qua API, giải thích phương án do rule chọn.<br>**TUYỆT ĐỐI KHÔNG:** tự nghĩ ra trạm, số pin hoặc tình trạng trụ; tự chọn trạm ngoài danh sách rule đã duyệt; khẳng định còn trụ khi dữ liệu cũ hơn 5 phút; bảo tài xế đi tiếp khi không đủ tầm pin; tự đặt chỗ, tự thanh toán hay điều khiển xe.<br>**Cần duyệt:** tài xế xác nhận trước khi bắt đầu dẫn đường. Khi không có trạm trong tầm, chuyển tổng đài/cứu hộ. Khi xe đang chạy, chỉ tương tác bằng giọng nói. |

## 3.3. Future-State Flow & AI Fit

**AI Fit:** [x] Rule / State-Machine  [x] LLM Feature  [ ] Agentic Loop

| Lựa chọn | Làm tốt | Điểm yếu với bài toán này | Kết luận |
|---|---|---|---|
| **Rule / thuật toán** | Tính tầm pin, khớp cổng, xếp hạng trạm; kiểm chứng được, không bịa | Không hiểu yêu cầu tự do như "trưa muốn nghỉ ăn" | **Giữ mọi quyết định an toàn** |
| **LLM Feature** | Hiểu yêu cầu tự do, giải thích dễ hiểu bằng tiếng Việt | Có thể bịa số liệu nếu được quyền chọn trạm | **Chỉ làm lớp đầu vào và diễn giải** |
| **Agentic Loop** | Linh hoạt khi nhiều bước không biết trước | Luồng ở đây cố định; thêm độ trễ, chi phí và khó kiểm chứng | **Không dùng** |

Giá trị lớn nhất đến từ phần rule. LLM chỉ đáng thêm nếu dữ liệu cho thấy tài xế thực sự cần diễn đạt yêu cầu tự do; nếu không, một bộ lọc thông minh là đủ.

```text
Tài xế nói/gõ: "Đi Đà Lạt, còn 60% pin, trưa muốn nghỉ ăn"
   │
   ▼
🔵 AI Step: LLM trích JSON (điểm đến, giờ đi, điểm dừng mong muốn)
   │   ↩️ Fallback: thiếu thông tin → hỏi lại 1 câu
   │                vẫn không rõ, lỗi hoặc timeout → mở form tìm trạm thường
   ▼
⚙️ Rule: đọc API xe và trạm → lọc đúng cổng, đủ tầm pin có dự phòng 15%
   │   ↩️ Fallback: dữ liệu trụ cũ hơn 5 phút → gắn nhãn "chưa xác minh"
   │   ↩️ Fallback: không có trạm trong tầm → 🟢 chuyển tổng đài/cứu hộ
   ▼
⚙️ Rule: xếp hạng và trả về tối đa 3 phương án
   │
   ▼
🔵 AI Step: LLM diễn giải đúng 3 phương án đó bằng tiếng Việt
   │   ↩️ Fallback: kiểm tra thấy tên trạm/số liệu lệch → dùng mẫu câu cố định
   ▼
🟢 Human Step (HITL): tài xế chọn và xác nhận phương án
   │
   ▼
Dẫn đường → theo dõi trạm trong lúc đi
   │   ↩️ Fallback: trạm sắp kín → báo trước, đề xuất phương án kế tiếp để tài xế chọn lại
   ▼
Sạc và đi tiếp
```

---

## Nguồn tham khảo

Thông tin công khai, không phải dữ liệu nội bộ; các nguồn chưa thống nhất về độ phủ, nên cần xác nhận với VinFast/V-GREEN.

- [Vietnamnet — EV boom clashes with charger shortage in Vietnam](https://vietnamnet.vn/en/ev-boom-clashes-with-charger-shortage-in-vietnam-2421050.html)
- [Tuổi Trẻ News — Vietnam's EV charging sector races to unify fragmented networks](https://news.tuoitre.vn/vietnams-ev-charging-sector-races-to-unify-fragmented-networks-10326062911594651.htm)
- [Mekong Eye — Charging EVs with solar power](https://www.mekongeye.com/2025/04/21/charging-evs-with-solar-power-viet-firm-says-not-easy)
- [MoMo — Tra cứu trạm sạc VinFast](https://www.momo.vn/tien-ich-giao-thong/tram-sac/vinfast)
