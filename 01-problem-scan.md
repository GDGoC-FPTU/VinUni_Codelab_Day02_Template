---
## 🏛️ Bối cảnh: Tôi là ai?

Tôi là **Vũ**, AI Engineer tại **Vin Group**. Nhóm chúng tôi được giao nhiệm vụ phối hợp với Khối Vận Hành của **Vinpearl** để tìm kiếm các cơ hội tối ưu hóa bằng trí tuệ nhân tạo.

Thông qua khảo sát Tổng hợp & Phân tích review khách sạn trên Booking.com, Agoda, Google Map của Vinpearl để lọc ra các phàn nàn của khách hàng , tôi nhận thấy các trải nghiệm của khách hàng đang bị ảnh hương nghiêm trọng từ các vần đề về vệ sinh an toàn, thái độ phục vụ cho tới khâu booking phòng đều đang có những bất cập, dẫn đến việc trải nghiệm khách hàng đi xuống giảm tỷ lệ khách quay lại hoặc giới thiệu tới khách hàng mới. Bài toán tôi mang vào buổi Lab hôm nay đến từ chính quan sát thực tế này.
---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

Dùng **4 Lenses** quét qua vận hành của các công ty thành viên Vingroup.

| #   | Subsidiary | Lens               | Mô tả ngắn bài toán                                                                                                                                                        |
| --- | ---------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Vinhomes   | AI có thể tốt hơn  | Trợ lý cư dân ảo hỗ trợ tra cứu quy trình và draft hồ sơ đăng ký thi công nội thất, đăng ký vé gửi xe hằng tháng, giảm nhu cầu liên hệ trực tiếp ban quản lý.chừng.        |
| 2   | Vinpearl   | Pain từ người khác | Tổng hợp review từ Booking.com, Agoda, Google Maps để phát hiện các phàn nàn nghiêm trọng như phòng bẩn, thái độ nhân viên kém, thiết bị hỏng và gửi cảnh báo đến Manager. |
| 3   | Vinpearl   | Tốn thời gian      | Đọc và trích xuất thông tin từ email Group Booking phức tạp của công ty lữ hành, đối chiếu quỹ phòng trống và tự động draft lệnh đặt phòng.                                |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Thẻ bài toán tiêu biểu: Card #7 — Vinhomes Trợ lý cư dân ảo

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #7                                       │
│                                                             │
│ Bài toán: Cư dân cần tìm hiểu quy trình và chuẩn bị hồ sơ   │
│ đăng ký thi công nội thất, đăng ký vé gửi xe hằng tháng.    │
│                                                             │
│ Công ty thành viên:  Vinhomes                               │
│                                                             │
│ Actor / Operator? Cư dân (mất thời gian tìm hiểu thủ tục),  │
│ Ban quản lý (phải giải đáp các câu hỏi lặp lại).            │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Cư dân liên hệ ban quản lý để hỏi thủ tục.             │
│   → 2. Nhân viên tìm kiếm biểu mẫu và quy định liên quan.   │
│   → 3. Hướng dẫn cư dân chuẩn bị giấy tờ cần thiết.         │
│   → 4. Cư dân điền biểu mẫu và gửi hồ sơ.                   │
│   → 5. Ban quản lý kiểm tra và yêu cầu bổ sung nếu thiếu.   │
│                                                             │
│ Bottleneck? Bước 1-3 (tra cứu và giải đáp thủ tục).         │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1-3.             │
│ (Chatbot tra cứu quy định, hướng dẫn theo từng trường hợp,  │
│ draft biểu mẫu và checklist giấy tờ cần chuẩn bị).          │
│                                                             │
│ Success Metric?                                             │
│ Mục tiêu đề xuất: Giảm 50% thời gian nhân viên giải đáp     │
│ các câu hỏi thủ tục thông thường.                           │
│                                                             │
│ Quick Architecture: [x] RAG + LLM Feature                   │
│ (RAG truy xuất quy định chính thức, LLM tư vấn và soạn      │
│ hồ sơ mẫu; cư dân xác nhận trước khi gửi).                  │
└─────────────────────────────────────────────────────────────┘

Thẻ bài toán tiêu biểu: Card #8 — Vinpearl Tổng hợp & Phân tích Review khách sạn

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #8                                       │
│                                                             │
│ Bài toán: Manager khách sạn khó theo dõi và tổng hợp lượng  │
│ lớn review từ Booking.com, Agoda, Google Maps. Những phản   │
│ ánh nghiêm trọng như phòng bẩn, nhân viên thái độ kém,      │
│ thiết bị hỏng có thể bị bỏ sót giữa hàng trăm review.       │
│                                                             │
│ Công ty thành viên:  Vinpearl                               │
│                                                             │
│ Actor / Operator? Manager (khó nắm bắt vấn đề tổng thể),    │
│ Bộ phận vận hành và chăm sóc khách hàng (phản hồi chậm),    │
│ Khách hàng (trải nghiệm không được cải thiện kịp thời).     │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Nhân viên truy cập các nền tảng đánh giá khách sạn.    │
│   → 2. Đọc từng review và xác định nội dung phàn nàn.       │
│   → 3. Phân loại vấn đề theo bộ phận (Housekeeping,         │
│      Front Office, F&B, Maintenance...).                    │
│   → 4. Tổng hợp các vấn đề nổi bật và báo cáo Manager.      │
│   → 5. Manager chuyển thông tin đến bộ phận phụ trách       │
│      để xử lý và theo dõi kết quả.                          │
│                                                             │
│ Bottleneck? Bước 1-4 (đọc, phân loại và tổng hợp            │
│ lượng lớn review từ nhiều nền tảng).                        │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4.             │
│ (NLP/LLM phân tích cảm xúc, nhận diện vấn đề, phân loại     │
│ mức độ nghiêm trọng, nhóm các phản ánh trùng lặp và         │
│ tự động tạo báo cáo cảnh báo cho Manager).                  │
│                                                             │
│ Success Metric?                                             │
│ Mục tiêu đề xuất:                                           │
│ - Giảm ít nhất 70% thời gian đọc và tổng hợp review.        │
│ - Recall >= 95% đối với nhóm phàn nàn nghiêm trọng.         │
│ - 100% cảnh báo nghiêm trọng được chuyển đến đúng bộ phận   │
│   phụ trách để kiểm tra và xử lý.                           │
│                                                             │
│ Quick Architecture:  NLP + LLM Feature                      │
│ (Thu thập dữ liệu hợp lệ -> NLP phân loại cảm xúc và vấn đề │
│ -> LLM tổng hợp, đánh giá mức độ ưu tiên -> Dashboard và    │
│ cảnh báo đến Manager).                                      │
└─────────────────────────────────────────────────────────────┘

Thẻ bài toán tiêu biểu: Card #9 — Vinpearl Tự động hóa kiểm tra phòng trống & Booking

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #9                                       │
│                                                             │
│ Bài toán: Nhân viên đặt phòng phải đọc email Group Booking  │
│ từ các công ty lữ hành với nhiều thông tin phức tạp như     │
│ ngày nhận/trả phòng, số lượng khách, loại phòng, yêu cầu    │
│ đặc biệt và đối chiếu thủ công với quỹ phòng hiện có.       │
│                                                             │
│ Công ty thành viên:  Vinpearl                               │
│                                                             │
│ Actor / Operator? Nhân viên Reservation                     │
│  (xử lý email thủ công)                                     │
│ Bộ phận kinh doanh (phản hồi đối tác chậm),                 │
│ Khách hàng/đối tác lữ hành (chờ xác nhận đặt phòng).        │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Nhận email yêu cầu đặt phòng theo đoàn.                │
│   → 2. Đọc email và trích xuất thông tin đặt phòng.         │
│   → 3. Kiểm tra quỹ phòng theo ngày, loại phòng và số lượng.│
│   → 4. Đối chiếu các yêu cầu đặc biệt và chính sách giá.    │
│   → 5. Soạn phản hồi và draft lệnh booking để xác nhận.     │
│                                                             │
│ Bottleneck? Bước 2-4 (trích xuất, đối chiếu và              │
│ kiểm tra tình trạng phòng).                                 │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-5.             │
│ (LLM trích xuất dữ liệu từ email, chuyển thành cấu trúc     │
│ chuẩn, kết nối hệ thống quản lý phòng để kiểm tra tồn kho   │
│ và draft lệnh booking).                                     │
│                                                             │
│ Success Metric?                                             │
│ Mục tiêu đề xuất:                                           │
│ - Giảm ít nhất 60% thời gian xử lý một yêu cầu Group Booking│
│ - Độ chính xác trích xuất thông tin >= 98%.                 │
│ - 100% booking được nhân viên xác nhận trước khi ghi nhận   │
│   chính thức vào hệ thống.                                  │
│                                                             │
│ Quick Architecture:  LLM Feature + API Integration          │
│ (LLM trích xuất email -> Structured Data -> API kiểm tra    │
│ quỹ phòng -> Draft Booking -> Nhân viên xác nhận).          │
└─────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết định lựa chọn của nhóm:

Nhóm quyết định chọn bài toán "Card #8 — Vinpearl Tổng hợp & Phân tích Review khách sạn" để thực hiện Deep-Dive.

## Lý do lựa chọn và loại bỏ các thẻ khác:

Lý do lựa chọn và loại bỏ các thẻ khác

Card #8 (Vinpearl — Tổng hợp & Phân tích Review khách sạn):
Pain rõ ràng: Manager phải tiếp nhận lượng lớn đánh giá từ nhiều nền tảng, khó theo dõi toàn bộ phản ánh và dễ bỏ sót những vấn đề nghiêm trọng.
AI thực sự tạo ra giá trị: Không chỉ tìm kiếm từ khóa mà còn hiểu ngữ cảnh, phân tích cảm xúc, nhận diện vấn đề, đánh giá mức độ nghiêm trọng và tổng hợp các phản ánh tương tự.
Tác động trực tiếp đến hoạt động kinh doanh: Phát hiện sớm vấn đề về chất lượng phòng, thái độ nhân viên và dịch vụ giúp khách sạn xử lý kịp thời, cải thiện trải nghiệm khách hàng và uy tín thương hiệu.
Có thể đo lường hiệu quả: Đánh giá bằng Recall đối với phàn nàn nghiêm trọng, thời gian tổng hợp review và tỷ lệ cảnh báo được xử lý đúng bộ phận.
Có khả năng mở rộng: Có thể triển khai trước tại một khách sạn, sau đó mở rộng sang nhiều khách sạn trong hệ thống Vinpearl.

Card #7 (Vinhomes — Trợ lý cư dân ảo):
Bài toán có tính ứng dụng cao nhưng phần lớn câu hỏi thủ tục có thể được giải quyết bằng hệ thống FAQ, Rule-based và RAG trên bộ quy định chính thức.
Những thủ tục liên quan đến pháp lý, phí dịch vụ và điều kiện thi công cần độ chính xác cao, phải có cơ chế kiểm duyệt và xác nhận từ ban quản lý.
Mức độ khác biệt của AI so với một hệ thống tra cứu thông minh có thể chưa đủ nổi bật trong phạm vi MVP.

Card #9 (Vinpearl — Tự động hóa kiểm tra phòng trống & Booking):
Có tiềm năng tiết kiệm thời gian vận hành lớn nhưng phụ thuộc nhiều vào khả năng tích hợp email, PMS (Property Management System) và hệ thống quản lý tồn kho phòng.
Sai sót khi trích xuất ngày tháng, số lượng phòng hoặc loại phòng có thể dẫn đến overbooking và thiệt hại doanh thu.
Cần quyền truy cập dữ liệu vận hành nội bộ và cơ chế xác nhận booking chặt chẽ, khiến việc xây dựng MVP có thể phức tạp hơn.
Kết luận: Card #8 được ưu tiên vì cân bằng tốt giữa mức độ đau của người dùng, khả năng ứng dụng AI thực chất, tính khả thi của MVP và tác động trực tiếp đến chất lượng dịch vụ của Vinpearl.

---
