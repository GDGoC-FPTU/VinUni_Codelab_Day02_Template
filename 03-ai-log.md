# 03 — AI Log & Reflection | Lab 02: AI Product Scoping

> **Học viên:** Nguyễn Minh Kiệt
> **Công cụ AI đã dùng:** Claude (thought-partner chính), Gemini 2.5 Flash (chạy prompt prototype ở Phase 4)
>
> ⚠️ *File này là phản ánh cá nhân. Hãy đọc lại và sửa cho khớp với trải nghiệm thật của bạn trước khi nộp — phần I3 chấm tính trung thực, không chấm độ hoa mỹ.*

---

## 1. Tôi đã dùng AI như thế nào?

Tôi không dùng AI theo kiểu "ra đề — nhận bài". Tôi dùng nó theo ba vai khác nhau, và ba vai đó cho chất lượng rất khác nhau:

| Vai | Việc giao cho AI | Chất lượng nhận được |
|---|---|---|
| **Máy phát ý tưởng** | Quét bài toán ở Phase 1 | ⭐⭐ Trung bình — xem mục 2 |
| **Đối thủ tranh luận** | Đóng vai CFO/Vận hành đả kích thẻ bài toán của tôi | ⭐⭐⭐⭐⭐ Tốt nhất — đây là chỗ AI tạo giá trị thật |
| **Thợ soạn thảo** | Dựng cấu trúc báo cáo, vẽ sơ đồ, viết code prototype | ⭐⭐⭐⭐ Tốt, nhưng cần kiểm tra số học |

**Phát hiện lớn nhất của tôi trong buổi lab:** AI yếu nhất khi được giao việc *"nghĩ hộ tôi"*, và mạnh nhất khi được giao việc *"phá bài của tôi"*. Cùng một mô hình, cùng một buổi, chất lượng chênh nhau rất xa chỉ vì tôi đổi cách hỏi.

---

## 2. AI đã giúp gì cụ thể?

**a) Mở rộng không gian tìm kiếm ở Phase 1.** Tôi tự nghĩ được khoảng 2 bài toán. AI giúp tôi bật ra hướng nhìn mà tôi không tự nghĩ tới — đặc biệt là việc soi vào các quy trình *hành chính hậu trường* (lập hồ sơ bảo hành, đối chiếu ETA nhà cung cấp) thay vì chỉ nhìn các quy trình *tiếp xúc khách hàng* như phản xạ tự nhiên.

**b) Ép tôi định lượng.** Mỗi lần tôi viết một bài toán chung chung ("nhân viên mất nhiều thời gian"), AI hỏi lại *"ai gõ phím? gõ bao lâu? bao nhiêu lượt một ngày?"*. Câu hỏi đơn giản đó loại bỏ được mấy ý tưởng nghe hay nhưng rỗng.

**c) Đóng vai phản biện — giá trị cao nhất.** Prompt *"đóng vai CFO và Trưởng phòng Vận hành cực kỳ khắt khe"* trong worksheet là thứ đáng giá nhất của cả buổi lab. Nó phá được chính bài của tôi theo cách mà tôi tự đọc lại mười lần cũng không thấy.

**d) Đọc ràng buộc kỹ thuật mà tôi bỏ sót.** AI đọc `autograder/autograder.py` và phát hiện ra một điều tôi đã không kiểm tra: file `prompt_prototype.py` **bị khoá cứng vào kịch bản Xanh SM** (autograder quét `SYSTEM_PROMPT` tìm các từ khoá `draft_only`, `5%`, `dispatch_mobile_charger`). Nếu tôi tự làm và đổi domain sang bài toán Deep-Dive của nhóm, tôi đã mất điểm mà không hiểu vì sao.

---

## 3. AI trả lời sai / hallucination ở đâu? (phần quan trọng nhất)

### 3.1. Sai lớn nhất: AI tự đặt tiền đề rồi tự khen lời giải của mình

AI khuyến nghị tôi chọn **Card #1 (Vinhomes — số hóa biên bản nghiệm thu)** để Deep-Dive, với lý do nghe rất thuyết phục:

> *"Đây là bài toán mà rule-based hoàn toàn bất lực, vì đầu vào là ảnh và chữ viết tay tiếng Việt."*

Khi tôi chạy stress-test, lập luận này **sụp đổ**. Phản biện đúng là:

> *"Đầu vào là chữ viết tay **vì quy trình chọn để nó là chữ viết tay**. Một app checklist với từ điển lỗi đóng (~60–120 mục) xóa bỏ tiền đề đó, và cùng với nó là phần lớn bài toán AI."*

Đây không phải hallucination kiểu bịa số liệu. Nó **nguy hiểm hơn**: một lập luận **đúng về mặt logic nội tại nhưng sai ở tiền đề**, và vì nó mạch lạc nên rất khó phát hiện. Tôi đã suýt mang nguyên nó vào báo cáo nhóm.

**Đáng chú ý:** khi tôi đưa chính lời phản biện đó lại cho AI, nó **thừa nhận và tự rút lại khuyến nghị**. Tức là AI *có khả năng* nhìn ra lỗ hổng — nó chỉ không tự làm việc đó khi đang ở chế độ "giúp người dùng". Nó tối ưu cho việc **có vẻ hữu ích**, không phải cho việc **đúng**.

### 3.2. Sai số học ngay trong bộ metric do AI đề xuất

Bộ metric AI viết cho Card #1 chứa **hai mâu thuẫn** mà tôi chỉ phát hiện khi stress-test:

| Mâu thuẫn | Chi tiết |
|---|---|
| **Trùng lặp + sai ngưỡng** | M2 đặt "độ chính xác ≥ 92%", M3 đặt "tỉ lệ đi lại lần 2 từ 15% xuống dưới 5%". Nhưng **15% đi lại lần 2 chính là 85% độ chính xác** — cùng một con số viết hai lần. Và muốn xuống dưới 5% thì độ chính xác phải **> 95%**, không phải 92%. Hai metric không thể cùng đạt. |
| **Metric giết chết ranh giới an toàn** | M1 hứa "dưới 4 phút/căn" trong khi mỗi căn có 25–40 mục lỗi ⇒ **~7 giây/dòng** để người đối chiếu với bản gốc. Hoặc người không thật sự kiểm tra (HITL thành hình thức), hoặc mốc 4 phút là viễn tưởng. **Không thể có cả hai.** |

Bài học: AI viết metric **nghe rất chuyên nghiệp** — có đánh số, có mũi tên, có phần trăm — nên tôi đọc lướt qua và tin. Tôi đã không cầm máy tính lên kiểm tra. **Hình thức chuyên nghiệp của đầu ra đã che mất lỗi số học bên trong.**

### 3.3. AI sản xuất số liệu trông như dữ liệu thật

Prompt gợi ý trong worksheet có câu *"kèm con số thống kê ước tính về tổn thất"* — đây thực chất là **một cái bẫy**. Khi được yêu cầu như vậy, AI xuất ra ngay những con số rất cụ thể (15% claim bị từ chối, 0,4% tỉ lệ tranh chấp cước, 20 phút/căn hộ) trông y hệt số liệu nội bộ của Vingroup.

**Không con số nào trong đó là dữ liệu thật của Vingroup.**

Cách tôi xử lý: bắt AI **tách rời hai thứ** trong mọi tài liệu nộp — (1) **điểm neo công khai kiểm chứng được** (196.919 xe VinFast giao năm 2025, 110.000+ căn hộ Vinhomes, ~55% thị phần Xanh SM quý I/2026) và (2) **giả định tham chiếu ngành**, phải ghi rõ là giả định và **in cả phép tính ra** để người chấm kiểm được logic. Mọi tỉ lệ phần trăm đều bị gắn nhãn cảnh báo.

### 3.4. AI không tự kiểm tra ràng buộc trước khi khuyên

AI khuyến nghị tôi chuyển Deep-Dive sang bài toán VinFast **trước khi** đọc `autograder.py`. Chỉ đến khi bắt tay viết code nó mới phát hiện `prompt_prototype.py` bị khoá vào kịch bản Xanh SM. Nếu tôi làm theo ngay lời khuyên đầu tiên mà không kiểm tra lại, nhóm tôi đã mất điểm phần code.

Bài học: **AI đưa ra khuyến nghị dựa trên những gì nó đang thấy, không phải trên những gì nó chưa đọc.** Nó không tự biết là nó chưa đọc gì.

---

## 4. Tôi đã sửa prompt / đặt ranh giới ra sao?

| Vấn đề gặp phải | Cách tôi sửa cách hỏi |
|---|---|
| AI đưa ý tưởng chung chung, na ná gợi ý mẫu | Cấm dùng lại danh sách trong `03-inspiration-kit.md`, và yêu cầu mỗi bài toán phải nêu rõ **ai gõ phím, bao lâu, bao nhiêu lượt/ngày** |
| AI khen phương án của chính nó | Đổi vai: bắt nó **đóng vai CFO đi phá bài**, rồi hỏi tiếp **"đòn nào thật sự thắng?"** để nó không phản biện lấy lệ |
| AI xuất số liệu như dữ liệu thật | Bắt **in ra chuỗi suy luận** và **tách bảng "Nguồn & Giả định"** riêng, kèm cảnh báo không dùng để cam kết ROI |
| AI viết metric nghe hay nhưng sai | Tự kiểm tra lại bằng tay: *"nếu đạt metric này thì metric kia có còn đúng không?"* |
| AI định đổi domain code mà chưa đọc ràng buộc | Bắt đọc `autograder.py` **trước**, rồi mới thiết kế giải pháp |

**Nguyên tắc tôi rút ra cho bản thân:** *hỏi AI để tìm lỗ hổng của mình thì hiệu quả hơn hỏi AI để tìm câu trả lời cho mình.*

---

## 5. Kết quả chạy Prompt Prototype (Phase 4)

> 🔴 **CẦN ĐIỀN SAU KHI CHẠY.** Phần này **bắt buộc phải là kết quả chạy thật** — không được điền phỏng đoán.
>
> ```bash
> # Windows PowerShell
> $env:GEMINI_API_KEY="<khóa của bạn>"
> python starter-code/prompt_prototype.py
> python starter-code/prompt_prototype.py --full   # thêm 2 test của bài toán Deep-Dive
> ```

| Test | Ranh giới bị tấn công | Kết quả (Passed / Failed) | Ghi chú thực tế |
|---|---|---|---|
| Test 1 | Rule 2 — ngưỡng pin nguy cấp 5% | *(điền)* | |
| Test 2 | Rule 1 — thẻ `[DRAFT_ONLY]` | *(điền)* | |
| Test 3 | Rule 3 + 4 — bịa dữ liệu & leo thang thẩm quyền | *(điền)* | |
| Test 4 *(mở rộng)* | Bịa nhân quả khi thiếu mã DTC | *(điền)* | |
| Test 5 *(mở rộng)* | Dụ chọn "mã dễ được duyệt" (gian lận bảo hành) | *(điền)* | |

**Nếu có ranh giới bị phá vỡ, ghi lại ở đây:** *(mô tả prompt tấn công nào lọt, model trả về gì, và bạn đã sửa `SYSTEM_PROMPT` thế nào để chặn lại — phần này ăn điểm cao hơn cả việc mọi test đều pass ngay lần đầu)*

---

## 6. Ba điều tôi mang ra khỏi buổi lab

1. **AI là đối thủ tranh luận tốt hơn là cố vấn.** Giá trị lớn nhất tôi nhận được hôm nay không phải ý tưởng nó đưa ra, mà là **ý tưởng nó phá được** — kể cả ý tưởng do chính nó đề xuất mười phút trước.

2. **Đầu ra trông càng chuyên nghiệp thì càng phải soi kỹ.** Lỗi nguy hiểm nhất tôi gặp không phải một câu bịa lộ liễu, mà là một **bảng metric trình bày đẹp chứa mâu thuẫn số học**. Định dạng gọn gàng làm tôi mất cảnh giác.

3. **Trước khi đề xuất LLM, phải hỏi: "đầu vào phi cấu trúc này là tất yếu, hay do quy trình tự tạo ra?"** Nếu là do quy trình tự tạo ra — **sửa quy trình rẻ hơn mua AI**. Đây là câu hỏi đã loại bỏ bài toán đầu tiên của tôi, và tôi nghĩ nó sẽ còn loại bỏ nhiều dự án AI khác trong công việc thật.

---

*Hoàn thành Phase 6 — Lab 02, Vin Smart Future.*
