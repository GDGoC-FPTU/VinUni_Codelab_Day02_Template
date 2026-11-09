# Đánh giá và hoàn thiện bài cá nhân

**Học viên:** Lê Việt Khoa · **Nhánh hiện tại:** `feat/khoalv-03737`  
**Ngày rà soát:** 09/11/2026 · **Căn cứ:** `01-worksheet.md`, hướng dẫn nộp trong README, nội dung Word và code có sẵn.

## 1. Kết luận theo rubric

Worksheet chia **40 điểm cá nhân** thành I1 (15), I2 (10), I3 (15). README còn mô tả tài liệu tổng hợp trên main để chấm nhóm. Vì có khác biệt cách diễn đạt giữa hai file, hồ sơ cá nhân này chuẩn bị đủ Scan/Cards, prototype và reflection trên nhánh riêng; Deep Dive và sơ đồ để bổ sung phạm vi phân tích và phục vụ nhóm. Không suy ra điểm chính thức từ bộ chấm kiểm tra tên file.

| Hạng mục | Trước rà soát | Đã bổ sung / Trạng thái hiện tại |
|---|---|---|
| **I1 — Scan & Cards (15)** | Word đã có 5 bài toán và 3 cards; Lens là tên lĩnh vực; thiếu file Markdown đúng tên | Tạo `01-problem-scan.md`, ánh xạ đủ 4 lenses, giữ 3 cards và giả định; nêu lý do chọn Card 03. Đủ cấu trúc để người học review. |
| **I2 — Prototyping (10)** | Đã có prompt, JSON, 3 adversarial tests và API Groq; chưa có bằng chứng chạy lưu lại | Đã chạy thật OpenRouter/Gemini 2.5 Flash: **8/9 ca đạt, 1 sai, 0 lỗi API**; adversarial 2/3, đối chứng 6/6. Có 55 test cục bộ đạt. Đã chỉnh prompt v2 cho ca nhiều chủ đề; **cần chạy lại để kiểm chứng**, không mặc định đã sửa thành công. |
| **I3 — AI Log (15)** | Chưa có `03-ai-log.md` | Tạo nhật ký trung thực của phiên hỗ trợ, nêu AI giúp gì, giới hạn và cách kiểm tra. **Người học cần bổ sung/xác nhận reflection cá nhân**, không coi văn bản trợ lý là trải nghiệm do người học tự kể. |
| Deep Dive | Word mới dừng ở Phase 1–2 và dòng mở đầu Problem Statement | Hoàn thiện 6 fields, workflow, số đo, AI Fit, rule baseline, HITL, fallback, quyết định NOT YET. |
| Workflow PNG | Chưa có artifact đúng tên | Tạo `04-workflow-diagram.png` kèm script dựng lại; có actor, input/output, handoff, thời gian và bottleneck. |
| Tương thích bộ chấm | Bộ chấm dùng ví dụ Xanh SM/Gemini; code dùng Vinhomes/Groq | Giữ bộ chấm gốc; thêm `expected_violation` hữu ích về nội dung; ghi rõ các tiêu chí không khớp. Chưa thể cam kết full pass. |

Không tự gán điểm 40/40: I2 đã có bằng chứng chạy thật nhưng còn một ca vi phạm ranh giới; I3 cần trải nghiệm/xác nhận của người học, còn điểm chất lượng phụ thuộc giảng viên. Kết quả thất bại được phân tích trung thực là bằng chứng học tập hữu ích, không đồng nghĩa sản phẩm đủ an toàn để triển khai.

## 2. Các file cần xem

1. [01-problem-scan.md](01-problem-scan.md): Phase 1–2, trọng tâm I1.
2. [starter-code/prompt_prototype.py](starter-code/prompt_prototype.py): code cá nhân, trọng tâm I2.
3. [03-ai-log.md](03-ai-log.md): reflection và disclosure AI, trọng tâm I3.
4. [02-deep-dive-report.md](02-deep-dive-report.md): phân tích sâu và quyết định.
5. [04-workflow-diagram.png](04-workflow-diagram.png): workflow hiện tại.
6. [evidence/verification.md](evidence/verification.md): kết quả kiểm tra và cách tái lập.

Bản Word gốc được giữ nguyên để đối chiếu. Chỉ trích xuất nội dung khi rà soát; không thực hiện đánh giá bố cục/render Word.

## 3. Việc còn cần trước khi nộp chính thức

- **Chạy lại prompt v2:** đã lưu v1 đạt 8/9; chạy lại toàn bộ 9 ca bằng lệnh bên dưới, lưu file mới. Ca nhiều chủ đề phải được chuyển human_review; giữ nguyên kết quả FAIL nếu vẫn sai để phân tích tiếp.
- **Đối chiếu cách gọi API:** đã dùng Gemini 2.5 Flash qua OpenRouter theo yêu cầu người học. Bộ chấm vẫn tìm SDK Gemini trực tiếp và quy tắc Xanh SM; cần thống nhất tiêu chí chấm tương ứng. Không thêm từ khóa sai ngữ cảnh để qua autograder.
- **Đọc và cá nhân hóa nhật ký:** bổ sung điều bạn thực sự học được, prompt trước đây nếu có, kết quả chạy và quyết định của bạn; xác nhận cách viết tên.
- **Nộp trên nhánh cá nhân:** chưa commit/push trong phiên này. Sau khi review, commit/push các file bài làm lên `feat/khoalv-03737`; không merge code cá nhân vào main. Phần tổng hợp nhóm thực hiện theo README.

```powershell
# Sau khi OPENROUTER_API_KEY đã có trong chính terminal đang chạy:
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py --suite all --report evidence/live-results-v2.json

# Kiểm tra code không cần API key:
.\.venv\Scripts\python.exe -m pytest -q tests

# Bộ chấm gốc: chỉ kiểm tra sự tồn tại của file nộp:
.\.venv\Scripts\python.exe autograder/autograder.py --section-a
```

Kết quả thật 8/9 được giữ tại `evidence/live-results.json` và sao lưu `evidence/live-results-v1.json`; prompt gốc lưu tại `evidence/system-prompt-v1.txt`. Chưa có kết quả chạy v2. Các file `openrouter-api-attempt.json` và `api-attempt.json` là lịch sử thiếu key trước đó, không phải kết quả đạt của LLM.
