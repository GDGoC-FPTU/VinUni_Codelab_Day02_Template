# Lab 02 — Problem Scan & Quick Assessments
**Học viên:** Dương Quang Bảo (Duong Quang Bao)  
**Vai trò:** AI Product Engineer — Vin Smart Future (Vingroup)  
**Đơn vị phối hợp:** Ban Truyền Thông & Ban Pháp Chế Tập đoàn Vingroup / VinFast  

---

## 🏛️ 1. Bối cảnh & Mục tiêu

Tại **Vin Smart Future**, sứ mệnh của chúng tôi là áp dụng công nghệ Trí tuệ Nhân tạo thực chất, giải quyết trực tiếp các điểm nghẽn vận hành (Operational Bottlenecks) thực tế của các công ty thành viên Vingroup. 

Trong kỷ nguyên số, không gian mạng chứng kiến sự lan truyền theo cấp số nhân của tin đồn thất thiệt, tin giả (fake news) và các chiến dịch kích động tiêu cực có chủ đích (Ragebait). Đối với một tập đoàn đa ngành lớn như Vingroup, một thông tin xuyên tạc liên quan đến tài chính, chất lượng kỹ thuật xe ô tô VinFast hay danh dự lãnh đạo nếu không được phát hiện trong vòng 15–30 phút đầu tiên có thể gây thiệt hại hàng nghìn tỷ đồng về giá trị vốn hóa, bào mòn uy tín thương hiệu và làm gián đoạn chuỗi cung ứng sản xuất.

Tài liệu này ghi nhận quá trình **Quét cơ hội (SCAN)** và **Đánh giá sơ bộ (QUICK-ASSESS)** để xác lập bài toán có mức độ ảnh hưởng chiến lược cao nhất: **Hệ thống AI Phát Hiện Sớm Khủng Hoảng Truyền Thông, Kiểm Soát Tin Đồn Thất Thiệt & Đóng Gói Chứng Cứ Pháp Lý**.

---

# 🔍 Phase 1 — SCAN: Quét Cơ Hội Qua 4 Lenses

Áp dụng 4 lăng kính nghiệp vụ:
1. **Lặp lại (Repetitive):** Tần suất cao, logic xử lý tương tự nhau mỗi ngày.
2. **Tốn thời gian (Time-consuming):** Thao tác thủ công ngốn nhiều giờ làm việc của nhân viên.
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ hiện tại bị rập khuôn, thiếu khả năng hiểu ngữ cảnh ẩn dụ/ngôn ngữ mạng xã hội biến đổi liên tục.
4. **Pain từ người khác (Stakeholder Pain):** Gây thiệt hại trực tiếp đến khách hàng, cổ đông, uy tín thương hiệu và nhân sự vận hành.

### 📋 Bảng Quét 6 Bài Toán Nghiệp Vụ Tại Vingroup:

| # | Đơn vị thành viên | Lens áp dụng | Mô tả bài toán & Điểm nghẽn vận hành thực tế |
|---|-------------------|--------------|---------------------------------------------|
| 1 | **Vingroup / VinFast (PR & Legal)** | AI-upgrade & Pain từ người khác | **Xử lý khủng hoảng truyền thông & kiểm soát thông tin mạng xã hội:** Tin đồn tiêu cực/Ragebait lan truyền cấp số nhân. Bộ lọc từ khóa (Keyword matching) thông thường thất bại trước teencode, tiếng lóng mỉa mai, ẩn dụ. Thu thập thủ công phát hiện quá chậm (> 30 phút), tỷ lệ nhiễu cao và tốn nhiều ngày để gom chứng cứ lập hồ sơ pháp lý. |
| 2 | **Xanh SM (GSM)** | Tốn thời gian & Pain | **Xử lý sự cố sạc pin / hết pin khẩn cấp trên đường đón khách:** Tài xế gọi về tổng đài báo sắp hết pin. Điều phối viên phải tra cứu thủ công 3 hệ thống (bản đồ xe, trạng thái trụ sạc VinFast, danh bạ xe cứu hộ) mất 12-15 phút/lượt. |
| 3 | **VinFast** | AI có thể tốt hơn | **Chẩn đoán sơ bộ mã lỗi xe điện từ mô tả tự nhiên của khách hàng:** Khách hàng mô tả tiếng Việt đời thường (*"xe rung giật nhẹ khi đạp ga ở tốc độ 40km/h"*). CSKH mất 15-20 phút tra cứu sổ tay kỹ thuật để ghi nhận đúng nhóm lỗi. |
| 4 | **Vinhomes** | Lặp lại & AI-upgrade | **Phân loại & Định tuyến phản ánh cư dân trên App Vinhomes Resident:** Hàng ngàn phản ánh mỗi ngày (mất nước, rò rỉ, ồn ào). CSKH đọc và phân loại thủ công mất 4-8 tiếng để chuyển đúng Ban Quản lý từng tòa/cụm. |
| 5 | **Vinmec** | Tốn thời gian | **Soạn thảo tóm tắt hồ sơ bệnh án xuất viện (Discharge Summary):** Bác sĩ lâm sàng mất 20-30 phút/bệnh nhân để tổng hợp các kết quả xét nghiệm, chẩn đoán, thuốc điều trị thành tài liệu tóm tắt dễ hiểu cho bệnh nhân tái khám. |
| 6 | **VinFast** | Lặp lại | **Đối chiếu hóa đơn sạc điện từ trạm sạc đối tác nhượng quyền:** Kế toán vận hành phải so khớp hàng chục nghìn bản ghi giao dịch sạc điện từ bên thứ ba với dữ liệu viễn thám xe gửi về. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Thẻ Bài Toán Tiềm Năng

---

### 🎴 QUICK PROBLEM CARD #1: Vingroup / VinFast — Hệ Thống Giám Sát, Cảnh Báo Sớm Khủng Hoảng Truyền Thông & Thu Thập Chứng Cứ Pháp Lý (LỰA CHỌN ƯU TIÊN)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                       │
│                                                                             │
│ Bài toán: Phát hiện sớm tin đồn thất thiệt / chiến dịch điều hướng dư luận │
│ tiêu cực (Ragebait) trong vòng 10 phút, phân loại mức độ rủi ro ngữ nghĩa,  │
│ cảnh báo khẩn cấp cho lãnh đạo và tự động đóng gói hồ sơ chứng cứ pháp lý.  │
│ Công ty thành viên: [x] Vingroup Corporate   [x] VinFast                    │
│                                                                             │
│ Ai đang đau (Actor)?                                                        │
│ - Giám đốc Truyền thông (PR Director): Chịu áp lực phản ứng trước truyền    │
│   thông trong 15-30 phút vàng để bảo vệ giá trị vốn hóa và uy tín.         │
│ - Chuyên viên Pháp chế (Legal Counsel): Tốn hàng ngày trời lội tìm link,    │
│   chụp ảnh màn hình thủ công để lập vi bằng và hồ sơ tố tụng.               │
│ - Chuyên viên Social Listening: Kiệt sức vì 80% dữ liệu cào về là tin rác.   │
│                                                                             │
│ Workflow thủ công hiện tại (4 bước):                                        │
│   1. [Thu thập dữ liệu]: Dùng keyword matching quét Facebook, TikTok, Forum │
│   → 2. [Phân loại & Đánh giá]: Chuyên viên đọc từng bài, gạn lọc tin nhiễu  │
│   → 3. [Báo cáo & Cảnh báo]: Soạn email/tin nhắn tóm tắt gửi lên Lãnh đạo    │
│   → 4. [Xử lý & Lưu trữ pháp lý]: Chụp màn hình, lưu URL, lập file chứng cứ. │
│                                                                             │
│ Bước nào tốn thời gian/lỗi nhất?                                            │
│ - Bước 1 & 2: Phát hiện quá muộn (> 30-45 phút), bỏ sót teencode/ẩn ý,      │
│   nhiễu thông tin đến 80% khiến đội ngũ phản ứng thụ động.                  │
│ - Bước 4: Tốn 1-3 ngày làm thủ công để gom hồ sơ nộp cơ quan chức năng.     │
│                                                                             │
│ AI can help at:                                                             │
│ - Thu thập dữ liệu công khai tự động, làm sạch lỗi BOM, teencode, ký tự lạ. │
│ - Phân cụm (Clustering) bài viết trùng lặp nội dung, hiểu ngữ nghĩa ẩn ý.   │
│ - Đánh giá mức độ rủi ro (Risk Scoring) và bắn alert real-time dưới 2 phút. │
│ - Tự động trích xuất bằng chứng (Link, User ID, Timestamp, Screenshot).    │
│                                                                             │
│ Đo thành công bằng gì (Metric có số)?                                        │
│ - Thời gian phát hiện bài viết vi phạm: từ 30-45 phút ──> dưới 10 phút.     │
│ - Tỷ lệ lọc nhiễu thông tin: giảm trên 80% tin rác không liên quan.         │
│ - Tốc độ phản ứng & cảnh báo tới lãnh đạo: dưới 2 phút từ lúc phân loại.    │
│ - Thời gian đóng gói hồ sơ chứng cứ pháp lý: từ 2-3 ngày ──> dưới 1 ngày.   │
│                                                                             │
│ Quick Architecture: [x] Hybrid (Data Crawler + Clustering + LLM + HITL)     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🎴 QUICK PROBLEM CARD #2: Xanh SM — Trợ Lý Điều Phối Khẩn Cấp Sự Cố Sạc Pin

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                       │
│                                                                             │
│ Bài toán: Hỗ trợ điều phối viên tra cứu trạm sạc khả dụng và điều động      │
│ xe sạc cứu hộ di động khi xe taxi điện gặp nguy cơ cạn pin giữa đường.     │
│ Công ty thành viên: [x] Xanh SM (GSM)     [x] VinFast                       │
│                                                                             │
│ Ai đang đau? Tài xế Xanh SM, Điều phối viên trung tâm.                      │
│ Workflow hiện tại: 1. Nhận báo pin ──> 2. Tra cứu GPS ──> 3. Tra trạm sạc  │
│   ──> 4. Soạn tin nhắn hướng dẫn ──> 5. Điều xe cứu hộ nếu cạn pin.         │
│ Bước tốn nhất: Tra cứu trạm sạc và tính cự ly an toàn (⏱ 10-12 phút).       │
│ Đo thành công: Giảm AHT từ 15 phút ──> dưới 2.5 phút.                       │
│ Quick Architecture: [x] LLM Co-pilot with Boundary Checks                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 🎴 QUICK PROBLEM CARD #3: VinFast — Trợ Lý Chẩn Đoán Lỗi Xe Điện Ban Đầu

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                       │
│                                                                             │
│ Bài toán: Phân loại sơ bộ mã lỗi và nhóm kỹ thuật từ mô tả triệu chứng xe   │
│ bằng tiếng Việt tự nhiên của chủ xe VF e34, VF5, VF8, VF9.                  │
│ Công ty thành viên: [x] VinFast                                             │
│                                                                             │
│ Ai đang đau? Chủ xe điện, Nhân viên tiếp nhận dịch vụ (Service Advisor).    │
│ Workflow hiện tại: 1. Khách tả lỗi ──> 2. CSKH hỏi lại ──> 3. Tra sổ tay    │
│   ──> 4. Lập phiếu dịch vụ xưởng bảo dưỡng.                                 │
│ Bước tốn nhất: Đặt câu hỏi và tra cứu sổ tay mã lỗi chuẩn (⏱ 15 phút).      │
│ Đo thành công: Giảm thời gian tiếp nhận ca từ 15 phút ──> dưới 4 phút.       │
│ Quick Architecture: [x] LLM Classification & Extraction                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Quyết định lựa chọn bài toán Deep-Dive

**Lựa chọn:** **QUICK PROBLEM CARD #1 — Hệ Thống Giám Sát, Cảnh Báo Sớm Khủng Hoảng Truyền Thông & Thu Thập Chứng Cứ Pháp Lý (Vingroup / VinFast).**

### Lý do lựa chọn và loại bỏ các thẻ khác:
1. **Mức độ khẩn cấp & Tác động tài chính sống còn:** Khủng hoảng truyền thông mạng xã hội có tốc độ bùng nổ theo cấp số nhân. Việc chậm trễ 15–30 phút có thể xóa sổ hàng trăm tỷ đồng vốn hóa thị trường của VinFast (VFS trên NASDAQ / VIC trên HOSE) và hủy hoại niềm tin người tiêu dùng.
2. **Khắc phục triệt để điểm yếu của công nghệ cũ:** Các giải pháp Social Listening dựa trên Keyword Matching truyền thống hiện đã bất lực trước teencode, thuật ngữ lóng, và ngôn từ mỉa mai ẩn ý. LLM là công nghệ duy nhất có khả năng hiểu sâu ngữ cảnh (Semantic & Sentiment Context).
3. **Ranh giới an toàn (Operational Boundaries) & Trách nhiệm pháp lý đặc biệt rõ ràng:**
   - Hệ thống được phép tự động cào dữ liệu công khai, làm sạch ký tự, gom cụm và đóng gói chứng cứ.
   - Hệ thống **tuyệt đối không được phép** tự động gỡ bài, tự động comment tranh cãi, hay xâm nhập group kín trái luật.
   - Bắt buộc có **Human-in-the-loop (Giám đốc truyền thông phê duyệt kịch bản; Chuyên viên pháp lý xác minh chứng cứ)** trước khi đưa ra hành động ra ngoài xã hội.
