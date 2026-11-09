# Chấm điểm ưu tiên — Trợ lý xử lý sự cố pin Xanh SM

## 1. Kết quả và cách chấm

**Tổng điểm tạm thời: 37/100, tương đương 3,7/10.**

Đây là điểm đánh giá dự án theo bảng 10 tiêu chí và trọng số người dùng cung cấp, không phải điểm chất lượng bài lab hoặc tỷ lệ vượt qua kiểm thử. Đối tượng chấm là phạm vi hiện có: trợ lý phân tích tin nhắn và soạn đề xuất chờ người duyệt, chưa tích hợp dữ liệu vận hành hoặc điều xe.

Cách tính: **điểm quy đổi = điểm tiêu chí / 10 × trọng số tính trên 100 điểm**. Ví dụ 6/10 ở tiêu chí trọng số 5% đóng góp 3 điểm.

Bảng người dùng chưa quy định cách xử lý thiếu bằng chứng. Trong lần chấm này, các tiêu chí thiếu dữ liệu định lượng được tạm chấm thấp, thường 2/10, và ghi rõ lý do. Đây là quy ước thận trọng bổ sung cho lần đánh giá, không phải khẳng định dự án chắc chắn không có giá trị. Không tự đặt ngưỡng tổng để phê duyệt hoặc loại dự án vì bảng chưa quy định ngưỡng đó.

Nguồn căn cứ: [báo cáo hiện tại](02-deep-dive-report.md), [nhật ký thử nghiệm](03-ai-log.md) và [code](starter-code/prompt_prototype.py). Các con số 20 lượt/ngày, 15 phút/lượt và mục tiêu 5 phút/lượt là giả định của bài làm. Kết quả chạy Gemini 6/6 được người dùng cung cấp, chưa chứng minh tiết kiệm giờ công hay chi phí.

## 2. Chấm 10 tiêu chí

| # | Tiêu chí | Trọng số | Điểm /10 | Quy đổi /100 | Căn cứ và lý do |
|---|---|---:|---:|---:|---|
| 1 | Cắt giảm giờ công & OPEX nhân sự | 15% | **2** | **3,0** | Chưa đo giờ công trước/sau, chi phí hoặc khả năng chuyển đổi nhân sự. Mục tiêu giảm 15 xuống 5 phút chưa được kiểm chứng. Không lấy tốc độ trả lời của mô hình để thay cho giờ công vận hành. |
| 2 | Ngăn chặn rò rỉ, sai sót & bồi hoàn | 10% | **2** | **2,0** | Có mục đích giảm đề xuất sai, nhưng chưa có tần suất sự cố, mức bồi hoàn hoặc giá trị thiệt hại tránh được. Chưa chứng minh bất kỳ ngưỡng tiết kiệm tiền nào trong bảng; không suy ra tổn thất thực tế dưới 50 triệu/tháng. |
| 3 | Tăng doanh thu & khai thác tài sản | 10% | **3** | **3,0** | Có đường tác động gián tiếp tới thời gian xe ngừng hoạt động và trải nghiệm tài xế, nhưng chưa đo uptime, số cuốc hoặc doanh thu. Prototype không điều xe và chưa chứng minh tăng công suất tài sản. |
| 4 | Rút ngắn cycle time | 10% | **3** | **3,0** | Có baseline và mục tiêu giả định, chưa có phép đo toàn bộ quy trình. Mục tiêu 15 → 5 phút là giảm 66,7%, chưa đạt ngưỡng ≥75% của dải ưu tiên cao và chưa phải kết quả thực tế. |
| 5 | Quy mô & tần suất lặp lại | 10% | **2** | **2,0** | Kịch bản hiện có giả định 20 ca/ngày, thuộc dải dưới 100. Chưa có log để xác nhận, chưa được phép dùng tổng số cuốc toàn hệ sinh thái làm số ca sự cố pin. |
| 6 | Tính bắt buộc dùng AI | 10% | **4** | **4,0** | LLM có ích cho tin nhắn tự do và soạn nháp, phù hợp mức xử lý văn bản cơ bản. Quyết định ngưỡng pin, yêu cầu GPS và thông điệp mẫu có thể làm bằng form + rule; chưa so sánh để chứng minh AI là bắt buộc. Không có audio, CV hoặc dữ liệu BMS đang được xử lý. |
| 7 | Độ sẵn sàng dữ liệu | 10% | **2** | **2,0** | Chỉ có 6 tình huống tự tạo và log thử. Chưa có dữ liệu GPS/BMS/trạm, log nghiệp vụ, nhãn độc lập hoặc API vận hành được xác nhận. Kết nối được Gemini API không đồng nghĩa dữ liệu nghiệp vụ đã sẵn sàng. |
| 8 | Tốc độ PoC & rollout | 5% | **6** | **3,0** | Có demo thật chạy được, là điểm mạnh rõ ràng. Tuy nhiên chưa có tích hợp, người dùng vận hành và kế hoạch được xác nhận để pilot trong 4–6 tuần; chưa đủ toàn bộ điều kiện dải 8–10. Không có bằng chứng rằng PoC phải mất 3–4 tuần; điểm 6 phản ánh demo sớm nhưng rollout chưa rõ. |
| 9 | Kiểm soát rủi ro & an toàn | 10% | **7** | **7,0** | Không có công cụ gửi tin/điều xe; nháp có cờ duyệt; có kiểm tra cấu trúc và 6/6 ca đạt. Tuy nhiên HITL chưa được triển khai thành luồng phê duyệt thực tế, rule chưa chặn hết lỗi ngữ nghĩa, và từng có ca chọn sai hành động. Chưa chứng minh mức kiểm soát dải 8–10; không coi HITL hoặc 6 ca thử là bảo đảm tuyệt đối. |
| 10 | Định vị & trải nghiệm Vingroup | 10% | **8** | **8,0** | Liên hệ trực tiếp hỗ trợ vận hành xe điện, tài xế và dịch vụ di chuyển xanh. Điểm cao về mức phù hợp chiến lược theo bảng; chưa phải bằng chứng CSAT/NPS hoặc tác động Net Zero đã tăng. Không chấm 9–10 vì chưa có kết quả trải nghiệm ngoài thực địa. |
| | **Tổng** | **100%** | | **37,0** | |

## 3. Tổng hợp theo nhóm

| Nhóm | Điểm đạt / điểm tối đa | Nhận định |
|---|---:|---|
| Tài chính & P&L | **8/35** | Thiếu chứng cứ giờ công, tổn thất tránh được và doanh thu. |
| Vận hành & Quy mô | **5/20** | Chưa đo cycle time; giả định volume thấp. |
| Kỹ thuật & Triển khai | **9/25** | Demo đã chạy; dữ liệu nghiệp vụ và ưu thế so với rule chưa rõ. |
| Rủi ro & Chiến lược | **15/20** | Phạm vi chỉ soạn nháp giúp hạn chế quyền thực thi; phù hợp định vị xe điện. |
| **Tổng** | **37/100** | |

## 4. Điều gì cần thay đổi để được chấm cao hơn?

1. **Đo giờ công và cycle time riêng:** ghi thời gian thực hiện, thời gian chờ, thời gian duyệt/sửa cho từng bước trên các ca có thật được phép dùng. So sánh thủ công, form + mẫu tin và LLM trên cùng dữ liệu; ghi tổng giờ công chứ không chỉ thời gian API trả lời.
2. **Xác minh volume đúng đối tượng:** thống kê số ca sự cố pin thực tế/ngày trong phạm vi triển khai. Chỉ cộng ca từ địa bàn/đơn vị khác khi có căn cứ; không tăng giả định 20 thành 2.000 để đạt dải điểm cao.
3. **Lượng hóa P&L:** có chi phí nhân sự thực, mức bồi hoàn và chi phí sự cố. Giờ công giải phóng không tự động trở thành tiền lương tiết kiệm nếu chưa có phương án phân bổ lại công việc hoặc giảm chi phí. Trừ chi phí API, tích hợp, giám sát, duyệt và vận hành trước khi nói đến lợi ích ròng.
4. **Chứng minh phần AI mang lại:** so sánh chất lượng với form + rule; chỉ mở rộng sang audio/BMS nếu có nhu cầu nghiệp vụ và dữ liệu thật, không thêm công nghệ để lấy điểm.
5. **Làm rõ đường tới pilot:** xác nhận nguồn pin/GPS, cơ chế phê duyệt, trách nhiệm, fallback và kế hoạch tích hợp. Thử nhiều lượt trên tập độc lập, thêm pin sát ngưỡng, dữ liệu mâu thuẫn và nội dung không rõ ràng.

## 5. Kết luận đánh giá

Đề tài phù hợp để học và trình diễn cách kiểm tra ranh giới prompt, có bằng chứng sửa từ 3/4 lên 6/6. Với bảng ưu tiên đầu tư do người dùng cung cấp, điểm yếu hiện tại nằm ở **P&L, volume và độ sẵn sàng dữ liệu**. Tài chính và quy mô cùng chiếm 55% nên demo thành công chưa đủ kéo điểm tổng lên cao.

Giữ quyết định **NOT YET cho triển khai thực tế**, tập trung thu dữ liệu và so sánh với rule trước khi mở rộng. Đây là nhận định về mức đủ căn cứ hiện có, không phải kết luận đề tài không có tiềm năng hoặc bài lab chỉ được 37 điểm. Không thay thế rubric 100 điểm gốc của môn học bằng bảng đánh giá này.
