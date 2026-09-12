## Team

- Team: Fournity
- Members: 
    2A202602853 Hoàng Văn Nam
    2A202602489 Nguyễn Hải Hoàng
    2A202602977 Dương Hà Đức Anh
    2A202603018 Tạ Đăng Dương

---

**Bài toán được chọn (từ `01-problem-scan.md`):** Card #1 — Vinmec: Chuẩn hóa chẩn đoán sang mã ICD-10

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Current-State Workflow

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1        │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Bác sĩ ghi    │     │ Coder đọc    │     │ Coder tra    │     │ Nhập mã vào  │
│ chẩn đoán     │ ──→ │ free-text    │ ──→ │ cứu tay bảng │ ──→ │ hệ thống BHYT│
│ (free-text)   │     │ chẩn đoán    │     │ mã ICD-10 🔴 │     │              │
│ Ai: Bác sĩ    │     │ Ai: Coder    │     │ Ai: Coder    │     │ Ai: Coder    │
│ ⏱ 1 phút      │     │ ⏱ 1 phút     │     │ ⏱ 5 phút 🔴  │     │ ⏱ 1 phút     │
│ In: Khám bệnh │     │ In: Hồ sơ    │     │ In: Tên bệnh │     │ In: Mã ICD-10│
│ Out: Hồ sơ    │     │ Out: Tên bệnh│     │ Out: Mã ICD  │     │ Out: Claim   │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ┌──────────────┐
                                                               │ Bước 5 🔄    │
                                                               │ (Handoff:    │
                                                               │ Coder→BHYT)  │
                                                               │ BHYT từ chối │
                                                               │ nếu sai mã → │
                                                               │ làm lại 🔴   │
                                                               │ ⏱ 10-15 phút │
                                                               └──────────────┘
🔴 = Bottlenecks   🔄 = Handoff (Coder ↔ Hệ thống BHYT)
⏱ Tổng thời gian xử lý thủ công: ~8 phút/hồ sơ (chưa tính làm lại khi bị từ chối).
```

## 3.2. Problem Statement (6-field)

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Nhân viên hành chính y tế (medical coder) tại phòng khám Vinmec. |
| **2. Current Workflow** | Bác sĩ ghi chẩn đoán tự do → coder đọc và tra cứu tay bảng mã ICD-10 (bản Excel của Bộ Y tế) → nhập mã vào hệ thống bảo hiểm → nếu sai mã, hồ sơ bị BHYT từ chối và phải sửa lại. 5 bước, thủ công hoàn toàn, ~8 phút/hồ sơ. |
| **3. Bottleneck** | Bước 3 (tra cứu tay): coder phải tự đối chiếu tên bệnh viết tự do, nhiều biến thể chính tả/viết tắt, với hàng nghìn mã ICD-10 — dễ chọn sai mã gần giống. |
| **4. Business Impact** | Ước tính ~200 hồ sơ/ngày/phòng khám. Tỷ lệ sai mã ~10-15% → hồ sơ bị BHYT từ chối, phải làm lại tốn thêm 10-15 phút/hồ sơ, ảnh hưởng tốc độ giải ngân bảo hiểm. |
| **5. Success Metric** | 1. Giảm thời gian chuẩn hóa từ 5 phút → dưới 30 giây/hồ sơ (Efficiency).<br>2. Độ chính xác match ICD-10 ≥ 90% (Quality). |
| **6. Operational Boundary** | AI được phép: trích xuất tên bệnh/triệu chứng từ free-text (NER) và đề xuất top-3 mã ICD-10 khớp nhất kèm confidence score. **CẤM:** AI không được tự động ghi mã cuối cùng vào hệ thống BHYT mà không có coder xác nhận (bắt buộc HITL); không đề xuất mã có confidence dưới ngưỡng an toàn (70%) mà không gắn cờ "cần review thủ công". |

## 3.3. Future-State Flow & AI Fit

**AI Fit:** **LLM Feature** (NER + fuzzy/semantic matching). Không chọn Rule-based thuần vì tên bệnh viết tự do có quá nhiều biến thể ngôn ngữ tự nhiên mà rule cứng không phủ hết được. Không cần Agentic Loop vì workflow có cấu trúc cố định, không đòi hỏi lập kế hoạch nhiều bước hay gọi nhiều công cụ động.

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ 🔵 AI trích   │     │ 🔵 AI match  │     │ 🟢 Coder     │
│ Bác sĩ ghi    │ ──→ │ xuất tên bệnh│ ──→ │ top-3 mã ICD │ ──→ │ chọn/duyệt   │
│ chẩn đoán    │     │ (NER)        │     │ + confidence │     │ mã cuối cùng │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                      │
                                                                      ▼
                                                               ↩️ Fallback:
                                                               Nếu confidence <70%,
                                                               coder tra cứu tay
                                                               như cũ (không AI).
```

---

# 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist:
- [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? — Có (dataset chẩn đoán y tế tiếng Việt + danh mục ICD-10 chính thức của Bộ Y tế).
- [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? — Có (coder luôn là người duyệt mã cuối; ngưỡng confidence 70% chặn các đề xuất không chắc chắn).
- [x] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? — Có (coder chỉ chuyển từ "tự tra cứu" sang "duyệt đề xuất", không thay đổi lớn về vai trò).

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp.

**Justification:**
> Bài toán có phạm vi hẹp, rõ ràng (chuẩn hóa 1 loại thông tin — tên bệnh sang mã ICD-10), có dữ liệu sẵn để huấn luyện/kiểm thử, và rủi ro sai sót được kiểm soát chặt qua ngưỡng confidence + bắt buộc con người duyệt trước khi ghi vào hệ thống BHYT. Metric đo lường cụ thể (thời gian, độ chính xác) giúp đánh giá hiệu quả rõ ràng sau triển khai. Giải pháp LLM Feature đơn giản, không cần Agentic Loop phức tạp, phù hợp để làm prototype nhanh và mở rộng dần.