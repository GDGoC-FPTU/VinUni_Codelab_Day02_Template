# 01 — Problem Scan (Cá nhân)

## Phase 1 — SCAN

Quét 5 ý tưởng theo các lens của worksheet: **Lặp lại (Repetitive)**, **Tốn thời gian (Time-consuming)**, **AI có thể tốt hơn (AI-upgrade)** và **Pain từ người khác (Stakeholder Pain)**. Các quy trình dưới đây là giả thuyết ban đầu để scoping, không phải mô tả đã được xác nhận về quy trình nội bộ của doanh nghiệp.

### Danh sách bài toán

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| 1 | VinFast | AI có thể tốt hơn (AI-upgrade) | Hỗ trợ kỹ thuật viên tổng hợp triệu chứng và thông tin kiểm tra để nêu giả thuyết nguyên nhân cần kiểm chứng; DTC/tài liệu kỹ thuật chỉ là dữ liệu bổ sung nếu được cung cấp hợp lệ, không bắt buộc cho prototype. |
| 2 | Vinhomes | Lặp lại (Repetitive) | Phân loại phản ánh cư dân, ước lượng mức ưu tiên ban đầu và gợi ý bộ phận tiếp nhận để nhân viên kiểm tra, điều hướng. |
| 3 | Vinpearl | Pain từ người khác (Stakeholder Pain) | Phân tích đánh giá khách sạn, trích xuất nội dung phàn nàn và đưa các trường hợp cần nhân viên chú ý ra xem xét. |
| 4 | VinFast | Tốn thời gian (Time-consuming) | Phân loại mô tả vấn đề xe của khách khi tiếp nhận dịch vụ và gợi ý thông tin cần hỏi thêm trước khi kỹ thuật viên kiểm tra. |
| 5 | Xanh SM | Pain từ người khác (Stakeholder Pain) | Phân tích phản hồi của khách hàng và tài xế để gom nhóm lý do hủy chuyến, hỗ trợ nhận diện các chủ đề cần xem xét. |

### Bối cảnh vận hành sơ bộ để kiểm chứng

Các luồng sau là **mô hình giả định** giúp xác định actor, điểm đau và vai trò AI cần khảo sát. Worksheet không cung cấp dữ liệu vận hành nội bộ; vì vậy tần suất thực tế, thời gian xử lý, số lượng trường hợp, quy định phân luồng và mức độ ảnh hưởng đều cần được xác minh với người làm quy trình.

#### 1. VinFast — Hỗ trợ quyết định bảo trì cho kỹ thuật viên

- **Actor:** Kỹ thuật viên dịch vụ/bảo trì; có thể có cố vấn dịch vụ tiếp nhận triệu chứng từ khách.
- **Workflow thủ công giả định:** Nhận mô tả triệu chứng và thông tin xe → tra tài liệu kỹ thuật hoặc mã DTC → đối chiếu triệu chứng với hướng dẫn → chọn bước kiểm tra → kỹ thuật viên tự kiểm tra và quyết định xử lý.
- **Pain point giả định:** Tìm kiếm và tổng hợp thông tin từ nhiều nguồn có thể tốn công; diễn giải triệu chứng tự do và liên hệ với mã lỗi có thể cần kinh nghiệm chuyên môn.
- **Tần suất:** Có thể lặp lại theo từng ca xe có vấn đề; số ca và tần suất tra cứu cần xác minh tại cơ sở dịch vụ.
- **Vai trò AI tiềm năng:** Tìm/trích dẫn thông tin từ tài liệu được duyệt, nối mô tả triệu chứng với DTC liên quan và gợi ý các bước kiểm tra ban đầu. AI chỉ hỗ trợ; kỹ thuật viên kiểm chứng tài liệu và quyết định. Không tự chẩn đoán kết luận, ra lệnh sửa chữa hoặc bỏ qua quy trình an toàn.
- **Giả định cần xác minh:** Kỹ thuật viên đang dùng nguồn tài liệu nào; dữ liệu DTC và tài liệu có thể tra cứu được không; mức độ cập nhật, quyền truy cập, quy trình phê duyệt và ranh giới an toàn áp dụng.

#### 2. Vinhomes — Phân loại phản ánh cư dân

- **Actor:** Cư dân gửi phản ánh; nhân viên tiếp nhận/chăm sóc cư dân và bộ phận vận hành liên quan.
- **Workflow thủ công giả định:** Cư dân gửi phản ánh qua một kênh tiếp nhận → nhân viên đọc nội dung → xác định loại vấn đề và mức cần chú ý → chuyển bộ phận phù hợp → nhân viên/bộ phận xác nhận và xử lý.
- **Pain point giả định:** Nội dung tự do có thể khó phân loại đồng nhất; chuyển nhầm hoặc thiếu thông tin có thể dẫn đến chuyển tiếp bổ sung.
- **Tần suất:** Phản ánh có thể phát sinh thường xuyên trong vận hành khu dân cư; số lượng, phân bố theo loại và theo kênh cần xác minh.
- **Vai trò AI tiềm năng:** Gợi ý nhãn, mức ưu tiên sơ bộ, bộ phận nhận và thông tin còn thiếu; nhân viên duyệt trước khi phân luồng, nhất là trường hợp khẩn cấp hoặc mơ hồ.
- **Giả định cần xác minh:** Các kênh tiếp nhận, taxonomy hiện tại, định nghĩa mức ưu tiên, danh sách bộ phận, SLA và cách xử lý tình huống khẩn cấp.

#### 3. Vinpearl — Phân tích đánh giá khách sạn

- **Actor:** Nhân viên trải nghiệm khách hàng/quan hệ khách hàng và quản lý khách sạn; khách lưu trú là người viết đánh giá.
- **Workflow thủ công giả định:** Nhân viên theo dõi đánh giá trên các kênh → đọc nội dung → ghi nhận chủ đề/khiếu nại → chuyển trường hợp cần chú ý cho nhân viên liên quan → phản hồi hoặc xử lý theo quy trình hiện hành.
- **Pain point giả định:** Đọc và tổng hợp nhiều đánh giá thủ công có thể tốn thời gian; phản ánh nghiêm trọng có thể khó nổi bật giữa các đánh giá thông thường.
- **Tần suất:** Phụ thuộc lượng đánh giá theo cơ sở, mùa và kênh; cần xác minh dữ liệu thực tế và quyền truy cập từng nền tảng.
- **Vai trò AI tiềm năng:** Tóm tắt, gắn chủ đề/cảm xúc, trích xuất nội dung phàn nàn và gắn cờ để nhân viên đánh giá; không tự đăng phản hồi hoặc kết luận sự việc đã được xác minh.
- **Giả định cần xác minh:** Các kênh được phép thu thập, khối lượng và ngôn ngữ đánh giá, tiêu chí ưu tiên, quy trình phản hồi và cách bảo vệ dữ liệu cá nhân.

#### 4. VinFast — Phân loại vấn đề xe lúc tiếp nhận dịch vụ

- **Actor:** Cố vấn dịch vụ hoặc nhân viên tiếp nhận; khách hàng mô tả vấn đề; kỹ thuật viên nhận thông tin để kiểm tra.
- **Workflow thủ công giả định:** Hỏi khách về biểu hiện → ghi nhận mô tả và điều kiện xảy ra → hỏi thêm chi tiết → phân loại/ghi phiếu tiếp nhận → chuyển thông tin cho kỹ thuật viên.
- **Pain point giả định:** Mô tả không chuẩn hóa hoặc thiếu chi tiết có thể khiến cần hỏi lại; cách ghi nhận có thể khác nhau giữa nhân viên.
- **Tần suất:** Có thể xuất hiện ở các lượt tiếp nhận xe cần kiểm tra; số lượt và mức độ phải hỏi bổ sung cần xác minh.
- **Vai trò AI tiềm năng:** Chuẩn hóa mô tả, gợi ý nhóm vấn đề và câu hỏi làm rõ; cố vấn dịch vụ xác nhận nội dung trước khi lưu/chuyển. Không đưa ra chẩn đoán cuối cùng hay cam kết nguyên nhân với khách.
- **Giả định cần xác minh:** Biểu mẫu tiếp nhận hiện có, nhóm phân loại, trường thông tin bắt buộc, quy trình bàn giao cho kỹ thuật viên và khả năng tích hợp với hệ thống dịch vụ.

#### 5. Xanh SM — Phân tích lý do hủy chuyến

- **Actor:** Nhân viên vận hành/phân tích; khách hàng và tài xế là các bên có thể cung cấp phản hồi về chuyến bị hủy.
- **Workflow thủ công giả định:** Ghi nhận chuyến bị hủy và phản hồi hiện có → nhân viên xem nội dung → xác định lý do → gắn nhóm lý do hoặc tổng hợp xu hướng → chuyển vấn đề cần xử lý cho đội phù hợp.
- **Pain point giả định:** Phản hồi dạng văn bản tự do có thể khó gom nhóm nhất quán; thiếu thông tin từ một phía có thể khiến nguyên nhân chưa rõ.
- **Tần suất:** Việc hủy chuyến có thể xảy ra trong vận hành thường nhật, nhưng lượng phản hồi có thể phân tích và tỷ lệ có đủ ngữ cảnh cần xác minh.
- **Vai trò AI tiềm năng:** Phân loại phản hồi thành các chủ đề, nêu mức độ không chắc chắn và tổng hợp xu hướng để nhân viên rà soát; không suy diễn nguyên nhân khi thiếu bằng chứng và không tự áp dụng chế tài cho khách/tài xế.
- **Giả định cần xác minh:** Nguồn phản hồi (văn bản, ghi chú hay ghi âm), khả năng sử dụng dữ liệu, taxonomy lý do, cách xử lý trường hợp hai phía bất đồng và người nhận kết quả phân tích.

### Ghi chú về dữ liệu và kiểm chứng

- Các pain point, workflow và tần suất ở trên là giả thuyết scoping, không phải dữ kiện nội bộ đã xác nhận.
- Chưa gán số liệu về lượng hồ sơ/chuyến/đánh giá, thời gian xử lý, chi phí, SLA hay tỷ lệ lỗi. Cần phỏng vấn actor và xem quy trình/log được phép sử dụng trước khi đặt baseline hoặc metric định lượng.
- Lens được gán là lens nổi bật nhất cho từng ý tưởng; có thể có nhiều lens phù hợp. Ví dụ, phân loại phản ánh cư dân cũng có thể tiết kiệm thời gian, và phân tích review cũng có thể hỗ trợ phát hiện pain point.
- Với các trường hợp liên quan đến an toàn xe, AI chỉ nên hỗ trợ tra cứu/gợi ý có nguồn; kỹ thuật viên vẫn chịu trách nhiệm đánh giá và quyết định.

## Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

> **Cách đọc:** Quy trình, điểm đau và tần suất trong các thẻ là giả thuyết scoping kế thừa từ Phase 1, chưa được xác minh với doanh nghiệp. Chưa có baseline thực tế, nên metric được viết thành phép đo và chỗ trống để điền sau khi khảo sát; không đặt mục tiêu số liệu giả định.

### QUICK PROBLEM CARD #1 — VinFast: Hỗ trợ quyết định bảo trì

- **Bài toán (1 câu):** Hỗ trợ kỹ thuật viên tổng hợp triệu chứng khách hàng, lịch sử bảo dưỡng giả lập và kết quả quan sát/kiểm tra để nêu các giả thuyết nguyên nhân cần kiểm chứng cùng thông tin còn thiếu.
- **Công ty thành viên:** [x] VinFast
- **Ai đang đau (Actor)?** Kỹ thuật viên đánh giá nguyên nhân; nhân viên tiếp nhận thu thập thông tin khách hàng/xe và mô tả vấn đề. Đây là vai trò theo quan sát cá nhân, chưa xác minh là chức danh/quy trình thống nhất ở mọi trung tâm.
- **Workflow thủ công hiện tại (5 bước gộp từ quan sát cá nhân):** (1) Nhân viên hỏi thông tin khách hàng, tra VIN và lịch sử bảo dưỡng → (2) hỏi khách về vấn đề xe → (3) kỹ thuật viên quan sát, kiểm tra trực tiếp và chạy thử khi phù hợp → (4) kỹ thuật viên đánh giá nguyên nhân từ kết quả kiểm tra và kinh nghiệm → (5) thông báo lỗi, phương án sửa chữa và báo giá; khách quyết định có đồng ý sửa chữa hay không. Đây là trải nghiệm cá nhân, không khẳng định quy trình thống nhất ở mọi trung tâm.
- **Bước nào tốn thời gian/lỗi nhất?** **Giả thuyết cần kiểm chứng:** tổng hợp triệu chứng và kết quả kiểm tra để hình thành/đối chiếu giả thuyết nguyên nhân ở bước đánh giá của kỹ thuật viên. Chưa có quan sát đủ để kết luận đây là bottleneck. Phút/lượt: **chưa có dữ liệu; cần đo baseline**.
- **AI có thể nhảy vào hỗ trợ ở bước nào?** Sau khi có mô tả triệu chứng, lịch sử bảo dưỡng giả lập và ghi chú quan sát/kiểm tra/chạy thử: sắp xếp bằng chứng, nêu giả thuyết nguyên nhân cần kiểm chứng và liệt kê thông tin còn thiếu. DTC chỉ là đầu vào tùy chọn nếu được cung cấp hợp lệ; không giả định luôn có.
- **Đo thành công bằng gì (metric có số)?** **KPI chính:** thời gian từ tiếp nhận xe đến khi khách quyết định sửa chữa; ước tính cá nhân khoảng **20 phút/xe**, mục tiêu đề xuất **15 phút/xe** (giảm 25%), chưa phải baseline đo trên nhiều ca hoặc kết quả đã đạt. Theo dõi thêm thời gian tổng hợp/đánh giá sơ bộ, tỷ lệ giả thuyết có căn cứ (%) và tỷ lệ gợi ý không có căn cứ (%); cần rubric và dữ liệu để đo.
- **Quick Architecture:** [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent — LLM có thể tổng hợp mô tả/ghi chú tự do; chỉ đưa giả thuyết kèm bằng chứng, không ra quyết định hay hành động.
- **Tính khả thi sơ bộ:** Có thể làm prototype trên hồ sơ xe hoàn toàn giả lập với triệu chứng, lịch sử bảo dưỡng mẫu và ghi chú kiểm tra. Tính đại diện cho thực tế, nguồn tài liệu được phép dùng và tiêu chuẩn đánh giá cần xác minh.
- **Rủi ro / ranh giới:** Giả thuyết sai hoặc thiếu căn cứ có thể gây thiên lệch cho đánh giá kỹ thuật. Kỹ thuật viên phải kiểm tra dữ liệu gốc và tự quyết định. AI không tự kết luận lỗi, quyết định sửa chữa, báo giá hay đưa hướng dẫn kỹ thuật không có căn cứ.
- **Giả định cần kiểm chứng:** Workflow khác nhau thế nào giữa trung tâm/loại ca; kỹ thuật viên có dùng tài liệu hoặc máy chẩn đoán ở một số trường hợp nào; dữ liệu giả lập phản ánh đủ tình huống; tiêu chí nào xác định giả thuyết có căn cứ và hữu ích.

### QUICK PROBLEM CARD #2 — Vinhomes: Phân loại và điều hướng phản ánh cư dân

- **Bài toán (1 câu):** Gợi ý loại phản ánh, mức ưu tiên ban đầu và bộ phận tiếp nhận để nhân viên rà soát trước khi điều hướng.
- **Công ty thành viên:** [x] Vinhomes
- **Ai đang đau (Actor)?** Nhân viên tiếp nhận/chăm sóc cư dân và bộ phận vận hành; cư dân là người gửi phản ánh.
- **Workflow thủ công hiện tại (3–5 bước, giả định):** Nhận phản ánh → đọc nội dung → xác định loại và mức cần chú ý → chuyển bộ phận phù hợp → nhân viên/bộ phận xác nhận và xử lý.
- **Bước nào tốn thời gian/lỗi nhất?** Giả thuyết: phân loại nội dung tự do và chọn đúng bộ phận; có thể phát sinh chuyển tiếp nếu thiếu thông tin. Phút/lượt: **chưa có dữ liệu; cần đo baseline**.
- **AI có thể nhảy vào hỗ trợ ở bước nào?** Sau khi nhận nội dung: đề xuất nhãn, thông tin còn thiếu, ưu tiên sơ bộ và bộ phận phù hợp; nhân viên duyệt trước khi chuyển, đặc biệt khi nội dung khẩn cấp hoặc mơ hồ.
- **Đo thành công bằng gì (metric có số)?** Thời gian từ tiếp nhận đến phân loại (phút; baseline ___ → mục tiêu ___); tỷ lệ phân loại/bộ phận gợi ý được nhân viên chấp nhận (%); tỷ lệ phải chuyển lại (%). Ngưỡng cần xác lập từ baseline và quy trình.
- **Quick Architecture:** [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent — taxonomy rõ thì rule có thể đủ; LLM chỉ đáng thử nếu nội dung tự do khó xử lý bằng quy tắc.
- **Tính khả thi sơ bộ:** Có thể làm prototype với ví dụ phản ánh đã ẩn danh, taxonomy và bộ phận nhận đã được xác nhận. Chưa biết các dữ liệu này có sẵn hoặc được phép dùng hay không.
- **Rủi ro / ranh giới:** Gắn nhãn ưu tiên sai hoặc chuyển nhầm có thể làm chậm xử lý. AI chỉ đề xuất; nhân viên duyệt. Cần quy trình xử lý riêng cho tình huống khẩn cấp và không để hệ thống tự đóng phản ánh.
- **Giả định cần kiểm chứng:** Kênh tiếp nhận, taxonomy, danh mục bộ phận, tiêu chí ưu tiên, quy trình khẩn cấp và cách đo chuyển nhầm/chuyển lại.

### QUICK PROBLEM CARD #3 — Vinpearl: Phân tích review và gắn cờ phàn nàn

- **Bài toán (1 câu):** Tóm tắt đánh giá khách sạn, trích xuất chủ đề phàn nàn và gắn cờ để nhân viên xem xét trường hợp cần chú ý.
- **Công ty thành viên:** [x] Khác (Vinpearl)
- **Ai đang đau (Actor)?** Nhân viên trải nghiệm/quan hệ khách hàng và quản lý khách sạn; khách lưu trú là người viết review.
- **Workflow thủ công hiện tại (3–5 bước, giả định):** Theo dõi review trên các kênh → đọc nội dung → ghi nhận chủ đề/phàn nàn → chuyển trường hợp cần chú ý → nhân viên xem xét và phản hồi/xử lý.
- **Bước nào tốn thời gian/lỗi nhất?** Giả thuyết: đọc và tổng hợp review từ nhiều kênh; nội dung cần chú ý có thể khó nổi bật. Phút/lượt: **chưa có dữ liệu; cần đo baseline**.
- **AI có thể nhảy vào hỗ trợ ở bước nào?** Sau khi review được thu thập hợp lệ: tóm tắt, gắn chủ đề, trích đoạn làm căn cứ và gắn cờ theo tiêu chí nhân viên xác nhận; không tự đăng phản hồi.
- **Đo thành công bằng gì (metric có số)?** Thời gian rà soát mỗi review (phút; baseline ___ → mục tiêu ___); precision/recall của cờ phàn nàn cần chú ý trên tập review được người phụ trách gán nhãn (%); tỷ lệ tóm tắt được nhân viên chấp nhận (%). Chưa có baseline hay nhãn chuẩn.
- **Quick Architecture:** [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent — LLM phù hợp cho tóm tắt/trích xuất ngôn ngữ tự do; rule có thể dùng cho từ khóa/điều kiện đơn giản.
- **Tính khả thi sơ bộ:** Prototype tương đối khả thi nếu có tập review được phép sử dụng, đã ẩn danh khi cần, và nhãn đánh giá của nhân viên. Khả năng truy cập dữ liệu các nền tảng chưa xác minh.
- **Rủi ro / ranh giới:** Hiểu sai mỉa mai/ngữ cảnh, gắn cờ thiếu hoặc quá mức, lộ dữ liệu cá nhân. Nhân viên kiểm tra nội dung gốc trước khi xử lý; AI không kết luận sự việc đúng/sai hay tự phản hồi khách.
- **Giả định cần kiểm chứng:** Kênh và quyền thu thập review, ngôn ngữ/khối lượng, tiêu chí gắn cờ, quy trình escalation và yêu cầu bảo vệ dữ liệu.

### So sánh sơ bộ ba ý tưởng

Đánh giá dưới đây là định tính để chọn hướng khảo sát tiếp, không khẳng định dữ liệu hay năng lực vận hành hiện có.

| Tiêu chí | VinFast — Hỗ trợ bảo trì | Vinhomes — Phân loại phản ánh | Vinpearl — Phân tích review |
|---|---|---|---|
| **Độ rõ của pain** | Luồng sáu bước cụ thể từ trải nghiệm cá nhân; pain tại bước đánh giá nguyên nhân vẫn là giả thuyết, chưa được chứng minh. | Khá rõ ở cấp quy trình: đọc, phân loại và điều hướng; mức độ chuyển nhầm/chậm chưa có dữ liệu. | Khá rõ ở cấp tác vụ: đọc và tổng hợp review; khối lượng thực tế chưa biết. |
| **AI fit** | Có thể phù hợp để tổng hợp dữ liệu mô tả tự do và nêu giả thuyết có căn cứ; quyết định kỹ thuật thuộc về kỹ thuật viên. | Trung bình–khá: rule có thể đủ nếu taxonomy ổn định; LLM hữu ích hơn với nội dung tự do. | Cao cho tóm tắt/trích xuất chủ đề từ văn bản; gắn cờ cần tiêu chí được người phụ trách xác nhận. |
| **Khả thi prototype** | Khá khả thi với ca xe giả lập và đầu ra được kỹ thuật viên/giảng viên đánh giá theo rubric; chưa chứng minh tính đại diện hoặc giá trị thực tế. | Trung bình–cao nếu có ví dụ đã ẩn danh, taxonomy và nhãn/bộ phận chuẩn. | Cao tương đối nếu có review hợp lệ và người gán nhãn; phụ thuộc quyền truy cập và chất lượng dữ liệu. |
| **Khả dụng dữ liệu** | Có thể tự tạo dữ liệu giả lập; không dùng VIN, khách hàng hay lịch sử xe thật. Khả năng có dữ liệu hợp lệ ngoài prototype chưa rõ. | Chưa rõ; cần mẫu phản ánh và danh mục phân loại đã xác nhận. | Chưa rõ; cần xác minh nguồn, quyền thu thập, ngôn ngữ và dữ liệu gán nhãn. |
| **An toàn / rủi ro** | Cao do liên quan đánh giá kỹ thuật xe; AI chỉ nêu giả thuyết kèm bằng chứng, kỹ thuật viên kiểm tra và quyết định. | Rủi ro trung bình; phân loại/ưu tiên sai có thể làm chậm xử lý, cần người duyệt và luồng khẩn cấp. | Rủi ro trung bình; sai ngữ cảnh, bỏ sót/gắn cờ nhầm và dữ liệu cá nhân cần được kiểm soát. |
| **Khả năng đánh giá** | Đo thời gian tổng hợp, mức độ giả thuyết có bằng chứng và khả năng nhận diện thông tin còn thiếu; cần rubric tham chiếu chuyên môn. | Đo được bằng thời gian, tỷ lệ chấp nhận nhãn và tỷ lệ chuyển lại; cần taxonomy/nhãn chuẩn. | Đo được bằng thời gian và precision/recall trên tập review gán nhãn; cần tiêu chí “cần chú ý” rõ. |

### Bài toán được chọn để đào sâu

**VinFast — AI hỗ trợ kỹ thuật viên đánh giá nguyên nhân sự cố xe khi bảo hành/sửa chữa.** Lý do chọn: bạn có trải nghiệm cá nhân để mô tả workflow sáu bước cụ thể hơn và có thể dùng dữ liệu hoàn toàn giả lập để xây prototype. Đây là lợi thế về hiểu bối cảnh và khả năng scoping, **không phải bằng chứng rằng VinFast có bottleneck hoặc pain point đã được chứng minh**. Bottleneck, tính đại diện của workflow và giá trị AI đều cần kiểm chứng.
