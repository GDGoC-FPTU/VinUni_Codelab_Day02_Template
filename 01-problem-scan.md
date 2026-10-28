# Lab 02 — Problem Scan & Quick Problem Cards

## 1. Thông tin người thực hiện

| Trường | Nội dung |
|---|---|


## 2. Bối cảnh và hướng tìm kiếm

**Công ty/mảng quan tâm:** [VinFast / Xanh SM / Vinhomes / Vinmec / Vinpearl / VinUni / Khác]

**Mục tiêu quét bài toán:** [Điền một hoặc hai câu mô tả loại quy trình bạn muốn tìm cơ hội cải thiện]

## 3. Phase 1 — SCAN: Danh sách cơ hội

> Liệt kê **ít nhất 5 bài toán/bottleneck thực tế**. Mỗi bài toán nên gắn với một lens cụ thể và mô tả được quy trình đang gây lãng phí.

| # | Công ty thành viên | Lens | Quy trình/bài toán | Ai bị ảnh hưởng? | Bằng chứng hoặc ước tính ban đầu |
|---:|---|---|---|---|---|
| 1 | VinFast | Time-consuming | Phân loại yêu cầu đặt lịch bảo dưỡng/sửa chữa từ mô tả tiếng Việt của khách hàng và chọn xưởng hoặc dịch vụ lưu động phù hợp. | Khách hàng, nhân viên CSKH, cố vấn dịch vụ | Ứng dụng VinFast yêu cầu chọn loại dịch vụ, mô tả vấn đề, địa điểm và thời gian; giả thuyết cần xác minh: nhân viên mất 10–20 phút/yêu cầu để kiểm tra và xác nhận thủ công. [Nguồn VinFast](https://vinfastauto.com/vn_vi/cau-hoi-thuong-gap/cau-hoi-xe-o-to/chinh-sach-hau-mai) |
| 2 | VinFast | Stakeholder Pain | Tiếp nhận và điều phối cứu hộ khi xe hết pin hoặc gặp sự cố giữa đường: xác minh vị trí, loại xe, khả năng tiếp cận và điểm kéo xe phù hợp. | Chủ xe, tổng đài viên, đội cứu hộ | VinFast có quy trình cứu hộ RSA cho trường hợp xe hết pin; giả thuyết cần xác minh: mất 10–30 phút/lượt để thu thập thông tin và điều phối thủ công. [Nguồn VinFast](https://vinfastauto.com/vn_vi/thong-bao-ve-viec-dieu-chinh-phuong-thuc-cuu-ho-cho-cac-truong-hop-xe-het-pin-tu-ngay-06062025) |
| 3 | Vinhomes | Repetitive | Phản ánh cư dân về điện, nước, thang máy, an ninh và tiếng ồn phải được nhân viên đọc rồi chuyển đến đúng tòa nhà/bộ phận. | Cư dân, CSKH, ban quản lý và đội kỹ thuật | Giả định cần xác minh: 3–5 phút/ticket; ticket chuyển sai làm tăng một vòng handoff và kéo dài SLA. | Bộ phân loại kết hợp rule theo tòa/căn hộ với LLM nhận diện chủ đề, mức khẩn cấp và tóm tắt; tự route ticket có độ tin cậy cao, còn ticket nhạy cảm hoặc mơ hồ chuyển người duyệt. |
| 4 | Vinmec | Time-consuming | Phân loại yêu cầu đặt khám và gợi ý chuyên khoa/bác sĩ/lịch phù hợp trước khi chuyển nhân viên Contact Center xác nhận. | Bệnh nhân, nhân viên Contact Center, lễ tân | Form đặt lịch yêu cầu chọn cơ sở, chuyên khoa, bác sĩ, ngày khám và lý do khám; yêu cầu vẫn cần Contact Center xác nhận. [Nguồn Vinmec](https://www.vinmec.com/eng/booking/) |
| 5 | Vinmec | Repetitive | Kiểm tra và chuẩn hóa hồ sơ tiếp nhận bệnh nhân, giấy tờ tùy thân, bảo hiểm, phiếu đồng ý dịch vụ và chứng từ thanh toán để giảm nhập liệu lặp lại. | Bệnh nhân, lễ tân, thu ngân, nhân viên bảo hiểm | Quy trình công khai gồm nhiều bước kiểm tra hồ sơ, định danh, ký phiếu xét nghiệm/điều trị và thanh toán; giả thuyết cần xác minh: 10–20 phút/ca cho phần giấy tờ và nhập liệu. [Nguồn Vinmec](https://www.vinmec.com/vie/bai-viet/quy-trinh-kham-chua-benh-tai-vinmec-vi) |

### Ghi chú về 4 lenses

- **Repetitive:** Tác vụ lặp đi lặp lại nhiều lần mỗi ngày.
- **Time-consuming:** Nhân viên mất nhiều thời gian xử lý thủ công.
- **AI-upgrade:** Dịch vụ hiện tại chậm, rập khuôn hoặc có thể cá nhân hóa tốt hơn.
- **Stakeholder Pain:** Khách hàng, nhân viên hoặc đối tác đang gặp khó chịu/bottleneck rõ ràng.

## 4. Phase 2 — QUICK-ASSESS

### Quick Problem Card #1

**Tên bài toán:** Phân loại yêu cầu đặt lịch bảo dưỡng/sửa chữa

**Bài toán trong một câu:** Khách hàng mô tả lỗi xe bằng tiếng Việt, nhưng nhân viên phải đọc, hỏi lại và phân loại thủ công để chọn đúng dịch vụ, xưởng hoặc lịch hẹn.

**Công ty thành viên:** VinFast

**Lens:** Time-consuming

**Ai đang đau (Actor/Stakeholder):** Khách hàng, nhân viên Contact Center, cố vấn dịch vụ.

**Workflow thủ công hiện tại:**

1. Khách hàng gửi yêu cầu qua ứng dụng hoặc gọi tổng đài.
2. Nhân viên đọc mô tả lỗi và hỏi thêm thông tin.
3. Nhân viên phân loại loại dịch vụ cần thực hiện.
4. Nhân viên kiểm tra xưởng/dịch vụ lưu động và thời gian phù hợp.
5. Nhân viên xác nhận lịch với khách hàng.

**Bước tốn thời gian hoặc dễ lỗi nhất:** Bước 2–4 — khoảng 10–20 phút/yêu cầu, là ước tính cần kiểm chứng.

**AI có thể hỗ trợ ở bước:** Bước 2–3: trích xuất triệu chứng, phân loại sơ bộ loại dịch vụ và đề xuất xưởng phù hợp. Nhân viên vẫn phải kiểm tra và xác nhận.

**Success metric có số:** Giảm thời gian phân loại ban đầu từ 10–20 phút xuống dưới 5 phút/yêu cầu; tỷ lệ chuyển đúng nhóm dịch vụ đạt tối thiểu 90%.

**Quick Architecture:** [ ] No AI  &nbsp;&nbsp; [ ] Rule  &nbsp;&nbsp; [x] LLM Feature  &nbsp;&nbsp; [ ] Agent

**Rủi ro hoặc điều cần kiểm chứng:** AI không được tự chẩn đoán lỗi nghiêm trọng hoặc tự xác nhận lịch; cần kiểm tra độ chính xác với các mô tả lỗi thực tế. Quy trình đặt dịch vụ công khai của VinFast gồm chọn loại dịch vụ, mô tả vấn đề, địa điểm và thời gian. [Nguồn VinFast](https://vinfastauto.com/vn_vi/cau-hoi-thuong-gap/cau-hoi-xe-o-to/chinh-sach-hau-mai)

### Quick Problem Card #2

**Tên bài toán:** Điều phối cứu hộ RSA khi xe hết pin

**Bài toán trong một câu:** Khi xe hết pin hoặc gặp sự cố giữa đường, nhân viên phải thu thập thông tin, xác minh vị trí và điều phối xe kéo thủ công, khiến khách hàng phải chờ lâu.

**Công ty thành viên:** VinFast

**Lens:** Stakeholder Pain

**Ai đang đau (Actor/Stakeholder):** Chủ xe, nhân viên tổng đài, đội cứu hộ.

**Workflow thủ công hiện tại:**

1. Khách hàng gọi tổng đài và báo xe gặp sự cố.
2. Nhân viên xác minh biển số, vị trí, mức pin và tình trạng xe.
3. Nhân viên kiểm tra điều kiện tiếp cận và điểm cứu hộ phù hợp.
4. Nhân viên điều phối xe kéo RSA.
5. Nhân viên thông báo hướng dẫn và thời gian dự kiến cho khách hàng.

**Bước tốn thời gian hoặc dễ lỗi nhất:** Bước 2–4 — khoảng 10–30 phút/lượt, là ước tính cần kiểm chứng.

**AI có thể hỗ trợ ở bước:** Bước 2–3: chuyển nội dung cuộc gọi thành dữ liệu có cấu trúc, kiểm tra thông tin còn thiếu và đề xuất phương án điều phối. Nhân viên phải phê duyệt trước khi điều xe.

**Success metric có số:** Giảm thời gian tiếp nhận và điều phối từ 20 phút xuống dưới 8 phút/lượt; tỷ lệ hồ sơ có đủ thông tin ngay lần đầu đạt 95%.

**Quick Architecture:** [ ] No AI  &nbsp;&nbsp; [x] Rule  &nbsp;&nbsp; [x] LLM Feature  &nbsp;&nbsp; [ ] Agent

**Rủi ro hoặc điều cần kiểm chứng:** AI không được tự động điều xe, không được đưa ra hướng dẫn thiếu an toàn và phải xác minh vị trí/điều kiện giao thông. VinFast đã công bố sử dụng cứu hộ bằng xe kéo RSA cho trường hợp xe hết pin từ ngày 06/06/2025. [Nguồn VinFast](https://vinfastauto.com/vn_vi/thong-bao-ve-viec-dieu-chinh-phuong-thuc-cuu-ho-cho-cac-truong-hop-xe-het-pin-tu-ngay-06062025)

### Quick Problem Card #3

**Tên bài toán:** Gợi ý chuyên khoa và lịch khám phù hợp

**Bài toán trong một câu:** Bệnh nhân mô tả lý do khám chưa rõ ràng, khiến nhân viên phải đọc, hỏi lại và xác định chuyên khoa/bác sĩ trước khi xác nhận lịch.

**Công ty thành viên:** Vinmec

**Lens:** Time-consuming

**Ai đang đau (Actor/Stakeholder):** Bệnh nhân, nhân viên Contact Center, lễ tân.

**Workflow thủ công hiện tại:**

1. Bệnh nhân gửi yêu cầu đặt lịch và mô tả lý do khám.
2. Nhân viên đọc nội dung và gọi lại nếu thông tin chưa đầy đủ.
3. Nhân viên xác định chuyên khoa hoặc bác sĩ phù hợp.
4. Nhân viên kiểm tra ngày giờ còn trống.
5. Nhân viên gọi lại để xác nhận lịch khám.

**Bước tốn thời gian hoặc dễ lỗi nhất:** Bước 2–4 — khoảng 10–15 phút/yêu cầu, là ước tính cần kiểm chứng.

**AI có thể hỗ trợ ở bước:** Bước 2–3: tóm tắt lý do khám, gợi ý chuyên khoa và tạo danh sách câu hỏi cần hỏi thêm. Nhân viên Contact Center chịu trách nhiệm xác nhận cuối cùng.

**Success metric có số:** Giảm thời gian xử lý yêu cầu từ 10–15 phút xuống dưới 4 phút/yêu cầu; tỷ lệ gợi ý đúng chuyên khoa đạt tối thiểu 90%.

**Quick Architecture:** [ ] No AI  &nbsp;&nbsp; [x] Rule  &nbsp;&nbsp; [x] LLM Feature  &nbsp;&nbsp; [ ] Agent

**Rủi ro hoặc điều cần kiểm chứng:** AI chỉ hỗ trợ phân loại hành chính, không được chẩn đoán bệnh, tư vấn điều trị hoặc tự đặt lịch. Form đặt lịch Vinmec yêu cầu cơ sở, chuyên khoa, bác sĩ, ngày khám và lý do khám; Contact Center vẫn xác nhận lịch cuối cùng. [Nguồn Vinmec](https://www.vinmec.com/eng/booking/)

## 5. Lựa chọn bài toán cho Deep Dive

**Bài toán nhóm chọn:** Card #[Điền số] — [Điền tên bài toán]

**Lý do lựa chọn:**

- [Quy trình hiện tại nhóm hiểu rõ ở điểm nào?]
- [Bottleneck có đủ lớn và đo được không?]
- [Dữ liệu hoặc khả năng thử nghiệm hiện có là gì?]
- [Vì sao giải pháp AI phù hợp hơn hoặc bổ trợ cho quy trình hiện tại?]

**Lý do không chọn Card #[Điền số]:** [Điền]

**Lý do không chọn Card #[Điền số]:** [Điền]

**Câu hỏi cần xác minh trong Deep Dive:**

1. [Điền câu hỏi về workflow/dữ liệu]
2. [Điền câu hỏi về metric/chi phí]
3. [Điền câu hỏi về rủi ro và Human-in-the-loop]

## 6. Checklist hoàn thành

- [ ] Có ít nhất 5 bài toán trong bảng SCAN.
- [ ] Các bài toán sử dụng nhiều lens khác nhau.
- [ ] Đã hoàn thiện 3 Quick Problem Cards.
- [ ] Mỗi card có workflow từ 3–5 bước.
- [ ] Mỗi card có bottleneck và thời gian ước tính.
- [ ] Mỗi card có metric đo được bằng số.
- [ ] Nhóm đã chọn một bài toán cho `02-deep-dive-report.md`.



