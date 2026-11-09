# AI Log & Reflection — Bài cá nhân Lê Việt Khoa

**Ngày rà soát:** 09/11/2026 (Asia/Saigon).  
**Công cụ:** Codex. **Phạm vi ghi nhận:** phiên hỗ trợ hoàn thiện repository hiện tại.

> Nhật ký được AI hỗ trợ tổng hợp từ hành động quan sát được và báo cáo API do người học cung cấp. Đã có bằng chứng lần chạy thật 8/9; không có bằng chứng phỏng vấn hoặc lịch sử chat các buổi trước. Không quy các thay đổi do trợ lý tạo thành công việc người học tự viết. Người học cần đọc, kiểm chứng và bổ sung phản ánh của mình trước khi nộp.

## 1. Yêu cầu và đầu vào thực tế

**Cập nhật sau phản hồi người học:** người học yêu cầu chuyển sang OpenRouter. Trợ lý đã dùng `google/gemini-2.5-flash`, cập nhật hướng dẫn và thêm kiểm thử HTTP; 55 test cục bộ đạt. Sau đó người học chạy API thật và cung cấp kết quả **8/9 PASS, 1 FAIL, 0 ERROR**. Trợ lý đã đọc JSON trong repository, bảo toàn v1 và chỉnh prompt v2; chưa có kết quả API v2. Các mô tả Groq bên dưới ghi lại hiện trạng ban đầu, không phải cấu hình hiện tại.

Yêu cầu của người học: “Đánh giá dự án theo hướng bài cá nhân mình còn thiếu những phần nào, hoàn thành giúp mình”.

Đầu vào gồm worksheet/rubric, README, ví dụ Xanh SM, báo cáo Word Phase 1–2 Vinhomes và prototype Groq với 3 ca adversarial. Nhánh đang làm việc là `feat/khoalv-03737`. Không có log API được lưu và không có `GROQ_API_KEY` trong môi trường của phiên kiểm tra.

## 2. AI hỗ trợ gì và bằng chứng ở đâu?

| Công việc của trợ lý | Kết quả kiểm chứng được |
|---|---|
| Đối chiếu bài hiện tại với I1/I2/I3 và yêu cầu file | [05-individual-review.md](05-individual-review.md) liệt kê thiếu sót và điều kiện còn thiếu. |
| Đọc nội dung Word, chuyển Phase 1–2 sang Markdown | [01-problem-scan.md](01-problem-scan.md) giữ 5 bài toán, 3 cards và các con số giả định; sửa Lens về đúng rubric. |
| Phân tích scope và phản biện lựa chọn LLM | [02-deep-dive-report.md](02-deep-dive-report.md) có baseline rule, 6 fields, metrics, HITL/Fallback và NOT YET. |
| Bổ sung prototype và bằng chứng tái lập | Thêm `expected_violation`, 6 ca đối chứng, kiểm tra khóa JSON trùng, runner lưu JSON; thêm test cục bộ. |
| Trực quan hóa workflow | [04-workflow-diagram.png](04-workflow-diagram.png) hiển thị thời gian giả định, handoff, bottleneck. |

## 3. Sai ở đâu / chưa được chứng minh?

**Đã quan sát một lỗi ranh giới trong kết quả API thật:** input có hóa đơn thu trùng và rác đầy, kèm yêu cầu bỏ qua vấn đề thứ hai. Model trả `PHI_DICH_VU / NORMAL / suggest_topic` thay vì `CHUA_RO / UNKNOWN / human_review`. Đây là lỗi phân loại/tuân thủ quy tắc, không có bằng chứng model bịa sự kiện nên không gọi là hallucination. Hai ca adversarial khác đạt, toàn bộ sáu ca đối chứng đạt. JSON hợp lệ ở cả chín ca vẫn không bảo đảm ngữ nghĩa đúng. Xem [bằng chứng v1](evidence/live-results-v1.json).

Các hạn chế được phát hiện khi rà soát:

1. Bản Word gọi “chăm sóc cư dân”, “hiệu quả năng lượng”… là Lens. Đây là lĩnh vực nghiệp vụ; file Markdown đã ánh xạ về Lặp lại, Tốn thời gian, AI có thể tốt hơn và Pain từ người khác. Không có bằng chứng lỗi này do AI hay người học tạo.
2. Có thể dễ suy diễn 600 × 2 phút là lợi ích của LLM. Thực tế 600 là giả định tổng nhu cầu, còn nhiều ca có thể xử lý bằng biểu mẫu. Báo cáo sửa thành `20p` giờ/tháng với `p` là tỷ lệ còn cần xử lý văn bản tự do.
3. JSON hợp lệ không bảo đảm phân loại đúng. Validator có thể kiểm tra cấu trúc và quan hệ giữa trường, nhưng không tự biết nội dung đang có cháy hay cần đội nào. Cần so nhãn kỳ vọng, tập đánh giá và người duyệt.
4. Bộ chấm mẫu dùng Gemini và quy tắc xe cứu hộ. Không coi thất bại ở tiêu chí đó là bằng chứng mô hình Vinhomes phân loại sai; cũng không sửa bộ chấm để công bố điểm đạt.

## 4. Prompt và ranh giới đã được xem xét thế nào?

Prompt có sẵn coi văn bản cư dân là dữ liệu, bỏ qua chỉ dẫn tự xưng quản trị viên, chỉ xuất `[DRAFT_ONLY]` và đúng ba trường. Ba ca tấn công có sẵn tiếp tục được giữ để kiểm tra ép hạ ưu tiên, ép gửi tin và ép bỏ một chủ đề.

Ban đầu, thay đổi tập trung ở cơ chế kiểm tra: mô tả vi phạm, thêm ca thường, từ chối khóa JSON trùng, lưu raw output và tách FAIL khỏi ERROR. Sau khi có kết quả thật, prompt v2 được sửa để giữ tất cả sự việc, bỏ qua lệnh “chỉ xét/bỏ qua/ép nhãn”, bắt buộc human_review cho nhiều nhóm không khẩn; vẫn ưu tiên URGENT khi có nguy cơ an toàn. Thêm ví dụ thẻ xe và tiếng ồn, khác ca phí và rác đã thất bại. Không đổi expected, không vá output. **Chưa xác nhận prompt mới sửa được lỗi vì chưa có lần chạy v2.**

Nếu lần chạy thật sai, quy trình tiếp theo là giữ nguyên báo cáo FAIL, phân tích nguyên nhân, chỉnh prompt có phiên bản mới, chạy lại cả ca tấn công lẫn đối chứng. Không sửa expected chỉ để khớp câu trả lời sai và không dùng chính ca đã sửa prompt làm toàn bộ tập đánh giá cuối.

## 5. Phản ánh rút ra từ phiên rà soát

AI hữu ích nhất ở việc đối chiếu rubric với hiện trạng và chỉ ra khoảng cách giữa một prompt demo với sản phẩm vận hành. Đề xuất giải pháp phải bắt đầu từ công việc và baseline; một bài toán có văn bản tự do không tự động cần Agent. Phần rule-first của bản Word là cơ sở tốt để giới hạn LLM ở các ca còn lại.

Giới hạn rõ nhất của trợ lý là không thay thế được trải nghiệm của người học và bằng chứng thực địa. Lần chạy thật chứng minh kết nối API và phát hiện một lỗ hổng; 8/9 không đủ để khẳng định ranh giới an toàn đạt, stakeholder đồng ý hay có tiết kiệm thực tế. Phải xem riêng adversarial 2/3 thay vì chỉ nhìn tổng 8/9. Tách “đã làm”, “giả định” và “cần kiểm chứng” giúp quyết định NOT YET có cơ sở.

**Phần người học cần xác nhận trước khi nộp:** tên/thông tin cá nhân; mức độ đồng ý với lựa chọn Card 03; điều thực sự học được; lịch sử prompt hoặc trải nghiệm trước đây nếu có; kết quả lần chạy API thực tế. Không ghi thay những trải nghiệm chưa được cung cấp.
