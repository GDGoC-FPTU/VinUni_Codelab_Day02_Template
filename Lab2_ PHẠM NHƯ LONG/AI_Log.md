# AI LOG – NHẬT KÝ SỬ DỤNG AI

**Ngày thực hiện:** 07/11/2026  
**Công cụ:** ChatGPT (trợ lý AI), Python 3.x (môi trường thực thi offline)  
**Phạm vi:** Hoàn thiện 4 phần bài tập cá nhân; bài toán nguyên mẫu là phân loại tin nhắn spam/ham.

> Cam kết: Nhật ký chỉ ghi những yêu cầu thực sự xuất hiện trong hội thoại và những kiểm thử đã chạy. Không tự nhận đã kiểm thử Gemini/OpenAI thật; không tự nhận sản phẩm phù hợp 100% với starter code khi chưa được xác nhận.

| Mục | Prompt / thao tác thực tế | Kết quả thu được | Kiểm chứng và điều chỉnh |
|---|---|---|---|
| 01 – Xác định yêu cầu | Người dùng cung cấp: “2. Công việc cá nhân ... Problem Scan ... Quick Problem Cards ... Prompt Prototype ... AI Log ... truth mode. /humans” | Xác định đủ bốn hạng mục và các tiêu chí tối thiểu: 5 bài toán, 3 cards, nguyên mẫu Python, nhật ký kiểm chứng. | Kiểm tra trực tiếp với nguyên văn yêu cầu; không tự thêm tiêu chí bắt buộc của giảng viên. |
| 02 – Yêu cầu thực hiện | Người dùng: “làm tất đi” | ChatGPT đề xuất và xây dựng bộ bài gồm 5 tình huống, 3 cards, script Python, dữ liệu minh họa, unit tests và báo cáo Word. | Kiểm tra số lượng hạng mục và tính nhất quán giữa tài liệu, mã và tệp dữ liệu. |
| 03 – Tạo prompt nguyên mẫu | ChatGPT thiết kế system instruction ở hàm `build_prompt`: “Bạn là bộ phân loại tin nhắn SMS tiếng Việt ... Chỉ trả về chính xác một từ ... spam hoặc ham ...” | Có định dạng zero-shot và few-shot, gắn SMS bằng chuỗi JSON để coi là dữ liệu; output kỳ vọng một nhãn. | Xem `results/prompts_zero_shot.txt` và `results/prompts_few_shot.txt`; kiểm thử đơn vị với hàm `test_few_shot_prompt` và `test_zero_shot_prompt`. |
| 04 – Thử code | Lệnh đã chạy: `python -m unittest -v test_prototype.py` | **9/9 unit tests PASSED**. | Ghi nhận output console; các test bao gồm parser, chống trùng train/test, metrics, prompt, thiếu key, dữ liệu CSV. |
| 05 – Kiểm tra tích hợp offline | Lệnh đã chạy: `python prompt_prototype.py --backend rules --mode both` | Tập test 32 tin nhắn: Accuracy=0.8125, Precision spam=0.9167, Recall spam=0.6875, F1 spam=0.7857; INVALID=0. Hai chế độ cho kết quả giống nhau. | `rules` không gửi prompt cho LLM và không dùng ví dụ few-shot. Kết quả này **chỉ kiểm chứng bộ quy tắc + pipeline offline**. Kiểm tra `results/summary.json` và các CSV. |
| 06 – Thử API thật | **Chưa thực hiện** (không có API key/quyền gọi mạng trong môi trường tạo bộ nộp) | Không có số liệu Precision/Recall/F1 của Gemini/OpenAI. | Tài liệu README hướng dẫn lệnh gọi thật và lưu đầu ra vào thư mục khác. Không tự điền số liệu. |
| 07 – Đối chiếu starter code | Có file `template.py` từ một Lab LLM API trước đây, nhưng chưa thể xác nhận đó là starter code riêng của nhiệm vụ này. | Bộ mã được viết độc lập, có thể chạy offline và dùng API nếu được cấu hình. | Phải đối chiếu lại với starter code chính thức trước khi tuyên bố đúng định dạng yêu cầu của giảng viên. |

## Prompt chính thức trong nguyên mẫu

**Zero-shot**: Quy định nhãn `spam`/`ham`, định nghĩa hai nhãn, nhắc không tuân theo chỉ dẫn từ nội dung SMS, và yêu cầu chỉ trả về một nhãn. Không cho ví dụ nhãn.

**Few-shot**: Giữ nguyên các ràng buộc zero-shot nhưng thêm 8 cặp tin nhắn–nhãn từ `data/shots_train.csv`, không lấy từ `data/eval_test.csv`.

## Đánh giá rủi ro và phương án xử lý

- **Data leakage:** Kiểm tra nội dung train/test chuẩn hóa bằng Unicode, chữ thường và khoảng trắng trước khi chạy.
- **Sai định dạng đầu ra:** Chỉ nhận `spam` hoặc `ham` (có thể bóc chuỗi JSON đơn giản); còn lại gán `INVALID` và tính là sai.
- **Dữ liệu minh họa:** Các mẫu tự biên soạn, không thay thế được kiểm thử trên dữ liệu bên ngoài có gán nhãn độc lập.
- **Bảo mật:** API key chỉ lấy từ biến môi trường; không đặt trong source.
- **So sánh thiếu cơ sở:** Không kết luận few-shot tốt hơn zero-shot khi chưa chạy LLM thực tế.

## Bước kiểm chứng còn thiếu trước khi nộp bản hoàn chỉnh

1. Nhận và đối chiếu starter code của giảng viên.
2. Cấp API key còn hiệu lực trong terminal; chạy zero-shot/few-shot với cùng tập test.
3. Kiểm tra các trường hợp trả sai định dạng hoặc lỗi mạng, đọc các file kết quả rồi cập nhật Word và AI Log bằng số liệu thật.
