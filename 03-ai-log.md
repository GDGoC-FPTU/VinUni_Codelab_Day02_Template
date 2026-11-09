# AI Log & Reflection — Lab 02

**Công cụ:** Claude Code (Claude Opus 5.5), kết hợp tìm kiếm web.

**Phạm vi nhật ký:** phiên làm việc dùng để làm lại Phase 2 và hoàn thành Phase 3, Phase 5, Phase 6. Nhật ký chỉ ghi những gì đã xảy ra trong phiên này.

**Vai trò:** AI soạn phần lớn nội dung và vẽ sơ đồ. Tôi quyết định chọn bài toán, phạm vi và cách nộp bài.

## 1. AI đã giúp gì

- Đọc README, worksheet, rubric và branch của tôi để liệt kê những phần còn thiếu.
- Tìm thông tin công khai về mạng lưới trạm sạc VinFast/V-GREEN.
- Viết Card #2, lý do loại Card #4 và #5, Problem Statement 6 trường, so sánh Rule, LLM và Agent, future-state flow và phần Evaluate.
- Vẽ `04-workflow-diagram.png` bằng script, sau đó tự xem lại ảnh và chỉnh chỗ hiển thị chưa đẹp.

## 2. AI đã sai hoặc chưa đáng tin ở đâu

| # | Vấn đề | Cách phát hiện | Cách xử lý |
|---|---|---|---|
| 1 | **Làm rộng hơn yêu cầu.** AI đưa file `.py` vào danh sách việc và xem branch của thành viên khác để tìm bài toán chung của nhóm. | Tôi xem kế hoạch AI báo cáo. | Tôi yêu cầu chỉ làm phần của tôi và chỉ làm những gì có thể merge vào `main`. README không cho merge `.py`, nên Phase 4 bị loại khỏi phạm vi. |
| 2 | **Số liệu trên web mâu thuẫn.** Con số 150.000 cổng sạc lúc được mô tả là đang vận hành, lúc là quy hoạch, lúc gồm cả xe máy điện. Độ phủ cũng khác nhau (34 và 63 tỉnh thành). | Đối chiếu các kết quả tìm kiếm. | Chỉ dùng làm bối cảnh, ghi rõ là số báo chí và chưa thống nhất. |
| 3 | **Không xác nhận được thông số kỹ thuật.** Tìm kiếm không xác nhận được VF5, VF8, VF9 dùng cổng nào, nên CCS2/GBT trong danh sách SCAN vẫn chưa được kiểm chứng. | Kết quả tìm kiếm nói rõ là không có thông tin này. | Không khẳng định loại cổng theo từng dòng xe trong báo cáo; hệ thống phải lấy từ dữ liệu xe. |
| 4 | **Lập luận tự mâu thuẫn.** Bản nháp đầu loại Card #5 vì thiếu baseline, trong khi Card #2 cũng thiếu baseline. | Rà lại khi viết lý do loại thẻ. | Đổi lý do sang điểm khác biệt thật và ghi rõ #2 cũng chưa có baseline. |
| 5 | **Nguy cơ biến giả định thành sự thật.** Các mốc 12-21 phút và 1.000 lượt/ngày không có dữ liệu thật. | Không có nguồn nào cho các số này. | Đánh dấu *(giả định)* ở báo cáo và ghi ngay trên sơ đồ. |

## 3. Tôi đã chỉnh prompt và ranh giới thế nào

- "Do the #2 idea" chưa nói rõ thẻ nào bị thay. AI tạm chọn bỏ #3, sau đó tôi chốt rõ: top 3 là #2, #4, #5 và chọn #2 để Deep-Dive.
- Tôi yêu cầu có Card #2 kèm lý do loại #4 và #5, theo cấu trúc của bài mẫu.
- Tôi đặt quy tắc mỗi phase một commit và yêu cầu xóa commit cũ đã chọn #3, #4, #5.
- Tôi giới hạn phạm vi vào phần việc của riêng mình, vì mỗi thành viên làm độc lập và tôi sẽ chọn bài tốt nhất để merge.

## 4. Bài học

- AI làm nhanh hơn khi phạm vi rõ. Khi yêu cầu rộng như "finish everything", AI dễ tự mở rộng, nên cần chốt ranh giới sớm.
- Báo cáo trôi chảy không có nghĩa là số liệu đúng. Mỗi con số cần có nguồn hoặc được ghi rõ là giả định.
- Với bài toán này, phần tạo ra giá trị chủ yếu là rule và chất lượng dữ liệu. Vì vậy quyết định trung thực là **NOT YET**, dù AI có thể viết một bản đề xuất GO rất thuyết phục.

## 5. Giới hạn

- Chưa có dữ liệu nội bộ VinFast, chưa phỏng vấn tài xế hay tổng đài.
- Bản phân tích này chưa được kiểm chứng bằng prototype: Phase 4 (`.py`) không nằm trong phần việc của phiên này.
