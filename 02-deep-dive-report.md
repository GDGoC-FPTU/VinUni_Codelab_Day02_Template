# 🏗️ Phase 3 — DEEP-DIVE (Nhóm, 85 min)

## 3.1. Current-State Workflow Mapping (25 min)
```
                 CURRENT-STATE WORKFLOW
        Tóm tắt hồ sơ bệnh án trước khi khám
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 1. Bệnh nhân đặt lịch / đến khám                          │
│    ⏱ ~2 phút                                              │
└────────────────────────┬───────────────────────────────────┘
                         │
                         🔄 HANDOFF
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 2. Nhân viên mở hồ sơ bệnh nhân trên hệ thống             │
│    ⏱ ~1 phút                                              │
└────────────────────────┬───────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 🔴 3. Đọc lịch sử khám và bệnh án cũ                      │
│    - Các lần khám trước                                   │
│    - Chẩn đoán                                             │
│    - Tiền sử bệnh                                          │
│    ⏱ ~3–7 phút                                            │
└────────────────────────┬───────────────────────────────────┘
                         │
                         🔄 HANDOFF
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 🔴 4. Kiểm tra kết quả xét nghiệm / chẩn đoán hình ảnh    │
│    - Xét nghiệm máu                                        │
│    - X-quang / CT / MRI...                                │
│    - So sánh kết quả cũ và mới                             │
│    ⏱ ~2–5 phút                                            │
└────────────────────────┬───────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 🔴 5. Kiểm tra thuốc đang sử dụng                         │
│    - Thuốc hiện tại                                        │
│    - Liều lượng                                             │
│    - Thay đổi thuốc                                        │
│    ⏱ ~1–3 phút                                            │
└────────────────────────┬───────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 6. Bác sĩ tự tổng hợp thông tin quan trọng                │
│    → Xác định vấn đề chính                                │
│    → Ghi nhớ các điểm cần hỏi                              │
│    ⏱ ~2–5 phút                                            │
└────────────────────────┬───────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 7. Bắt đầu khám bệnh                                      │
│    ⏱ ~1 phút chuẩn bị                                     │
└──────────────────────────────────────────────────────────┘


⏱ TỔNG CỘNG: ~12–25 PHÚT/BỆNH NHÂN
```

## 3.2. Problem Statement (6-field) & Metrics (15 min)
| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | **Bác sĩ khám bệnh** là người sử dụng chính. Điều dưỡng/nhân viên y tế có thể hỗ trợ chuẩn bị và kiểm tra hồ sơ trước khi bệnh nhân vào khám. |
| **2. Current Workflow** | Bác sĩ/nhân viên y tế mở hồ sơ bệnh án điện tử → đọc lịch sử khám → xem xét nghiệm & chẩn đoán hình ảnh → kiểm tra chẩn đoán và thuốc → tự tổng hợp thông tin quan trọng → bắt đầu khám. Công cụ: EMR/HIS và các hệ thống xét nghiệm, CĐHA. |
| **3. Bottleneck** | 🔴 Đọc và tổng hợp lượng lớn thông tin y tế từ nhiều lần khám. Đặc biệt tốn thời gian với bệnh nhân có nhiều lịch sử khám, xét nghiệm, chẩn đoán và thuốc. |
| **4. Business Impact** | **Ước tính workshop:** ~12–25 phút/lượt cho toàn bộ quá trình chuẩn bị, trong đó ~5–15 phút dành cho đọc và tổng hợp. Có thể làm tăng thời gian chờ, giảm thời gian tương tác trực tiếp với bệnh nhân và tạo áp lực lên năng lực phục vụ. *Cần time-study thực tế để xác nhận.* |
| **5. Success Metric** | 🎯 ≥80% hồ sơ được tạo clinical summary trong ≤30 giây; giảm ≥50% thời gian chuẩn bị hồ sơ; ≥95% thông tin quan trọng trong summary được bác sĩ đánh giá chính xác/đầy đủ. |
| **6. Operational Boundary** | ✅ AI được phép đọc dữ liệu được cấp quyền, trích xuất, tóm tắt lịch sử khám/xét nghiệm/chẩn đoán/thuốc và tạo clinical summary. ❌ Không được tự chẩn đoán, kê thuốc, thay đổi phác đồ, đưa ra quyết định y khoa cuối cùng hoặc tự sửa hồ sơ. **Bác sĩ phải review và xác nhận trước khi sử dụng.** |

## 3.3. Future-State Flow & AI Fit (25 min)
* **Xác định mức AI Fit (AI-Fit Matrix):** Giải pháp thuộc nhóm nào? [✅] LLM Feature.
* **Vẽ Future-State Flow:** 
  
┌──────────────────────────────────────────────────────────┐
│ 1. Bệnh nhân đến khám                                    │
│    ⏱ ~2 phút                                             │
└────────────────────────┬─────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 2. Hệ thống lấy hồ sơ bệnh án                            │
│    Lịch sử khám + Xét nghiệm + CĐHA + Thuốc              │
│    ⏱ ~10–30 giây                                         │
└────────────────────────┬─────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 🔵 3. AI đọc & trích xuất thông tin                      │
│    LLM phân tích dữ liệu hồ sơ                           │
│    ⏱ ~10–20 giây                                         │
└────────────────────────┬─────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────┐
│ 🔵 4. AI tạo Clinical Summary                            │
│    • Tiền sử quan trọng                                  │
│    • Chẩn đoán trước đây                                 │
│    • Kết quả xét nghiệm / CĐHA                           │
│    • Thuốc đang sử dụng                                 │
│    • Các điểm cần lưu ý                                  │
│    ⏱ ~10–20 giây                                         │
└────────────────────────┬─────────────────────────────────┘
                         │
                         ▼
                 ┌───────────────────┐
                 │ AI đủ tin cậy?    │
                 └─────────┬─────────┘
                           │
              ┌────────────┴────────────┐
              │                         │
             CÓ                      KHÔNG
              │                         │
              ▼                         ▼
┌───────────────────────────┐   ┌───────────────────────────┐
│ 🟢 5. Bác sĩ REVIEW       │   │ ↩️ FALLBACK               │
│    Clinical Summary       │   │    Không sử dụng output  │
│    ⏱ ~1–2 phút            │   │    AI                     │
└─────────────┬─────────────┘   │    → Xem hồ sơ gốc        │
              │                 │    → Xử lý thủ công       │
              │                 └─────────────┬─────────────┘
              │                               │
              ▼                               │
┌───────────────────────────┐                 │
│ 🟢 6. Bác sĩ xác nhận /   │◄────────────────┘
│    chỉnh sửa summary      │
│    ⏱ ~30 giây–1 phút      │
└─────────────┬─────────────┘
              │
              ▼
┌──────────────────────────────────────────────────────────┐
│ 7. Bắt đầu khám bệnh                                     │
│    🩺 Bác sĩ đưa ra quyết định y khoa                    │
│    ⏱ ~1 phút chuẩn bị                                    │
└──────────────────────────────────────────────────────────┘
