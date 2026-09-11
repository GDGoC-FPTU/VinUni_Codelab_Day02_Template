# 📝 03-ai-log.md — Nhật ký tương tác AI

## 1. Mục đích sử dụng AI trong bài lab
Trong quá trình làm bài này, tôi dùng AI như một người trợ lý đồng hành để hỗ trợ nhiều bước: brainstorm bài toán, rà soát logic ở Phase 2, viết lại mô tả cho Phase 3, kiểm tra tính rõ ràng của metric, và thử nghiệm prompt prototype. AI giúp tôi tiết kiệm thời gian trong việc chuyển từ ý tưởng thô thành nội dung có cấu trúc, đồng thời giúp tôi nhìn lại bài làm từ góc độ chuyên nghiệp hơn.

Tôi không dùng AI để “viết thay toàn bộ”, mà chủ yếu dùng nó để:
- gợi ý các bài toán thực tế phù hợp với bối cảnh Vingroup,
- kiểm tra xem bài toán đã đủ cụ thể chưa,
- sửa lại câu văn cho rõ ràng và mạch lạc,
- phát hiện các điểm chưa hợp lý trong workflow hoặc metric,
- thử nghiệm giới hạn an toàn của prompt trước khi đưa vào prototype.

---

## 2. AI đã giúp tôi điều gì

### 2.1. Brainstorm bài toán và chọn top 3
Khi bắt đầu làm Phase 1, tôi chưa có nhiều ý tưởng rõ ràng. Tôi đã dùng AI để đối chiếu các bài toán theo 4 lenses: Repetitive, Time-consuming, AI-upgrade, Stakeholder Pain. AI giúp tôi nhanh chóng suy ra các pain point đáng chú ý trong môi trường VinFast, Xanh SM, Vinhomes và Vinmec.

Ví dụ, AI đã hỗ trợ tôi hình thành các idea như:
- VinFast: nhân viên kỹ thuật cần tra cứu tài liệu sửa chữa quá nhiều,
- Xanh SM: điểm đón khách chưa chính xác tại khu vực đông người,
- Vinmec: cần tổng hợp hồ sơ bệnh án trước khám.

Điều này giúp tôi xây dựng được bảng Phase 1 nhanh hơn và có tính thực tế hơn.

### 2.2. Tăng chất lượng Phase 2 và Phase 3
AI cũng giúp tôi viết lại các Quick Problem Cards để có cùng format và dễ đọc hơn. Tôi đã dùng AI để rà soát:
- Bài toán có đủ ngắn gọn và rõ trọng tâm không,
- Actor có xác định đúng không,
- Workflow có đủ 3–5 bước và bước bottleneck đã rõ chưa,
- Metric có số liệu cụ thể và khả thi không.

Sau đó, AI giúp tôi chuyển từ Phase 2 sang Phase 3 bằng cách đề xuất cấu trúc Problem Statement theo 6-field, và giúp tôi định hình Future-State Flow cùng AI Fit. Nhờ vậy, nội dung file deep-dive trở nên logic và chuyên nghiệp hơn.

### 2.3. Kiểm tra prompt và ranh giới an toàn
Trong quá trình làm Prototype, AI được dùng để kiểm tra xem prompt có đủ rõ về hành vi an toàn và giới hạn của hệ thống hay không. Tôi đã yêu cầu AI phân tích các trường hợp nguy hiểm, ví dụ khi người dùng muốn bỏ qua bước nháp hoặc yêu cầu hệ thống tự động gửi thông tin mà không cần phê duyệt.

Nhờ đó, tôi nhận ra rằng nếu không đặt rõ ranh giới, AI có thể “vượt quá giới hạn” và trả lời theo cách không phù hợp với quy trình vận hành thực tế.

---

## 3. Những lần AI trả lời sai / hallucination
AI không phải lúc nào cũng đúng, và đây là điểm quan trọng nhất tôi học được trong quá trình làm bài.

### 3.1. Sai ở phần metric
Lúc đầu, AI gợi ý các metric quá chung chung như “giảm thời gian xử lý” mà chưa có mốc cụ thể. Nếu không chỉnh lại prompt, kết quả sẽ dễ bị mơ hồ và không đủ sức thuyết phục.

Ví dụ, tôi đã sửa từ:
- “Giảm thời gian xử lý” thành
- “Giảm thời gian xác định điểm đón từ 10 phút xuống dưới 3 phút/lượt”

Điều này khiến bài báo cáo trở nên đo lường được và hợp lý hơn.

### 3.2. Sai ở phần workflow
AI ban đầu có thể mô tả workflow thiếu tính thực tế, ví dụ nhấn mạnh AI làm quá nhiều bước mà bỏ qua vai trò con người. Tôi nhận ra nếu không đặt rõ “AI chỉ gợi ý, không tự gửi đi”, bài toán sẽ vượt quá ranh giới vận hành thực tế.

Vì vậy, tôi đã yêu cầu AI tái cấu trúc nội dung theo hướng:
- AI chỉ đề xuất,
- con người mới phê duyệt,
- trường hợp không chắc chắn thì fallback về quy trình cũ.

### 3.3. Hallucination/đề xuất quá mơ hồ
AI đôi khi tạo ra các ý tưởng rất hấp dẫn nhưng thiếu bằng chứng thực tế hoặc không phù hợp với bối cảnh Vingroup. Ví dụ, AI có thể gợi ý thêm nhiều tính năng nâng cao mà thực tế không phải là ưu tiên ban đầu. Tôi đã sửa bằng cách bắt AI trả lời theo đúng khung bài toán đã chọn, không lạc sang giải pháp quá rộng.

---

## 4. Tôi đã sửa prompt và ranh giới như thế nào
Đây là phần quan trọng nhất trong quá trình làm việc với AI. Tôi nhận ra rằng prompt chất lượng tốt sẽ quyết định chất lượng đầu ra rất nhiều.

### 4.1. Thay vì hỏi “hãy giúp tôi làm bài”, tôi hỏi theo cấu trúc rõ ràng
Tôi đã bắt đầu dùng prompt kiểu:
- “Hãy đóng vai trò là người viết báo cáo Vin Smart Future.”
- “Chỉ tập trung vào bài toán Xanh SM về điểm đón khách.”
- “Đưa ra 3 Quick Problem Cards theo đúng format.”
- “Bao gồm Actor, Workflow, Bottleneck, Metric, AI Fit.”

Nhờ vậy, AI không còn trả lời quá mơ hồ hoặc lan man.

### 4.2. Thêm ranh giới vận hành
Tôi đã chủ động yêu cầu AI tuân theo các nguyên tắc sau:
- AI chỉ đề xuất, không tự động hành động mà không có phê duyệt.
- Không được giả định dữ liệu không có căn cứ.
- Metric phải có mốc số cụ thể.
- Nếu không đủ dữ liệu, phải nói rõ và đề xuất fallback.

Đây là bước quan trọng để tránh AI tưởng tượng quá mức hoặc bỏ qua yếu tố an toàn.

### 4.3. Dùng AI để stress-test chính mình
Sau khi viết xong một phần, tôi đưa nội dung vào AI để kiểm tra xem phần đó có điểm yếu nào không. Tôi hỏi:
- “Bài toán này có hợp lý không?”
- “Metric này có đo được không?”
- “Có thể rule-based chi tiết hơn AI không?”
- “Điểm nào còn chưa chặt chẽ?”

Khi AI trả lời ra lỗi, tôi không chấp nhận ngay mà sửa lại prompt, bổ sung context và yêu cầu đánh giá lại. Cách này giúp tôi học cách dùng AI như một công cụ phản biện, không chỉ là công cụ sinh nội dung.

---

## 5. Bài học rút ra
Qua bài lab này, tôi học được 3 điều rất quan trọng:

1. AI mạnh nhất khi được dùng với prompt có mục tiêu rõ ràng và bối cảnh cụ thể.  
2. AI dễ mắc lỗi ở phần metric, ranh giới và độ thực tế của workflow nếu người dùng không kiểm tra kỹ.  
3. Dù AI mạnh đến đâu, người dùng vẫn phải giữ vai trò đánh giá, chỉnh sửa và quyết định cuối cùng.

Nói cách khác, AI không thay thế tư duy của con người; nó là công cụ giúp tôi suy nghĩ nhanh hơn, tổ chức tốt hơn và viết rõ ràng hơn.

---

## 6. Kết luận
Tổng kết lại, AI đã giúp tôi rất nhiều trong bài lab này: từ việc tìm bài toán, dựng Phase 1, đến việc hoàn thiện Phase 2, Phase 3 và kiểm tra prompt prototype. Tuy nhiên, sự khác biệt lớn nhất giữa “dùng AI tốt” và “dùng AI sai” chính là cách đặt prompt và kiểm soát ranh giới.

Nếu có thể làm lại, tôi sẽ tiếp tục dùng AI theo hướng:
- rõ mục tiêu,
- rõ ranh giới,
- rõ metric,
- và luôn có bước review bằng con người.

Vì thế, tôi thấy đây không chỉ là bài tập về AI, mà còn là bài học về cách sử dụng AI một cách có trách nhiệm và hiệu quả.
