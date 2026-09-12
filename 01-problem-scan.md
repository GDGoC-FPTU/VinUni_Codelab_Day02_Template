## Team

- Team: Fournity
- Members: 
    2A202602853 Hoàng Văn Nam
    2A202602489 Nguyễn Hải Hoàng
    2A202602977 Dương Hà Đức Anh
    2A202603018 Tạ Đăng Dương

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|----------------------|
| 1 | **Vinmec** | AI-upgrade | Nhân viên hành chính y tế (coder) mất nhiều thời gian tra cứu tay để chuẩn hóa tên bệnh/chẩn đoán tự do của bác sĩ sang mã ICD-10 khi làm báo cáo BHYT. |
| 2 | **Vinmec** | Time-consuming | Bác sĩ nội trú mất 20-30 phút/bệnh nhân để viết tay tóm tắt hồ sơ xuất viện (chẩn đoán, điều trị, thuốc, dặn dò). |
| 3 | **VinFast** | Repetitive | Nhân viên trung tâm bảo hành phải đọc và phân loại thủ công mô tả lỗi tự do của khách hàng (qua hotline/app) theo danh mục kỹ thuật trước khi chuyển kỹ thuật viên. |
| 4 | **Xanh SM** | Stakeholder Pain | Tài xế phàn nàn hệ thống gợi ý điểm đón khách không chính xác, gây mất thời gian di chuyển thừa và giảm số cuốc/giờ. |
| 5 | **Vinhomes** | Time-consuming | Nhân viên tổng đài soạn tay từng phản hồi cho khiếu nại của cư dân trên App Vinhomes Resident, phản hồi rập khuôn và chậm. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

## Card #1 — Vinmec: Chuẩn hóa chẩn đoán sang mã ICD-10

```
QUICK PROBLEM CARD #1
Bài toán: Chuẩn hóa tên bệnh/thuốc trong hồ sơ khám để khớp mã ICD-10 cho báo cáo BHYT
Công ty thành viên: [x] Vinmec

Ai đang đau (Actor)? Nhân viên hành chính y tế (medical coder) tại các phòng khám Vinmec

Workflow thủ công hiện tại:
1. Bác sĩ ghi chẩn đoán tự do (free-text)
→ 2. Coder đọc và tra cứu tay bảng mã ICD-10
→ 3. Nhập mã vào hệ thống bảo hiểm
→ 4. Nếu sai mã, hồ sơ bị BHYT từ chối, phải sửa lại

Bước nào tốn thời gian/lỗi nhất? Bước 2 (tra cứu tay) — ⏱ 5-7 phút/hồ sơ, tỷ lệ sai mã ~10-15%
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 — NER trích xuất tên bệnh từ free-text rồi match với danh mục ICD-10 chính thức

Đo thành công bằng gì (Metric có số)?
Giảm thời gian chuẩn hóa từ 5-7 phút ──> dưới 30 giây/hồ sơ; độ chính xác match ICD-10 ≥ 90%

Quick Architecture: [x] LLM Feature (NER + normalization, có fallback rule-based fuzzy match)
```

## Card #2 — Vinmec: Tóm tắt hồ sơ xuất viện

```
QUICK PROBLEM CARD #2
Bài toán: Bác sĩ mất nhiều thời gian viết tay tóm tắt hồ sơ xuất viện cho bệnh nhân
Công ty thành viên: [x] Vinmec

Ai đang đau (Actor)? Bác sĩ nội trú

Workflow thủ công hiện tại:
1. Khám và theo dõi bệnh nhân trong ngày (ghi chú lâm sàng rải rác)
→ 2. Bác sĩ tự tổng hợp và viết tóm tắt (chẩn đoán, điều trị, thuốc, dặn dò)
→ 3. Nhập vào hệ thống HIS
→ 4. In cho bệnh nhân khi xuất viện

Bước nào tốn thời gian/lỗi nhất? Bước 2 — ⏱ 20-30 phút/bệnh nhân, dễ quên chi tiết khi quá tải
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 — LLM soạn draft tóm tắt từ ghi chú lâm sàng trong ngày, bác sĩ chỉnh sửa và duyệt

Đo thành công bằng gì (Metric có số)?
Giảm thời gian soạn tóm tắt từ 25 phút ──> dưới 5 phút; thông tin thuốc/liều lượng phải đúng 100% (bắt buộc bác sĩ duyệt trước khi in)

Quick Architecture: [x] LLM Feature (bắt buộc HITL do rủi ro y tế)
```

## Card #3 — VinFast: Phân loại lỗi bảo hành

```
QUICK PROBLEM CARD #3
Bài toán: Phân loại thủ công mô tả lỗi tự do của khách hàng để chuyển đúng bộ phận kỹ thuật
Công ty thành viên: [x] VinFast

Ai đang đau (Actor)? Nhân viên trung tâm bảo hành

Workflow thủ công hiện tại:
1. Khách mô tả lỗi tự do qua hotline/app
→ 2. Nhân viên đọc và phân loại lỗi theo danh mục kỹ thuật
→ 3. Tạo phiếu yêu cầu bảo hành
→ 4. Gửi kỹ thuật viên phù hợp xử lý

Bước nào tốn thời gian/lỗi nhất? Bước 2 — ⏱ ~5 phút/lượt, dễ phân loại sai → gửi nhầm bộ phận kỹ thuật, phải chuyển lại
AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 — LLM classify + extract loại lỗi/bộ phận liên quan từ mô tả tự do của khách

Đo thành công bằng gì (Metric có số)?
Giảm thời gian phân loại từ 5 phút ──> dưới 30 giây/lượt; độ chính xác phân loại đúng bộ phận ≥ 85%

Quick Architecture: [x] LLM Feature (classification, có ngưỡng confidence để flag review thủ công)
```