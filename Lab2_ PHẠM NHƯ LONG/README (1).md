# BỘ BÀI TẬP CÁ NHÂN – ỨNG DỤNG AI TRONG THỰC TẾ

**Tình trạng:** Đã viết Problem Scan (5 bài toán), Quick Problem Cards (3 bài toán), Prompt Prototype (Python) và AI Log. Đã chạy unit tests + rules baseline offline; **chưa gọi Gemini/OpenAI API thực tế**. Đây là bản nguyên mẫu độc lập, **chưa xác nhận khớp starter code của giảng viên**.

## Cấu trúc bộ nộp

- `Bao_cao_bai_tap_ca_nhan_AI.docx`: nội dung nộp theo 4 yêu cầu, Times New Roman, chữ đen.
- `prompt_prototype.py`: phân loại SMS spam/ham; tạo prompt zero-shot/few-shot; hỗ trợ `rules`, `gemini`, `openai`.
- `test_prototype.py`: kiểm thử đơn vị offline.
- `data/shots_train.csv`: 8 ví dụ few-shot được biên soạn minh họa.
- `data/eval_test.csv`: 32 tin nhắn đánh giá minh họa, không trùng ví dụ few-shot.
- `results/summary.json`, `predictions_*.csv`, `prompts_*.txt`: kết quả baseline và các prompt mẫu được tạo từ lần chạy thật.
- `AI_Log.md`: nhật ký sử dụng ChatGPT, phương pháp kiểm chứng và phần chưa thực hiện.

## Bước 1 — Chạy kiểm tra offline (KHÔNG cần API, không tốn phí)

Mở **Windows PowerShell** tại thư mục giải nén:

```powershell
python -m unittest -v test_prototype.py
python prompt_prototype.py --backend rules --mode both
```

Lưu ý: `rules` chỉ là bộ quy tắc kiểm tra đường đi dữ liệu và cách tính metric; **không hề sử dụng LLM**. Vì vậy zero-shot và few-shot trong `rules` cho cùng kết quả.

## Bước 2 — Kiểm thử API Gemini thật

Không ghi API key vào file Python hoặc nộp kèm key trong ZIP. Trong PowerShell:

```powershell
$env:GEMINI_API_KEY = "DAN_API_KEY_CUA_BAN"
python prompt_prototype.py --backend gemini --model gemini-2.5-flash --mode both --limit 10 --pause 1 --out results_gemini
```

Sau khi kiểm tra 10 mẫu đầu, muốn đánh giá toàn bộ 32 mẫu thì bỏ `--limit 10`:

```powershell
python prompt_prototype.py --backend gemini --model gemini-2.5-flash --mode both --pause 1 --out results_gemini_full
```

Các lệnh trên **chỉ là hướng dẫn**, chưa được chạy trong bản nộp này. Mỗi chế độ sẽ gọi API một lần cho mỗi mẫu; kiểm thử toàn bộ 2 chế độ và 32 mẫu đồng nghĩa **64 yêu cầu API**, có thể phát sinh chi phí/quota. Tên model có thể cần đổi nếu tài khoản không hỗ trợ.

## Tùy chọn — Kiểm thử API OpenAI thật

```powershell
$env:OPENAI_API_KEY = "DAN_API_KEY_CUA_BAN"
python prompt_prototype.py --backend openai --model gpt-4o-mini --mode both --limit 10 --out results_openai
```

## Đánh giá

Những chỉ số được tính với lớp dương `spam`:

- `Precision = TP/(TP+FP)`
- `Recall = TP/(TP+FN)`
- `F1 = 2PR/(P+R)`
- `Accuracy = (TP+TN)/N`
- `INVALID` (API không trả đúng một nhãn) được tính là sai; không âm thầm loại khỏi mẫu.

Dữ liệu thử do người viết biên soạn và có tính chất minh họa, không đại diện phân phối tin nhắn thực tế. Để đánh giá mô hình có giá trị, cần kiểm thử tập ngoài, đối chiếu thủ công các nhãn khó và báo cáo rõ phiên bản mô hình, thời gian, lượng mẫu, chi phí.

## Bảo mật và trung thực

- Không đặt API key trực tiếp vào code, CSV hoặc AI Log.
- Không nộp nhầm kết quả `rules` như kết quả Gemini/OpenAI.
- Không gán kết quả từ một bài Lab khác cho bài này.
- Khi giảng viên cung cấp starter code chính xác, đối chiếu lại tên hàm, tham số và định dạng đầu ra trước khi nộp.
