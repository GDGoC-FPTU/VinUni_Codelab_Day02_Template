# 🏗️ Phase 3 — DEEP-DIVE (Nhóm)

## 3.1. Current-State Workflow

Quy trình xử lý và tổng hợp đánh giá khách hàng (Review Analysis) hiện tại của Manager khách sạn Vinpear

```text
┌──────────────┐     ┌───────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2        │     │ Bước 3       │
│ Thu thập     │     │ Đọc và phân   │     │ Xác định     │
│ review từ    │ ──> │ tích từng     │ ──> │ vấn đề và    │
│ các nền tảng │     │ review        │     │ mức độ lỗi   │
│              │     │               │     │              │
│ Ai: CSKH     │     │ Ai: CSKH      │     │ Ai: CSKH     │
│ ⏱ 5 phút    │     │ ⏱ 10 phút 🔴 │     │ ⏱ 5 phút 🔴 │
│ In: Review   │     │ In: Nội dung  │     │ In: Review   │
│ Out: Raw data│     │ Out: Phân tích│     │ Out: Nhóm lỗi│
└──────────────┘     └───────────────┘     └──────────────┘
                                                   │
                                                   ▼
                     ┌────────────────┐     ┌──────────────┐
                     │ Bước 5         │     │ Bước 4       │
                     │ Manager phân   │     │ Tổng hợp     │
                     │ công bộ phận   │ <── │ báo cáo      │
                     │ xử lý          │     │              │
                     │                │     │              │
                     │ Ai: Manager    │     │ Ai: CSKH     │
                     │ ⏱ 5 phút      │     │ ⏱ 5 phút 🔴 │
                     │ In: Báo cáo    │     │ In: Nhóm lỗi │
                     │ Out: Phân công │     │ Out: Báo cáo │
                     └────────────────┘     └──────────────┘

🔴 = Bottlenecks

⏱ Tổng thời gian xử lý thủ công giả định: 30 phút/10 review, chưa tính thời gian chờ truy cập và đồng bộ dữ liệu từ các nền tảng.

Quy trình có thể kéo dài hơn khi lượng review tăng cao hoặc nhiều khách sạn cần được theo dõi đồng thời.
```

---

## 3.2. Problem Statement (6-field) — Vin Smart Future Standard

| Field                       | Nội dung                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Actor / Operator**     | Nhân viên CSKH và Manager khách sạn thuộc hệ thống Vinpearl. CSKH chịu trách nhiệm thu thập, đọc và phân loại review; Manager tiếp nhận báo cáo, đánh giá và điều phối bộ phận xử lý.                                                                                                                                                                                                                                                                          |
| **2. Current Workflow**     | Nhân viên thu thập review từ Booking.com, Agoda và Google Maps; đọc từng đánh giá; xác định cảm xúc và vấn đề khách hàng phản ánh; phân loại theo bộ phận như Housekeeping, Front Office, F&B, Maintenance; tổng hợp báo cáo và gửi Manager để phân công xử lý. Quy trình phụ thuộc nhiều vào thao tác thủ công.                                                                                                                                               |
| **3. Bottleneck**           | Bước 2, 3 và 4: Đọc từng review, nhận diện vấn đề, xác định mức độ nghiêm trọng và tổng hợp báo cáo. Review có thể sử dụng ngôn ngữ không chuẩn, viết tắt, mỉa mai hoặc chứa nhiều vấn đề trong cùng một nội dung khiến việc phân loại mất thời gian và dễ bỏ sót phản ánh khẩn cấp.                                                                                                                                                                           |
| **4. Business Impact**      | Manager không có cái nhìn tổng thể và kịp thời về chất lượng dịch vụ. Các vấn đề như phòng bẩn, thái độ nhân viên kém, thiết bị hỏng có thể không được phát hiện sớm. Điều này làm tăng thời gian phản hồi, ảnh hưởng trải nghiệm khách hàng, điểm đánh giá trực tuyến và uy tín thương hiệu Vinpearl.                                                                                                                                                         |
| **5. Success Metric**       | 1. Giảm ít nhất 70% thời gian đọc và tổng hợp review (Efficiency). 2. Recall >= 95% đối với nhóm phàn nàn nghiêm trọng (Quality). 3. Precision >= 90% đối với cảnh báo nghiêm trọng để hạn chế cảnh báo sai (Quality). 4. 100% cảnh báo nghiêm trọng được chuyển đến Manager/bộ phận phụ trách để kiểm tra (Operational Coverage).                                                                                                                             |
| **6. Operational Boundary** | AI được phép phân tích review, nhận diện cảm xúc, trích xuất vấn đề, phân loại theo bộ phận, đánh giá mức độ ưu tiên, nhóm các phản ánh tương tự và tạo báo cáo/cảnh báo dạng nháp. CẤM: AI không được tự ý phản hồi khách hàng, xóa hoặc chỉnh sửa review, tự kết luận nhân viên có lỗi, hoặc tự động kỷ luật/phân công xử lý khi chưa có Manager phê duyệt. Dữ liệu phải được thu thập từ nguồn được phép truy cập và tuân thủ điều khoản của từng nền tảng. |

---

## 3.3. Future-State Flow & AI Fit

- **AI Fit:** Chọn **LLM Feature** Không cần Agent tự trị ở giai đoạn MVP vì quy trình có cấu trúc tương đối cố định: tiếp nhận review → phân tích → phân loại → đánh giá mức độ ưu tiên → báo cáo.

LLM giúp hiểu ngữ cảnh và nội dung phản ánh, NLP hỗ trợ phân loại cảm xúc/chủ đề, còn Rule-based đảm nhiệm các quy tắc ưu tiên và ngưỡng cảnh báo rõ ràng.

- **Quy trình tương lai (Future-State):**

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │
│ Thu thập     │     │ 🔵 Auto      │     │ 🔵 AI phân   │
│ review từ    │ ──> │ chuẩn hóa    │ ──> │ tích review  │
│ nguồn hợp lệ │     │ dữ liệu      │     │ và cảm xúc   │
│              │     │              │     │              │
│              │     │              │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
                                                   │
                                                   ▼
 ┌──────────────┐    ┌──────────────┐     ┌──────────────┐
 │ Bước 6       │    │ Bước 5       │     │ Bước 4       │
 │ Chuyển đến   │ <──│ 🟢 Manager  │ <── │ 🔵 AI tổng   │
 │ bộ phận liên │    │ kiểm tra và  │     │ hợp báo cáo  │
 │ quan xử lý   │    │ xác nhận     │     │ + cảnh báo   │
 │              │    │              │     │              │
 │              │    └──────────────┘     └──────────────┘
 └──────────────┘

🔵 = AI / Automation
🟢 = Human-in-the-loop (HITL)

↩️ Fallback:
Nếu AI không phân loại được review, độ tin cậy thấp
hoặc phát hiện nội dung bất thường:
→ Chuyển review vào danh sách cần kiểm tra thủ công.
→ CSKH/Manager tự phân loại và xác nhận.
→ Không được tự động bỏ qua review.
```

# 🏁 Phase 5 — EVALUATE (Nhóm, 20 min)

### AI Readiness Checklist:

1. [ ] Có sẵn dữ liệu review mẫu từ các khách sạn để xây dựng tập dữ liệu kiểm thử và gán nhãn?
2. [ ] Đã xác định được tiêu chí phân loại cảm xúc, chủ đề và mức độ nghiêm trọng của review?
3. [ ] Có cơ chế HITL và Fallback để Manager/CSKH kiểm tra những cảnh báo sai hoặc review AI không hiểu?
4. [ ] Có nguồn dữ liệu review hợp pháp và phương án tích hợp/thu thập dữ liệu ổn định?
5. [ ] Các bộ phận Housekeeping, Front Office, F&B, Maintenance và Manager sẵn sàng tiếp nhận quy trình cảnh báo mới?

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:

[ ] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):** Chuẩn bị dữ liệu, xác minh khả năng truy cập nguồn review và thiết lập bộ tiêu chí đánh giá trước khi triển khai Prototype chính thức.
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):** Hủy bỏ dự án AI này.

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**

> Lựa chọn NOT YET vì bài toán có tiềm năng ứng dụng AI rõ ràng, nhưng hiện chưa có đủ bằng chứng về dữ liệu đầu vào, quyền truy cập review và hiệu quả thực tế để cam kết triển khai chính thức.

1. Về tính khả thi kỹ thuật:
   LLM có khả năng hiểu ngữ cảnh, nhận diện các cách diễn đạt khác nhau và trích xuất nhiều vấn đề trong cùng một review.
   NLP kết hợp Rule-based có thể hỗ trợ phân loại cảm xúc, chủ đề và mức độ nghiêm trọng.
   Tuy nhiên, cần kiểm thử các trường hợp khó như mỉa mai, tiếng lóng, review đa ngôn ngữ, nội dung ngắn và review chứa nhiều vấn đề cùng lúc.

2. Về dữ liệu:
   Cần thu thập review từ các nguồn được phép truy cập.
   Cần xây dựng tập dữ liệu đã gán nhãn để đánh giá Precision, Recall và F1-score.
   Cần xác định rõ thế nào là phàn nàn nghiêm trọng để tránh cảnh báo sai hoặc bỏ sót sự cố thực sự.

3. Về chi phí:
   Chi phí chính bao gồm thu thập và chuẩn hóa dữ liệu, sử dụng API LLM, lưu trữ, xây dựng Dashboard và bảo trì hệ thống.
   Cần so sánh chi phí sử dụng LLM với phương án phân loại từ khóa/Rule-based.
   Chỉ nên sử dụng LLM cho những review cần hiểu ngữ cảnh phức tạp để tối ưu chi phí.

4. Kế hoạch trước khi GO:
   Giai đoạn 1: Thu thập review hợp lệ từ một khách sạn Vinpearl.
   Giai đoạn 2: Xây dựng bộ dữ liệu mẫu và gán nhãn các nhóm vấn đề.
   Giai đoạn 3: Xây dựng Prototype phân tích review và Dashboard cảnh báo.
   Giai đoạn 4: Đánh giá trên tập kiểm thử, đặc biệt tập trung vào Recall của nhóm phàn nàn nghiêm trọng.
   Giai đoạn 5: Cho Manager sử dụng thử, ghi nhận phản hồi và so sánh với quy trình thủ công.

Kết luận: Không bác bỏ tính khả thi của AI nhưng mà lựa chọn NOT YET để giảm rủi ro đầu tư khi chưa có baseline. Khi dữ liệu, quyền truy cập và kết quả kiểm thử đáp ứng yêu cầu, thì mới tính chuyển sang mức GO để triển khai Prototype tại một khách sạn trước khi mở rộng toàn hệ thống Vinpearl.

---
