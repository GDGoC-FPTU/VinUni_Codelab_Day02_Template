# 🏁 Phase 5 — EVALUATE

## AI Readiness Checklist

1. [ ] **Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test?**

   Hiện nhóm chưa có dataset maintenance ticket thực tế của Vinhomes đã được
   anonymize và gán ground truth cho category, severity, routing team và kết quả xử lý.
   Các tình huống trong prototype hiện chủ yếu là synthetic test cases.

2. [x] **Rủi ro khi AI sai có nằm trong tầm kiểm soát qua HITL hoặc Fallback?**

   Có. Prototype áp dụng Human-in-the-loop bắt buộc cho các trường hợp
   safety-critical như điện, cháy, thang máy, kết cấu hoặc khi model không chắc chắn.

   Phase 4 đã stress-test 3 tình huống:
   - Dangerous electrical DIY request
   - Critical-ticket severity downgrade
   - Prompt injection + fake root cause

   Kết quả: **3/3 adversarial tests passed**.

3. [ ] **Stakeholders sẵn sàng thay đổi quy trình làm việc cũ?**

   Chưa có dữ liệu xác nhận từ đội CSKH, Ban Quản lý và đội kỹ thuật Vinhomes.
   Cần pilot thực tế với phạm vi nhỏ và thu thập feedback trước khi thay đổi workflow.

---

## Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future

[ ] **GO — Bắt đầu xây dựng Production**

[x] **NOT YET — Cần tích lũy thêm dữ liệu/xác lập baseline**

[ ] **NO-GO — Rule-based tốt hơn / Không khả thi**

---

## Justification

Bài toán **Vinhomes Multimodal Maintenance Triage** có AI-fit cao vì đầu vào
bao gồm text, ảnh/video và mô tả tự do của cư dân. Đây là dạng dữ liệu
không cấu trúc mà rule-based system đơn thuần khó xử lý linh hoạt.

Prototype ở Phase 4 chứng minh rằng LLM có thể tuân thủ các operational
boundaries quan trọng. Hệ thống đã vượt qua **3/3 adversarial tests**,
bao gồm yêu cầu hướng dẫn sửa điện nguy hiểm, cố tình hạ mức severity
và prompt injection nhằm bypass Human Review.

Tuy nhiên, kết quả trên mới chứng minh **prompt-level safety**, chưa chứng minh
hiệu quả vận hành thực tế. Nhóm hiện chưa có dataset ticket thật, baseline của
quy trình hiện tại hoặc ground truth đủ để đánh giá accuracy và routing quality.

Vì vậy, quyết định phù hợp hiện tại là **NOT YET**.

### Điều kiện để chuyển sang GO

- Thu thập và anonymize maintenance tickets thực tế.
- Xây dựng taxonomy chuẩn cho category và severity.
- Có ground truth từ nhân viên vận hành/kỹ thuật.
- Đo baseline của manual triage workflow.
- Benchmark model trên tập dữ liệu offline.
- Category accuracy ≥ 90%.
- Routing accuracy ≥ 85%.
- Critical-case recall ≥ 95%.
- 100% critical cases đi qua Human Review.
- Pilot thành công trên một phạm vi nhỏ trước khi scale.

Nếu đạt các điều kiện trên, dự án có thể chuyển từ **NOT YET → GO cho controlled pilot**.