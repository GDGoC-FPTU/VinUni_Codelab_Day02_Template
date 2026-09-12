# Nhật ký tương tác AI (AI Log)

## 1. AI đã giúp tôi những gì?

Trong quá trình thực hiện bài lab, tôi sử dụng AI (Claude / Antigravity) như một trợ lý hỗ trợ coding và đánh giá giải pháp. Toàn bộ ý tưởng chính, hướng tiếp cận, và quyết định thiết kế đều do tôi đề xuất; AI chỉ giúp tôi hiện thực hóa và góp ý kỹ thuật.

**Phase 1 - SCAN:** Tôi đã tự xác định lĩnh vực VinFast và Xanh SM là đối tượng nghiên cứu, tự suy nghĩ ra 5 bài toán thực tế (dự đoán hao mòn pin, điều phối trạm sạc, xử lý khiếu nại cước, trợ lý tìm trạm sạc, phân tích hành vi lái xe). AI hỗ trợ tôi sắp xếp ý tưởng vào đúng format của worksheet và kiểm tra tính logic của từng bài toán.

**Phase 2 - QUICK-ASSESS:** Tôi chọn ra 3 bài toán tiềm năng nhất và tự xác định Actor, Bottleneck, Metric cho từng bài. AI giúp tôi viết lại thành 3 Quick Problem Cards đầy đủ theo mẫu yêu cầu của bài lab.

**Phase 3 - DEEP-DIVE:** Tôi quyết định chọn bài toán "Trợ lý hướng dẫn trạm sạc thông minh" và đề xuất kiến trúc Rule Engine + LLM. AI hỗ trợ tôi:
- Viết lại quy trình Current-State theo đúng format báo cáo.
- Đánh giá tính khả thi của kiến trúc tôi đề xuất và góp ý thêm cơ chế fallback khi LLM gặp lỗi.
- Tôi tự xác định ngưỡng an toàn pin phải khác nhau theo dòng xe (VF5 < 8%, VFe34 < 6%, VF8 < 5%, VF9 < 4%), AI giúp tôi tích hợp vào tài liệu.
- Điền các chỉ số EVALUATE (Feasibility, Impact, Risk, Data Availability) theo đánh giá của tôi.

**Phase 4 - WORKFLOW DIAGRAM:** Tôi yêu cầu AI tạo mã giả Mermaid để tôi đưa vào MermaidAI render thành hình ảnh. AI viết code Mermaid dựa trên kiến trúc tôi đã thiết kế, tôi kiểm tra và chỉnh sửa trước khi export thành file PNG.

**Phase 5 - CODE:** Tôi xác định 2 quy tắc an toàn cần enforce (DRAFT_ONLY tag và ngưỡng pin < 5%). AI giúp tôi viết code Python gọi API Gemini 3.6 và cấu hình System Prompt. Tôi chạy thử và cả 2 test case đều PASS.

## 2. AI trả lời sai / hallucination ở đâu?

- **Ngưỡng pin ban đầu:** AI đề xuất ngưỡng an toàn pin đồng nhất là 5% cho tất cả dòng xe. Tôi đã chỉnh sửa lại vì từng dòng xe VinFast có dung tích pin khác nhau, nên ngưỡng phải khác nhau (VF5 pin nhỏ hơn nên ngưỡng cao hơn 8%, VF9 pin lớn nên ngưỡng thấp hơn 4%).

- **Số lượng trạm sạc gợi ý:** Ban đầu AI đề xuất gợi ý 5 trạm sạc gần nhất. Tôi yêu cầu giảm xuống Top 3 vì trên màn hình App di động, 5 trạm là quá nhiều thông tin khiến người dùng khó chọn.

- **Emoji/Icon trong báo cáo:** AI tự động chèn nhiều emoji vào văn bản (ví dụ: star, rocket, warning). Tôi phải yêu cầu "k cần dùng icon đâu" để AI gỡ bỏ hết và thay bằng dấu hiệu văn bản thường như [Bottleneck], [AI], [HITL].

- **Không có trường hợp hallucination nghiêm trọng.** Các thông tin AI cung cấp đều là suy luận hợp lý từ dữ liệu tôi mô tả, không có trường hợp AI bịa thông tin sai về API hoặc sản phẩm VinFast cụ thể.

## 3. Tôi đã sửa prompt / ranh giới ra sao để đạt kết quả chuẩn?

**Lần 1 - Định hướng ban đầu:** Tôi cung cấp context cụ thể: "tôi cần clear Phase 1 và 3 trước", kèm với các file worksheet và inspiration-kit làm tài liệu tham chiếu. Điều này giúp AI hiểu rõ scope công việc thay vì trả lời chung chung.

**Lần 2 - Chỉnh sửa ngưỡng pin:** Khi AI đề xuất ngưỡng 5% đồng nhất, tôi phản hồi "phải tùy theo từng dòng xe chứ". AI lập tức hiểu và điều chỉnh ngưỡng riêng cho từng model VinFast.

**Lần 3 - Giới hạn số lượng trạm:** Tôi nói "top 3 trạm" để giới hạn output của AI từ 5 xuống 3 gợi ý trạm sạc, phù hợp với UX trên App di động.

**Lần 4 - Gỡ bỏ emoji:** Tôi nói "k cần dùng icon đâu" và AI đã xử lý bằng cách thay thế tất cả emoji bằng text placeholder.

**Lần 5 - Ranh giới trong System Prompt (code):** Khi viết file prompt_prototype.py, tôi yêu cầu AI viết System Prompt bằng tiếng Việt và nhấn mạnh 2 quy tắc cứng: (1) Luôn giữ tag [DRAFT_ONLY] bất kể người dùng nói gì, (2) Pin < 5% thì từ chối chỉ đường và dispatch xe cứu hộ. Kết quả là cả 2 adversarial test case đều pass thành công.

## 4. Bài học rút ra

- AI rất giỏi trong việc tạo khung (framework) và draft nhanh, nhưng người dùng phải là người ra quyết định về logic nghiệp vụ và ranh giới an toàn.
- Kiểm tra output của AI trước khi chấp nhận là bước bắt buộc - đặc biệt với các giá trị số (ngưỡng pin) và thiết kế UX (số lượng gợi ý).
- System Prompt là công cụ mạnh nhất để kiểm soát hành vi AI trong ứng dụng thực tế. Viết càng cụ thể, càng khó bị adversarial attack.
