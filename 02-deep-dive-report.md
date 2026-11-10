# Báo cáo phân tích bài toán — Hỗ trợ xử lý đánh giá 1 sao cho tài xế Xanh SM

## 1. Mục tiêu kinh doanh và phạm vi của nhóm

Nhóm đề xuất cải thiện quy trình tiếp nhận, phân loại và xem xét đánh giá 1 sao nhằm giảm khối lượng xử lý thủ công, rút ngắn thời gian phản hồi và bảo đảm việc xem xét phản ánh công bằng với cả khách hàng lẫn tài xế.

Mục tiêu là xử lý đúng và kịp thời từng phản ánh. Việc giữ hay gỡ đánh giá phải dựa trên bằng chứng và chính sách của doanh nghiệp; số lượng đánh giá được gỡ không phải thước đo thành công.

Báo cáo tập trung vào xác định vấn đề, giá trị kinh doanh và điều kiện để tiếp tục nghiên cứu. Nhóm chưa đề xuất xây dựng hệ thống hoặc lựa chọn kiến trúc kỹ thuật ở giai đoạn này.

**Cơ sở phân tích:** Các số liệu về quy mô, tỷ lệ đánh giá và thời gian dưới đây được kế thừa từ bản thảo của nhóm để lập kịch bản minh họa, chưa có nguồn hoặc dữ liệu vận hành xác nhận. Chúng không phải kết quả khảo sát hay cam kết hiệu quả.

## 2. Quy trình hiện tại và điểm nghẽn

Quy trình dưới đây diễn giải từ mô tả của nhóm, cần được bộ phận vận hành xác nhận trước khi dùng làm cơ sở đo lường.

| Bước | Người phụ trách | Công việc và đầu ra | Thời gian theo bản thảo |
|---|---|---|---|
| 1. Tiếp nhận | Nhân viên tiếp nhận | Ghi nhận đánh giá 1 sao và nội dung phản ánh | Chưa đo |
| 2. Kiểm tra thông tin | Nhân viên tiếp nhận | Kiểm tra thông tin vụ việc, xác định nội dung còn thiếu | Chưa đo |
| 3. Phân loại | Nhân viên tiếp nhận | Xác định loại phản ánh và bộ phận phụ trách | 3–5 phút |
| 4. Chuyển giao | Tiếp nhận → xử lý vi phạm | Bàn giao hồ sơ để xem xét | Chưa đo thời gian chờ |
| 5. Tiếp nhận hồ sơ | Nhân viên xử lý vi phạm | Rà soát hồ sơ, yêu cầu bổ sung nếu cần | Chưa đo |
| 6. Xác minh và đề xuất kết luận | Nhân viên xử lý vi phạm | Đối chiếu phản ánh, thông tin liên quan và giải trình của tài xế | 15–45 phút |
| 7. Quyết định và phản hồi | Nhân sự có thẩm quyền | Quyết định theo chính sách, thông báo kết quả và ghi nhận lý do | Chưa đo |

Hai điểm nghẽn nhóm nhận diện là **phân loại thủ công ở bước 3** và **xác minh ở bước 6**. Điểm bàn giao giữa hai bộ phận cũng cần khảo sát để xác định có phát sinh chờ đợi, thiếu hồ sơ hoặc xử lý lại hay không.

Bản thảo dùng **45 phút/hồ sơ** làm mức trung bình minh họa. Đây chưa phải tổng thời gian được đo từ các bước trên. Cần phân biệt thời gian nhân viên trực tiếp xử lý với thời gian từ lúc nhận phản ánh đến khi có kết quả, bao gồm cả chờ đợi.

## 3. Problem Statement — 6 trường

| Trường | Nội dung |
|---|---|
| **Actor / Operator** | Nhân viên tiếp nhận và nhân viên xử lý vi phạm là người thực hiện chính. Khách hàng và tài xế là các bên chịu tác động; nhân sự có thẩm quyền chịu trách nhiệm quyết định cuối cùng. |
| **Current Workflow** | Tiếp nhận đánh giá 1 sao → kiểm tra thông tin → phân loại → chuyển hồ sơ → xác minh → quyết định và phản hồi. Phần phân loại và xác minh hiện được mô tả là xử lý thủ công. |
| **Bottleneck** | Phân loại mất khoảng 3–5 phút, xác minh mất khoảng 15–45 phút theo ước lượng của nhóm. Cần làm rõ phần thời gian dành cho đọc hiểu, tìm thông tin, chờ bổ sung và ra quyết định để chọn đúng điểm cải thiện. |
| **Business Impact** | Khối lượng phản ánh lớn có thể tạo áp lực nhân sự, tăng hồ sơ tồn và kéo dài thời gian giải quyết. Quyết định thiếu nhất quán có thể ảnh hưởng niềm tin của khách hàng và sự công bằng với tài xế. Quy mô tác động cần được kiểm chứng bằng dữ liệu thực tế. |
| **Success Metric** | Giữ mục tiêu ban đầu của nhóm: thời gian xử lý trung bình dưới 15 phút/hồ sơ và độ chính xác tối thiểu 98%. Cần thống nhất cách đo, phạm vi hồ sơ và chuẩn đối chiếu trước khi đánh giá; chi tiết tại mục 5. |
| **Operational Boundary** | AI có thể hỗ trợ phân loại, tóm tắt và đề xuất nội dung cần xác minh từ thông tin vụ việc đã loại bỏ dữ liệu định danh. Nhân viên kiểm tra bằng chứng và quyết định. AI không tự gỡ đánh giá, kết luận vi phạm hoặc áp dụng chế tài. Hồ sơ thiếu thông tin, mâu thuẫn hay nhạy cảm được chuyển người phụ trách xem xét. |

## 4. Tác động kinh doanh — kịch bản cần kiểm chứng

Bản thảo nhóm nêu khoảng **70.000 tài xế**, **1 triệu chuyến/ngày** trên toàn hệ sinh thái và tỷ lệ đánh giá xấu **0,5%**. Chưa có nguồn xác nhận các số liệu này hoặc tỷ lệ đánh giá xấu nào thực sự là đánh giá 1 sao thuộc phạm vi xử lý.

Nếu tạm giả định 0,5% tổng chuyến tạo ra một hồ sơ 1 sao cần xử lý, quy mô minh họa là:

| Chỉ tiêu | Cách tính theo giả định | Kết quả minh họa |
|---|---|---|
| Hồ sơ cần xử lý mỗi ngày | 1.000.000 × 0,5% | 5.000 hồ sơ |
| Tổng công xử lý ở mức hiện tại | 5.000 × 45 phút ÷ 60 | 3.750 giờ công/ngày |
| Tổng công xử lý ở mốc mục tiêu 15 phút | 5.000 × 15 phút ÷ 60 | 1.250 giờ công/ngày |
| Chênh lệch công xử lý tiềm năng | 3.750 − 1.250 | 2.500 giờ công/ngày |

Kịch bản này chỉ đúng nếu số hồ sơ và thời gian công trực tiếp trên mỗi hồ sơ đúng với giả định. Nếu 45 phút bao gồm thời gian chờ, không thể quy toàn bộ thành giờ công. Chênh lệch trên chưa phải khoản tiết kiệm tiền hoặc mức giảm nhân sự đã được chứng minh.

Nhóm kỳ vọng giá trị ở ba mặt:

- **Hiệu quả vận hành:** giảm thao tác đọc, phân loại và tổng hợp lặp lại; dành thêm thời gian cho hồ sơ phức tạp.
- **Chất lượng dịch vụ:** phản hồi sớm hơn, giảm hồ sơ tồn và duy trì cách giải quyết nhất quán.
- **Công bằng với tài xế:** xem xét phản ánh trên cơ sở bằng chứng, hạn chế kết luận thiếu thông tin và xử lý lại.

Chưa đủ cơ sở để khẳng định mỗi hồ sơ làm tài xế mất một chuyến xe. Cần xác nhận tài xế có bị gián đoạn hoạt động trong thời gian xem xét hay không, trong trường hợp nào và trong bao lâu trước khi tính tác động đến thu nhập hoặc doanh thu.

## 5. Mục tiêu và cách đánh giá hiệu quả

| Chỉ tiêu | Mục tiêu đề xuất | Cách đánh giá ở góc độ nghiệp vụ |
|---|---|---|
| Thời gian công xử lý | Trung bình dưới 15 phút/hồ sơ trong phạm vi đã thống nhất | Ghi thời gian trực tiếp xử lý; tách riêng thời gian chờ và phân tích theo độ phức tạp |
| Chất lượng phân loại | Tối thiểu 98% trên bộ hồ sơ được nghiệp vụ thống nhất | So sánh phân loại đề xuất với kết quả chuyên viên đã rà soát; báo cáo cả số hồ sơ và từng nhóm phản ánh |
| Chất lượng kết luận | Không suy ra từ độ chính xác phân loại | Đánh giá riêng kết luận giữ/gỡ đánh giá theo bằng chứng và chính sách; theo dõi sai sót ảnh hưởng khách hàng hoặc tài xế |
| Thẩm quyền quyết định | 100% quyết định giữ/gỡ đánh giá do người có thẩm quyền xác nhận | Kiểm tra hồ sơ quyết định và lý do xử lý |
| Trải nghiệm và tiến độ giải quyết | Xác lập mục tiêu sau khi đo hiện trạng | Theo dõi thời gian đến kết quả cuối cùng, hồ sơ tồn, tỷ lệ bổ sung thông tin và tỷ lệ khiếu nại lại |

Mốc 98% được cụ thể hóa trước hết cho **phân loại phản ánh** để có cách đo rõ ràng. Nhóm cần thống nhất thêm tiêu chí đánh giá kết luận vi phạm; phân loại đúng chưa đủ để chứng minh quyết định cuối cùng đúng. Các mục tiêu trên chưa phải kết quả đã đạt.

## 6. Vai trò dự kiến của AI và quy trình mong muốn

AI có thể phù hợp với các tác vụ đọc phản ánh bằng ngôn ngữ tự nhiên, tóm tắt vụ việc và gợi ý phân loại. Giá trị cần kiểm chứng là nhân viên có xử lý nhanh hơn và duy trì chất lượng hay không.

Quy trình mong muốn ở mức nghiệp vụ:

1. Nhân viên tiếp nhận kiểm tra thông tin và bảo đảm hồ sơ đủ điều kiện xem xét.
2. AI hỗ trợ tóm tắt, gợi ý nhóm phản ánh và chỉ ra thông tin cần bổ sung.
3. Nhân viên rà soát gợi ý, chuyển đúng bộ phận và thực hiện xác minh.
4. Người có thẩm quyền quyết định giữ hoặc gỡ đánh giá theo chính sách.
5. Nhân viên phản hồi, ghi nhận lý do và theo dõi khiếu nại lại nếu có.

Nếu gợi ý không rõ hoặc thiếu bằng chứng, nhân viên tiếp tục xử lý theo quy trình hiện hành. Không trì hoãn hồ sơ chỉ để chờ AI.

**AI Fit:** Định hướng hiện tại là AI hỗ trợ nhân viên trong một số bước cụ thể. Việc tự phân loại và đưa ra gợi ý chưa đủ để kết luận cần AI Agent. Nhóm chưa chốt cách triển khai; trước hết cần so sánh giá trị với việc chuẩn hóa biểu mẫu, tiêu chí phân loại và hướng dẫn nghiệp vụ.

## 7. Mức độ sẵn sàng và việc cần làm tiếp

| Điều kiện | Hiện trạng theo tài liệu nhóm | Việc cần xác nhận |
|---|---|---|
| Dữ liệu mẫu và kết quả xử lý | Bản thảo đánh dấu chưa có dữ liệu sạch để đánh giá | Thu thập hồ sơ đại diện đã loại bỏ dữ liệu định danh, có kết quả và lý do xử lý |
| Số liệu hiện trạng | Có các ước lượng về quy mô và thời gian | Xác nhận số hồ sơ 1 sao thực tế, thời gian công, thời gian chờ và tỷ lệ xử lý lại |
| Khả năng kiểm soát sai sót | Nhóm dự kiến nhân viên kiểm tra và phê duyệt | Làm rõ ai chịu trách nhiệm, trường hợp nào cần chuyển cấp và cách sửa quyết định sai |
| Sự sẵn sàng của các bên | Bản thảo đánh dấu sẵn sàng thay đổi | Xác nhận với bộ phận tiếp nhận, xử lý vi phạm và người phê duyệt; chưa có biên bản hoặc bằng chứng kèm theo |
| Giá trị kinh tế | Chưa có chi phí thực tế để đối chiếu | Ước lượng lợi ích từ thời gian tiết kiệm, đồng thời tính cả công rà soát và xử lý lại |

Ưu tiên tiếp theo của nhóm là trao đổi với người làm nghiệp vụ, thu thập hồ sơ mẫu, đo hiện trạng và thống nhất tiêu chí phân loại cùng nguyên tắc giữ/gỡ đánh giá. Sau đó mới quyết định có cần thử nghiệm AI hay cải tiến quy trình hiện hành đã đủ đáp ứng.

## 8. Đề xuất quyết định của nhóm

**NOT YET — tiếp tục làm rõ dữ liệu và cơ sở kinh doanh trước khi xây dựng.**

Bài toán có tiềm năng cải thiện hiệu quả vận hành và chất lượng giải quyết phản ánh, nhưng chưa đủ bằng chứng để cam kết mức tiết kiệm hoặc hiệu quả của AI. Đây là đề xuất của nhóm trong bài lab, chưa phải quyết định phê duyệt thực tế của Ban Giám đốc.

Nhóm đề xuất xem xét lại khi đã có số liệu hiện trạng được xác nhận, hồ sơ mẫu đủ để đánh giá, tiêu chí nghiệp vụ thống nhất và người phụ trách quy trình đồng thuận về phạm vi. Quyết định bước tiếp theo sẽ dựa trên lợi ích kinh doanh có thể đo được và khả năng duy trì chất lượng xử lý.
