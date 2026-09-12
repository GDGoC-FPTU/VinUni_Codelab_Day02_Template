# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | VinFast | **After-sales / Warranty**  | Tự động phân loại và phân tích Warranty Claim từ mô tả lỗi, hình ảnh và lịch sử sửa chữa, giảm thời gian xử lý và phát hiện claim bất thường. 
| 2 | VinFast | **Manufacturing / Quality** | Dùng Computer Vision phát hiện và phân loại lỗi ngoại quan trên xe trong quá trình sản xuất, giảm phụ thuộc vào kiểm tra thủ công. |
| 3 | VinFast | **Vehicle Quality / RCA** | Phân tích hàng loạt DTC, repair order và warranty claim để phát hiện pattern lỗi lặp lại và hỗ trợ kỹ sư tìm Root Cause. |
| 4 | VinFast | **Supply Chain / Parts** | Dự báo nhu cầu phụ tùng theo model, khu vực và pattern lỗi để tối ưu tồn kho, hạn chế thiếu hoặc dư phụ tùng. |
| 5 | VinFast | **After-sales / Service** | Tự động chuyển đổi hội thoại/mô tả của khách hàng thành structured service request, xác định triệu chứng và đề xuất checklist xử lý cho Service Advisor. |
---

# 🃏 Phase 2 — QUICK-ASSESS

```QUICK PROBLEM CARD #1 — Warranty Claim Intelligence
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│ Bài toán: Nhân viên Warranty phải kiểm tra thủ công thông   │
│ tin, mô tả lỗi và hồ sơ để xác định tính hợp lệ của claim. │
│ Công ty thành viên: [x] VinFast                            │
│ Ai đang đau? Warranty Specialist / Service Advisor         │
│ Workflow thủ công hiện tại (5 bước):                      │
│ 1. Nhận Warranty Claim                                     │
│ → 2. Đọc mô tả lỗi + kiểm tra hình ảnh                     │
│ → 3. Tra cứu lịch sử sửa chữa / thông tin xe                │
│ → 4. Đối chiếu chính sách Warranty                          │
│ → 5. Approve / Reject / Escalate claim                      │
│ Bước nào tốn nhất? Bước 2-4 (⏱ cần đo baseline thực tế)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4             │
│ (Extract thông tin → Tổng hợp hồ sơ → Đề xuất xử lý)       │
│ Đo thành công bằng gì (Metric có số)?                      │
│ Giảm thời gian xử lý trung bình/claim; tăng % claim được   │
│ xử lý tự động mà không làm tăng False Positive/Negative.   │
│ Quick Architecture: [x] LLM + Rule + Human-in-the-loop     │
└─────────────────────────────────────────────────────────────┘
```
```Card #2 — VinFast Failure / RCA Intelligence
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│ Bài toán: Kỹ sư phải tổng hợp nhiều nguồn dữ liệu để phát  │
│ hiện pattern lỗi lặp lại và điều tra nguyên nhân gốc.      │
│ Công ty thành viên: [x] VinFast                            │
│ Ai đang đau? Quality Engineer / Reliability Engineer        │
│ Workflow thủ công hiện tại (5 bước):                      │
│ 1. Thu thập DTC, Repair Order, Warranty Claim               │
│ → 2. Filter dữ liệu theo model / component / thời gian      │
│ → 3. Tìm pattern lỗi lặp lại                                │
│ → 4. Đối chiếu các case và tài liệu kỹ thuật                │
│ → 5. Đề xuất và xác nhận Root Cause                         │
│ Bước nào tốn nhất? Bước 2-4 (⏱ cần đo baseline thực tế)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-4             │
│ (Tìm pattern → Tổng hợp evidence → Đề xuất RCA hypothesis) │
│ Đo thành công bằng gì (Metric có số)?                      │
│ Giảm thời gian điều tra RCA; giảm Time-to-Detect recurring │
│ issue; tăng % AI hypothesis được kỹ sư xác nhận.            │
│ Quick Architecture: [x] LLM + Analytics + Human-in-the-loop │
└─────────────────────────────────────────────────────────────┘
```
```Card #3 — VinFast Visual Quality Inspection
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                       │
│ Bài toán: Nhân viên QC phải kiểm tra thủ công ngoại quan    │
│ xe để phát hiện và phân loại các lỗi chất lượng.            │
│ Công ty thành viên: [x] VinFast                            │
│ Ai đang đau? QC Inspector / Production Quality Engineer     │
│ Workflow thủ công hiện tại (5 bước):                      │
│ 1. Xe vào khu vực Inspection                                │
│ → 2. Inspector quan sát từng khu vực                        │
│ → 3. Đối chiếu tiêu chuẩn chất lượng                        │
│ → 4. Ghi nhận và phân loại defect                           │
│ → 5. Chuyển xe sang Rework nếu phát hiện lỗi                │
│ Bước nào tốn nhất? Bước 2-4 (⏱ cần đo baseline thực tế)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3             │
│ (Phát hiện defect → Phân loại → Human review case nghi ngờ)│
│ Đo thành công bằng gì (Metric có số)?                      │
│ Giảm thời gian inspection/xe; tăng Defect Detection Recall;│
│ giảm Defect Escape Rate và False Rejection Rate.            │
│ Quick Architecture: [x] Computer Vision + Human-in-the-loop │
└─────────────────────────────────────────────────────────────┘
```
