# Căn cứ lựa chọn đề tài Lab 02 — AI Product Scoping

Tài liệu này giải thích những tiêu chí đã dùng khi đề xuất ba đề tài để người dùng lựa chọn, dựa trên các file Markdown ban đầu. Đây là tài liệu giải thích bổ sung, không phải một deliverable bắt buộc mới của đề.

## 1. Mỗi file ban đầu cung cấp căn cứ gì?

| File nguồn | Đặc điểm nội dung | Vai trò khi lựa chọn |
|---|---|---|
| [01-worksheet.md](01-worksheet.md) | Có rubric 100 điểm, 4 lenses, mẫu Quick Card, Problem Statement 6 trường, yêu cầu prototype và readiness checklist. | Nguồn chính để xác định một đề tài phải phân tích và chứng minh được những gì. |
| [03-inspiration-kit.md](03-inspiration-kit.md) | Gợi ý bài toán theo công ty; nhấn mạnh hiểu quy trình, ranh giới vận hành và “Problem First, AI Second”. Các ý tưởng không phải danh sách bắt buộc. | Nguồn để tìm ứng viên và đánh giá độ phù hợp với năng lực/dữ liệu của nhóm. |
| [02-deliverable-example.md](02-deliverable-example.md) | Bài mẫu đầu-cuối về Xanh SM, chọn sự cố pin, minh họa flow, metric, HITL và hai quy tắc an toàn. | Nguồn tham khảo cách làm đủ chiều sâu; không bắt buộc sao chép đề tài, số liệu, khảo sát hoặc kết luận GO. |
| [README.md](README.md) | Hướng dẫn tạo file nộp, cấu hình API và quy trình branch cá nhân/nhóm. | Căn cứ về hình thức và cách nộp; không phải bảng xếp hạng đề tài. Chỉ phần hướng dẫn gốc được dùng làm căn cứ, không dùng phần bài làm bổ sung sau này để biện minh ngược. |

## 2. Bốn góc nhìn để tìm ít nhất 5 bài toán

Nguồn: **Phase 1 — SCAN** trong worksheet. Đây là góc nhìn để phát hiện cơ hội, chưa phải thang điểm đánh giá chất lượng giải pháp.

| Góc nhìn | Đặc điểm cần tìm | Câu hỏi cần trả lời | Ví dụ ứng viên |
|---|---|---|---|
| **Lặp lại — Repetitive** | Nhân viên làm cùng loại thao tác nhiều lần. | Việc gì lặp lại? Tần suất bao nhiêu? Có thể dùng form hoặc rule thay AI không? | Phân loại phản ánh cư dân; đối soát hóa đơn sạc. |
| **Tốn thời gian — Time-consuming** | Quy trình có thao tác thủ công kéo dài. | Bước nào tốn thời gian, ai làm, mất bao nhiêu phút/lượt? | Tra cứu và soạn phương án hỗ trợ tài xế báo pin yếu. |
| **AI có thể tốt hơn — AI-upgrade** | Cách xử lý hiện tại chậm, cứng nhắc hoặc khó đáp ứng diễn đạt tự do. | AI cải thiện phần nào? Chứng minh tốt hơn bằng phép đo gì? | Soạn phản hồi đánh giá khách sạn phù hợp ngữ cảnh. |
| **Pain từ người khác — Stakeholder Pain** | Khách hàng hoặc nhân viên chịu khó khăn cụ thể. | Ai phàn nàn? Có ví dụ, ghi chú hoặc bằng chứng nào? | Tổng hợp nguyên nhân hủy chuyến từ phản ánh khách/tài xế. |

Worksheet có một điểm không thống nhất: rubric I1 ghi “3 lenses”, còn Phase 1 liệt kê **4 lenses**. Bài làm hiện tại bao phủ cả 4 để đáp ứng phần hướng dẫn đầy đủ hơn; không có yêu cầu mỗi bài toán phải đồng thời thuộc cả 4 góc nhìn.

## 3. Tám tiêu chí để sàng lọc và chọn đề tài phân tích sâu

Các tiêu chí dưới đây là cách tổng hợp yêu cầu từ tài liệu, không phải một bảng chấm điểm mới do giảng viên ban hành.

| # | Tiêu chí | Căn cứ trong file gốc | Ý nghĩa thực hiện |
|---|---|---|---|
| 1 | **Hiểu người dùng và quy trình hiện tại** | Inspiration Kit: ưu tiên bài toán ít nhất một thành viên hiểu rõ; worksheet: Actor, Current Workflow và Workflow Mapping. | Nêu được ai làm, các bước, công cụ, đầu vào/đầu ra và handoff. Nếu chỉ có mô phỏng, phải ghi rõ điều chưa xác minh. |
| 2 | **Có điểm nghẽn cụ thể và tác động kinh doanh** | Quick Card: bước chậm/lỗi nhất và phút/lượt; Problem Statement: Bottleneck, Business Impact. | Chọn một tác vụ rõ, ví dụ soạn phản hồi sự cố pin, thay vì mục tiêu rộng như “AI tối ưu toàn bộ điều vận”. |
| 3 | **Có mục tiêu đo được** | Quick Card và Problem Statement yêu cầu metric có số; rubric G2 chấm metric và ranh giới. | Xác định baseline, ngưỡng mục tiêu, cách đo; phân biệt con số giả định với số đo thật. |
| 4 | **Giải thích được vì sao cần AI** | Worksheet yêu cầu so sánh Rule/LLM/Agent; Inspiration Kit: “Problem First, AI Second”. | Dùng rule cho điều kiện rõ, LLM cho ngôn ngữ tự do nếu có lợi ích. Không chọn agent chỉ vì phức tạp hơn. |
| 5 | **Có ranh giới, người duyệt và fallback rõ** | Inspiration Kit nhấn mạnh Operational Boundary; worksheet yêu cầu AI step, HITL và fallback. | Viết được AI được làm gì, cấm gì, ai phê duyệt, khi thiếu dữ liệu hoặc lỗi thì ai xử lý tiếp. |
| 6 | **Có thể thử bằng một prototype nhỏ** | Phase 4 yêu cầu Python, system prompt, JSON output và ít nhất 3 adversarial prompts. | Chọn phạm vi có đầu vào/đầu ra cụ thể, có thể cố tình thử phá ranh giới và quan sát kết quả. Không cần dựng toàn bộ hệ thống doanh nghiệp. |
| 7 | **Đánh giá được mức sẵn sàng bằng bằng chứng** | Phase 5: dữ liệu sạch, kiểm soát rủi ro, stakeholder sẵn sàng; quyết định GO/NOT YET/NO-GO. | Không đồng nhất “code chạy được” với “sẵn sàng triển khai”. Có thể chọn NOT YET nếu thiếu dữ liệu hoặc baseline. |
| 8 | **Ghi lại được quá trình dùng AI và sửa sai** | Phase 6, rubric I3 và README phần AI Log. | Lưu AI giúp gì, sai gì, sửa prompt thế nào, chạy lại ra sao; không chỉ trình bày một đáp án cuối trông hoàn hảo. |

## 4. Các tiêu chí này liên hệ với điểm số thế nào?

Nguồn: **Cơ cấu tính điểm bài lab** trong worksheet. Tổng 100 điểm là rubric nội dung, khác với thang 10 điểm của script autograder.

| Hạng mục | Điểm | Nội dung cần chứng minh |
|---|---:|---|
| G1. Workflow Mapping | 20 | Quy trình hiện tại có bước, handoff, thời gian và bottleneck. |
| G2. Problem Statement | 20 | Đủ 6 trường; metric có số; ranh giới rõ. |
| G3. AI Fit & Future Flow | 10 | So sánh Rule/LLM/Agent; có AI step, con người và fallback. |
| G4. Decision Quality | 10 | GO/NOT YET/NO-GO có bằng chứng và lập luận trung thực. |
| I1. Scan & Cards | 15 | Ít nhất 5 bài toán và 3 Quick Cards có chất lượng. |
| I2. Prototyping | 10 | Chạy thành công bản mẫu prompt bằng lập trình. |
| I3. AI Log & Reflection | 15 | Phản ánh trung thực AI giúp, sai và cách sửa. |

**Hàm ý khi chọn:** G1 và G2 chiếm **40/100 điểm**, nên hiểu quy trình và diễn đạt đúng bài toán là trọng tâm. Phần prototype chiếm 10 điểm; việc chọn đúng tên model hoặc có nhiều công cụ không thay thế được phân tích nghiệp vụ.

## 5. Vì sao tôi đưa ra đúng ba lựa chọn đó?

Ba ứng viên này xuất hiện ngay trong bài mẫu: sự cố pin Xanh SM, phản ánh cư dân Vinhomes và phân tích hủy chuyến Xanh SM. Tôi dùng chúng làm danh sách ngắn để giảm số quyết định ban đầu, không phải vì đề chỉ cho phép ba đề tài này.

| Ứng viên | Điểm phù hợp với tài liệu | Thông tin còn cần | Nhận định lúc lựa chọn |
|---|---|---|---|
| **Sự cố pin Xanh SM** | Có bài mẫu end-to-end; hai ranh giới `[DRAFT_ONLY]` và pin <5%/trạm >5 km được mô tả ngay trong file mẫu. | Quy trình thực tế, GPS, nguồn dữ liệu hỗ trợ, baseline và người duyệt. | Phù hợp nhất để làm một bản mẫu hẹp, đồng nhất báo cáo và bài thử code hiện có. |
| **Phân loại phản ánh cư dân Vinhomes** | Có trong inspiration kit và bài mẫu; người dùng, tác vụ phân loại/chuyển tuyến có thể mô tả rõ. | Danh mục phản ánh, bộ phận nhận, quy tắc ưu tiên và phản ánh mẫu đã gán nhãn. | Là đề tài hợp lệ; nếu chọn thì cần xử lý sự khác biệt với code mẫu sự cố pin. Không mặc định rằng mọi bài toán Vinhomes đều có rủi ro pháp lý cao. |
| **Phân tích lý do hủy chuyến Xanh SM** | Có trong inspiration kit và bài mẫu; phù hợp xử lý ghi chú tự do theo lô. | Ghi chú đã ẩn định danh, bộ nhãn lý do và tiêu chí đánh giá phân loại. | Là đề tài hợp lệ; có thể bắt đầu bằng bộ nhãn cố định + LLM, không nhất thiết cần agent. |

**Phần do tôi suy ra để đề xuất:** ưu tiên sự cố pin vì có phạm vi thử nhỏ, ranh giới cụ thể và thuận lợi tái sử dụng template. Đây là lựa chọn phù hợp bài lab với thông tin đang có, chưa chứng minh nó có ROI cao nhất, rủi ro thấp nhất hoặc là đề tài duy nhất được điểm cao.

Ngoài Markdown, starter code và autograder cũng đang bám các ranh giới sự cố pin. Đó là căn cứ kỹ thuật bổ sung cho lời khuyên ban đầu, không phải một yêu cầu trong worksheet rằng mọi nhóm bắt buộc chọn Xanh SM.

## 6. Vì sao tôi hỏi thêm về dữ liệu thật hay giả định?

Worksheet yêu cầu bài toán thực tế, tác động kinh doanh, metric và quyết định có bằng chứng. Readiness checklist hỏi trực tiếp về dữ liệu sạch và sự sẵn sàng của stakeholder. Vì vậy, cần biết người làm đang có những căn cứ nào trước khi viết báo cáo.

| Lựa chọn đã đưa ra | Khi nào phù hợp | Điều cần ghi rõ |
|---|---|---|
| **Có dữ liệu thực tế** | Có quy trình, số liệu hoặc quan sát được phép sử dụng. | Nguồn, phạm vi, cách đo và giới hạn dữ liệu; không đưa thông tin nhạy cảm vào prompt. |
| **Dùng giả định ghi rõ** | Chưa có dữ liệu vận hành nhưng cần xây dựng tình huống học tập để thử prototype. | Số liệu là minh họa; chưa khảo sát, chưa xác nhận baseline hay stakeholder. Không dùng kết quả mô phỏng để khẳng định lợi ích thực tế. |

Hai phương án dữ liệu là câu hỏi tôi đặt ra để làm rõ tình trạng bài làm; không phải hai hình thức nộp thay thế được đề gốc tuyên bố là tương đương. Dùng giả định không làm biến mất yêu cầu chứng minh độ sẵn sàng.

Người dùng đã chọn **sự cố pin Xanh SM + dữ liệu giả định có ghi rõ**. Bài hiện tại đã có kết quả chạy model thật 6/6 trên tình huống tự tạo, nhưng số liệu vận hành vẫn là giả định. Vì vậy, bản mẫu kỹ thuật đã chạy được; quyết định triển khai thực tế vẫn là **NOT YET**. Trong worksheet, GO có thể chỉ là bắt đầu prototype phạm vi hẹp; cần nêu rõ đang quyết định về prototype hay triển khai thực tế để tránh nhầm hai mức này.
