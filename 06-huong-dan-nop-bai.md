# Chốt và nộp Lab 02

## 1. Trạng thái hiện tại

| Nội dung | Trạng thái |
|---|---|
| Scan 5 bài toán và 3 Quick Cards | Đã có `01-problem-scan.md`. |
| Deep-dive, 6 trường, AI Fit, future flow, readiness | Đã có `02-deep-dive-report.md`; giữ NOT YET cho triển khai thực tế. |
| Nhật ký và reflection | Đã có `03-ai-log.md`, ghi lỗi và kết quả thật; người làm bài đọc lại trước khi nộp. |
| Sơ đồ current-state | Đã có `04-workflow-diagram.pdf`, 5 bước, handoff, bottleneck, tổng 15 phút giả định. |
| Prototype Gemini | Model thay thế `gemini-3.5-flash-lite` chạy đạt 6/6 theo log người dùng. Đây là mặc định mới, không cần biến model ngoài máy chấm. |
| Kiểm tra offline | 50 tests đạt; deliverables 5/5; 3 mục tĩnh code đạt. |
| Autograder đầy đủ với API thật | Đã đạt **10/10** qua lệnh `--live` do người dùng chạy; báo cáo có `live_autograder: passed`, `passed: true`; bước autograder mất 7,447 giây. |
| Commit/push/merge | Chưa thực hiện. Không tự nộp form hoặc gửi thông tin tới giảng viên. |
| Branch làm bài | Đã tạo và chuyển sang `dev-xanh-sm-lab02`; thay đổi chưa commit được giữ nguyên. |

## 2. Một lệnh kiểm tra trước khi nộp

Tại thư mục project trong terminal riêng của bạn đã export `GEMINI_API_KEY` hoặc `GOOGLE_API_KEY`:

```bash
conda activate AI20k
unset GEMINI_MODEL
python tools/check_submission.py --live
```

`unset GEMINI_MODEL` chỉ bỏ ghi đè model cũ, không đụng vào khóa; code sẽ dùng mặc định `gemini-3.5-flash-lite` đã kiểm thử. Nếu chưa có khóa, nhập kín theo hướng dẫn Ubuntu trong README. Không dán khóa vào chat hoặc lưu trong repository.

Lệnh chạy tests, kiểm tra file, kiểm tra tĩnh và autograder đầy đủ. Báo cáo tại `artifacts/submission-check.json`; `live_autograder: passed` và `passed: true` mới xác nhận mọi kiểm tra được yêu cầu đã đạt. Thư mục kết quả được Git bỏ qua. Không suy ra điểm nội dung môn học từ điểm autograder.

Lượt kiểm tra đã hoàn thành, không cần gọi API lại nếu code/cấu hình không đổi và không có lỗi mới. Autograder gốc có timeout 30 giây cho script gọi Gemini; lượt này hoàn thành trong giới hạn. Khi cần chạy lại, nếu timeout thì giữ kết quả để chẩn đoán, không sửa autograder hoặc bỏ ca thử để báo đạt. Chi phí và quota phụ thuộc project của người dùng, không được kiểm chứng bằng tests offline.

## 3. Branch cá nhân và commit chọn lọc

Branch hiện tại của bài này: **`dev-xanh-sm-lab02`**, đã được tạo và chuyển sang trong bước hoàn thiện. Kiểm tra bằng `git branch --show-current`. Nếu làm lại trên một bản clone chưa có branch này, tạo branch trước khi commit:

```bash
git switch -c dev-xanh-sm-lab02
```

Sau khi review và kiểm tra live đạt, người dùng có thể commit chọn lọc:

```bash
git add .gitignore README.md requirements.txt
git add 01-problem-scan.md 02-deep-dive-report.md 03-ai-log.md 04-workflow-diagram.pdf
git add 00-tieu-chi-lua-chon.md 05-danh-gia-uu-tien-du-an.md 06-huong-dan-nop-bai.md
git add starter-code/prompt_prototype.py tests tools
git diff --cached --stat
git commit -m "Complete Lab 02 Xanh SM prompt prototype and reports"
git push -u origin dev-xanh-sm-lab02
```

Các lệnh commit/push là hướng dẫn cho người dùng, chưa được AI thực hiện. Không thêm `.vscode/`, khóa, file `.env` hoặc kết quả cục bộ vào commit chỉ để có trạng thái Git sạch. Các file `00`, `05`, `06` là tài liệu bổ sung; không thay thế 4 file báo cáo/sơ đồ bắt buộc.

## 4. Phần nhóm và trưởng nhóm

Theo README gốc, trưởng nhóm review và tổng hợp báo cáo sau khi các thành viên nộp branch cá nhân. Chỉ đưa báo cáo/sơ đồ đã chọn vào `main`; không merge toàn branch cá nhân vì sẽ kéo theo code hoàn thiện. Việc chuyển branch và lấy báo cáo phải làm sau khi bài cá nhân đã được commit, tránh mang thay đổi chưa lưu sang `main`.

Chỉ trưởng nhóm điền form chính thức bằng họ tên và link repository. Cần ghi rõ model thay thế do model trong template trả 404, cùng việc các baseline vận hành đang là giả định. Không nhận đã khảo sát hiện trường, đo ROI hoặc được stakeholder phê duyệt khi chưa có bằng chứng.

## 5. Những việc không cần xây thêm để chốt bản mẫu hiện tại

Không cần dựng app hoàn chỉnh, tích hợp điều xe thật hoặc làm đủ pilot 30 ca để minh họa prototype lab. Dữ liệu thật, baseline tài chính, tập thử độc lập, đánh giá độ ổn định và tích hợp vận hành vẫn cần nếu muốn nâng điểm ưu tiên đầu tư hoặc triển khai thực tế. Đây là phần phát triển tiếp, không được ghi thành kết quả đã hoàn thành.
