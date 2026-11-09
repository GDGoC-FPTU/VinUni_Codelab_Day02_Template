# AI Log & Reflection — Day 02: AI Product Scoping

**Đề tài đề xuất:** Trợ lý soạn phương án hỗ trợ sự cố pin cho điều phối viên Xanh SM.  
**Ngày lập nhật ký:** 09/11/2026.  
**Người học:** Bổ sung họ tên, MSSV và branch cá nhân trước khi nộp.  
**Trạng thái:** Dự thảo cá nhân dựa trên cuộc trao đổi và kết quả terminal đã cung cấp; chưa xác nhận bằng thử nghiệm prototype Day 02.

> Đây là nhật ký có AI hỗ trợ biên soạn. Người học cần đọc lại, chỉnh phần tự phản ánh theo đúng hiểu biết của mình và bổ sung công việc thực tế sau khi chạy thử. Nội dung không đại diện cho trải nghiệm của mọi thành viên hoặc quyết định đã được cả nhóm thông qua.

## 1. Phạm vi và cách ghi nhận bằng chứng

Nhật ký gồm quá trình chuẩn bị với Gemini API ở Day 01 và quá trình xây dựng phạm vi sản phẩm ở Day 02. Các ví dụ Day 01 được giữ lại vì chúng ảnh hưởng trực tiếp đến cách thiết kế ranh giới, đo lường và đánh giá prototype Day 02.

| Nhãn bằng chứng | Ý nghĩa trong tài liệu |
| --- | --- |
| Đã quan sát | Có đoạn code, kết quả terminal hoặc yêu cầu của người học trong cuộc trao đổi. |
| Đã soạn | AI đã hỗ trợ tạo nội dung tài liệu; nội dung đó chưa trở thành bằng chứng về hoạt động thực tế của doanh nghiệp. |
| Đề xuất, chưa xác nhận | Hướng sửa hoặc thiết kế đã được đưa ra nhưng chưa có kết quả chạy lại hay xác nhận từ người dùng nghiệp vụ. |
| Chưa thực hiện | Chưa có kết quả được cung cấp để ghi nhận là đã hoàn thành. |

ChatGPT hỗ trợ giải thích, rà soát code và soạn tài liệu. Gemini API được người học gọi để thử sinh nội dung. Không ghi nhận chính xác phiên bản backend cho từng lần gọi; đoạn code chatbot được cung cấp sau đó sử dụng tên model `gemini-3.5-flash-lite`.

Không có phỏng vấn điều phối viên, dữ liệu vận hành Xanh SM, lịch sử điều xe hoặc xác nhận của doanh nghiệp trong bằng chứng hiện có.

## 2. Nhật ký tương tác và những thay đổi tạo ra

Các mục dưới đây được nhóm theo nội dung, không phải bản ghi có mốc giờ cho từng lần tương tác. Những yêu cầu không đặt trong dấu trích dẫn là phần tóm lược cuộc trao đổi.

| Mục | Yêu cầu hoặc vấn đề của người học | AI hỗ trợ gì | Kết quả và giới hạn bằng chứng |
| --- | --- | --- | --- |
| L01 — Hiểu SDK và API | Hỏi module, client, config, API và SDK khác nhau như thế nào. | Giải thích các đối tượng trong đoạn gọi Gemini và tách việc xử lý phía chương trình khỏi việc sinh nội dung trên máy chủ. | Người học tiếp tục chạy ví dụ API và cung cấp đầu ra. Việc hiểu đúng cần kiểm tra bằng giải thích và thực hành, không suy ra chỉ từ code chạy được. |
| L02 — Kết nối dịch vụ | Gặp lỗi thiếu thư viện, lỗi model, timeout, 503 và 504. | Hướng dẫn dùng đúng Python trong môi trường ảo, kiểm tra model và cấu hình lời gọi. | Có các lần gọi thành công sau đó. Vì prompt, model và cấu hình đã thay đổi qua nhiều lần thử, chưa thể kết luận biến nào là nguyên nhân duy nhất giúp hết lỗi. |
| L03 — Kiểm soát nội dung | Model mô tả bàn phím vượt quá dữ kiện được cung cấp. | Đề xuất prompt giới hạn dữ kiện và cấm thêm nhận xét về chất lượng, hiệu năng, giá rẻ. | Có đầu ra sau chỉnh prompt phù hợp hơn với ba dữ kiện. Đây là quan sát trên vài lần gọi, chưa chứng minh độ tin cậy trên tập dữ liệu lớn. |
| L04 — Đo hiệu năng | Người học nhận thấy thời gian phản hồi có vẻ không chính xác. | Rà soát vị trí `time.perf_counter()` và chỉ ra lỗi đo cộng dồn bên ngoài vòng lặp. | Lỗi được xác định từ code đã gửi. Hướng sửa được đề xuất; chưa có kết quả chạy lại của phiên bản vòng lặp đã sửa để xác nhận. |
| L05 — Đọc yêu cầu Day 02 | Yêu cầu đọc repo và hướng dẫn làm bài nhóm. | Tách các phần scan, deep dive, prototype, AI log và sơ đồ; đối chiếu README với worksheet. | Đã xác định các đầu ra cần có. Đối với adversarial tests, chọn tối thiểu 3 theo worksheet thay vì chỉ dừng ở 2 test trong starter. |
| L06 — Problem Scan | Yêu cầu làm phần 1. | Soạn 5 giả thuyết vấn đề và 3 Quick Cards; đề xuất ưu tiên bài toán hỗ trợ sự cố pin. | Đã soạn `01-problem-scan.md`. Chưa có bằng chứng nhóm đã bỏ phiếu chọn hoặc người dùng nghiệp vụ đã xác nhận vấn đề. |
| L07 — Deep Dive | Yêu cầu sang phần tiếp theo sau phần 1. | Soạn workflow, Problem Statement, so sánh phương án, ranh giới, kế hoạch kiểm thử và điều kiện triển khai. | Đã soạn `02-deep-dive-report.md`, bao gồm 20 ca kiểm thử dự kiến. Trạng thái là **NOT YET**, không ghi nhận các ca đó đã pass. |
| L08 — Tự phản ánh | Yêu cầu tiếp tục sang phần 3. | Tổng hợp AI giúp gì, sai hoặc thiếu gì, cách điều chỉnh và những việc còn cần tự thực hiện. | Tài liệu hiện tại là bản dự thảo để người học rà soát và bổ sung kết quả cá nhân. |

## 3. Ví dụ thực tế: model thêm thông tin ngoài dữ kiện

**Dữ kiện ban đầu:** Bàn phím có dây, kết nối USB, giá 500.000 đồng; yêu cầu viết hai câu mô tả.

Một kết quả do người học cung cấp có nội dung:

> This wired keyboard features a reliable USB connection for seamless typing. It is available now at an affordable price of 500,000 VND.

Các nhận xét `reliable`, `seamless typing` và `affordable` không được dữ kiện đầu vào chứng minh. Đầu ra có thể nghe tự nhiên nhưng chưa đáp ứng yêu cầu chỉ dùng thông tin đã cung cấp. Đây là vấn đề về độ bám dữ kiện, không phải lỗi cú pháp Python hoặc lỗi truyền nhận của SDK.

AI hỗ trợ đề xuất prompt chặt hơn:

```text
Write exactly two factual sentences in English for a product listing.
Use only these facts: wired keyboard, USB connection, price 500,000 VND.
Do not add opinions or claims about quality, reliability, affordability,
performance, or other features.
```

Người học cung cấp các lần chạy sau:

| Lần quan sát | Nội dung đáng chú ý | Input token | Token văn bản trả về | Thời gian được báo |
| --- | --- | ---: | ---: | --- |
| A — Trước khi siết dữ kiện | “reliable USB connection”, “affordable price” | 42 | 30 | Không cung cấp |
| B — Sau khi siết dữ kiện | “This wired keyboard features a USB connection. The price of this product is 500,000 VND.” | 54 | 24 | Không cung cấp |
| C — Một lần chạy tiếp theo | “This wired keyboard features a USB connection. The price is 500,000 VND.” | 54 | 21 | 1,20 giây |

Các con số trên được chép từ kết quả terminal người học gửi. Không coi đây là benchmark có kiểm soát hoặc phép đo đầy đủ token tính phí. Chưa có đủ metadata và bảng giá tại thời điểm gọi để tính chi phí thực tế.

**Điều rút ra để áp dụng vào Day 02:** Prompt cần chỉ rõ dữ liệu được phép sử dụng và điều phải làm khi thiếu dữ liệu. Trợ lý không được tự tạo địa điểm trạm sạc, khoảng cách, khả năng tương thích hoặc trạng thái “đã điều xe”. Sự tự nhiên của câu trả lời không thay thế việc kiểm tra dữ kiện.

## 4. Những lỗi và giới hạn đã nhận diện

### 4.1. Câu trả lời của AI khẳng định quá mức về SDK

Trong một đầu ra Gemini người học gửi, model kết luận rằng muốn tích hợp một hệ thống thì “chắc chắn sẽ phải dùng đến SDK”. Đây là khẳng định quá rộng: có thể gọi HTTP API trực tiếp bằng công cụ hoặc thư viện HTTP, miễn tuân theo giao thức của dịch vụ.

Cách diễn đạt được điều chỉnh: SDK giúp chương trình gọi API và xử lý dữ liệu thuận tiện hơn; SDK không bắt buộc cho mọi tích hợp. Nội dung ngôn ngữ do model sinh ra; SDK không tự nghĩ ra hoặc diễn đạt lại câu trả lời thay model.

**Bài học:** Câu trả lời giải thích có cấu trúc vẫn cần kiểm tra những từ tuyệt đối như “luôn”, “chắc chắn”, “bắt buộc”.

### 4.2. Đo thời gian sai phạm vi

Đoạn code người học cung cấp đặt `start = time.perf_counter()` trước `while True`. Khi đó, thời gian ở lượt sau bao gồm cả thời gian nhập bàn phím và các lượt trước. Các số 3,24; 9,90; 32,76 giây trong phiên đó không phải ba phép đo API độc lập.

AI đề xuất sửa phạm vi đo như sau:

```python
# Đoạn minh họa vị trí đo, không phải toàn bộ chương trình.
prompt = input("Bạn: ").strip()

# Sau khi xử lý quit/exit và bỏ qua input rỗng:
start = time.perf_counter()
response = client.models.generate_content(...)  # Giữ các tham số thực tế.
latency = time.perf_counter() - start

# In nội dung sau khi đã chốt thời gian.
print(response.text)
```

Đây là thời gian của lời gọi SDK, có thể gồm mạng, xử lý phía dịch vụ và retry của SDK; không phải thời gian tính toán thuần của model. Chưa có kết quả người học chạy lại phiên bản vòng lặp đã sửa.

**Áp dụng vào Day 02:** Phải tách API latency khỏi tổng thời gian nghiệp vụ gồm nhận dữ liệu, xác minh, sửa bản nháp, duyệt và xử lý fallback.

### 4.3. Danh sách model và thông báo lỗi chưa chứng minh khả năng sử dụng

Người học đã liệt kê được một số model, trong đó có `gemini-2.5-flash`. Ở các lần gọi sinh nội dung khác, đã gặp lỗi 404, timeout, 503 hoặc 504.

Không coi việc liệt kê model thành công là bằng chứng rằng mọi lời gọi sinh nội dung đều sẽ thành công. Đồng thời, một lỗi dịch vụ không đủ để kết luận SDK hỏng hoặc prompt sai. Tên model trong starter là cấu hình cần kiểm tra với tài khoản sử dụng, không phải cam kết khả dụng lâu dài.

### 4.4. Kiểm tra chuỗi có thể tạo cảm giác an toàn sai

Starter Day 02 kiểm tra sự hiện diện của `[DRAFT_ONLY]` và một số từ khóa. Tuy nhiên:

- Tag có thể xuất hiện giữa hoặc cuối phản hồi, trong khi yêu cầu là phải ở đầu.
- Phản hồi có thể chứa `dispatch_mobile_charger` nhưng vẫn khuyên đi đến trạm xa không phù hợp.
- Câu “đã điều xe cứu hộ” có thể chứa từ khóa mong đợi nhưng lại khẳng định một hành động chưa diễn ra.

Trong báo cáo phần 2, hướng đánh giá được nâng lên: kiểm tra prefix, parse JSON sau prefix, kiểm tra trường bắt buộc, action và nội dung phù hợp tình huống. Các kiểm tra đó mới là thiết kế; chưa có bằng chứng đã được cài đặt hoặc chạy thành công.

## 5. AI hỗ trợ thiết kế ranh giới Day 02 như thế nào?

AI giúp chuyển yêu cầu chung thành các quyết định có thể kiểm tra. Các quyết định sau đã được viết trong báo cáo phần 2, chưa phải kết quả thử model:

| Quyết định thiết kế | Lý do | Việc còn phải xác nhận |
| --- | --- | --- |
| Rule xử lý ngưỡng pin, LLM hỗ trợ diễn đạt, con người duyệt | Điều kiện số học cần nhất quán; lời nhắn vẫn cần linh hoạt theo dữ liệu. | So sánh với phương án chỉ dùng rule và mẫu tin nhắn. |
| Pin `< 5%` tạo đề xuất `dispatch_mobile_charger` | Theo boundary của bài lab; không khuyên trạm xa để đáp ứng yêu cầu thúc ép của người dùng. | Chạy ca dưới ngưỡng, đúng ngưỡng và các ca tấn công. Không coi ngưỡng lab là hướng dẫn vận hành đã được doanh nghiệp phê duyệt. |
| Mọi đầu ra bắt đầu bằng `[DRAFT_ONLY]` | Thể hiện kết quả là bản nháp cần duyệt. | Kiểm tra bằng code; không dựa vào tag như một cơ chế cấp quyền. |
| Không có công cụ gửi tin hoặc điều xe trong prototype | Phạm vi thử nghiệm là đề xuất hỗ trợ quyết định. | Nếu mở rộng sau này, cần thiết kế quyền gọi công cụ và bước phê duyệt riêng. |
| Pin thiếu, không hợp lệ hoặc mâu thuẫn thì yêu cầu xác minh | Không tự đoán dữ liệu quyết định phương án. | Kiểm tra tình huống thiếu hoặc xung đột dữ kiện. |
| Pin critical nhưng thiếu GPS: giữ đề xuất hỗ trợ di động ở dạng nháp, đồng thời nêu trường thiếu | Không được chuyển thành lời khẳng định đã điều xe hoặc tự tạo vị trí. | Kiểm tra cả action, `missing_fields` và nội dung nháp. |
| Prefix rồi đến JSON | Vừa giữ yêu cầu tag, vừa cho phép kiểm tra cấu trúc phần nội dung. | Không parse toàn bộ phản hồi như JSON thuần; phải kiểm tra và tách prefix trước. |

Đề xuất có `requires_human_approval: true` chỉ mô tả trạng thái mong muốn. Việc chặn hành động phải do chương trình và quyền thực thi bảo đảm, không giao cho lời hứa trong prompt.

## 6. Phản ánh cá nhân — bản để người học rà soát

Trong quá trình học, tôi dùng AI để hiểu cách gọi API, đọc các đối tượng của SDK và phân tích kết quả thực hành. Tôi đã chạy các ví dụ và gửi lại đầu ra, thay vì chỉ xem code được đề xuất. Khi thời gian phản hồi có vẻ bất thường, tôi nêu nghi vấn và cung cấp đoạn code để rà soát phạm vi đo.

Qua ví dụ mô tả bàn phím, tôi thấy rằng câu trả lời trôi chảy vẫn có thể thêm nhận xét không được dữ liệu chứng minh. Khi áp dụng sang bài toán sự cố pin, điều cần kiểm tra không chỉ là văn phong mà còn là nguồn dữ kiện, điều kiện số học, trạng thái bản nháp và quyền thực hiện hành động.

Trong Day 02, AI hỗ trợ mở rộng các hướng bài toán và tổ chức tài liệu. Tuy nhiên, các báo cáo được soạn chưa chứng minh rằng nhóm đã hiểu đúng quy trình thực tế hoặc giải pháp tạo ra hiệu quả kinh doanh. Tôi cần tự rà soát yêu cầu bài, giải thích được các quyết định thiết kế và thực hiện prototype trước khi dùng kết quả đó để kết luận.

Phần tôi còn cần làm là kiểm tra code đang có, hoàn thiện `SYSTEM_PROMPT` và `evaluate_prompt()`, chạy các ca kiểm thử, đọc phản hồi thô và ghi nhận cả lỗi. Tôi cũng cần đối chiếu với thành viên nhóm để xác nhận đề tài, phân công và phạm vi; hiện chưa có dữ liệu cho phép viết rằng nhóm đã thống nhất hoặc người dùng nghiệp vụ đã chấp nhận.

## 7. Việc chưa hoàn thành và cách bổ sung nhật ký

| Hạng mục | Trạng thái tại thời điểm lập tài liệu | Bằng chứng cần bổ sung |
| --- | --- | --- |
| Khởi chạy môi trường Day 02 | Chưa có kết quả xác nhận sau lỗi không tìm thấy `.venv\Scripts\python.exe`. | Lệnh chạy thành công bằng đúng Python và import thư viện cần thiết. |
| `SYSTEM_PROMPT` và `evaluate_prompt()` | Phiên bản người học đã gửi còn TODO / `NotImplementedError`. | Code cá nhân đã hoàn thiện và giải thích cách truyền system instruction. |
| Bộ 20 ca T01–T20 | Đã thiết kế, chưa chạy. | Input, raw output, kết quả validator và nhận xét cho từng ca. |
| Sửa vị trí đo thời gian trong chatbot loop | Đã đề xuất, chưa có kết quả chạy lại. | Code mới và số đo của các lượt độc lập. |
| Hiệu quả so với xử lý thủ công hoặc rule-only | Chưa đo. | Cùng tập tình huống, cùng tiêu chí, thời gian gồm cả review và sửa lỗi. |
| Mục tiêu giảm ít nhất 30% thời gian | Mục tiêu đề xuất, chưa đạt được bằng thực nghiệm. | Baseline, thời gian sau áp dụng và cách tính trên ít nhất 10 ca ghép cặp như phần 2 đề xuất. |
| Nhóm chọn đề tài và phân công | Chưa ghi nhận xác nhận. | Quyết định thực tế, người phụ trách và đóng góp cá nhân. |

Khi chạy prototype, mỗi lần thử nên ghi: ngày chạy, commit, tên model được cấu hình, cấu hình sinh nội dung, mã ca, input, raw output, thời gian, usage được trả về, kiểm tra pass/fail và giải thích. Không lưu API key vào nhật ký.

Nếu sửa prompt hoặc validator, giữ lại kết quả trước và sau sửa. Không đổi câu trả lời sai thành câu đúng rồi ghi như phản hồi nguyên gốc của model. Một lần pass không đủ để kết luận model luôn tuân thủ; trường hợp lỗi, response rỗng và lỗi dịch vụ cũng phải được ghi nhận.

**Quyết định hiện tại: NOT YET.** Đây là trạng thái phù hợp với bằng chứng đang có: đã soạn phạm vi và kế hoạch, chưa xác nhận prototype hoặc hiệu quả vận hành.

## 8. Tài liệu đối chiếu

- [Problem Scan](01-problem-scan.md): 5 giả thuyết vấn đề, 3 Quick Cards và hướng ưu tiên đề xuất.
- [Deep Dive Report](02-deep-dive-report.md): workflow, Problem Statement, boundary, 20 ca dự kiến và điều kiện đánh giá lại.
- [README của Day 02](https://github.com/GDGoC-FPTU/VinUni_Codelab_Day02_Template/blob/main/README.md): yêu cầu đầu ra và cách tổng hợp bài nhóm.
- [Worksheet Day 02](https://github.com/GDGoC-FPTU/VinUni_Codelab_Day02_Template/blob/main/01-worksheet.md): tiêu chí AI Log & Reflection và phần phản ánh cá nhân.
- Kết quả terminal và đoạn code do người học cung cấp trong cuộc trao đổi: nguồn cho các quan sát thực hành Day 01 và tình trạng Day 02 hiện có.

**Lưu ý khi tổng hợp nhóm:** Mỗi thành viên cần có phản ánh đúng trải nghiệm của mình. Không đổi tên người thực hiện để dùng nguyên nhật ký này như thể mọi thành viên đều đã chạy cùng các thử nghiệm.
