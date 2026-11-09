# 01 — Problem Scan & Quick Problem Cards

**Bài lab:** Day 02 — AI Product Scoping (Vin Smart Future)  
**Ngày soạn:** 09/11/2026  
**Trạng thái:** Bản đề xuất để nhóm thảo luận và kiểm chứng.

> Tài liệu được phát triển từ bối cảnh và yêu cầu của repo bài lab. Nhóm chưa cung cấp kết quả phỏng vấn, log nghiệp vụ hay dữ liệu vận hành thực tế. Vì vậy, các vấn đề dưới đây là **giả thuyết cần xác minh**; các ngưỡng đánh giá là **mục tiêu thử nghiệm đề xuất**, chưa phải kết quả đã đạt. Không coi số liệu trong bài mẫu hoặc dữ liệu mô phỏng là bằng chứng về hoạt động thực tế của doanh nghiệp.

## 1. SCAN — Năm giả thuyết bài toán

Bảng sử dụng cả bốn góc nhìn trong worksheet: lặp lại, tốn thời gian, AI có thể cải thiện và khó khăn do người liên quan phản ánh.

| # | Mảng trong bối cảnh bài lab | Lens chính | Giả thuyết bài toán vận hành | Người cần hỗ trợ | Cách xác minh giả thuyết |
|---|---|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Khi nhận thông báo sự cố pin bằng ngôn ngữ tự nhiên, điều phối viên phải làm rõ thông tin và soạn hướng dẫn thủ công; thông báo thiếu dữ kiện có thể kéo dài xử lý. | Điều phối viên và tài xế | Phỏng vấn người hiểu điều vận; xác định trường thông tin bắt buộc; đo thời gian xử lý một bộ tình huống; nếu chỉ dùng dữ liệu mô phỏng phải ghi rõ. |
| 2 | Vinhomes | Lặp lại | Nhân viên tiếp nhận phải đọc, phân loại và chuyển phản ánh cư dân đến đúng bộ phận; nội dung nhiều ý hoặc thiếu vị trí có thể gây chuyển sai hoặc phải hỏi lại. | Nhân viên tiếp nhận và ban quản lý | Thu thập phản ánh mẫu đã được phép sử dụng hoặc tạo dữ liệu mô phỏng; thống nhất nhãn và quy tắc chuyển tuyến với người hiểu nghiệp vụ. |
| 3 | Vinpearl | Pain từ người liên quan | Người quản lý phải đọc nhiều nhận xét để nhận ra các vấn đề lặp lại và soạn bản tổng hợp cho bộ phận vận hành. | Quản lý chất lượng dịch vụ | Xem cách tổng hợp nhận xét hiện tại; kiểm tra khối lượng công việc, thời gian và tiêu chí xác định chủ đề quan trọng. |
| 4 | VinFast | Lặp lại | Việc đối chiếu bản ghi phiên sạc với hóa đơn cần phát hiện giao dịch thiếu, trùng hoặc lệch số tiền. | Nhân viên đối soát | Kiểm tra cấu trúc dữ liệu, mã giao dịch và quy tắc tính tiền; thử giải pháp đối chiếu bằng code trước để biết có thực sự cần AI không. |
| 5 | VinUni | AI-upgrade | Kết quả autograder có thể khó hiểu đối với sinh viên mới học; giảng viên cần chuyển lỗi kỹ thuật thành phản hồi ngắn, đúng và có tính hướng dẫn. | Sinh viên và trợ giảng | Lấy bài lỗi, log chấm và phản hồi mẫu được phép sử dụng; kiểm tra phản hồi có đúng với lỗi thực tế và phù hợp mục tiêu học tập không. |

**Nhận xét sơ bộ:** không phải cả năm bài toán đều cần LLM. Bài toán #4 có thể phù hợp với quy tắc xác định và đối chiếu dữ liệu có cấu trúc. Bài toán #5 cần giới hạn mức độ gợi ý, tránh tự giải toàn bộ bài tập thay sinh viên.

## 2. QUICK-ASSESS — Ba thẻ bài toán

Chọn #1, #2 và #3 để lập thẻ. Đây là ba ứng viên có tác vụ xử lý ngôn ngữ rõ ràng và có thể thiết kế prototype hẹp với bước con người kiểm tra.

### Card 1 — Hỗ trợ điều phối sự cố pin bằng thông tin có cấu trúc và tin nhắn nháp

**Bài toán trong một câu:** Điều phối viên cần chuyển thông báo sự cố pin của tài xế thành thông tin đủ để xem xét phương án xử lý và bản nháp hướng dẫn, đồng thời tuân thủ ranh giới của bài lab.

- **Mảng:** Xanh SM.
- **Lens:** tốn thời gian; bổ sung góc nhìn tác vụ lặp lại.
- **Actor chính:** điều phối viên. Người hưởng lợi tiếp theo là tài xế.
- **Đầu vào dự kiến:** thông báo tài xế, mức pin, vị trí, loại xe và dữ liệu trạm sạc đã được xác minh hoặc được đánh dấu rõ là mô phỏng. Không mặc định tất cả trường này luôn có sẵn.

**Quy trình hiện tại giả định — cần xác minh:**

1. Điều phối viên tiếp nhận thông báo sự cố từ tài xế.
2. Hỏi lại và ghi nhận các thông tin còn thiếu về xe, mức pin, vị trí.
3. Tra cứu dữ liệu liên quan và xem xét phương án xử lý theo quy trình nghiệp vụ.
4. Soạn hướng dẫn hoặc đề nghị hỗ trợ, kiểm tra thông tin trước khi gửi.
5. Ghi lại phương án đã được duyệt và theo dõi phản hồi.

**Bottleneck giả định:** bước 2 và 4: làm rõ thông tin từ lời nhắn tự do và soạn bản nháp nhất quán.

**Thời gian hiện tại:** chưa đo. Nhóm cần đo trên cùng một bộ ít nhất 10 tình huống khi xử lý thủ công, ghi thời gian từng lượt và lấy trung vị làm baseline. Không lấy thời gian trong bài mẫu làm baseline thực tế của nhóm.

**AI hỗ trợ ở đâu?**

- Trích xuất các dữ kiện được nêu trong thông báo; trường chưa có phải được đánh dấu thiếu.
- Soạn bản nháp dựa trên dữ liệu và phương án đã được kiểm tra.
- Phần kiểm tra ngưỡng pin và khoảng cách nên được thực hiện bằng code có quy tắc rõ ràng, không giao hoàn toàn cho khả năng tuân thủ prompt của LLM.

**Mục tiêu thử nghiệm đề xuất — chưa đo:**

| Tiêu chí | Cách đo và ngưỡng mục tiêu |
|---|---|
| Định dạng nháp | 20/20 đầu ra trong bộ thử bắt đầu bằng `[DRAFT_ONLY]`. |
| Giữ ranh giới đề bài | Không có đầu ra khuyến nghị trạm xa hơn 5 km trong các trường hợp pin dưới 5%; đầu ra phải đề xuất `dispatch_mobile_charger`. |
| Không bịa dữ liệu vận hành | Không có trường hợp tự tạo vị trí xe, tình trạng trạm hoặc xác nhận đã điều xe khi không có dữ liệu/công cụ thực hiện. |
| Hiệu quả xử lý | Trung vị thời gian từ tiếp nhận đến bản nháp được người duyệt chấp nhận giảm ít nhất 30% so với baseline thủ công trên cùng bộ tình huống. Tính cả thời gian duyệt và sửa. |

**Ranh giới của prototype:**

- Dùng các ngưỡng pin dưới 5% và khoảng cách 5 km như quy tắc của đề lab; không suy diễn chúng thành quy luật kỹ thuật về tầm hoạt động thực tế của xe.
- Mọi phương án và tin nhắn đều là nháp để điều phối viên duyệt. Prototype không gửi tin hay điều xe thật.
- Thiếu dữ kiện cần thiết thì yêu cầu bổ sung hoặc chuyển người xử lý; không đoán các giá trị còn thiếu.
- Thẻ `[DRAFT_ONLY]` là yêu cầu định dạng. Trong thiết kế hệ thống, quyền gửi hoặc điều xe phải được kiểm soát bằng code và quy trình phê duyệt.

**Quick Architecture:** Rule + LLM Feature + Human-in-the-loop. Chưa cần Agent tự trị.

**Dữ liệu và điều kiện cần bổ sung:** định nghĩa trường thông tin bắt buộc, bộ tình huống và kết quả mong đợi, quy trình xác minh dữ liệu, người duyệt, baseline thời gian. Trước mắt có thể xây 20 tình huống mô phỏng có nhãn rõ ràng, gồm tình huống thường, pin thấp, thiếu dữ liệu và yêu cầu cố tình vượt ranh giới. Kết quả trên dữ liệu này chỉ chứng minh hành vi trong phạm vi thử nghiệm mô phỏng.

### Card 2 — Phân loại phản ánh cư dân và đề xuất bộ phận tiếp nhận

**Bài toán trong một câu:** Nhân viên tiếp nhận cần chuyển phản ánh tự do của cư dân thành phiếu có nhóm vấn đề và dữ kiện cần thiết để xem xét chuyển đúng bộ phận.

- **Mảng:** Vinhomes.
- **Lens:** lặp lại; bổ sung góc nhìn tốn thời gian.
- **Actor chính:** nhân viên tiếp nhận phản ánh. Người hưởng lợi là cư dân và bộ phận xử lý.
- **Đầu vào dự kiến:** nội dung phản ánh, địa điểm người gửi cung cấp và danh mục chuyển tuyến do nhóm mô phỏng hoặc đơn vị nghiệp vụ xác nhận.

**Quy trình hiện tại giả định — cần xác minh:**

1. Tiếp nhận phản ánh từ kênh hỗ trợ.
2. Đọc và xác định nội dung, địa điểm, dữ kiện còn thiếu.
3. Hỏi lại nếu chưa đủ thông tin để tạo phiếu.
4. Chọn nhóm vấn đề và đề xuất bộ phận tiếp nhận.
5. Nhân viên kiểm tra, chuyển phiếu và theo dõi tình trạng.

**Bottleneck giả định:** bước 2–4, đặc biệt với phản ánh dài, có nhiều vấn đề hoặc thiếu vị trí.

**Thời gian hiện tại:** chưa đo. Dùng ít nhất 10 phiếu trong bộ thử để đo thời gian phân loại và chuẩn bị phiếu thủ công; ghi cả thời gian hỏi lại nếu kịch bản có bước đó.

**AI hỗ trợ ở đâu?** Trích xuất trường thông tin, đề xuất nhóm vấn đề và soạn câu hỏi bổ sung. Việc chuyển bộ phận dựa trên bảng ánh xạ đã được duyệt; nhân viên chốt phiếu trước khi chuyển.

**Mục tiêu thử nghiệm đề xuất — chưa đo:**

| Tiêu chí | Cách đo và ngưỡng mục tiêu |
|---|---|
| Phân loại | Ít nhất 27/30 phiếu được phân loại đúng theo bộ nhãn tham chiếu do nhóm thống nhất. Bộ nhãn thử gồm điện/nước, vệ sinh, tiếng ồn, bãi xe và khác. |
| Xử lý thiếu dữ kiện | Tất cả tình huống được gắn nhãn thiếu địa điểm phải được yêu cầu bổ sung hoặc chuyển người kiểm tra, không tự tạo số căn hộ/tòa nhà. |
| Hiệu quả xử lý | Trung vị thời gian chuẩn bị phiếu được nhân viên chấp nhận giảm ít nhất 30% so với baseline thủ công trên cùng bộ dữ liệu. |

**Ranh giới của prototype:** không tự cam kết thời hạn hoàn thành, mức bồi thường hoặc kết quả xử lý; không tự suy diễn chính sách. Phản ánh mơ hồ, nhiều nhóm vấn đề hoặc ngoài danh mục phải được nhân viên kiểm tra.

**Quick Architecture:** Rule-based routing + LLM Feature + Human review.

**Dữ liệu và điều kiện cần bổ sung:** danh mục nhãn, bảng ánh xạ bộ phận, quy tắc xử lý trường hợp nhiều nhóm, 30 phiếu thử đã ẩn thông tin cá nhân hoặc được tạo mô phỏng, nhãn tham chiếu được con người kiểm tra. Bộ thử đánh giá phải được chốt riêng, không vừa xem đáp án vừa sửa prompt để báo điểm của chính bộ đó.

### Card 3 — Tổng hợp nhận xét khách sạn thành báo cáo vấn đề cần xem xét

**Bài toán trong một câu:** Người quản lý cần tổng hợp nhiều nhận xét thành các chủ đề có bằng chứng để xem xét ưu tiên cải thiện dịch vụ.

- **Mảng:** Vinpearl.
- **Lens:** pain từ người liên quan; bổ sung góc nhìn tốn thời gian.
- **Actor chính:** quản lý chất lượng dịch vụ hoặc nhân viên tổng hợp phản hồi.
- **Đầu vào dự kiến:** bộ nhận xét được phép sử dụng hoặc dữ liệu mô phỏng, kèm mã nhận xét để truy vết. Prototype không tự thu thập dữ liệu từ các nền tảng bên ngoài.

**Quy trình hiện tại giả định — cần xác minh:**

1. Tập hợp nhận xét từ nguồn được phép sử dụng.
2. Đọc từng nhận xét và ghi các ý khen, chê, yêu cầu cụ thể.
3. Nhóm những ý tương đồng và ghi lại mã nhận xét làm căn cứ.
4. Soạn bản tổng hợp vấn đề để người quản lý xem xét.
5. Người quản lý kiểm tra các ý chính trước khi chuyển bộ phận liên quan.

**Bottleneck giả định:** bước 2–4: đọc lặp lại nhiều nội dung và tổng hợp mà không bỏ sót vấn đề quan trọng.

**Thời gian hiện tại:** chưa đo. Nhóm chuẩn bị 10 bộ nhận xét, mỗi bộ 5 nhận xét, rồi đo thời gian tổng hợp thủ công và thời gian có AI hỗ trợ, gồm cả khâu kiểm tra.

**AI hỗ trợ ở đâu?** Đề xuất nhóm chủ đề và bản tóm tắt, mỗi nhận định có mã nhận xét hỗ trợ. Con người kiểm tra mức độ quan trọng và quyết định xử lý.

**Mục tiêu thử nghiệm đề xuất — chưa đo:**

| Tiêu chí | Cách đo và ngưỡng mục tiêu |
|---|---|
| Độ đúng và đủ của bản tổng hợp | Ít nhất 9/10 bản tổng hợp phản ánh đúng các ý chính trong bộ đáp án tham chiếu do hai thành viên kiểm tra và thống nhất. |
| Truy vết thông tin | Mọi vấn đề được nêu đều có ít nhất một mã nhận xét thực sự chứa thông tin hỗ trợ; không thêm địa điểm, số liệu hoặc sự cố không có trong đầu vào. |
| Hiệu quả xử lý | Trung vị thời gian tạo báo cáo được duyệt giảm ít nhất 30% so với cách thủ công trên cùng bộ nhận xét. |

**Ranh giới của prototype:** không tự gửi phản hồi cho khách, không tự hứa hoàn tiền/bồi thường, không biến một nhận xét đơn lẻ thành kết luận về toàn bộ khách hàng. Khi dữ liệu mâu thuẫn, phải trình bày sự khác biệt và dẫn mã nhận xét để người duyệt kiểm tra.

**Quick Architecture:** LLM Feature + Human review. Bước thống kê số lượng theo mã nhận xét nên dùng code, sau khi quy tắc gán nhóm được xác định.

**Dữ liệu và điều kiện cần bổ sung:** tiêu chí xác định ý chính, bộ nhận xét và đáp án tham chiếu, người đánh giá, quy tắc bảo vệ dữ liệu cá nhân và baseline thời gian. Các phản ánh trong dữ liệu thử không được trình bày như sự cố thật tại doanh nghiệp.

## 3. Đề xuất đưa một thẻ vào DEEP-DIVE

**Đề xuất sơ bộ: Card 1 — Hỗ trợ điều phối sự cố pin Xanh SM.** Đây là đề xuất của bản soạn để nhóm cân nhắc, chưa phải quyết định đã được tất cả thành viên xác nhận.

| Tiêu chí | Card 1 — Điều phối pin | Card 2 — Phản ánh cư dân | Card 3 — Tổng hợp nhận xét |
|---|---|---|---|
| Tác vụ LLM | Trích xuất dữ kiện và viết nháp | Trích xuất, phân loại và hỏi bổ sung | Nhóm chủ đề và tóm tắt có căn cứ |
| Cơ chế kiểm tra | Quy tắc pin/khoảng cách của lab, nhãn nháp và người duyệt | Bộ nhãn, bảng chuyển tuyến và người duyệt | Đáp án tham chiếu, mã nhận xét và người duyệt |
| Dữ liệu nghiệp vụ thực tế | Chưa có | Chưa có | Chưa có |
| Điểm thuận lợi cho buổi lab | Khớp trực tiếp với starter code và tình huống ranh giới của repo | Có thể tạo bộ phiếu thử để đánh giá phân loại | Có thể tạo bộ nhận xét thử để đánh giá độ trung thành |
| Việc phải làm rõ | Quy trình thật, nguồn dữ liệu xác minh, quyền phê duyệt | Danh mục nhãn và quy tắc chuyển tuyến | Tiêu chí ý chính và độ nhất quán giữa người chấm |

**Lý do ưu tiên Card 1 trong bài lab:** phạm vi có thể giới hạn ở bản nháp; có ranh giới cụ thể để kiểm tra; thuận tiện đối chiếu prototype được cung cấp. Điều này không chứng minh giá trị triển khai thực tế cao hơn hai thẻ còn lại.

**Lý do giữ hai thẻ làm phương án thay thế:** Card 2 cần thống nhất taxonomy và bảng chuyển tuyến; Card 3 cần xây tiêu chí chấm tóm tắt và bằng chứng truy vết. Nếu nhóm tiếp cận được dữ liệu/người dùng của một trong hai bài toán này tốt hơn, nhóm nên xem xét đổi ưu tiên.

## 4. Việc nhóm cần xác nhận trước khi viết báo cáo phân tích sâu

1. Chốt bài toán và người chịu trách nhiệm xác minh quy trình; ghi lại lý do chọn và chưa chọn các thẻ còn lại.
2. Xác định dữ liệu nào là thật, dữ liệu nào là mô phỏng; ghi nguồn, quyền sử dụng và các giả định.
3. Đo baseline trên bộ tình huống đã chuẩn bị. Tách thời gian gọi API khỏi tổng thời gian nghiệp vụ có bước con người duyệt.
4. Vẽ Current-State Workflow, xác định handoff và bottleneck trước khi vẽ Future-State Flow.
5. Sau khi thử nghiệm mới điền kết quả đạt/không đạt; chưa kết luận GO dựa trên các mục tiêu trong tài liệu này.

## 5. Nguồn và phạm vi sử dụng AI

- [README — yêu cầu làm bài và nộp bài](https://github.com/GDGoC-FPTU/VinUni_Codelab_Day02_Template/blob/main/README.md).
- [01-worksheet.md — SCAN, Quick Cards và rubric](https://github.com/GDGoC-FPTU/VinUni_Codelab_Day02_Template/blob/main/01-worksheet.md).
- [02-deliverable-example.md — ví dụ điều phối Xanh SM](https://github.com/GDGoC-FPTU/VinUni_Codelab_Day02_Template/blob/main/02-deliverable-example.md).
- [03-inspiration-kit.md — nguồn gợi ý bài toán](https://github.com/GDGoC-FPTU/VinUni_Codelab_Day02_Template/blob/main/03-inspiration-kit.md).
- Phiên bản repo tham khảo khi soạn: commit `b221b79`.

**Đóng góp của AI trong bản này:** hỗ trợ phát triển giả thuyết, cấu trúc thẻ, đề xuất cách đo và rà soát ranh giới. AI không thực hiện phỏng vấn hay quan sát vận hành; không có kết quả thử nghiệm thực tế được tạo ra trong quá trình soạn. Nhóm cần review, chỉnh theo hiểu biết và bổ sung bằng chứng trước khi nộp.
