## Team

- Team: Fournity
- Members: 
    2A202602853 Hoàng Văn Nam
    2A202602489 Nguyễn Hải Hoàng
    2A202602977 Dương Hà Đức Anh
    2A202603018 Tạ Đăng Dương

---

## 1. AI đã giúp gì?
- Cấu trúc hóa quy trình theo đúng format Problem Statement 6-field / Quick
  Problem Card, giúp tiết kiệm thời gian trình bày
- Gợi ý các lens/pattern để brainstorm bài toán (ví dụ: liên hệ trực tiếp giữa
  bài toán ICD-10 normalization với kiến thức NLP y tế mình đang làm ở khóa luận)
- Viết sẵn adversarial test case mẫu cho Phase 4 để mình có điểm khởi đầu
- Sinh code Python (matplotlib) để vẽ nhanh sơ đồ workflow thay vì phải vẽ tay,
  tiết kiệm đáng kể thời gian cho Phase 3.1

## 2. AI sai/hallucination ở đâu?
- **Số liệu bịa (chưa kiểm chứng):** Khi soạn phần "Business Impact" (mục 4 của
  Problem Statement), AI đưa ra các con số như "~200 hồ sơ/ngày", "tỷ lệ sai mã
  ~10-15%" mà không có nguồn thật — đây là số liệu AI tự ước lượng cho có vẻ
  thuyết phục (giống dạng hallucination số liệu), không phải dữ liệu thực tế từ
  Vinmec. → Mình đã phải tự thay bằng số liệu khảo sát/nguồn thật của nhóm, hoặc
  ghi chú rõ đây là giả định cần kiểm chứng trước khi nộp.
- **Sơ đồ PNG bị lỗi hiển thị:** Lần render đầu tiên của `04-workflow-diagram.png`,
  dòng chữ "Time: 10-15 phút" ở Bước 5 bị cắt mất vì canvas (ylim) đặt quá sát
  mép dưới. Mình phải yêu cầu AI chỉnh lại kích thước canvas và render lại mới
  ra bản đầy đủ — cho thấy output kỹ thuật của AI cần luôn được xem/kiểm tra lại
  bằng mắt, không thể tin tưởng "chạy code xong là xong".
- **Thiếu nhất quán giữa các file:** File `prompt_prototype.py` AI viết ban đầu
  theo đúng template gốc (bài toán Xanh SM sạc pin), trong khi `02-deep-dive-report.md`
  của nhóm lại đang theo bài toán Vinmec ICD-10. AI không tự phát hiện hay cảnh
  báo sự lệch pha này — mình phải tự nhận ra và quyết định sẽ đồng bộ lại bài
  toán giữa các file trước khi nộp.

## 3. Mình đã sửa prompt/ranh giới ra sao?
- Yêu cầu AI gắn nhãn rõ ràng số liệu nào là ước lượng, số liệu nào cần nhóm tự
  điền từ khảo sát thật, thay vì để lẫn vào báo cáo như số liệu chính thức
- Khi phát hiện sơ đồ bị cắt chữ, mình không tự sửa tay mà yêu cầu AI chỉnh lại
  kích thước canvas và chạy lại script, sau đó tự kiểm tra ảnh xuất ra trước khi
  chấp nhận kết quả
- Yêu cầu AI thêm test case tấn công thứ 3 (giả mạo "SYSTEM OVERRIDE" để đổi
  ngưỡng pin an toàn) ngoài 2 test case có sẵn trong starter code, để đáp ứng
  đúng yêu cầu tối thiểu 3 prompt tấn công của worksheet gốc
- Ghi chú lại rõ ràng rằng `prompt_prototype.py` hiện đang theo bài toán mẫu
  (Xanh SM), cần yêu cầu AI viết lại SYSTEM_PROMPT và test case cho đúng bài
  toán Vinmec nếu nhóm chốt hướng đó, để tránh nộp nhầm hai file không khớp nhau

## 4. Bài học rút ra
- AI là công cụ tăng tốc cấu trúc và brainstorm, nhưng số liệu định lượng/nghiệp
  vụ đặc thù (business impact, tỷ lệ lỗi thật) bắt buộc phải do nhóm khảo sát và
  xác nhận, không thể nhận nguyên từ AI
- Output kỹ thuật (hình ảnh, code) cần được tự kiểm tra trực tiếp (xem ảnh, chạy
  thử code với API key thật) chứ không chỉ tin vào việc "không báo lỗi khi biên dịch"
- Khi làm việc với AI qua nhiều lượt/nhiều file riêng lẻ, người dùng phải là
  người chịu trách nhiệm giữ tính nhất quán giữa các deliverable, vì AI không tự
  động đối chiếu ngữ cảnh giữa các file nếu không được nhắc lại rõ ràng