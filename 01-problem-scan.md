# Lab 02 — Worksheet: AI Product Scoping (Vin Smart Future)

---

## 🏛️ 1. Bối cảnh thực tế: Vin Smart Future (Vingroup)

**Vingroup** — Tập đoàn tư nhân lớn nhất Việt Nam — vừa sáp nhập toàn bộ các phòng ban công nghệ thuộc các công ty thành viên thành một đơn vị công nghệ thống nhất mang tên **Vin Smart Future**. 

Nhiệm vụ của **Vin Smart Future** là xây dựng các giải pháp AI, số hóa, và tự động hóa cốt lõi để nâng cao hiệu suất vận hành và trải nghiệm khách hàng xuyên suốt các công ty thành viên:
* 🚗 **VinFast:** Hệ thống xe điện thông minh (EV), trợ lý AI ảo trong xe, dự đoán bảo trì pin, và quản lý chuỗi cung ứng sản xuất.
* 🚕 **Xanh SM (GSM):** Vận hành đội xe taxi/xe máy điện thông minh, điều vận thông minh (Smart Dispatching), tối ưu hóa lộ trình di chuyển.
* 🏢 **Vinhomes:** Quản lý đô thị thông minh (Smart Cities), trợ lý cư dân thông minh, tối ưu hóa mức tiêu thụ năng lượng.
* 🏥 **Vinmec:** Y tế thông minh, chẩn đoán hình ảnh bằng AI, tối ưu hóa quản lý hồ sơ bệnh án.
* 🎢 **Vinpearl / VinWonders:** Trải nghiệm du lịch số hóa, quản lý phòng và luồng khách thông minh tại các khu vui chơi.

Trong buổi Lab hôm nay, nhóm của bạn sẽ đóng vai trò là **AI Product Engineer** tại **Vin Smart Future**, tiến hành tìm kiếm, scoping, phân tích độ khả thi, thiết lập ranh giới vận hành, và xây dựng một **bản mẫu kỹ thuật (prompt prototype)** cho một bài toán cụ thể thuộc một trong những mảng kinh doanh trên.

---

## 📊 2. Cơ cấu tính điểm bài lab

### 👥 Điểm nhóm (60 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **G1. Workflow Mapping** | 20 | Problem Deep-Dive | Vẽ chi tiết quy trình hiện tại: các bước, handoff, thời gian, bottleneck |
| **G2. Problem Statement** | 20 | Problem Deep-Dive | Problem Statement 6-field bám sát thực tế, metric có số và ranh giới rõ ràng |
| **G3. AI Fit & Future Flow** | 10 | Problem Deep-Dive | So sánh Rule vs LLM vs Agent, future flow có bước AI, ranh giới và Fallback |
| **G4. Decision Quality** | 10 | Problem Deep-Dive | Quyết định Go/Not Yet/No-Go trung thực và có chứng cứ rõ ràng |

### 👤 Điểm cá nhân (40 điểm)

| Gate | Điểm | Deliverable | Tiêu chí chấm |
|---|---:|---|---|
| **I1. Scan & Cards** | 15 | Quick Cards | Liệt kê 5 problems sử dụng 3 lenses, hoàn thiện 3 quick cards chất lượng |
| **I2. Prototyping** | 10 | 02-lab/ | Chạy thử nghiệm programmatic prompt prototype thành công |
| **I3. AI Log & Reflection** | 15 | 03-ai-log.md | Phản ánh trung thực về việc dùng AI làm thought-partner (giúp gì, sai gì, sửa gì) |

---

# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

*Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI.*
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Xanh SM | Lặp lại + Tốn thời gian | Phân loại khiếu nại và chuyển ticket đến đúng bộ phận đang được xử lý thủ công; ước tính 8 phút/khiếu nại, với 3.000 khiếu nại/ngày tương đương khoảng 400 giờ công/ngày. |
| 2 | Xanh SM | Stakeholder Pain | Điều phối lại chuyến khi tài xế hủy hoặc không nhận cuốc; mỗi sự cố có thể mất khoảng 5 phút và làm thời gian chờ của khách tăng thêm 3-7 phút. |
| 3 | Xanh SM | Lặp lại + Tốn thời gian | Đối soát chuyến đi, doanh thu và phụ phí giữa ứng dụng, hệ thống thanh toán và báo cáo tài xế; ước tính 3 phút/giao dịch, với 20.000 giao dịch/ngày cần khoảng 1.000 giờ công kiểm tra. |
| 4 | Xanh SM | AI-upgrade + Stakeholder Pain | Phát hiện và xử lý các trường hợp điểm đón sai do địa chỉ hoặc GPS không chính xác; khoảng 2.000 trường hợp/ngày, mỗi trường hợp mất 6 phút và có thể làm khách chờ thêm 5-10 phút. |
| 5 | Xanh SM | Lặp lại + AI-upgrade | Lập lịch sạc và bảo trì xe bằng bảng tính dựa trên mức pin, lịch sử sử dụng và tình trạng xe; ước tính 4 phút/xe cho 500 xe/ngày, đồng thời có nguy cơ làm giảm 5-10% thời gian xe hoạt động nếu phân bổ chưa tối ưu. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

### QUICK PROBLEM CARD #1 — Phân loại khiếu nại khách hàng

**Bài toán (1 câu):** Nhân viên đang đọc và phân loại thủ công khiếu nại của khách hàng trước khi chuyển đến bộ phận phụ trách, làm chậm thời gian phản hồi.

**Công ty thành viên:** [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Khác

**Ai đang đau (Actor)?** Nhân viên chăm sóc khách hàng, bộ phận vận hành xử lý khiếu nại và khách hàng chờ phản hồi.

**Workflow thủ công hiện tại:**
1. Nhận tin nhắn/cuộc gọi khiếu nại -> 2. Đọc và hiểu nội dung -> 3. Gán nhóm lỗi và mức độ ưu tiên -> 4. Chuyển ticket -> 5. Soạn phản hồi ban đầu.

**Bước tốn thời gian/lỗi nhất:** Đọc, phân loại và chuyển ticket, khoảng **8 phút/khiếu nại**. Với giả định 3.000 khiếu nại/ngày, khối lượng tương đương khoảng 400 giờ công/ngày.

**AI có thể hỗ trợ:** Trích xuất ý định, mã chuyến, nhóm lỗi và mức độ khẩn cấp; đề xuất bộ phận xử lý và tạo bản nháp phản hồi.

**Metric thành công:**
- Giảm thời gian phân loại từ 8 phút xuống dưới 2 phút/ticket.
- Độ chính xác phân loại tối thiểu 90% trên tập kiểm thử đã được gán nhãn.
- 90% bản nháp được nhân viên chấp nhận hoặc chỉ cần chỉnh sửa nhỏ.

**Quick Architecture:** [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent

**Ranh giới:** AI chỉ phân loại và tạo bản nháp; nhân viên phải duyệt trước khi gửi. Các trường hợp đe dọa an toàn, pháp lý, hoàn tiền hoặc bồi thường phải chuyển người có thẩm quyền.

---

### QUICK PROBLEM CARD #2 — Điều phối lại chuyến bị hủy

**Bài toán (1 câu):** Khi tài xế hủy hoặc không nhận cuốc, điều phối viên phải tìm và liên hệ tài xế thay thế thủ công, làm khách chờ lâu hơn.

**Công ty thành viên:** [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Khác

**Ai đang đau (Actor)?** Điều phối viên, khách hàng đặt xe và tài xế được mời nhận chuyến thay thế.

**Workflow thủ công hiện tại:**
1. Ghi nhận chuyến bị hủy -> 2. Kiểm tra tài xế gần khu vực -> 3. Gọi hoặc gửi thông báo cho từng tài xế -> 4. Chọn tài xế đồng ý -> 5. Cập nhật chuyến và báo khách.

**Bước tốn thời gian/lỗi nhất:** Tìm và liên hệ tài xế thay thế, khoảng **5 phút/sự cố**; thời gian chờ phát sinh của khách có thể tăng 3-7 phút.

**AI có thể hỗ trợ:** Xếp hạng các tài xế phù hợp theo vị trí, trạng thái, loại xe, thời gian đến điểm đón và lịch sử nhận cuốc; soạn lời mời nhận chuyến.

**Metric thành công:**
- Giảm thời gian tìm tài xế từ 5 phút xuống dưới 1 phút.
- 85% đề xuất đầu tiên được điều phối viên chấp nhận.
- Giảm thời gian chờ phát sinh xuống dưới 2 phút.
- Giảm tỷ lệ chuyến bị hủy hoàn toàn ít nhất 20% so với baseline.

**Quick Architecture:** [ ] No AI  [x] Rule  [ ] LLM  [x] Agent

**Ranh giới:** Hệ thống chỉ đề xuất và gửi bản nháp lời mời; không tự ý phạt tài xế, hủy chuyến hoặc thay đổi giá. Nếu dữ liệu GPS lỗi hoặc không có tài xế đủ điều kiện, chuyển điều phối viên xử lý thủ công.

---

### QUICK PROBLEM CARD #3 — Lập lịch sạc và bảo trì xe

**Bài toán (1 câu):** Điều phối viên dùng bảng tính để lập lịch sạc và bảo trì, có thể khiến xe thiếu pin, xếp lịch trùng hoặc giảm thời gian sẵn sàng phục vụ.

**Công ty thành viên:** [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  [ ] Vinmec  [ ] Khác

**Ai đang đau (Actor)?** Điều phối viên đội xe, nhân viên trạm sạc/bảo trì, tài xế và khách hàng bị ảnh hưởng khi thiếu xe hoạt động.

**Workflow thủ công hiện tại:**
1. Thu thập mức pin và trạng thái xe -> 2. Kiểm tra lịch chạy -> 3. Kiểm tra công suất trạm sạc/xưởng -> 4. Lập lịch trên bảng tính -> 5. Gửi lịch và xử lý thay đổi phát sinh.

**Bước tốn thời gian/lỗi nhất:** Ghép xe, thời gian rảnh và công suất trạm, khoảng **4 phút/xe**. Với 500 xe/ngày, khối lượng lập lịch khoảng 33 giờ công/ngày.

**AI có thể hỗ trợ:** Dự báo nhu cầu xe theo khung giờ, dự báo xe sắp cần sạc/bảo trì và đề xuất lịch tối ưu theo mức pin, ca chạy, vị trí và công suất trạm.

**Metric thành công:**
- Giảm thời gian lập lịch từ 4 phút xuống dưới 1 phút/xe.
- Giảm số xe thiếu mức pin tối thiểu trước ca chạy ít nhất 30%.
- Tăng tỷ lệ xe sẵn sàng phục vụ thêm tối thiểu 5%.
- Không làm tỷ lệ trễ bảo trì định kỳ vượt quá 1%.

**Quick Architecture:** [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent

**Ranh giới:** Quyết định cuối cùng phải dựa trên các quy tắc an toàn về pin và bảo trì; AI chỉ đề xuất lịch. Xe có cảnh báo an toàn, lỗi pin hoặc bảo trì bắt buộc phải được khóa khỏi điều phối và chuyển kỹ thuật viên xác nhận.

**Lưu ý CFO/Trưởng phòng Vận hành:** Bài toán này chỉ nên triển khai sau khi có dữ liệu lịch chạy, mức pin, lịch sử bảo trì và công suất trạm đủ sạch để so sánh với baseline.

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

---
