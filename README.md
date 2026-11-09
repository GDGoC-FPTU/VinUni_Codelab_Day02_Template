# 📖 Hướng Dẫn Học Viên (Student Guide) — Lab 02: AI Product Scoping

## Bài cá nhân Vinhomes — Lê Việt Khoa

Xem [đánh giá và checklist bài cá nhân](05-individual-review.md),
[Scan & 3 Cards](01-problem-scan.md), [Deep Dive](02-deep-dive-report.md),
[AI Log](03-ai-log.md) và [sơ đồ workflow](04-workflow-diagram.png).
Nội dung mới kế thừa báo cáo Word Phase 1–2, các số liệu vẫn là giả định.

Kiểm tra code không cần API key:

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests
```

Chạy 3 ca tấn công và 6 ca đối chứng qua OpenRouter (cần `OPENROUTER_API_KEY`):

```powershell
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py --suite all --report evidence/live-results.json
```

Xem [bằng chứng kiểm tra](evidence/verification.md). Unit test dùng phản hồi giả lập;
không thay thế chứng cứ chạy API thật. Bộ chấm gốc vẫn có các tiêu chí riêng cho Gemini/Xanh SM.

---

Tài liệu này hướng dẫn chi tiết cách thiết lập môi trường lập trình Python, cấu hình API Key, quy trình phân nhánh Git làm việc nhóm và chuẩn bị sản phẩm nộp bài cho **Lab 02: AI Product Scoping (Vin Smart Future)**.

---

## 🛠️ 1. Hướng dẫn thiết lập Môi trường ảo (`.venv`)

Môi trường ảo (virtual environment) giúp cô lập các thư viện của dự án này, tránh xung đột với các phiên bản thư viện khác cài trên máy của bạn.

### 💻 Bước 1: Tạo môi trường ảo
Mở terminal tại thư mục gốc của dự án (`VinUni_Day02-AI-Product-Lab`) và chạy lệnh tương ứng với hệ điều hành của bạn:

*   **Windows (PowerShell hoặc CMD):**
    ```powershell
    python -m venv .venv
    ```
*   **macOS / Linux:**
    ```bash
    python3 -m venv .venv
    ```

### 🔌 Bước 2: Kích hoạt (Activate) môi trường ảo
Bạn phải kích hoạt môi trường ảo mỗi khi mở terminal mới trước khi chạy code.

*   **Windows (PowerShell):**
    ```powershell
    .venv\Scripts\Activate.ps1
    ```
    *(Nếu gặp lỗi "Execution Policy", hãy chạy lệnh: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` rồi kích hoạt lại).*
*   **Windows (CMD):**
    ```cmd
    .venv\Scripts\activate.bat
    ```
*   **macOS / Linux:**
    ```bash
    source .venv/bin/activate
    ```
*   **Dấu hiệu kích hoạt thành công:** Ở đầu dòng lệnh của terminal xuất hiện ký hiệu `(.venv)`.

### 📥 Bước 3: Cài đặt thư viện cần thiết
Phiên bản `starter-code/prompt_prototype.py` dùng **OpenRouter API**, mặc định gọi **Gemini 2.5 Flash**. Cài thư viện một lần trong `.venv` của dự án:
```bash
python -m pip install -r requirements.txt
```

Không cần tạo lại `.venv` hoặc cài lại thư viện mỗi lần chạy. Code dùng `httpx` gọi HTTP trực tiếp; không cần SDK Groq hay Google. Lệnh trên không tự gỡ thư viện cũ.

---

## 🔑 2. Thiết lập và sử dụng OpenRouter API

### Tạo API key (lần đầu)

1. Đăng nhập [OpenRouter](https://openrouter.ai/).
2. Mở [API Keys của workspace](https://openrouter.ai/workspaces/default/keys), tạo API key và sao chép giá trị key.
3. Đặt key trong terminal như bên dưới. **Không ghi key vào file Python, README hoặc commit lên Git.**

Model mặc định `google/gemini-2.5-flash` có tính phí; kiểm tra số dư và hạn mức key trong tài khoản trước khi chạy. Xem [trang model](https://openrouter.ai/google/gemini-2.5-flash) và [tài liệu lỗi, gồm lỗi thiếu credit](https://openrouter.ai/docs/api/reference/errors-and-debugging). Không tự đổi sang model khác khi hết credit.

### Chạy trên Windows PowerShell

Mở terminal tại thư mục gốc của dự án, thay `KEY_OPENROUTER_CUA_BAN` bằng key vừa tạo:

```powershell
$env:OPENROUTER_API_KEY="KEY_OPENROUTER_CUA_BAN"
.\.venv\Scripts\python.exe starter-code/prompt_prototype.py --suite all --report evidence/live-results.json
```

Lệnh trên dùng Python trong `.venv` trực tiếp nên không cần activate. Biến `$env:OPENROUTER_API_KEY` chỉ áp dụng cho terminal hiện tại và các tiến trình con. Các biến `GROQ_API_KEY`, `GEMINI_API_KEY`, `GOOGLE_API_KEY` không được dùng. Không tự đọc `.env`.

Trên CMD:

```cmd
.venv\Scripts\activate.bat
set OPENROUTER_API_KEY=KEY_OPENROUTER_CUA_BAN
python starter-code/prompt_prototype.py
```

Trên macOS/Linux:

```bash
source .venv/bin/activate
export OPENROUTER_API_KEY="KEY_OPENROUTER_CUA_BAN"
python starter-code/prompt_prototype.py
```

Kiểm tra biến môi trường đã có giá trị mà không in key:

```bash
python -c "import os; print('API Key status: OK' if os.getenv('OPENROUTER_API_KEY') else 'API Key status: MISSING')"
```

`OK` chỉ xác nhận có giá trị, chưa xác nhận key hợp lệ hoặc có quyền gọi API.

### Model, prompt và kết quả

- Model mặc định là `google/gemini-2.5-flash`, khớp tên model trong worksheet, được gọi **qua OpenRouter** bằng key OpenRouter. Không cần key Google. Tham khảo [trang model](https://openrouter.ai/google/gemini-2.5-flash).
- Nếu cần đổi model, đặt `$env:OPENROUTER_MODEL="ID_MODEL_TREN_OPENROUTER"` trước khi chạy. Đổi model có thể làm khác yêu cầu worksheet; báo cáo JSON ghi model đã yêu cầu. Endpoint cố định: `https://openrouter.ai/api/v1/chat/completions`.
- Sửa vai trò/quy tắc ở `SYSTEM_PROMPT`; sửa tình huống cụ thể tại từng trường `input` trong `ADVERSARIAL_TESTS` của `starter-code/prompt_prototype.py`.
- Chương trình gọi API cho từng ca thử, nhận văn bản nguyên gốc, kiểm tra thẻ `[DRAFT_ONLY]`, cấu trúc JSON và nhãn mong đợi, rồi in `PASS` hoặc `FAIL`. Không tự thêm thẻ hoặc sửa câu trả lời để làm ca thử đạt.
- `FAIL` là câu trả lời chưa đạt yêu cầu kiểm thử; khác với lỗi gọi API. Khi đó xem kết quả thực tế và điều chỉnh prompt nếu cần.

### Xử lý lỗi

| Thông báo | Cách kiểm tra |
| :--- | :--- |
| Thiếu `OPENROUTER_API_KEY` | Đặt key trong chính terminal đang chạy chương trình. |
| Thiếu thư viện `httpx` | Chạy `python -m pip install -r requirements.txt` trong `.venv`. |
| Key chứa Unicode/khoảng trắng hoặc vẫn là giá trị mẫu | Sao chép **giá trị key**, không phải tên mô tả key, từ OpenRouter. Thay toàn bộ `KEY_OPENROUTER_CUA_BAN` bằng key thật, không thêm dấu cách/xuống dòng. |
| `UnicodeEncodeError` | Chương trình hiển thị encoding và vị trí lỗi, không in nội dung gây lỗi để tránh lộ key. Kiểm tra lại key và các header tùy chỉnh; không cần xóa dấu tiếng Việt khỏi prompt. |
| HTTP 401 | Kiểm tra key OpenRouter có đúng, còn hiệu lực và không dán kèm khoảng trắng. |
| HTTP 402 | Kiểm tra credit và hạn mức chi tiêu của key/tài khoản OpenRouter. |
| HTTP 403 | Đọc thông báo chi tiết, kiểm tra quyền truy cập và chính sách của key/model. |
| HTTP 404 | Kiểm tra `OPENROUTER_MODEL` và danh sách model đang được hỗ trợ. |
| HTTP 429 | Xem hạn mức và thời gian chờ; chạy lại sau khi hạn mức được phục hồi. |

Tham khảo [Quickstart](https://openrouter.ai/docs/quickstart) và [mã lỗi OpenRouter](https://openrouter.ai/docs/api/reference/errors-and-debugging). Chương trình che key trong lỗi, kiểm tra cả trường `error` khi HTTP trả 200, và không tự retry. Timeout kết nối/đọc là 30 giây; không phải giới hạn tổng thời gian cả bộ ca thử.

**Lưu ý khi nộp bài:** Model mặc định là Gemini 2.5 Flash theo worksheet, nhưng `autograder/autograder.py` vẫn kiểm tra SDK Gemini trực tiếp và quy tắc của bài mẫu điều phối xe. Gọi Gemini qua OpenRouter không tự làm các kiểm tra đó đạt; cần giảng viên thống nhất tiêu chí cho Vinhomes/OpenRouter. Bản chuyển đổi không sửa bộ chấm.

---

## 👥 3. Quy định Làm bài và Nộp bài Nhóm (Group Workflow & Git Rules)

Môn học này áp dụng mô hình cộng tác nhóm kết hợp chấm điểm cá nhân và chấm điểm nhóm thông qua Git Branching.

### 📌 Quy định chung:
1. **Tổ chức Nhóm & Repository:**
   * Mỗi nhóm gồm **4 đến 6 thành viên**.
   * **Trưởng nhóm** chịu trách nhiệm khởi tạo Repository chung của nhóm và **thêm (add) tất cả các thành viên vào danh sách Contributors** với quyền write.
   * Tất cả thành viên (bao gồm cả Nhóm trưởng) đều phải thực hiện làm bài trên **Branch riêng (nhánh cá nhân)** của mình.

2. **Bài tập Code (`.py`) — Chấm điểm CÁ NHÂN:**
   * Mỗi thành viên tự hoàn thành file code `.py` cá nhân của mình.
   * Push file `.py` lên **branch cá nhân**.
   * 🛑 **LƯU Ý QUAN TRỌNG:** **KHÔNG merge file code (`.py`) vào branch `main`**. Điểm nhóm sẽ **KHÔNG** tính cho các file code. Phần code `.py` sẽ được hệ thống/giảng viên chấm điểm độc lập trên từng branch cá nhân.

3. **Bài tập Báo cáo/Tài liệu (`.md`) — Chấm điểm NHÓM:**
   * Mỗi bạn tự hoàn thiện các file `.md` cá nhân trên branch riêng và push bài lên branch cá nhân đó.
   * Sau khi **TẤT CẢ** các thành viên trong nhóm đã hoàn thành và push bài lên branch cá nhân, **Trưởng nhóm sẽ tổ chức họp/bàn luận với các thành viên** để review và chọn ra các ý tưởng hay nhất, file `.md` chất lượng nhất.
   * Trưởng nhóm (hoặc đại diện nhóm) tổng hợp, chỉnh sửa và **merge các file `.md` xuất sắc nhất vào branch `main`**. Branch `main` là căn cứ duy nhất để tính điểm báo cáo chung cho toàn nhóm.

4. **Điền Form Nộp bài chính thức:**
   * 🛑 **QUAN TRỌNG:** Khi điền form nộp bài, **CHỈ CẦN TRƯỞNG NHÓM điền Họ tên và link Repository của nhóm**. 
   * Các thành viên khác **VUI LÒNG KHÔNG ĐIỀN THÊM FORM** để tránh trùng lặp thông tin nộp bài.

---

## 🔄 4. Hướng dẫn chi tiết Quy trình thao tác Git (Step-by-Step)

### 👑 Bước 1: Dành cho Trưởng nhóm (Tạo Repo & Thêm Thành viên)
1. Tạo repo mới trên GitHub (hoặc accept link GitHub Classroom).
2. Vào tab **Settings** > **Collaborators** (hoặc **Manage access**) > Click **Add people**.
3. Nhập username GitHub hoặc email của 4-6 thành viên để mời họ làm Contributors.
4. Gửi link repo cho các thành viên clone về máy.

### 👤 Bước 2: Dành cho TẤT CẢ Thành viên (Tạo Branch cá nhân)
Sau khi clone repo về máy, mở terminal tại thư mục dự án và tạo nhánh riêng theo tên/mã sinh viên của bạn:

```bash
# Clone repo chung về máy
git clone <URL_REPOSITORY_CUA_NHOM>
cd VinUni_Codelab_Day02

# Tạo và chuyển sang branch cá nhân (Ví dụ: nguyenvana hoặc dev-student1)
git checkout -b <ten-cua-ban>
```

### 💻 Bước 3: Làm bài & Push lên Branch cá nhân
Thực hiện chỉnh sửa code `.py` và hoàn thiện các file `.md` trên branch cá nhân. Sau đó thực hiện commit và push:

```bash
# Kiểm tra các file đã chỉnh sửa
git status

# Thêm tất cả file đã làm vào staging
git add .

# Commit bài làm cá nhân
git commit -m "Feat: Complete individual assignment by <Ten-Cua-Ban>"

# Push bài làm lên branch cá nhân (KHÔNG push trực tiếp lên main)
git push origin <ten-cua-ban>
```

### 🤝 Bước 4: Thảo luận nhóm & Merge file `.md` vào `main` (Dành cho Trưởng nhóm)
Sau khi tất cả thành viên đã push branch cá nhân lên GitHub:

1. **Thảo luận:** Trưởng nhóm và các thành viên họp review các branch, thảo luận chọn ra bài viết `.md` (Problem Scan, Deep Dive Report, AI Log) xuất sắc nhất.
2. **Merge file `.md` vào `main`:**
   ```bash
   # Trưởng nhóm chuyển về branch main và cập nhật mới nhất
   git checkout main
   git pull origin main

   # Lấy nội dung các file .md được chọn từ branch thành viên (Ví dụ từ branch nguyenvana)
   git checkout nguyenvana -- 01-problem-scan.md 02-deep-dive-report.md 03-ai-log.md 04-workflow-diagram.png

   # Commit nội dung .md đã chắt lọc cho nhóm
   git commit -m "Chore: Select and merge best markdown reports into main"

   # Push main lên GitHub để nộp bài nhóm
   git push origin main
   ```
3. 🛑 **Nhắc lại:** **KHÔNG** thực hiện checkout hay merge file `.py` vào branch `main`. File `.py` chỉ nằm tại branch riêng của từng thành viên.

### 📝 Bước 5: Điền Form Nộp bài (Dành riêng cho Trưởng nhóm)
* **Duy nhất Trưởng nhóm** mở Form nộp bài của môn học, điền **Họ và tên Trưởng nhóm** cùng **Link Repository GitHub** của nhóm.
* Các thành viên còn lại **tuyệt đối không điền form** này nữa.

---

## 📝 5. Hướng dẫn chi tiết cách hoàn thiện các file nộp bài

### 📄 1. File `01-problem-scan.md` (Ý tưởng cá nhân & Nhóm)
File này thể hiện tư duy tìm kiếm bài toán thực tế.
*   **Cách làm:** Copy và hoàn thiện nội dung của **Phase 1 (SCAN)** và **Phase 2 (QUICK-ASSESS)** từ file `01-worksheet.md`.
*   **Yêu cầu nội dung:**
    *   **Bảng quét cơ hội (SCAN):** Điền tối thiểu 5 bài toán thực tế thuộc các công ty thành viên Vingroup.
    *   **3 Quick Problem Cards:** Điền đầy đủ thông tin cho 3 bài toán tiềm năng nhất (Actor, Quy trình hiện tại, Bottleneck, AI Solution, Metric...).

### 📄 2. File `02-deep-dive-report.md` (Báo cáo Phân tích sâu)
Báo cáo phân tích sâu dự án AI mà nhóm/cá nhân lựa chọn.
*   **Cách làm:** Copy và hoàn thiện nội dung của **Phase 3 (DEEP-DIVE)** và **Phase 5 (EVALUATE)** từ file `01-worksheet.md`.
*   **Yêu cầu nội dung:**
    *   **Problem Statement (6-field):** Điền đầy đủ 6 trường thông tin cho bài toán đã chọn.
    *   **Future-State Flow & AI Fit:** Mô tả quy trình tương lai có tích hợp AI (Rule, LLM, Agentic Loop), cơ chế Human-in-the-loop và Fallback.
    *   **Evaluate:** Đánh giá độ sẵn sàng qua bảng Checklist và đưa ra quyết định GO / NOT YET / NO-GO.

### 🖼️ 3. File `04-workflow-diagram.png` (hoặc `.pdf`)
Sơ đồ trực quan hóa quy trình vận hành hiện tại.
*   **Cách làm:** Vẽ sơ đồ quy trình hiện tại (Current-State Workflow) lên giấy/bảng trắng hoặc công cụ vẽ trực tuyến.
*   **Yêu cầu:** Thể hiện rõ các bước tuần tự, điểm chuyển giao (🔄 **Handoff**), thời gian xử lý và điểm nghẽn cổ chai (🔴 **Bottleneck**).

### 📄 4. File `03-ai-log.md` (Nhật ký tương tác AI)
*   **Cách làm:** Viết bài tự luận phản ánh quá trình sử dụng AI (ChatGPT, Gemini, Claude...) làm trợ lý đồng hành.
*   **Yêu cầu:** Nêu rõ AI giúp gì, AI trả lời sai/hallucination ở đâu, và bạn đã sửa prompt/ranh giới ra sao để đạt kết quả chuẩn.

### 🐍 5. File Code `.py` (Bài tập Code Cá nhân)
*   **Vị trí:** Lưu tại file `.py` cá nhân của bạn (ví dụ: `starter-code/prompt_prototype.py` hoặc file `.py` được yêu cầu).
*   **Lưu ý:** Chỉ nộp trên branch cá nhân (`git push origin <ten-cua-ban>`), không merge vào `main`.

---

## 📊 6. Tóm Tắt Quy Trình Chấm Điểm & Nộp Bài (Summary Rubric)

| Loại Bài Tập / Thao Tác | Định Dạng File / Hành Động | Vị Trí Nộp | Người Thực Hiện | Tiêu Chí Tính Điểm |
| :--- | :--- | :--- | :--- | :--- |
| **Code Python** | `.py` | Branch Cá nhân (`<ten>`) | Từng thành viên | **Điểm CÁ NHÂN** (chấm trên branch riêng) |
| **Báo cáo / Document** | `.md`, `.png` | Branch `main` (Sau khi chọn lọc & merge) | Cả nhóm / Trưởng nhóm đại diện merge | **Điểm NHÓM** (chấm trên branch `main`) |
| **Form Nộp Bài** | Form trực tuyến | Link Google Form / LMS | **Chỉ DUY NHẤT Trưởng nhóm điền** | Ghi nhận/tổng hợp bài nộp của nhóm |
