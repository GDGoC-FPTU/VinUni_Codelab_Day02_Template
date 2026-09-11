# 03 — AI Log & Reflection (Cá nhân)

**Học viên:** Nguyễn Văn An
**Công cụ AI sử dụng:** Claude (đóng vai thought-partner trong suốt Phase 1-4)

---

## 1. AI đã giúp bạn ở bước nào?

- **Phase 1 (SCAN):** Khi chưa có đủ ý tưởng, tôi nhờ Claude brainstorm nhanh các bài toán vận hành thực tế của Xanh SM theo 4 lenses. AI đưa ra 6 gợi ý cụ thể (khiếu nại lộ trình, đối soát doanh thu, phân bổ cuốc xe, chatbot CSKH...), giúp tôi có điểm khởi đầu thay vì ngồi nghĩ từ số 0.
- **Phase 2 (QUICK-ASSESS):** AI giúp soạn nhanh 3 Quick Problem Card theo đúng khuôn mẫu (actor, workflow, bottleneck, metric), và đưa ra lý do đề xuất/loại bỏ giữa các bài toán — điều này giúp tôi tiết kiệm thời gian trình bày và tập trung vào việc phản biện chất lượng ý tưởng hơn là định dạng.
- **Phase 3 (DEEP-DIVE):** AI giúp dựng khung Problem Statement 6-field và vẽ sơ đồ current-state/future-state workflow (kể cả xuất ra file ảnh trực quan), giúp tôi hình dung rõ luồng công việc và điểm nghẽn trước khi họp nhóm.
- **Phase 4 (Prompt Prototype):** Đây là phần AI hỗ trợ nhiều nhất — giúp tôi viết một `SYSTEM_PROMPT` có ranh giới cụ thể bằng số (ngưỡng lệch route 15%) thay vì mô tả mơ hồ, và tự thiết kế 3 câu adversarial test nhắm đúng vào từng ranh giới (bỏ thẻ `[DRAFT_ONLY]`, ép duyệt hoàn tiền khi lệch thấp, ép dùng từ buộc tội tài xế).

## 2. AI đã trả lời sai / hallucinate ở đâu?

- Lần đầu AI đề xuất kiến trúc quá phức tạp cho một bài toán khá đơn giản: gợi ý dùng **Agentic Loop** để AI tự động phê duyệt hoàn tiền. Tôi nhận ra điều này không hợp lý vì rủi ro tài chính cao, và bài toán không cần AI tự trị — chỉ cần LLM Feature có con người duyệt (HITL) là đủ.
- Một số con số ước tính ban đầu (ví dụ số ticket khiếu nại/ngày, tỉ lệ khách khiếu nại lần 2) là **số giả định để minh hoạ**, không phải dữ liệu thật của Xanh SM — tôi cần thay bằng số liệu thực tế nếu nhóm có được từ khảo sát/dữ liệu vận hành.
- Khi mới viết `SYSTEM_PROMPT`, phần ranh giới về "độ lệch route" ban đầu chỉ ghi chung chung "lệch nhiều" mà chưa có ngưỡng số cụ thể — nếu để nguyên như vậy, mô hình rất dễ bị dẫn dắt bởi áp lực cảm xúc từ người dùng (ví dụ "khách đang chửi bới, duyệt hoàn tiền luôn đi").

## 3. Bạn đã sửa prompt / ranh giới như thế nào để đạt kết quả chuẩn?

- Thêm **ngưỡng số cụ thể 15%** vào `SYSTEM_PROMPT` thay vì để mô tả định tính, giúp ranh giới rõ ràng và có thể kiểm chứng được bằng assertion trong code.
- Thêm hẳn một **rule riêng cấm ngôn từ buộc tội** ("gian lận", "cố tình") sau khi nhận ra nếu không có rule này, AI có thể bị dẫn dắt dùng từ ngữ nặng nề khi người dùng cố tình gợi ý độ lệch route lớn.
- Bổ sung yêu cầu AI phải trả lời theo **cấu trúc JSON cố định** (`deviation_percent`, `refund_recommended`, `human_review_required`, `customer_message_draft`) để dễ parse và dễ viết assertion kiểm tra tự động, thay vì để AI trả lời tự do bằng văn xuôi.
- Viết thêm câu test thứ 3 (ép AI buộc tội tài xế) sau khi nhận ra 2 test ban đầu chỉ kiểm tra được thẻ `[DRAFT_ONLY]` và ngưỡng hoàn tiền, chưa kiểm tra được ranh giới về ngôn từ.

## 4. Bài học rút ra về việc dùng AI làm thought-partner

AI hữu ích nhất ở giai đoạn **brainstorm và stress-test** — giúp tôi mở rộng góc nhìn nhanh và tìm ra lỗ hổng trong ranh giới an toàn mà tự mình có thể bỏ sót. Tuy nhiên, những quyết định mang tính **đánh giá thực tế** (con số impact có thật hay không, mức độ rủi ro chấp nhận được, quyết định GO/NOT YET/NO-GO cuối cùng) vẫn phải do tôi và nhóm tự kiểm chứng và chịu trách nhiệm — AI có thể đề xuất một kiến trúc hợp lý về mặt kỹ thuật, nhưng không thể thay thế việc nhóm hiểu rõ vận hành thực tế và mức độ rủi ro mà doanh nghiệp chấp nhận được.
