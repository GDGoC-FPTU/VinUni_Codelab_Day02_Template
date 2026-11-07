# Lab 02 — Problem Deep-Dive Report: AI Media Crisis Intelligence & Legal Evidence Packaging
**Dự án:** Hệ Thống AI Phát Hiện Sớm Khủng Hoảng Truyền Thông, Kiểm Soát Tin Đồn Thất Thiệt & Đóng Gói Chứng Cứ Pháp Lý  
**Đơn vị phát triển:** Vin Smart Future — AI Product Engineering Unit  
**Đơn vị thụ hưởng:** Ban Truyền Thông & Ban Pháp Chế Tập đoàn Vingroup / VinFast  
**Tác giả:** Dương Quang Bảo (Duong Quang Bao)  
**Ngày thực hiện:** 08/11/2026  

---

## 🏛️ 1. Tổng quan Dự án

Trong môi trường số hiện đại, thông tin sai sự thật hoặc các chiến dịch điều hướng dư luận tiêu cực có chủ đích (**Ragebait**) có tốc độ lan truyền theo cấp số nhân. Với một tập đoàn đa ngành quy mô hàng đầu Việt Nam và niêm yết quốc tế như **Vingroup**, một tin đồn thất thiệt liên quan đến sức khỏe tài chính, chất lượng sản phẩm (an toàn pin xe điện VinFast, trục trặc phần mềm) hay đời tư lãnh đạo nếu không được phát hiện trong vòng **15–30 phút đầu tiên** có thể gây ra những hậu quả không thể đảo ngược:
- Ảnh hưởng trực tiếp và tiêu cực đến giá cổ phiếu (mã **VIC** trên HOSE và **VFS** trên NASDAQ).
- Bào mòn nghiêm trọng niềm tin của khách hàng và đối tác quốc tế đối với thương hiệu xe điện quốc gia.
- Đẩy doanh nghiệp hoàn toàn vào thế bị động trước bão dư luận truyền thông xã hội.

Các phương pháp Social Listening truyền thống dựa trên lọc từ khóa cố định (**Keyword matching**) đã hoàn toàn lỗi thời do ngôn ngữ mạng xã hội biến đổi liên tục với tính ẩn ý cao, nói bóng gió, sử dụng tiếng lóng (slang), teencode và meme. **Vin Smart Future** phát triển giải pháp AI giám sát thông minh thế hệ mới, kết hợp khả năng hiểu ngữ nghĩa sâu sắc của LLM và quy trình đóng gói chứng cứ pháp lý tự động.

---

# 🏗️ Phase 3 — DEEP-DIVE

## 3.1. Phân Tích Quy Trình Hiện Tại (Current-State Workflow Mapping)

Quy trình xử lý khủng hoảng thông tin và kiểm soát tin đồn hiện tại của Vingroup bao gồm 4 giai đoạn chính:

```text
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ Giai đoạn 1:    │      │ Giai đoạn 2:    │      │ Giai đoạn 3:    │      │ Giai đoạn 4:    │
│ [Thu thập       │ ───> │ [Phân loại &    │ ───> │ [Báo cáo &      │ ───> │ [Xử lý &        │
│ dữ liệu]        │      │ Đánh giá]       │      │ Cảnh báo]       │      │ Lưu trữ pháp lý]│
│                 │ 🔄   │                 │ 🔄   │                 │ 🔴   │                 │
│ Quét từ khóa    │      │ Đọc từng bài    │      │ Soạn văn bản    │      │ Chụp màn hình,  │
│ thủ công / cào  │      │ lọc nhiễu       │      │ cảnh báo lãnh   │      │ lập vi bằng tay,│
│ mạng xã hội     │      │ teencode/ẩn ý   │      │ đạo tập đoàn    │      │ gom hồ sơ nộp CA│
│ ⏱ 25 - 40 phút  │ 🔴   │ ⏱ 20 - 30 phút  │ 🔴   │ ⏱ 10 - 15 phút  │      │ ⏱ 1 - 3 NGÀY    │
└─────────────────┘      └─────────────────┘      └─────────────────┘      └─────────────────┘
```

* **Tổng thời gian từ lúc tin xuất hiện đến khi báo cáo lãnh đạo (AHT):** **60 - 85 phút** (vượt xa "khung giờ vàng" 15-30 phút).
* **Thời gian hoàn tất hồ sơ pháp lý:** **1 - 3 ngày làm việc**.
* **Các điểm chuyển giao (🔄 Handoffs):**
  1. *Handoff 1 (Giai đoạn 1 ──> 2):* Đội ngũ Social Listening kết xuất danh sách bài viết thô gửi cho Chuyên viên Phân tích Truyền thông.
  2. *Handoff 2 (Giai đoạn 2 ──> 3):* Chuyên viên Phân tích gửi email tóm tắt cảnh báo lên Giám đốc Truyền thông.
  3. *Handoff 3 (Giai đoạn 3 ──> 4):* Giám đốc Truyền thông chuyển giao vụ việc sang Ban Pháp chế để thu thập tài liệu tố tụng.
* **Các điểm nghẽn nghiêm trọng (🔴 Bottlenecks):**
  - **Bottleneck 1 (Thu thập & Phát hiện chậm):** Dùng bộ lọc từ khóa đơn giản nên bỏ sót hoàn toàn các bài viết mang tính châm biếm, dùng từ lóng nói giảm nói tránh hoặc video ngắn trên TikTok/Reels. Phát hiện muộn sau 30-45 phút khi bài viết đã có hàng ngàn lượt chia sẻ.
  - **Bottleneck 2 (Nhiễu thông tin 80%):** Hơn 80% dữ liệu cào về là bài viết bán hàng rong, spam, hoặc nhắc đến từ khóa nhưng không liên quan đến uy tín doanh nghiệp, khiến chuyên viên kiệt sức khi phải rà soát bằng mắt thường.
  - **Bottleneck 3 (Đóng gói chứng cứ thủ công):** Chuyên viên pháp lý phải click vào từng link, chụp ảnh màn hình, ghi lại URL, ID tài khoản, mốc thời gian và lập bảng Excel thủ công. Nhiều trường hợp chủ tài khoản đã xóa bài hoặc khóa nick trước khi kịp lập vi bằng, làm mất dấu vết chứng cứ tố tụng.

---

## 3.2. Bảng Mô Tả Bài Toán Chi Tiết (6-Field Problem Statement)

| Trường thông tin (Field) | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | - **Giám đốc Truyền thông (PR Director):** Chịu trách nhiệm bảo vệ danh tiếng thương hiệu và đưa ra quyết định xử lý khủng hoảng.<br>- **Chuyên viên Ban Pháp chế (Legal Counsel):** Phụ trách lập hồ sơ chứng cứ pháp lý, vi bằng gửi cơ quan chức năng hoặc văn phòng luật sư.<br>- **Chuyên viên Giám sát Thông tin Mạng (Social Media Monitor):** Vận hành hệ thống theo dõi 24/7. |
| **2. Current Workflow** | **[Thu thập dữ liệu] ➡️ [Phân loại & Đánh giá] ➡️ [Báo cáo & Cảnh báo] ➡️ [Xử lý & Lưu trữ pháp lý]**.<br>Sử dụng công cụ social listening dựa trên keyword matching kết hợp nhân sự đọc lướt bằng tay; soạn email báo cáo và chụp màn hình bằng công cụ thủ công để lưu trữ. |
| **3. Bottleneck** | - Phát hiện chậm trễ ngoài khung giờ vàng (30-45 phút).<br>- Tỷ lệ nhiễu thông tin cực cao (80% dữ liệu rác).<br>- Bỏ sót các chiến dịch Ragebait dùng ngôn từ ẩn ý, tiếng lóng, mỉa mai.<br>- Gom hồ sơ và lập vi bằng pháp lý thủ công mất từ 1 đến 3 ngày. |
| **4. Business Impact** | - **SLA Fail:** Đẩy doanh nghiệp hoàn toàn vào thế bị động trước dư luận mạng xã hội.<br>- **Error Rate cao:** Gây lãng phí nghiêm trọng nguồn lực vận hành khi chuyên viên mất 80% thời gian xử lý tin rác.<br>- **Thiệt hại tài chính trực tiếp:** Ảnh hưởng tiêu cực đến giá cổ phiếu VIC/VFS, giảm doanh số bán xe và tốn kém hàng tỷ đồng cho các chiến dịch dập lửa khủng hoảng. |
| **5. Success Metric** | - **Thời gian phát hiện bài viết vi phạm:** Giảm từ > 30-45 phút xuống **dưới 10 phút** kể từ thời điểm đăng tải.<br>- **Tỷ lệ lọc nhiễu thông tin:** Tự động lọc sạch và giảm **80%** lượng tin rác.<br>- **Tốc độ phản ứng & cảnh báo khẩn cấp:** **Dưới 2 phút** gửi thông báo kèm kịch bản draft tới Giám đốc Truyền thông.<br>- **Thời gian gom hồ sơ chứng cứ pháp lý:** Rút ngắn từ 2-3 ngày xuống **dưới 1 ngày** (xuất file hoàn chỉnh chỉ trong vài cú click chuột). |
| **6. Operational Boundary** | **Hệ thống ĐƯỢC PHÉP làm:**<br>1. Tự động quét và cào dữ liệu công khai trên mạng xã hội và web (Public API / Public Web Crawling).<br>2. Tự động tiền xử lý dữ liệu thô: làm sạch triệt để lỗi BOM (Byte Order Mark), ký tự lạ, chuẩn hóa teencode và ngôn ngữ mạng.<br>3. Tự động gom cụm (Clustering) các bài viết trùng lặp nội dung hoặc cùng một kịch bản seeding.<br>4. Tự động xuất file hồ sơ bằng chứng đầy đủ: URL, ID người dùng, nội dung nguyên bản, mốc thời gian (timestamp) và ảnh chụp màn hình tự động.<br>5. Mọi nội dung khuyến nghị kịch bản xử lý BẮT BUỘC gắn nhãn tiền tố `[DRAFT_ONLY]`.<br><br>**Hệ thống TUYỆT ĐỐI CẤM (Ranh giới cấm nghiêm ngặt):**<br>1. **Tuyệt đối không tự động thực hiện các hành động phản hồi ra bên ngoài:** Không tự động gỡ bài viết vi phạm, không tự động comment đính chính, tranh cãi hoặc gửi tin nhắn đe dọa/cảnh cáo tài khoản người dùng.<br>2. **Tuân thủ pháp luật:** Tuyệt đối không sử dụng các biện pháp tấn công mạng hoặc biện pháp trái pháp luật để xâm nhập các hội nhóm kín (Private Groups) hoặc tin nhắn riêng tư (Inbox).<br><br>**Điểm kiểm soát con người bắt buộc (Human-in-the-Loop - HITL):**<br>- *Phê duyệt kịch bản:* Khi AI Agent kích hoạt cảnh báo "Nghiêm trọng", Giám đốc Truyền thông (Con người) phải là người duy nhất quyết định phương án hành động (Yêu cầu nền tảng gỡ bài, ban hành thông cáo báo chí, hay tiến hành khởi kiện).<br>- *Xác minh chứng cứ cuối cùng:* Chuyên viên Pháp chế (Con người) kiểm tra lại tính hợp pháp, chuỗi bảo quản chứng cứ số và độ chính xác của tệp dữ liệu do AI đóng gói trước khi chính thức nộp lên Cơ quan Công an hoặc Văn phòng Luật sư. |

---

## 3.3. Thiết Kế Quy Trình Tương Lai & Khung Phù Hợp AI (Future-State Flow & AI Fit)

### 📊 Phân tích Khung Phù Hợp AI (AI-Fit Matrix)

| Khâu nghiệp vụ | Công nghệ áp dụng | Lý do kỹ thuật & Biện luận |
|---|---|---|
| **Cào dữ liệu công khai & Làm sạch BOM/Ký tự lạ** | ⚙️ **Deterministic Data Pipeline (Python Scraper & Regex)** | Các thao tác cào web công khai, xử lý encoding UTF-8/BOM, tách teencode từ điển là quy tắc tất định, tốc độ tính bằng mili-giây, không cần tốn token LLM. |
| **Gom cụm các bài viết trùng lặp (Seeding Clustering)** | 🧮 **Machine Learning Clustering (Sentence-Transformers & DBSCAN/K-Means)** | Gom cụm các bài viết có nội dung tương đồng từ hàng trăm tài khoản clone/bot để đo lường mức độ bùng phát của chiến dịch mà không cần đọc thủ công từng bài. |
| **Đánh giá mức độ độc hại, ẩn ý & Chấm điểm rủi ro** | 🔵 **LLM Feature (Gemini 3.8 Flash)** | Khả năng đọc hiểu ngữ cảnh sâu sắc, nhận diện mỉa mai (sarcasm), phân tích mức độ xâm hại uy tín thương hiệu VinFast/Vingroup và phân cấp mức độ nguy cơ (Low / Medium / High / Critical). |
| **Tự động chụp màn hình & Đóng gói bằng chứng** | 🤖 **Automated Evidence Agent (Headless Playwright Browser)** | Tự động hóa chụp full-page ảnh màn hình, trích xuất ID, URL, timestamp và xuất tệp ZIP hồ sơ pháp lý chuẩn hóa. |
| **Phê duyệt kịch bản ứng phó & Nộp hồ sơ tố tụng** | 🟢 **Human-in-the-Loop (PR Director & Legal Counsel)** | Quyền quyết định pháp lý và phát ngôn công chúng luôn thuộc về con người. AI chỉ đóng vai trò hỗ trợ phân tích và chuẩn bị tư liệu. |

---

### 🔄 Sơ đồ Quy trình Tương lai (Future-State Workflow)

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [Đầu vào: Mạng xã hội công khai - Facebook, TikTok, YouTube, Diễn đàn] │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │
                                     ▼
      ┌────────────────────────────────────────────────────────────┐
      │ ⚙️ Bước 1: Data Pipeline Tự động (Public Scraping & Clean): │
      │ - Cào dữ liệu bài viết, bình luận công khai                │
      │ - Xử lý triệt để lỗi BOM, ký tự lạ, chuẩn hóa teencode    │
      │ - 🧮 Gom cụm (Clustering) các bài viết seeding trùng lặp   │
      └──────────────────────────────┬─────────────────────────────┘
                                     │
                                     ▼
      ┌────────────────────────────────────────────────────────────┐
      │ 🔵 Bước 2: AI Semantic Analysis & Risk Scoring (Gemini):   │
      │ - Phân tích ngữ cảnh ẩn ý, sắc thái mỉa mai, độ công kích  │
      │ - Lọc bỏ 80% tin rác/nhiễu                                 │
      │ - Đánh giá thang điểm rủi ro thương hiệu (Scale 1-10)     │
      └──────────────────────────────┬─────────────────────────────┘
                                     │
                ┌────────────────────┴────────────────────┐
                ▼                                         ▼
      [Rủi ro Thấp/Trung bình]                  [Rủi ro Cao / Nghiêm trọng]
                │                                         │
                ▼                                         ▼
┌──────────────────────────────────────┐  ┌──────────────────────────────────────┐
│ Lưu trữ dữ liệu vào kho phân tích     │  │ 🚨 Cảnh báo Khẩn cấp (< 2 phút):     │
│ Báo cáo định kỳ thường nhật          │  │ Bắn Telegram/SMS cho PR Director     │
└──────────────────────────────────────┘  │ Tự động chụp màn hình & lưu chứng cứ │
                                          └──────────────────┬───────────────────┘
                                                             │
                                                             ▼
                                          ┌──────────────────────────────────────┐
                                          │ 🔵 AI Step: Soạn Thảo Kịch Bản Nháp  │
                                          │ BẮT BUỘC TIỀN TỐ [DRAFT_ONLY]        │
                                          │ Xuất tệp hồ sơ bằng chứng số hóa     │
                                          └──────────────────┬───────────────────┘
                                                             │
                                                             ▼
                                          ┌──────────────────────────────────────┐
                                          │ 🟢 HITL Gate 1: Giám đốc Truyền thông│
                                          │ Phê duyệt kịch bản: Gỡ bài / Ra TCBC │
                                          │ TUYỆT ĐỐI CẤM AI TỰ ĐỘNG PHẢN HỒI    │
                                          └──────────────────┬───────────────────┘
                                                             │
                                                             ▼
                                          ┌──────────────────────────────────────┐
                                          │ 🟢 HITL Gate 2: Chuyên viên Pháp chế │
                                          │ Kiểm tra tính hợp pháp & toàn vẹn    │
                                          │ của tệp hồ sơ trước khi nộp Công an  │
                                          └──────────────────┬───────────────────┘
                                                             │
                                                             ▼
                                          ┌──────────────────────────────────────┐
                                          │ ↩️ Fallback Circuit Breaker:          │
                                          │ Khi LLM timeout hoặc sự cố mạng,     │
                                          │ fallback về Rule-based Alert cứng    │
                                          │ dựa trên số lượng tương tác đột biến │
                                          └──────────────────────────────────────┘
```

---

# 🏁 Phase 5 — EVALUATE: Đánh Giá & Quyết Định

### 📋 AI Readiness Checklist

- [x] **Dữ liệu mẫu/Logs sạch để huấn luyện & thử nghiệm:** Ban Truyền thông Vingroup đã có kho lưu trữ lịch sử hơn 10.000 bài viết từ các vụ việc truyền thông thực tế (tin đồn về trạm sạc, pin xe, tài chính) để làm tập dữ liệu chuẩn hóa (Ground truth benchmark).
- [x] **Rủi ro AI sai được kiểm soát hoàn toàn:** 
  - Khóa chặt ranh giới cấm: AI không có quyền hạn tương tác mạng xã hội ra bên ngoài (không API post/delete/comment).
  - Thẻ `[DRAFT_ONLY]` đảm bảo mọi bản nháp phải qua tay Giám đốc Truyền thông phê duyệt.
  - Ban Pháp chế giữ chốt chặn cuối cùng thẩm định chứng cứ pháp lý.
- [x] **Stakeholders sẵn sàng thay đổi quy trình:** Cả Ban Truyền thông và Ban Pháp chế đều mong muốn có công cụ giải phóng họ khỏi công việc cào link và chụp ảnh màn hình thủ công, giúp bảo vệ uy tín tập đoàn kịp thời trong khung giờ vàng 15-30 phút.

---

### 🗳️ Quyết Định Đầu Tư Của Ban Giám Đốc Vin Smart Future:

**LỰA CHỌN:** **[x] GO (BẮT ĐẦU XÂY DỰNG PROTOTYPE)**

### 💡 Lý giải Quyết định (Justification):
1. **Bảo vệ giá trị vốn hóa và thương hiệu hàng chục tỷ USD:** Chi phí phát triển và vận hành hệ thống AI này chỉ chiếm một phần rất nhỏ (dưới 0.01%) so với thiệt hại tài chính nếu giá cổ phiếu VIC/VFS biến động tiêu cực do tin đồn thất thiệt không được dập tắt kịp thời.
2. **Nâng cao năng suất lao động đột phá:** Giảm 80% thời gian xử lý dữ liệu rác, rút ngắn thời gian phát hiện từ 40 phút xuống dưới 10 phút, và giảm thời gian đóng gói chứng cứ pháp lý từ 3 ngày xuống dưới 1 ngày.
3. **Tuân thủ pháp luật và an toàn tuyệt đối:** Hệ thống thiết lập ranh giới rõ ràng: chỉ thu thập dữ liệu công khai, không xâm nhập thông tin riêng tư, không tự động phát ngôn ra bên ngoài và luôn đặt con người ở vị trí người duyệt và chịu trách nhiệm cao nhất.
