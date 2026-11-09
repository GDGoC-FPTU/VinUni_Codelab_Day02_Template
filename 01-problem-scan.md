# 🔍 Báo Cáo Quét Cơ Hội & Đánh Giá Nhanh (Problem Scan & Quick Cards)

**Thành viên thực hiện:** trong-nghia  
**Đơn vị:** Vin Smart Future — AI Engineering  
**Dự án:** Lab 02: AI Product Scoping  

> *Lưu ý: Các tình huống nghiệp vụ, thời gian xử lý và tỷ lệ phần trăm tổn thất trong tài liệu này là các giả định phân tích dùng để thiết kế bài toán thử nghiệm (scoping prototype) trong khuôn khổ môn học.*

---

## 🧭 Phase 1 — SCAN: Quét cơ hội vận hành qua 4 Lenses

Áp dụng 4 lăng kính (*Lặp lại, Tốn thời gian, AI có thể tốt hơn, Pain từ người khác*) quét qua các mảng vận hành của Vingroup:

| # | Đơn vị thành viên | Lăng kính (Lens) | Mô tả bài toán & Tác động vận hành thực tế |
|---|---|---|---|
| **1** | **VinFast** | Tốn thời gian / Pain từ người khác | **Lệch pha cung - cầu và tồn kho xe điện cục bộ giữa các vùng:** Thiếu cơ chế dự báo nhu cầu động theo phiên bản/màu xe; điều phối viên phân bổ xe thủ công dựa trên báo cáo tuần tĩnh dẫn đến showroom thiếu mẫu xe khách cần giao ngay trong khi kho vùng khác tồn đọng. Giả định 5–10% giá trị vốn tồn kho xe bị phân bổ kém tối ưu, gây trễ hẹn giao xe và tăng chi phí vận chuyển trung chuyển chéo vùng. |
| **2** | **Vinmec** | Lặp lại / Rủi ro cao | **Rà soát thủ công hạn sử dụng (EXP) và số lô (Lot) kho dược phẩm:** Dược sĩ kiểm tra thủ công danh mục hàng nghìn loại thuốc trên bảng tính/hệ thống HIS, dễ bỏ sót các lô thuốc đặc trị cận date (FEFO không triệt để). Giả định rủi ro hao hụt, tiêu hủy thuốc quá hạn chiếm 0.5–2% giá trị tồn kho dược phẩm mỗi năm và tốn hàng chục giờ kiểm kê mỗi tuần. |
| **3** | **Vinhomes** | Lặp lại & Tốn thời gian | **Quá tải tiếp nhận và phê duyệt yêu cầu đặt lịch tiện ích nội khu:** Lễ tân/BQL tiếp nhận yêu cầu phân tán (App, hotline, nhóm chat); nhân viên tra cứu lịch trống thủ công trên phần mềm, đối soát nội quy cư dân và soạn xác nhận mất 5–15 phút/yêu cầu, gây trễ hẹn và quá tải nhân sự vào các khung giờ cao điểm hoặc dịp cuối tuần. |
| **4** | **Vinpearl** | Tốn thời gian / Lãng phí nguồn lực | **Phân công dọn phòng (Housekeeping) tĩnh, lệch nhịp check-out thực tế:** Giám sát buồng phòng chia danh sách cố định đầu ca, chưa cập nhật linh hoạt theo giờ khách thực tế trả phòng hoặc nhu cầu ưu tiên phòng VIP check-in sớm. Giả định lãng phí 10–20% giờ công lao động do nhân viên phải chờ việc hoặc di chuyển chéo tầng nhiều lần. |
| **5** | **VinUni** | Lặp lại & Tốn thời gian | **Tiếp nhận và xử lý thủ tục hành chính, dịch vụ sinh viên thủ công:** Chuyên viên Đào tạo/Công tác sinh viên đọc email, ticket tự do (xin bảng điểm, giấy xác nhận, bảo lưu, chuyển lớp), đối chiếu quy chế và soạn văn bản trả lời mất 10–20 phút/yêu cầu, kéo dài thời gian chờ đợi (SLA) của sinh viên và tăng áp lực giấy tờ trong mùa cao điểm. |

---

## 🃏 Phase 2 — QUICK-ASSESS: 3 Thẻ Đánh Giá Nhanh (Quick Problem Cards)

---

### 📇 Thẻ 1: Vinhomes — Tiếp nhận & Xác nhận Đặt lịch Tiện ích Cư dân

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1: VINHOMES AMENITY BOOKING ASSISTANT               │
│                                                                         │
│ Bài toán (1 câu): Tự động hóa tiếp nhận, kiểm tra lịch trống và soạn    │
│ nháp xác nhận yêu cầu sử dụng tiện ích nội khu (tennis, BBQ, hồ bơi).   │
│ Công ty thành viên: [x] Vinhomes                                        │
│                                                                         │
│ Ai đang đau (Actor)? Cư dân (chờ lâu) & Nhân viên Lễ tân/BQL (quá tải). │
│                                                                         │
│ Workflow thủ công hiện tại (4 bước):                                    │
│   1. Nhận yêu cầu (App / tin nhắn / hotline)                            │
│   ──> 2. Mở bảng biểu tra cứu khung giờ trống và đối chiếu nội quy      │
│   ──> 3. Kiểm tra tính hợp lệ cư dân (chính chủ, chưa vượt hạn mức tháng)│
│   ──> 4. Soạn tin nhắn/email xác nhận hoặc từ chối kèm lý do và cập nhật│
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 4 (⏱ 8-12 phút/yêu cầu)        │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1, 2 và 4:                   │
│ - Trích xuất ý định (ngày, giờ, loại sân, số người) từ tin nhắn tự do.  │
│ - Rule Engine tự động check slot trống và điều kiện cư dân.             │
│ - LLM tự động soạn nháp phản hồi [DRAFT_ONLY] cho nhân viên duyệt.      │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                    │
│ - Giảm thời gian xử lý của nhân viên từ 10 min ──> dưới 2 min/yêu cầu.  │
│ - 100% phản hồi được nhân viên duyệt trước khi gửi đi (Human-in-the-loop)│
│ - Tỷ lệ trùng lịch (Double booking) đạt 0%.                             │
│                                                                         │
│ Quick Architecture: [x] Rule + LLM Feature (Kết hợp kiểm tra slot & LLM)│
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 Thẻ 2: Vinmec — Giám sát & Cảnh báo Sớm Rủi ro Thuốc Cận Date (FEFO)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2: VINMEC PHARMACY EXPIRY SENTINEL                  │
│                                                                         │
│ Bài toán (1 câu): Tự động quét hạn dùng thuốc (EXP) và tốc độ tiêu thụ  │
│ để cảnh báo sớm các lô thuốc cận date có nguy cơ tiêu hủy.             │
│ Công ty thành viên: [x] Vinmec                                          │
│                                                                         │
│ Ai đang đau (Actor)? Dược sĩ quản lý kho & Kế toán trưởng bệnh viện.    │
│                                                                         │
│ Workflow thủ công hiện tại (5 bước):                                    │
│   1. Xuất file dữ liệu tồn kho hàng nghìn dòng từ hệ thống HIS/ERP      │
│   ──> 2. Lọc thủ công các dòng thuốc có date < 3-6 tháng                │
│   ──> 3. Tra cứu lịch sử kê đơn để tính mức độ tiêu thụ thực tế         │
│   ──> 4. Soạn email gửi Trưởng khoa Lâm sàng ưu tiên kê đơn lô cận date │
│   ──> 5. Lập biên bản điều chuyển thuốc sang bệnh viện khác trong hệ thống│
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2, 3 và 4 (⏱ 3-4 giờ/tuần)         │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 và 4:                   │
│ - Rule/Data Analytics tính toán tốc độ tiêu thụ và gắn cờ rủi ro FEFO.  │
│ - LLM tóm tắt danh sách cảnh báo cấp thiết và soạn thảo nháp email đề   │
│   xuất phương án điều chuyển thuốc cho dược sĩ duyệt.                   │
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                    │
│ - Phát hiện 100% lô thuốc có nguy cơ hủy trước 90 ngày.                 │
│ - Giảm thời gian lập báo cáo cảnh báo tuần từ 4 giờ ──> dưới 15 phút.   │
│ - Giảm tỷ lệ hao hụt do thuốc hết hạn ít nhất 30-50%.                   │
│                                                                         │
│ Quick Architecture: [x] Rule + LLM Feature (Rule tính toán + LLM soạn tin)
└─────────────────────────────────────────────────────────────────────────┘
```

---

### 📇 Thẻ 3: VinFast — Cân Bằng Cung - Cầu & Điều Chuyển Tồn Kho Xe Điện Vùng

```text
┌─────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3: VINFAST EV INVENTORY REBALANCING ASSISTANT       │
│                                                                         │
│ Bài toán (1 câu): Tự động phát hiện lệch pha cung - cầu tồn kho xe điện │
│ theo phiên bản/màu sắc giữa các vùng và soạn đề xuất điều chuyển xe.    │
│ Công ty thành viên: [x] VinFast                                         │
│                                                                         │
│ Ai đang đau (Actor)? Điều phối viên phân phối xe & Trưởng showroom.     │
│                                                                         │
│ Workflow thủ công hiện tại (5 bước):                                    │
│   1. Xuất báo cáo đơn cọc chờ giao xe và lượng xe tồn tại từng kho vùng │
│   ──> 2. Mở file Excel đối chiếu thủ công từng dòng xe (VF5/VF8), phiên │
│          bản (Eco/Plus), màu ngoại/nội thất giữa cung và cầu            │
│   ──> 3. Xác định các điểm nghẽn thiếu xe (Hà Nội thiếu, Đà Nẵng thừa)   │
│   ──> 4. Tính toán chi phí vận chuyển & soạn email đề xuất điều xe      │
│   ──> 5. Trình Trưởng phòng Cung ứng duyệt và thông báo nhà xe trung chuyển│
│                                                                         │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 4 (⏱ 3-5 giờ/tuần; 20-30 phút/cụm)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 và 4:                   │
│ - Data/Rule Engine tự động khớp ma trận tồn kho vs hợp đồng chờ theo    │
│   thời gian thực, tính toán tuyến điều chuyển tối ưu chi phí.            │
│ - LLM Feature đọc hiểu các ghi chú ưu tiên giao xe của đại lý và soạn   │
│   thảo bản nháp kế hoạch điều chuyển [DRAFT_ONLY] cho Trưởng phòng duyệt.│
│                                                                         │
│ Đo thành công bằng gì (Metric có số)?                                    │
│ - Giảm thời gian lập kế hoạch điều chuyển xe từ 4 giờ ──> dưới 30 phút. │
│ - Giảm tỷ lệ vốn tồn kho bị phân bổ sai lệch từ 5-10% ──> dưới 2%.      │
│ - Giảm thời gian chờ xe của khách hàng từ 14 ngày ──> dưới 5 ngày đối   │
│   với các xe đã sẵn có trong hệ thống kho toàn quốc.                    │
│ - 100% lệnh điều xe phải có phê duyệt của Trưởng phòng Cung ứng (HITL). │
│                                                                         │
│ Quick Architecture: [x] Rule + LLM Feature (Rule ma trận + LLM soạn kế hoạch)│
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Đề Xuất Lựa Chọn Đề Tài Deep-Dive

* **Bài toán đề xuất Deep-Dive:** **Thẻ 2: Vinmec — Giám sát & Cảnh báo Sớm Rủi ro Thuốc Cận Date (FEFO)** (*Vinmec Pharmacy Expiry Sentinel*).
* **Lý do lựa chọn:**
  1. **Tác động kinh tế và an toàn điều trị rất lớn (High Impact):** Dược phẩm cận date hoặc hết hạn không chỉ gây tổn thất tài chính trực tiếp (giả định 0.5–2% giá trị tồn kho mỗi năm) mà còn tiềm ẩn nguy cơ an toàn y tế nghiêm trọng nếu bỏ sót lô thuốc hết hạn. Việc tự động hóa giám sát giúp loại bỏ hoàn toàn sai sót do con người rà soát thủ công.
  2. **Ranh giới an toàn (Operational Boundary) sắc bén & chuẩn mực y tế:** Dữ liệu số lô (Lot), hạn dùng (EXP) và tốc độ tiêu thụ có cấu trúc rõ ràng. AI chỉ được phép quét cảnh báo và soạn thảo bản nháp đề xuất luân chuyển có gắn thẻ `[DRAFT_ONLY]`; AI **tuyệt đối không được tự ý ra y lệnh điều trị, không tự ý hủy thuốc hay điều chuyển** mà bắt buộc phải qua bước phê duyệt của Dược sĩ phụ trách kho và Trưởng khoa Lâm sàng (Human-in-the-loop).
  3. **Tỷ lệ AI-Fit tối ưu (Rule Engine + LLM Feature):** Dùng Rule-based/Data Analytics tính toán tốc độ tiêu thụ và lọc hạn dùng theo nguyên tắc FEFO (chính xác 100%), kết hợp LLM để tóm tắt danh sách ưu tiên hành động và soạn nháp báo cáo/email điều chuyển thuốc chuyên nghiệp.
* **Lý do không chọn Thẻ 1 (Vinhomes) & Thẻ 3 (VinFast):**
  * *Thẻ 1 (Vinhomes):* Bài toán đặt tiện ích mang tính chất dịch vụ dân sự thông thường, ít rủi ro và giá trị nghiệp vụ không mang tính sống còn như kiểm soát date dược phẩm trong bệnh viện.
  * *Thẻ 3 (VinFast):* Bài toán điều chuyển xe điện toàn quốc phụ thuộc vào mạng lưới logistics phức tạp và biến động chính sách bán hàng theo tháng, cần khối lượng dữ liệu lịch sử lớn hơn để xác lập baseline chuẩn.
