# Problem Scan & Quick Cards — VinFast Service Triage

# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).


### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **VinFast** | Repetitive + Time-consuming | **Phân loại và điều phối yêu cầu CSKH/sửa chữa:** yêu cầu đi vào từ hotline, email, website/chat và ứng dụng. Nhân viên cần xác định loại yêu cầu, xem có giải quyết ngay được không và nếu không thì chuyển đúng phòng ban/đại lý. Đây là bước có volume lớn và chứa nhiều nội dung free-text. |
| 2 | **Green SM** | Stakeholder Pain + AI-upgrade | **Điều phối phiên sạc và xử lý charging exception:** tài xế phải quyết định lúc nào sạc, trạm nào phù hợp và xử lý khi phiên sạc thất bại. Review Green SM Driver tháng 6/2026 phản ánh việc phiên sạc lỗi khiến tài xế phải chờ lâu mới quét lại, làm mất thời gian vận hành. |
| 3 | **Vinhomes** | Repetitive + Time-consuming | **Phân loại và route yêu cầu cư dân:** các đại đô thị tiếp nhận hàng nghìn yêu cầu mỗi ngày về kỹ thuật, căn hộ, tiện ích, an ninh và các tình huống khác. Yêu cầu có thể đi từ app, điện thoại hoặc quầy lễ tân và cần chuyển tới đúng bộ phận xử lý. |
| 4 | **Vinmec** | Time-consuming + AI-upgrade | **Xác nhận và sắp lịch khám:** người bệnh có thể chọn slot trên website nhưng Vinmec ghi rõ đây mới là “expected time”; Contact Center sau đó vẫn liên hệ để xác nhận thời gian chính xác. |
| 5 | **Vinhomes** | Stakeholder Pain | **Đồng bộ định danh cư dân/thẻ ra vào/thẻ xe:** một review Vinhomes Resident ngày 25/8/2026 phản ánh việc đồng bộ ứng dụng kéo dài khoảng một tuần, khiến người dùng chưa làm được thẻ ra vào và thẻ xe. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu):                                           │
│ Tự động đọc, tóm tắt, phân loại và đề xuất nơi xử lý       │
│ cho các yêu cầu dịch vụ/CSKH của khách hàng VinFast.        │
│                                                             │
│ Công ty thành viên: [X] VinFast  [ ] Xanh SM  [ ] Vinhomes │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│ Nhân viên Contact Center/CSKH, cố vấn dịch vụ, khách hàng.   │
│                                                             │
│ Workflow hiện tại (3–5 bước):                               │
│ 1. Nhận yêu cầu từ hotline/app/email/chat                    │
│    --> 2. Đọc và thu thập thông tin                         │
│    --> 3. Phân loại vấn đề/mức độ                           │
│    --> 4. Chuyển đúng phòng ban/đại lý                      │
│    --> 5. Theo dõi xử lý                                    │
│                                                             │
│ Bước tốn thời gian/lỗi nhất?                                │
│ Bước 2–4: đọc + phân loại + route ticket                    │
│ (⏱ giả định 3–5 phút/lượt)                                  │
│                                                             │
│ AI hỗ trợ ở bước nào?                                       │
│ Bước 2–4: extract thông tin, summarize, classify intent,     │
│ severity và đề xuất queue xử lý.                            │
│                                                             │
│ Đo thành công bằng gì?                                      │
│ - Routing accuracy >= 95%                                   │
│ - Safety-case recall >= 99%                                 │
│ - Giảm triage time từ 3–5 phút xuống < 30 giây             │
│ - 0 safety-critical case bị AI tự động đóng                 │
│                                                             │
│ Quick Architecture: [ ] No AI [ ] Rule [X] LLM [ ] Agent   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu):                                           │
│ Tự động phân loại và chuyển yêu cầu của cư dân Vinhomes     │
│ đến đúng bộ phận xử lý.                                     │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [X] Vinhomes │
│                     [ ] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│ Nhân viên Ban quản lý/CSKH, kỹ thuật, an ninh và cư dân.     │
│                                                             │
│ Workflow hiện tại (3–5 bước):                               │
│ 1. Cư dân gửi yêu cầu qua app/hotline                       │
│    --> 2. Nhân viên đọc nội dung/ảnh                        │
│    --> 3. Xác định loại sự cố + mức ưu tiên                 │
│    --> 4. Chuyển đội phụ trách                              │
│    --> 5. Theo dõi SLA                                      │
│                                                             │
│ Bước tốn thời gian/lỗi nhất?                                │
│ Bước 2–4: đọc ticket, hiểu vấn đề và route                  │
│ (⏱ giả định 2–4 phút/lượt)                                  │
│                                                             │
│ AI hỗ trợ ở bước nào?                                       │
│ Bước 2–4: đọc text + ảnh, xác định category, urgency,       │
│ location và bộ phận chịu trách nhiệm.                       │
│                                                             │
│ Đo thành công bằng gì?                                      │
│ - >= 90% Macro-F1 phân loại ticket                          │
│ - >= 95% routing accuracy                                   │
│ - Emergency recall >= 99%                                   │
│ - Giảm manual triage time >= 60%                            │
│ - 80% routine ticket được phân loại trong <10 giây          │
│                                                             │
│ Quick Architecture: [ ] No AI [ ] Rule [X] LLM [ ] Agent   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│                                                             │
│ Bài toán (1 câu):                                           │
│ Tự động hỗ trợ xác nhận và điều chỉnh các lịch khám         │
│ đơn giản sau khi bệnh nhân đặt lịch trực tuyến.             │
│                                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes │
│                     [X] Vinmec   [ ] Khác                   │
│                                                             │
│ Ai đang đau (Actor)?                                        │
│ Contact Center, điều phối viên, bác sĩ và bệnh nhân.         │
│                                                             │
│ Workflow hiện tại (3–5 bước):                               │
│ 1. Bệnh nhân chọn chuyên khoa/bác sĩ                        │
│    --> 2. Chọn thời gian dự kiến                            │
│    --> 3. Gửi booking                                       │
│    --> 4. Contact Center kiểm tra/xác nhận                   │
│    --> 5. Gọi lại hoặc điều chỉnh lịch                      │
│                                                             │
│ Bước tốn thời gian/lỗi nhất?                                │
│ Bước 4–5: kiểm tra availability + liên hệ xác nhận           │
│ (⏱ giả định 3–5 phút/booking)                               │
│                                                             │
│ AI hỗ trợ ở bước nào?                                       │
│ Bước 4–5: đọc yêu cầu, kiểm tra dữ liệu lịch, đề xuất slot, │
│ gửi xác nhận hoặc yêu cầu reschedule đơn giản.              │
│                                                             │
│ Đo thành công bằng gì?                                      │
│ - >= 70% routine booking xử lý không cần agent              │
│ - Confirmation time < 1 phút                               │
│ - Scheduling error < 0.5%                                   │
│ - Không tăng complaint/cancellation rate                    │
│ - 100% clinical exception chuyển Human-in-the-loop          │
│                                                             │
│ Quick Architecture: [ ] No AI [X] Rule [X] LLM [ ] Agent   │
└─────────────────────────────────────────────────────────────┘
```

---

## Bằng chứng và giả định

Các nhận định về review ứng dụng, số lượng yêu cầu và quy trình doanh nghiệp trong bảng SCAN là đầu vào cần xác minh, chưa phải kết quả khảo sát nội bộ. Cần bổ sung nguồn trước khi dùng làm bằng chứng quyết định. Các thời gian được ghi là giả định; các ngưỡng chất lượng là mục tiêu POC, chưa phải kết quả đo.

## Bài toán chọn để phân tích sâu

Chọn **Quick Card #1 — VinFast AI Service Intake & Triage Copilot**. Bài toán tập trung vào đọc hiểu, tóm tắt và phân loại ngôn ngữ tự nhiên, phù hợp với LLM Feature kết hợp Rules và Human Review. Xem [Deep-Dive Report](02-deep-dive-report.md).
