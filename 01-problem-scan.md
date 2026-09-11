Beautifful_Lưu Xuân Dũng_2A202602746
# 01 — Problem Scan & Quick Assessment

**Vai trò:** AI Product Engineer, Vin Smart Future  
**Lưu ý:** Các ước lượng thời gian/khối lượng trong tài liệu này là giả định để scoping bài lab; cần xác minh bằng log vận hành trước khi triển khai.

## Phase 1 — Scan cơ hội

| # | Công ty thành viên | Lens | Bài toán / bottleneck quan sát được |
|---:|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Khi tài xế báo pin thấp, điều phối viên phải lần lượt kiểm tra GPS, mức pin, trạm sạc, khả năng tương thích và soạn hướng dẫn. Việc chuyển giữa nhiều màn hình làm chậm phản hồi sự cố. |
| 2 | Vinhomes | Lặp lại | Ban quản lý nhận nhiều phản ánh cư dân qua app (mất nước, đèn hỏng, tiếng ồn). Nhân viên đọc, phân loại và chuyển ticket thủ công nên dễ gửi sai đội phụ trách. |
| 3 | VinFast | Lặp lại | Đối soát hóa đơn sạc từ đối tác với phiên sạc và hệ thống tài chính đòi hỏi kiểm tra các bản ghi lệch mã, thời gian hoặc số tiền. |
| 4 | Vinpearl | Pain từ người khác | Quản lý khách sạn phải đọc review từ nhiều kênh để phát hiện khiếu nại khẩn cấp; phản hồi chậm có thể ảnh hưởng trải nghiệm khách đang lưu trú. |
| 5 | Vinmec | Tốn thời gian | Bác sĩ tổng hợp thông tin từ bệnh án, xét nghiệm và ghi chú để soạn bản tóm tắt xuất viện dễ hiểu cho bệnh nhân; đây là tác vụ nhiều văn bản và cần kiểm tra nghiêm ngặt. |

## Phase 2 — Quick Problem Cards

### Quick Problem Card #1 — Đồng phi công điều phối sự cố pin Xanh SM

- **Bài toán:** Rút ngắn thời gian tạo phương án hỗ trợ an toàn khi tài xế Xanh SM báo pin thấp trên đường.
- **Công ty thành viên:** Xanh SM.
- **Ai đang đau:** Điều phối viên, tài xế đang chờ hướng dẫn và khách có cuốc xe bị ảnh hưởng.
- **Workflow hiện tại:**
  1. Tài xế gọi/chat báo sự cố và cung cấp biển số.
  2. Điều phối viên mở hệ thống để tra GPS, phần trăm pin và mẫu xe. 🔄
  3. Điều phối viên tra dashboard trạm sạc, kiểm tra khoảng cách, loại cổng và chỗ trống. 🔴
  4. Điều phối viên tự soạn tin hướng dẫn hoặc gọi cứu hộ, sau đó gửi cho tài xế. 🔴
- **Bước chậm/lỗi nhất:** Tra cứu trạm phù hợp và soạn hướng dẫn: giả định 8–10 phút/lượt; có rủi ro chỉ dẫn trạm quá xa khi pin rất thấp.
- **AI hỗ trợ:** Rule engine lọc các điều kiện an toàn; LLM tạo bản nháp hướng dẫn từ dữ liệu đã được lọc.
- **Metric pilot:** Giảm median handling time từ baseline cần đo xuống dưới 3 phút; ít nhất 98% đề xuất đúng loại cổng sạc; 100% case pin dưới 5% được chuyển cứu hộ hoặc người duyệt xử lý.
- **Quick architecture:** **Rule + LLM feature**, không dùng agent tự trị.

### Quick Problem Card #2 — Phân loại và điều hướng phản ánh cư dân Vinhomes

- **Bài toán:** Tự động tạo bản nháp phân loại và tuyến xử lý cho phản ánh cư dân nhưng không tự đóng ticket.
- **Công ty thành viên:** Vinhomes.
- **Ai đang đau:** Nhân viên CSKH/ban quản lý tòa nhà, đội kỹ thuật và cư dân chờ phản hồi.
- **Workflow hiện tại:**
  1. Cư dân gửi phản ánh kèm văn bản/ảnh qua app.
  2. CSKH đọc nội dung và kiểm tra tòa, căn hộ, mức độ khẩn. 🔴
  3. CSKH chọn danh mục và chuyển ticket cho đội kỹ thuật/an ninh/vệ sinh. 🔄
  4. Đội nhận ticket xác nhận và phản hồi cư dân.
- **Bước chậm/lỗi nhất:** Đọc nội dung tự do và xác định đúng đội xử lý; giả định 3–5 phút/ticket, đặc biệt khi thiếu thông tin vị trí.
- **AI hỗ trợ:** LLM trích xuất chủ đề, vị trí, mức độ khẩn và tạo bản nháp route; rule ưu tiên các từ khóa an toàn (cháy, rò điện, mất nước diện rộng).
- **Metric pilot:** 85% ticket được gợi ý đúng danh mục trong dưới 10 giây; giảm 30% ticket bị chuyển sai; 100% ticket khẩn được gắn cờ để người trực duyệt.
- **Quick architecture:** **Rule + LLM feature**; cần HITL trước khi gửi/đóng ticket.

### Quick Problem Card #3 — Tóm tắt review khẩn cấp cho Vinpearl

- **Bài toán:** Hỗ trợ quản lý nhận biết sớm nhóm khiếu nại lặp lại hoặc khẩn cấp trong review của khách.
- **Công ty thành viên:** Vinpearl.
- **Ai đang đau:** Duty manager, đội vận hành khách sạn và khách đang lưu trú.
- **Workflow hiện tại:**
  1. Nhân viên tải/đọc review từ các kênh.
  2. Nhân viên đánh dấu chủ đề và mức độ tiêu cực. 🔴
  3. Tổng hợp thủ công thành báo cáo ca/ngày. 🔴
  4. Quản lý phân công điều tra hoặc phản hồi.
- **Bước chậm/lỗi nhất:** Tổng hợp văn bản đa ngôn ngữ và phát hiện mẫu lặp; giả định 30–45 phút/ca.
- **AI hỗ trợ:** LLM phân cụm chủ đề, tóm tắt bằng chứng và tạo danh sách cảnh báo; nhân viên xác minh review gốc trước khi hành động.
- **Metric pilot:** Báo cáo ca hoàn thành trong dưới 10 phút; recall ít nhất 90% review có từ khóa khẩn theo tập nhãn mẫu; không tự đăng phản hồi công khai.
- **Quick architecture:** **LLM feature**; không cần agent vì đầu ra chỉ là báo cáo nội bộ.

## Lựa chọn để deep-dive

Nhóm chọn **Quick Problem Card #1**. Đây là quy trình có đầu vào và đầu ra rõ, tác động vận hành thời gian thực, đồng thời có thể kiểm soát rủi ro bằng rule cứng, Human-in-the-loop (HITL) và fallback thủ công. Các con số sẽ được đo lại từ log tối thiểu 2 tuần trước khi chốt business case.
