# Báo cáo đi sâu: Xử lý khiếu nại khách hàng phức tạp của Xanh SM

## 1. Bối cảnh và ranh giới bằng chứng

**Vấn đề được chọn:** xử lý các khiếu nại phức tạp của khách hàng Xanh SM, gồm
thất lạc đồ, sai giá cước và sự cố trong chuyến đi. Mục tiêu của báo cáo là
đánh giá một trợ lý AI cho nhân viên hỗ trợ, không phải tự động hóa toàn bộ
quyết định hoặc giao tiếp với khách hàng.

Để tránh nhầm lẫn giữa dữ kiện và suy đoán, báo cáo dùng ba nhãn:

- **Dữ kiện công khai:** thông tin có thể kiểm tra từ nguồn công khai hoặc
  tài liệu nội bộ đã được dẫn trong [03-ai-log.md](03-ai-log.md). Nhật ký này
  ghi nhận các tính năng Xanh SM được công bố và bối cảnh nghiên cứu; không có
  số liệu công khai xác nhận quy trình khiếu nại hay năng suất dưới đây.
- **Giả thuyết AI:** nhận định về cơ hội dùng AI, KPI và thiết kế vận hành,
  cần được kiểm định bằng dữ liệu thực tế.
- **Giả định pilot:** các con số minh họa trong báo cáo, gồm 15 phút mỗi ca,
  100.000 chuyến/ngày và tỷ lệ khiếu nại 2%. Đây không phải số liệu nội bộ
  Xanh SM đã được xác nhận.

## 2. Quy trình hiện tại (Current-State Workflow)

Quy trình dưới đây là **giả định pilot** để lập baseline và cần được đo lại
trên dữ liệu nội bộ.

| Bước | Tác nhân | Đầu vào | Hoạt động | Đầu ra | Bàn giao | Thời gian |
|---|---|---|---|---|---|---:|
| 1. Tiếp nhận và phân loại | Nhân viên hỗ trợ | Tin nhắn/cuộc gọi, mã chuyến nếu có | Ghi nhận, xác định nhóm thất lạc đồ, sai giá hoặc sự cố chuyến | Hồ sơ khiếu nại và nhãn ban đầu | Từ khách hàng sang nhân viên xử lý | 2 phút |
| 2. Tra cứu hồ sơ | Nhân viên hỗ trợ | Hồ sơ và mã chuyến | Tìm bản ghi chuyến, giá cước, tài xế và liên hệ trước | Timeline và dữ kiện liên quan | Có thể yêu cầu bổ sung dữ liệu từ khách hàng | 5 phút — **điểm nghẽn** |
| 3. Xác minh | Nhân viên hỗ trợ, tài xế hoặc nhóm chuyên trách | Timeline, câu hỏi xác minh | Liên hệ tài xế/nhóm chuyên trách để kiểm tra sự việc | Thông tin xác minh hoặc trạng thái chưa rõ | Hỗ trợ sang tài xế/nhóm chuyên trách rồi quay lại hỗ trợ | 4 phút — **điểm nghẽn/bàn giao** |
| 4. Escalate và soạn trả lời | Nhân viên hỗ trợ, chuyên gia khi cần | Dữ kiện đã tra cứu và xác minh | Escalate ca cần thiết, soạn phản hồi cho khách | Bản nháp phản hồi và trạng thái xử lý | Sang chuyên gia/pháp chế nếu thuộc ca nhạy cảm | 3 phút |
| 5. Theo dõi và đóng ca | Nhân viên hỗ trợ | Phản hồi được duyệt, kết quả xử lý | Theo dõi phản hồi, cập nhật hồ sơ và đóng ca | Ca hoàn tất hoặc được mở lại | Thông báo kết quả cho khách; mở lại nếu còn vấn đề | 1 phút |

**Tổng thời gian giả định:** 15 phút mỗi ca (2 + 5 + 4 + 3 + 1). Thời gian
thực tế, đặc biệt ở bước 2 và 3, cần được xác nhận bằng log hệ thống và
phỏng vấn nhân viên.

## 3. Problem Statement (đủ sáu trường)

| Trường | Mô tả |
|---|---|
| **Actor / Operator** | Nhân viên hỗ trợ khách hàng Xanh SM; tài xế và nhóm chuyên trách tham gia xác minh hoặc escalation. |
| **Current Workflow / Tools** | Nhân viên tiếp nhận khiếu nại, tra cứu nhiều bản ghi chuyến/giá cước/tài xế/liên hệ trước, liên hệ người liên quan, escalation khi cần, soạn phản hồi và đóng ca. Công cụ cụ thể và mức tích hợp hiện tại cần được kiểm kê nội bộ. |
| **Bottleneck** | Tra cứu chéo hệ thống, tái dựng bối cảnh và chọn đúng tuyến xử lý chiếm nhiều thời gian; thông tin không đầy đủ có thể dẫn đến phản hồi không nhất quán. |
| **Business Impact** | **Giả định pilot:** 100.000 chuyến/ngày × 2% khiếu nại = khoảng 2.000 ca/ngày. Với 15 phút/ca, tổng nỗ lực là 30.000 phút, tương đương **500 staff-hours/ngày**. Các con số này cần được Xanh SM xác thực, không phải số liệu công bố. |
| **Success Metrics** | Giảm thời gian xử lý trung bình từ 15 xuống **dưới 8 phút**; định tuyến đúng ngay lần đầu **ít nhất 85%**; tỷ lệ mở lại **≤5%**; **0** lần gửi ra ngoài trái phép. Đây là mục tiêu giả thuyết để thử nghiệm. |
| **Operational Boundary** | AI chỉ tóm tắt dữ liệu ca đã được cấp quyền, gợi ý danh mục/tuyến xử lý và soạn bản nháp trong môi trường/provider triển khai đã được phê duyệt. Trước khi xử lý, phải tối thiểu hóa và che/ẩn PII của khách hàng, tài xế; áp dụng kiểm soát truy cập, lưu giữ và xóa dữ liệu đã phê duyệt. Không được gửi dữ liệu khách hàng chưa được phê duyệt ra ngoài môi trường được ủy quyền. AI không được tự gửi, quyết định bồi thường, đóng ca nhạy cảm, truy cập dữ liệu trái phép, bịa dữ kiện hoặc thay thế chuyên gia/pháp chế. |

## 4. AI Fit Matrix

| Phương án | Mức phù hợp | Lý do |
|---|---|---|
| **Rule / State-Machine** | Phù hợp cho lớp kiểm soát | Xử lý tốt các kiểm tra xác định như trường bắt buộc, quyền truy cập và định tuyến theo quy tắc. Tuy nhiên, không phù hợp để hiểu ngữ cảnh khiếu nại tiếng Việt nhiều sắc thái, tái dựng diễn biến hoặc soạn phản hồi tự nhiên. |
| **LLM Feature — chọn** | Cao cho pilot có kiểm soát | Phù hợp để tóm tắt hồ sơ đã được phép truy cập, gợi ý phân loại/tuyến và soạn nháp trong các ca tiếng Việt có ngữ cảnh; nhân viên vẫn kiểm tra và quyết định. |
| **Agentic Loop / Autonomous Agent — loại** | Không phù hợp ở giai đoạn này | Agent tự truy cập nhiều nguồn, liên hệ tài xế, escalation hoặc gửi kết quả có thể vượt quyền, làm lộ dữ liệu, bịa thông tin hoặc tự quyết định ca nhạy cảm. Rủi ro tự chủ và quyền hạn chưa được kiểm soát đầy đủ. |

**Quyết định:** chọn **LLM Feature**, không chọn autonomous Agent. Đây là
giả thuyết thiết kế, không phải khẳng định rằng hệ thống hiện tại đã sẵn sàng.

## 5. Luồng tương lai (Future-State Flow)

1. **Tiếp nhận và kiểm tra bằng rule:** kiểm tra quyền truy cập, mã ca/mã
   chuyến và các trường bắt buộc. Nếu thiếu trường, không đủ quyền hoặc dữ
   liệu không khả dụng, yêu cầu bổ sung hoặc chuyển sang quy trình thủ công.
   **🔵 Rule/State-Machine Step:** lớp kiểm soát xác định trước khi gọi LLM.
2. **LLM hỗ trợ:** chỉ trong deployment/provider đã được phê duyệt, giữ dữ
   liệu trong môi trường được ủy quyền và tắt việc provider dùng dữ liệu để
   huấn luyện. Trước khi xử lý, phải xóa/tokenize tên, số điện thoại, biển
   số, mã tài khoản và vị trí chính xác, trừ khi trường đó thực sự bắt buộc.
   Chỉ người đánh giá/đầu mối chất lượng CS được chỉ định mới có quyền truy
   cập. LLM tạo bản tóm tắt timeline, gợi ý danh mục/tuyến và soạn nháp;
   mọi trường không có bằng chứng phải được đánh dấu là chưa xác minh.
   Không chuyển dữ liệu khách hàng chưa được phê duyệt ra ngoài môi trường
   được ủy quyền.
   **🔵 AI Step:** LLM tóm tắt, phân loại và soạn phản hồi nháp.
3. **Kiểm tra confidence/chất lượng:** nhân viên kiểm tra độ đầy đủ, nguồn
   của dữ kiện, sự phù hợp của phân loại và chất lượng ngôn ngữ. Confidence
   thấp, mâu thuẫn dữ liệu hoặc ca nhạy cảm thì chuyển ngay sang fallback.
   **🔵 AI Step:** kết quả được kiểm tra trước khi đưa cho người duyệt.
4. **🟢 Human Step (HITL) — approval:** nhân viên có thẩm quyền duyệt/chỉnh bản nháp, quyết
   định escalation và thực hiện các hành động được phép. Không có bước gửi
   tự động.
5. **↩️ Fallback thủ công:** dùng quy trình hiện tại khi thiếu dữ liệu, hệ
   thống lỗi, confidence thấp, ca có rủi ro cao hoặc cần chuyên gia/pháp
   chế. Kết quả pilot được ghi nhận để đánh giá, không dùng để tự động học
   trực tiếp trong lúc xử lý ca.

### Loại trừ rõ ràng

- Không tự động gửi bất kỳ tin nhắn nào cho khách hàng hoặc tài xế.
- Không tự quyết định hay chi trả bồi thường.
- Không tự đóng ca nhạy cảm, tranh chấp nghiêm trọng hoặc vấn đề pháp lý.
- Không truy cập dữ liệu ngoài quyền được cấp.
- Chỉ dùng deployment/provider đã được phê duyệt; phải tối thiểu hóa và
  che/ẩn PII khách hàng, tài xế trước khi xử lý; xóa/tokenize tên, số điện
  thoại, biển số, mã tài khoản và vị trí chính xác trừ khi thực sự bắt buộc.
- Provider phải tắt việc dùng dữ liệu để huấn luyện, giữ dữ liệu trong môi
  trường được ủy quyền và không nhận dữ liệu khách hàng chưa được phê duyệt.
- Chỉ đầu mối chất lượng CS/đánh giá viên được chỉ định mới được truy cập;
  lưu prompt/output tối đa 30 ngày rồi xóa có xác minh, đồng thời audit cả
  sự kiện truy cập và xóa dữ liệu.
- Không bịa, suy diễn hoặc trình bày dữ kiện chưa xác minh như sự thật.
- Không thay thế chuyên gia vận hành, nhóm xử lý chuyên biệt hoặc rà soát
  pháp chế.

## 6. Checklist sẵn sàng cho AI

- [ ] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?
- [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát qua HITL hoặc Fallback?
- [ ] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?
- [ ] Có mẫu ca khiếu nại đã ẩn danh và được phê duyệt quyền sử dụng.
- [ ] Có baseline thời gian xử lý thực tế, tách theo loại ca.
- [ ] Có nhãn định tuyến đúng và tiêu chí chất lượng phản hồi.
- [ ] Đã kiểm kê nguồn dữ liệu, quyền truy cập và trường bắt buộc.
- [ ] Đã phê duyệt deployment/provider, quy tắc tối thiểu hóa/che PII, thời
      hạn lưu giữ/xóa và kiểm soát truy cập; provider đã tắt huấn luyện trên
      dữ liệu pilot.
- [ ] Có người chịu trách nhiệm HITL, escalation và rà soát pháp chế.
- [ ] Có log audit cho đầu vào, bản nháp, chỉnh sửa, phê duyệt và fallback.
- [ ] Có tiêu chí đo hallucination, rò rỉ dữ liệu, gửi trái phép và mở lại ca.
- [ ] Đã thống nhất ngưỡng confidence và điều kiện dừng pilot.

## 7. Quyết định: NOT YET

**NOT YET** — chưa triển khai vào luồng sản xuất. Hiện còn thiếu mẫu ca ẩn
danh, baseline thời gian, nhãn định tuyến, tiêu chí chất lượng và phê duyệt
của các bên liên quan; các metric và giả định trong báo cáo cũng cần được
kiểm chứng bằng dữ liệu nội bộ.

Bước tiếp theo được khuyến nghị là **pilot shadow-mode**: LLM chỉ tạo tóm
tắt, phân loại và bản nháp song song với quy trình hiện tại; đầu ra được ẩn
khỏi người ra quyết định vận hành và khách hàng, chỉ hiển thị cho các đầu
mối đánh giá được chỉ định trong phạm vi quyền truy cập đã phê duyệt để rà
soát offline tính đúng dữ kiện và chất lượng. Không dùng đầu ra để tự động
gửi, bồi thường hay đóng ca.
Ở shadow mode, chỉ đo các chỉ số offline: độ chính xác định tuyến, mức bao
phủ trường bắt buộc, độ đúng/sát dữ kiện và chất lượng bản nháp qua rà soát,
cùng latency. **Thời gian xử lý, tỷ lệ mở lại và định tuyến trực tiếp không
thuộc shadow mode**; các chỉ số này chỉ đo ở giai đoạn sau, là
**HITL assisted pilot**, khi đầu ra được nhân viên có thẩm quyền sử dụng và
duyệt trong quy trình thật. Chỉ xem xét chuyển giai đoạn sau khi đạt ngưỡng
đã được phê duyệt và qua rà soát an toàn.

## 8. Ghi chú nguồn và nghiên cứu

Nhật ký nghiên cứu [03-ai-log.md](03-ai-log.md) là nguồn tham chiếu cho các
fact công khai và ghi lại cách phân biệt nguồn với giả thuyết AI. Nhật ký
không xác nhận quy trình hỗ trợ, 15 phút, 100.000 chuyến/ngày, 2% khiếu nại,
500 staff-hours/ngày hay các KPI nêu trên. **Tất cả metric vận hành nội bộ
cần được Xanh SM xác thực trước khi dùng làm baseline hoặc claim về tác động.**
