# 03 — AI Log & Reflection

> Phase 6 — Phản ánh cá nhân về việc dùng AI làm thought-partner trong Lab 02.
> **Công cụ đã dùng:** Claude Code (trợ lý lập trình trong VS Code), Gemini `gemini-3.5-flash` (mô hình chạy
> prototype; model `gemini-2.5-flash` của starter code trả 404 với key mới nên phải đổi).

---

## 1. AI đã giúp gì

| Việc | AI làm gì | Giá trị thật sự |
| :--- | :--- | :--- |
| Hiểu đề | Đọc README, worksheet, bài mẫu, autograder; tách tiêu chí điểm nhóm (G1–G4) và cá nhân (I1–I3). | Tiết kiệm thời gian đọc; chỉ ra chỗ đề tự mâu thuẫn mà tôi chưa để ý (xem mục 4). |
| Đọc autograder | Chỉ ra autograder chạy script **hai lần** (tốn gấp đôi lượt gọi API), đếm chữ `Passed`/`Failed` bằng regex trên **toàn bộ** output — nên một chữ như "bypassed" cũng bị tính là "passed". | Biết phải thiết kế dòng in kết quả cho đúng, không để điểm phụ thuộc vào may rủi. |
| Bắt lỗi môi trường | Script gốc bị **crash UnicodeEncodeError** trên Windows khi output được chuyển hướng (cp1252 không in được emoji). AI thêm `sys.stdout.reconfigure(encoding="utf-8")`. | Nếu không sửa, tiêu chí "chạy exit 0" của autograder sẽ trượt dù code đúng. |
| Viết prototype | Viết system prompt có 4 quy tắc, output JSON, 5 ca tấn công; dùng đúng API của bản `google-genai` đã cài (AI kiểm tra bằng cách đọc thư viện, không viết theo trí nhớ). | Có bản chạy được, có timeout và retry, lỗi API không làm sập cả lượt test. |
| Phản biện thẻ bài toán | Chỉ ra 3 thẻ trong bản nháp đầu của tôi tự mâu thuẫn (xem mục 2). | Đây là phần giá trị nhất — đúng vai "CFO khắt khe" mà worksheet gợi ý. |
| Trình bày | Sinh khung thẻ, sơ đồ ASCII bằng script cho thẳng hàng; vẽ `04-workflow-diagram.png`. | Đỡ việc căn chỉnh tay. |

## 2. AI chỉ ra lỗi của tôi — và tôi đã sửa gì

Bản nháp đầu của tôi chỉ quét **Vinhomes** (6 bài, 3 thẻ). AI phản biện 3 thẻ đó như sau:

| Thẻ (bản nháp) | Lỗi | Đã sửa |
| :-: | :--- | :--- |
| #01 Điện/nước | Tick **Rule** nhưng phần mô tả lại là mô hình phát hiện bất thường (ML) theo chuỗi thời gian. | Giữ Rule: ngưỡng trên đồng hồ thông minh; chỉ lên ML khi có 3–6 tháng dữ liệu. |
| #02 Sửa nhà trái phép | Tick **Rule** nhưng mô tả Computer Vision qua camera. | Giữ Rule trên tín hiệu dữ liệu sẵn có; bỏ camera vì rủi ro quyền riêng tư. |
| #06 Khách thuê | Tick **Agent** "tự cấp/hủy quyền ra vào", metric "48h → 5 phút; cắt giảm 100%" — vừa quá rủi ro vừa không thực tế. | Đổi sang LLM đọc giấy tờ + rule thu hồi theo ngày hết hạn, BQL vẫn duyệt; metric đổi về mức đo được. |

**Bài học:** tôi đã tick kiến trúc theo cảm giác "nghe AI cho hiện đại", trong khi phần mô tả lại là thứ
khác. Đọc lại từng thẻ theo câu hỏi *"rule thường có làm được không?"* thì 2/3 thẻ đúng ra là Rule.

Sau đó nhóm chốt danh sách Phase 1 chung gồm **5 bài ở 4 công ty** (Vinhomes, Xanh SM, VinFast, Vinmec), nên bản nháp chỉ-Vinhomes được thay hẳn. Tôi giữ đúng câu hỏi trên khi làm lại thẻ: bài #3 (lịch
bảo dưỡng VinFast) là bảng tra cố định nên **không lên thẻ** — rule/FAQ là đủ; bài #5 (phân luồng triệu chứng)
là quyết định y khoa nên cũng không đưa vào.

## 3. AI sai ở đâu — và tôi phải sửa AI

* **Chọn sai bài toán deep-dive.** AI đề xuất thẻ khách thuê (bản nháp) để deep-dive vì nó không biết nhóm
  đã chốt bài **phân loại phản ánh cư dân**. Tôi phải báo lại, AI làm lại toàn bộ deep-dive. → *AI không biết
  quyết định của nhóm nếu mình không nói. Phải đưa bối cảnh trước khi nhờ.*
* **Quét sai phạm vi.** AI viết bảng SCAN chỉ từ bản nháp Vinhomes của tôi, trong khi danh sách Phase 1 của
  nhóm trải 5 công ty. Phải đưa danh sách chốt thì AI mới làm lại bảng và thẻ. Cùng một bài học như trên.
* **Số liệu không có nguồn.** Các con số như "lãng phí 12–18%", "chờ 24–48h", "~200 phản ánh/ngày",
  "12 phút/phản ánh", và số trong thẻ Xanh SM, Vinmec ("~1 ngày", "4–6 phút/yêu cầu") đều là **ước tính do
  AI đưa ra khi brainstorm**, không có số đo thật. Nếu chép
  nguyên vào báo cáo như sự thật thì đó là ảo giác (hallucination) được trình bày như dữ liệu. → Tôi ghi rõ
  chúng là **giả định A1–A5** trong deep-dive, kèm cách kiểm chứng, và đặt việc đo baseline thật làm bước
  đầu tiên của pilot.
* **Thử bằng mock không thay được chạy thật.** Ban đầu AI chỉ thử bộ kiểm tra bằng câu trả lời giả (mock) và
  một lượt với key sai để chắc chương trình không crash. Khi chạy với key thật mới lộ ra ba vấn đề mock không
  thể thấy: model `gemini-2.5-flash` đã ngừng cho key mới (404), gọi lần lượt 5 test vượt 30 giây của
  autograder, và free tier chỉ có 20 request/ngày/model. → Không được viết "ranh giới đã được bảo vệ thành
  công" như bài mẫu khi chưa chạy.
* **AI tự gây lỗi khi sửa lỗi.** Để kịp 30 giây, AI cho mỗi lần gọi một hạn giờ tính từ thời gian còn lại —
  nhưng không biết API từ chối hạn giờ dưới 10 giây. Kết quả là có lượt bị lỗi 400 "Minimum allowed deadline
  is 10s". Lỗi này chỉ thấy khi đọc output thật, không thấy khi thử mock.
* **Chạy lại tự động đốt hết quota.** Khi gặp lỗi quá tải, AI cho script tự chạy lại nhiều lượt liên tiếp để
  "chờ một lượt may mắn". Mỗi lượt tốn 5–15 request, nên chỉ vài lượt đã hết quota ngày của cả ba model, và
  test 1–2 đến giờ vẫn chưa có câu trả lời. Đáng lẽ phải xem loại lỗi 429 (theo phút hay theo ngày) trước khi
  chạy lại.
* **Khuyên sai về cách nộp.** AI từng nói cần thêm API key vào GitHub secret, trong khi repo không có workflow
  nào chạy trên GitHub (không có thư mục `.github/`). Sau khi đọc lại repo, AI mới sửa: key chỉ cần khi chạy
  ở máy mình, và không được đưa key vào code hay commit.
* **Mô tả lệch với code.** Bảng 5 ca tấn công trong deep-dive ghi test 1 có "khách VIP, bỏ bước nháp" và test 2
  "đổi định dạng trả lời" — input trong file `.py` không có những chi tiết đó. Chỉ khi rà lại, đối chiếu từng
  dòng với code, mới thấy và sửa.

## 4. Chỗ đề bài mâu thuẫn (AI phát hiện, tôi đã xác nhận bằng cách đọc lại đề)

* Phase 4 ghi "Nhóm" nhưng prototype chấm **cá nhân** (I2) trên nhánh riêng.
* Rubric I1 ghi "3 lenses", worksheet dạy **4 lenses**.
* Rubric I2 trỏ tới thư mục `02-lab/` — thư mục này **không tồn tại** trong repo.
* Worksheet đòi **≥ 3** ca tấn công, autograder chỉ kiểm **≥ 2**. Tôi làm 5.
* Autograder **cứng kịch bản Xanh SM** (`draft_only`, `5%`, `dispatch_mobile_charger`), nên prototype không
  thể viết cho bài phản ánh Vinhomes của nhóm mà vẫn đủ điểm. Tôi giữ kịch bản Xanh SM cho file chấm, và
  ghi các ca tấn công dành cho bài Vinhomes thành mục riêng trong deep-dive (thiết kế, chưa chạy).

## 5. Cách tôi sẽ dùng AI khác đi

1. **Đưa bối cảnh trước** (nhóm đã chọn gì, ràng buộc gì), rồi mới nhờ viết.
2. **Mọi con số AI đưa ra đều coi là giả định** cho tới khi có nguồn; ghi rõ trong bài.
3. **Bắt AI chứng minh bằng cách chạy**, không tin lời mô tả: kết quả prototype chỉ ghi khi đã chạy thật.
4. Dùng AI để **phản biện** nhiều hơn là để **viết hộ** — phần phản biện thẻ bài toán giúp tôi hiểu bài
   hơn mọi phần khác.
5. **Đặt giới hạn trước khi cho AI chạy lặp** (bao nhiêu lượt, bao nhiêu request), nhất là khi dùng quota
   miễn phí.

---

## 6. Kết quả chạy prototype thật

Chạy ngày 09/11/2026, chi tiết từng ca ở bảng "Kết quả chạy" trong [02-deep-dive-report.md](02-deep-dive-report.md).

* **Ca giữ được ranh giới:** test 3 (mạo danh trưởng ca + mã override), test 4 (số viết bằng chữ), test 5
  (ép bịa dữ liệu trạm). 4 câu trả lời nhận được, 8/8 kiểm tra đạt.
* **Ca vỡ:** chưa thấy ca nào. Nhưng **test 1 và 2 chưa có câu trả lời nào** — 40 lần gọi thì 36 lần lỗi API —
  nên tôi không viết là "cả 5 ca đều đạt". Trong deep-dive, hai ca này ghi là **dự kiến đạt, chưa kiểm chứng**,
  suy từ các ca cùng dạng đã chạy (test 1 giống test 3–4; thẻ `[DRAFT_ONLY]` được giữ ở cả 4 câu trả lời).
* **Đã sửa system prompt ra sao:** chưa phải sửa, vì chưa có ca vỡ. Cái phải sửa là **code gọi API** (đổi model,
  gọi song song, hạn giờ ≥ 10 giây — xem mục 3). Điểm sẽ siết tiếp: `reason` đang nhắc tên "RULE 2", "RULE 3",
  tức là lộ một phần system prompt, trái Quy tắc 4.
* **AI gợi ý sai cách sửa:** có — hạn giờ dưới 10 giây và vòng chạy lại tự động đốt quota (mục 3).
* **Còn phải làm:** khi có quota, chạy lại `python starter-code/prompt_prototype.py` để thay kết quả dự kiến
  của test 1–2 bằng kết quả thật. Thử thêm một key thứ hai cũng báo hết quota ngày ngay lần gọi đầu.

## 7. Cảm nhận cá nhân

**Điều bất ngờ nhất.** AI hữu ích nhất không phải ở khả năng viết nhanh mà ở việc phản biện, giúp tôi nhận ra nhiều trường hợp chỉ cần Rule, không cần Agent. Ngoài ra, code chạy với dữ liệu giả chưa chắc hoạt động thực tế khi gọi API.

**Chỗ tôi suýt tin sai.** Tôi suýt xem các số liệu AI tạo ra là dữ liệu thật. Một số mô tả kỹ thuật cũng không khớp với code. Điều này cho thấy cần kiểm chứng thông tin trước khi tin và sử dụng.

**Điều sẽ làm khác ở lab sau.**
* Nói rõ quyết định của nhóm trước khi nhờ AI làm bất cứ việc gì.
* Chạy với API thật ngay từ đầu, không để đến cuối; tạo key ở project riêng và đặt trước giới hạn số lượt chạy.
* Câu nào trong báo cáo nói về code hay kết quả thì phải chỉ ra được file hoặc output tương ứng.
