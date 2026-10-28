# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|---|---|---|
| **1** | **Vinhomes** | **Repetitive + Time-consuming** | **Phân loại và điều phối phản ánh/yêu cầu của cư dân:** Nhân viên phải đọc từng ticket/chat/call, xác định loại sự cố, mức độ ưu tiên rồi chuyển đến đúng bộ phận xử lý. AI có thể tự động phân loại, đánh giá mức độ nghiêm trọng và route ticket. |
| **2** | **Vinhomes** | **Time-consuming + AI-upgrade** | **Kiểm tra defect khi bàn giao căn hộ:** Nhân viên phải đi kiểm tra từng phòng, chụp ảnh, ghi nhận lỗi và lập báo cáo. Computer Vision có thể phát hiện các lỗi như nứt tường, trầy xước, lỗi gạch/sàn và tự động tạo defect report. |
| **3** | **Xanh SM** | **Repetitive + Stakeholder Pain** | **Xử lý các chuyến có vấn đề về điểm đón/trả:** Tài xế thường phải xử lý tình huống điểm đón không chính xác hoặc liên hệ CSKH khi không tìm được khách. AI có thể dự đoán điểm đón tối ưu dựa trên GPS, lịch sử và đặc điểm địa điểm. |
| **4** | **VinFast** | **Repetitive + Time-consuming** | **Phân tích và phân loại lỗi xe từ dữ liệu bảo hành/service:** Kỹ thuật viên phải đọc mô tả lỗi, mã lỗi và lịch sử sửa chữa để xác định nguyên nhân/nhóm lỗi. AI có thể tự động phân loại lỗi, gợi ý nguyên nhân và hướng kiểm tra tiếp theo. |
| **5** | **Vinmec** | **Time-consuming + AI-upgrade** | **Tóm tắt hồ sơ bệnh án và chuẩn bị thông tin trước khám:** Bác sĩ/nhân viên phải đọc nhiều thông tin từ lịch sử khám, xét nghiệm, chẩn đoán và thuốc trước khi tiếp nhận bệnh nhân. AI có thể tổng hợp thành clinical summary để bác sĩ review nhanh hơn. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                      │
│                                                             │
│ Bài toán (1 câu):                                          │
│ Bác sĩ mất nhiều thời gian đọc và tổng hợp lịch sử khám,   │
│ xét nghiệm, chẩn đoán và thuốc của bệnh nhân trước khi    │
│ khám.                                                       │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes │
│                     [x] Vinmec   [ ] Khác                  │
│                                                             │
│ Ai đang đau (Actor)?                                       │
│ Bác sĩ, điều dưỡng và nhân viên tiếp nhận bệnh nhân.       │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                    │
│ 1. Mở hồ sơ bệnh nhân                                      │
│    ──> 2. Đọc lịch sử khám/xét nghiệm                      │
│    ──> 3. Kiểm tra chẩn đoán & thuốc                       │
│    ──> 4. Tổng hợp các thông tin quan trọng                │
│    ──> 5. Bắt đầu khám và đưa ra đánh giá                  │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                           │
│ Bước 2-4 – đọc và tổng hợp thông tin từ nhiều nguồn        │
│ (⏱ 5-15 phút/bệnh nhân, tùy độ phức tạp hồ sơ).            │
│                                                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                     │
│ Bước 2-4: AI tự động đọc, trích xuất và tóm tắt các thông  │
│ tin quan trọng thành một Clinical Summary để bác sĩ review.│
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                     │
│ Giảm thời gian chuẩn bị hồ sơ trước khám từ                │
│ 5-15 phút ──> dưới 2-3 phút/bệnh nhân;                    │
│ giảm thời gian đọc/tổng hợp hồ sơ ≥50%.                    │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM           │
│                     [ ] Agent                              │
└─────────────────────────────────────────────────────────────┘
```