# Bài làm cá nhân — Lab 02

Tài liệu này tập hợp Phase 0, 1, 2 và 6 từ worksheet. Phase 0 là worked example để tham khảo; Phase 1–2 là phần scan và quick cards cá nhân; Phase 6 cần được cá nhân tự rà soát và hoàn thiện các chỗ đánh dấu. Nguồn gốc nội dung và rubric đầy đủ: [01-worksheet.md](01-worksheet.md).

---

# 🚀 Phase 0 — worked Example: Xanh SM Intelligent Dispatcher (15 min)

*Giảng viên walk-through ví dụ thực tế từ Vin Smart Future để bạn hiểu rõ cách scoping một bài toán AI.*
Đọc chi tiết worked example tại file [02-deliverable-example.md](02-deliverable-example.md).

---

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

**Cơ sở bài làm:** Kết hợp ý tưởng cá nhân và tình huống mô phỏng cho lab. Các dòng dưới đây là **giả thuyết cần xác minh**, chưa phải kết luận từ khảo sát tại doanh nghiệp. Toàn bộ thời gian và ngưỡng chất lượng trong Phase 2 là **giả định hoặc mục tiêu đề xuất**, chưa có kết quả đo thực tế.

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vinmec | Lặp lại | Nhân viên tiếp đón trả lời nhiều câu hỏi giống nhau về giấy tờ, thủ tục và thông tin lịch hẹn. |
| 2 | Vinmec | Tốn thời gian | Nhân viên CSKH đọc từng phản hồi sau khám, phân nhóm vấn đề và chuyển đến bộ phận phụ trách. |
| 3 | Vinpearl Nha Trang | Tốn thời gian | Nhân viên đặt phòng tổng hợp yêu cầu khách đoàn qua nhiều email, dễ bỏ sót ngày ở, số phòng hoặc yêu cầu thay đổi. |
| 4 | Vinpearl Nha Trang | Pain từ người khác | Phản ánh về phòng và dịch vụ nằm ở nhiều kênh, khiến việc tổng hợp và bàn giao xử lý thiếu liền mạch. |
| 5 | Xanh SM | Pain từ người khác | Nhân viên vận hành đọc ghi chú và phản hồi để phân biệt nguyên nhân hủy chuyến, khó tìm điểm đón hoặc chờ lâu. |
| 6 | Vin Smart Future | AI có thể cải thiện | Nhân viên muốn chủ động tìm hỗ trợ tinh thần nhưng khó diễn đạt nhu cầu và tìm đúng đầu mối tiếp nhận. |
| 7 | Vin Smart Future | Tốn thời gian | Quản lý tổng hợp giờ làm, tăng ca và phản hồi nhân viên từ nhiều nguồn để phát hiện tình trạng quá tải công việc. |
| 8 | Vinmec | Pain từ người khác | Bệnh nhân còn thắc mắc về thuốc và hoạt động hỗ trợ giảm đau sau khám; bác sĩ thiếu thời gian giải thích cặn kẽ, khiến bệnh nhân chưa hiểu hoặc chưa hài lòng. |

**Nguồn ý tưởng:** Bài toán #8 do cá nhân đề xuất trong quá trình trao đổi với AI; các dòng còn lại là giả thuyết brainstorm để đối chiếu với trải nghiệm thực tế. Danh sách bao phủ đủ 4 lenses: Lặp lại, Tốn thời gian, AI có thể cải thiện (AI-upgrade), và Pain từ người khác.

---

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

**Ba bài toán được chọn:** #8 (Vinmec sau khám), #6 (kênh hỗ trợ tinh thần cá nhân tại Vin Smart Future), và #7 (tổng hợp tải công việc tại Vin Smart Future).

### Quick Problem Card 1 — Vinmec: Hỗ trợ kế hoạch điều trị và giải thích sau khám

- **Tham chiếu SCAN:** #8.
- **Bài toán một câu:** Hỗ trợ bác sĩ chuẩn bị kế hoạch điều trị và giải thích nội dung đã duyệt để bệnh nhân hiểu mục đích của từng chỉ định.
- **Công ty thành viên:** Vinmec.
- **Ai đang đau (Actor):** Bác sĩ khám ngoại trú; bệnh nhân là người nhận phần giải thích.

**Workflow thủ công hiện tại (giả định — 5 bước):**

1. Bác sĩ xem kết quả khám.
2. Bác sĩ lập kế hoạch điều trị.
3. Bác sĩ giải thích thuốc và hoạt động được chỉ định.
4. Bệnh nhân hỏi lại những nội dung chưa hiểu.
5. Bác sĩ giải thích bổ sung.

- **Bottleneck:** Chuẩn bị nội dung và giải thích lặp lại; **giả định 8 phút** trong tổng **12 phút/lượt**. Phạm vi đo là thời gian bác sĩ chuẩn bị và giải thích sau khám, chưa tính thời gian thăm khám hoặc chờ đợi.
- **AI hỗ trợ ở đâu:** Hỗ trợ bước 2–3 và 5 bằng cách tổng hợp thông tin, soạn dự thảo kế hoạch từ hồ sơ và tài liệu chuyên môn được cung cấp. Bác sĩ xem xét, điều chỉnh và duyệt kế hoạch trước khi AI diễn giải thành nội dung dễ hiểu cho bệnh nhân; AI gom câu hỏi còn lại để chuyển bác sĩ.
- **Metric đề xuất, chưa kiểm chứng:** Giảm thời gian thao tác của bác sĩ từ **baseline giả định 12 phút xuống mục tiêu ≤7 phút/lượt**, tính cả bước duyệt và sửa nội dung. Phần giải thích bao phủ **mục tiêu ≥95% ý trong checklist** của kế hoạch đã duyệt; đối chiếu từng ý để kiểm tra tính đúng và đủ.
- **Quick Architecture:** **LLM Feature** theo luồng cố định, kết hợp tài liệu được phê duyệt và bác sĩ kiểm tra.
- **Operational Boundary:** Bác sĩ quyết định kế hoạch điều trị. Phần gửi bệnh nhân bám nội dung đã duyệt; câu hỏi cần thay đổi thuốc, liều hoặc liệu trình được chuyển về bác sĩ. Khi thiếu dữ liệu, AI nêu phần cần làm rõ để bác sĩ bổ sung.
- **Phản biện về giá trị và chi phí:** Tài liệu hướng dẫn chuẩn có thể giải quyết nhiều câu hỏi thường gặp. Cần chứng minh LLM tạo thêm giá trị khi giải thích theo từng hồ sơ, đồng thời tính thời gian bác sĩ sửa lỗi vào tổng chi phí.

### Quick Problem Card 2 — Vin Smart Future: Tiếp nhận nhu cầu hỗ trợ tinh thần cá nhân

- **Tham chiếu SCAN:** #6.
- **Bài toán một câu:** Giúp nhân viên chủ động diễn đạt nhu cầu hỗ trợ và tìm đúng đầu mối theo danh mục hỗ trợ của doanh nghiệp.
- **Đơn vị áp dụng:** Vin Smart Future (bối cảnh mô phỏng).
- **Ai đang đau (Actor):** Nhân viên có nhu cầu; đầu mối hỗ trợ được doanh nghiệp chỉ định.

**Workflow thủ công hiện tại (giả định — 5 bước):**

1. Nhân viên nhận thấy cần hỗ trợ.
2. Nhân viên tìm thông tin liên hệ.
3. Nhân viên tự viết nội dung yêu cầu.
4. Nhân viên trao đổi với đầu mối để làm rõ nhu cầu.
5. Hai bên thống nhất bước tiếp theo.

- **Bottleneck:** Tìm đầu mối và diễn đạt nhu cầu ở bước 2–3; **giả định 10 phút** trong tổng **15 phút chuẩn bị/yêu cầu**, chưa tính thời gian chờ phản hồi. Thời gian chuẩn bị được tính theo phần thao tác chủ động của nhân viên trong quy trình.
- **AI hỗ trợ ở đâu:** Hỏi làm rõ ở mức cần thiết, giúp soạn bản tóm tắt và gợi ý đầu mối từ danh mục đã cung cấp; nhân viên xem, sửa và quyết định chia sẻ nội dung.
- **Metric đề xuất, chưa kiểm chứng:** Giảm thời gian chuẩn bị từ **baseline giả định 15 phút xuống mục tiêu ≤7 phút/yêu cầu**; **mục tiêu ≥90%** gợi ý đầu mối khớp đáp án của bộ tình huống mẫu; **mục tiêu 100%** nội dung chia sẻ có bước nhân viên xác nhận.
- **Quick Architecture:** **LLM Feature** kết hợp tra cứu danh mục hỗ trợ, có người tiếp nhận.
- **Operational Boundary:** Phạm vi là tiếp nhận và kết nối hỗ trợ. Nội dung cá nhân chỉ được chuyển theo lựa chọn của nhân viên; trước khi được xác nhận, nội dung được giữ ở dạng nháp. Nhu cầu vượt phạm vi được chuyển đến đầu mối chuyên môn, với sự xác nhận của nhân viên. AI không chẩn đoán hoặc đề xuất điều trị sức khỏe tinh thần.
- **Phản biện về giá trị và chi phí:** Một biểu mẫu riêng tư và danh mục liên hệ rõ ràng có thể đã đủ. Giá trị của LLM cần được kiểm chứng qua khả năng giúp nhân viên diễn đạt nhu cầu và mức độ họ sẵn sàng sử dụng.

### Quick Problem Card 3 — Vin Smart Future: Tổng hợp tải công việc để hỗ trợ điều chỉnh phân công

- **Tham chiếu SCAN:** #7.
- **Bài toán một câu:** Giúp quản lý tổng hợp dữ liệu làm việc và phản hồi tự nguyện để nhận ra đội nhóm đang chịu tải cao.
- **Đơn vị áp dụng:** Vin Smart Future (bối cảnh mô phỏng).
- **Ai đang đau (Actor):** Trưởng nhóm hoặc quản lý dự án.

**Workflow thủ công hiện tại (giả định — 5 bước):**

1. Thu thập giờ làm và tăng ca.
2. Kiểm tra dữ liệu thiếu.
3. Tổng hợp dữ liệu theo nhóm.
4. Đọc phản hồi tự nguyện của nhân viên.
5. Trao đổi với nhóm và điều chỉnh phân công.

- **Bottleneck:** Hợp nhất dữ liệu và tổng hợp phản hồi; **giả định 60 phút** trong tổng **90 phút/nhóm/tuần**. Phạm vi đo là thời gian thao tác để chuẩn bị và duyệt báo cáo, chưa tính thời gian chờ dữ liệu hoặc triển khai điều chỉnh phân công.
- **AI hỗ trợ ở đâu:** LLM tổng hợp chủ đề từ phản hồi văn bản ở bước 4. Code/rule tính giờ làm, tăng ca và áp dụng ngưỡng tải công việc do doanh nghiệp quy định ở bước 3.
- **Metric đề xuất, chưa kiểm chứng:** Giảm thời gian lập và duyệt báo cáo từ **baseline giả định 90 phút xuống mục tiêu ≤30 phút/nhóm/tuần**; phép tính trên dữ liệu mẫu đạt **mục tiêu khớp 100%** với kết quả kiểm tra độc lập.
- **Quick Architecture:** **Rule là nền tảng**, bổ sung **LLM Feature** khi có phản hồi văn bản cần tổng hợp.
- **Operational Boundary:** Báo cáo phản ánh tải công việc ở cấp nhóm; kết luận về sức khỏe tinh thần cá nhân cần căn cứ riêng. Dữ liệu thiếu phải được báo rõ, không tự điền thành số 0. Quản lý trao đổi với nhân viên trước khi quyết định điều chỉnh. Dữ liệu từ kênh hỗ trợ cá nhân ở Card 2 không tự động chuyển vào báo cáo tải công việc.
- **Phản biện về giá trị và chi phí:** Nếu dữ liệu chủ yếu là bảng giờ làm, dashboard và rule có thể đáp ứng toàn bộ nhu cầu. Khi đó, phương án phù hợp là giữ giải pháp thông thường.

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*

### Kiểm tra nội dung và các tình huống cần thử

- Danh sách SCAN gồm **8 bài toán**, bao phủ **4 lenses**; Phase 2 hoàn thiện **3 cards**, mỗi card có actor, workflow 5 bước, bottleneck, metric có số và kiến trúc sơ bộ.
- Các baseline được gắn nhãn **giả định**, các ngưỡng thành công được gắn nhãn **mục tiêu**; thời gian thao tác được phân biệt với thời gian chờ.
- Khi làm prototype, sử dụng hồ sơ và dữ liệu nhân viên **hư cấu**. Kết quả thử nghiệm chỉ được bổ sung sau khi thực sự chạy.

| Card | Tình huống cần thử | Hành vi kỳ vọng | Trạng thái |
|---|---|---|---|
| 1 — Vinmec | Bệnh nhân hỏi ngoài nội dung đã duyệt hoặc yêu cầu thay đổi thuốc, liều, liệu trình. | Chuyển câu hỏi về bác sĩ; giữ nguyên nội dung đã duyệt. | Chưa chạy thử. |
| 2 — Hỗ trợ cá nhân | Nhân viên chưa xác nhận chia sẻ bản tóm tắt. | Giữ bản nháp; chưa chuyển nội dung đến đầu mối tiếp nhận. | Chưa chạy thử. |
| 3 — Tải công việc | Một phần dữ liệu giờ làm hoặc tăng ca bị thiếu. | Báo rõ phần thiếu để bổ sung; không tự điền số 0 hoặc suy diễn sức khỏe tinh thần cá nhân. | Chưa chạy thử. |

**Bài toán đã chọn để làm Phase 3:** SCAN #8 / Quick Problem Card 1 — Vinmec: Hỗ trợ bác sĩ và giải thích sau khám. Đây là lựa chọn đã chốt với người làm bài trong phiên trao đổi; chưa có biên bản xác nhận của các thành viên nhóm hoặc kết luận GO / NOT YET / NO-GO.

---

---

# 📝 Phase 6 — REFLECTION (Cá nhân)
*Ghi nhận phản ánh của cá nhân bạn về việc phối hợp với AI trong buổi học hôm nay vào file `03-ai-log.md`. Phần dưới là khung tổng hợp từ quá trình làm worksheet; hãy bổ sung trải nghiệm và cảm nhận thật của chính bạn trước khi nộp.*

### AI đã hỗ trợ gì?

AI giúp mình brainstorm các bài toán, cấu trúc 3 Quick Problem Cards, làm rõ workflow và ranh giới bác sĩ/chatbot, rồi chuyển các quyết định đã chốt thành đặc tả Phase 4 và tiêu chí kiểm tra. AI cũng giúp phân biệt mục tiêu đề xuất với số liệu đã đo.

### AI có thể sai hoặc làm mình phải chỉnh ở đâu?

Các ý tưởng SCAN ngoài bài toán Vinmec là giả thuyết, không phải dữ liệu doanh nghiệp. Các con số thời gian và chất lượng ở Phase 2–3 cũng là giả định/mục tiêu. File JSON mẫu từng được tạo để minh họa schema nên không thể coi là bằng chứng API; trạng thái chạy thật cần được báo riêng. Mình cần kiểm tra code và kết quả chạy trước khi khẳng định hành vi prototype.

### Mình đã điều chỉnh cách dùng AI như thế nào?

Mình chốt Vinmec làm bài toán deep-dive, yêu cầu bác sĩ cung cấp/duyệt kiến thức và boundary, chatbot chỉ giải thích trong phạm vi được duyệt và chuyển câu hỏi vượt phạm vi về bác sĩ. Với prototype, mình chọn demo nhỏ: LLM chỉ chọn ID của đoạn đã duyệt, chương trình ghép nguyên văn; không để LLM tự viết lời tư vấn tự do. Mình cũng yêu cầu tách rõ log chạy thật với JSON ví dụ.

### Tự phản ánh trước khi nộp

- Điều mình trực tiếp kiểm tra/chỉnh sửa: **[bổ sung trải nghiệm thật]**
- Một điều AI đề xuất nhưng mình không dùng, và lý do: **[bổ sung]**
- Điều mình còn nghi ngờ hoặc cần xác minh: **[bổ sung]**
- Bài học cá nhân về cách dùng AI làm thought-partner: **[bổ sung bằng lời của mình]**
