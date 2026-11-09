# Problem Scan — Vin Smart Future

# 🔍 Phase 1 — SCAN

### 📝 List bài toán của tôi:

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **Xanh SM** | Tốn thời gian | **Điều vận thông minh (Smart Dispatching):** Tối ưu hóa điểm đón taxi điện Xanh SM dựa trên phân tích ngôn ngữ tự nhiên từ tin nhắn tài xế và tọa độ GPS thực tế. |
| 2 | **VinFast** | AI có thể tốt hơn | **Trợ lý hướng dẫn trạm sạc thông minh:** Tự động đề xuất lịch trình sạc tối ưu và trạm sạc trống phù hợp với loại cổng sạc (CCS2/GBT) của từng dòng xe điện (VF5, VF8, VF9). |
| 3 | **Vinmec** | Tốn thời gian | **Soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary):** Trích xuất thông tin lâm sàng từ bệnh án điện tử, xét nghiệm và ghi chú của bác sĩ để soạn thảo bản tóm tắt xuất viện bằng ngôn ngữ dễ hiểu cho bệnh nhân. |
| 4 | **Vinhomes** | Lặp lại | **Phân loại & Điều hướng phản ánh cư dân:** Phân loại tự động các khiếu nại (ví dụ: mất nước, hỏng đèn, ồn ào) gửi qua App Vinhomes Resident đến đúng ban quản lý từng tòa nhà. |
| 5 | **Vinpearl** | Pain từ người khác | **Tổng hợp & Phân tích review khách sạn:** Quét qua các review trên Booking.com, Agoda, Google Maps của Vinpearl để lọc ra các phàn nàn khẩn cấp (ví dụ: *"phòng bẩn"*, *"nhân viên thái độ tệ"*) gửi về Manager. |

---

# 🃏 Phase 2 — QUICK-ASSESS

Chọn top 3 từ danh sách SCAN: **#2 (VinFast), #4 (Vinhomes), #5 (Vinpearl).**

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tài xế VinFast đi đường dài phải tự ghép  │
│   quãng đường còn lại, trạm trên tuyến, loại cổng và tình   │
│   trạng trụ để quyết định sạc ở đâu, khi nào.               │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Tài xế/chủ xe VinFast (lo hết pin, chờ │
│   trụ); nhân viên tổng đài khi tài xế gọi hỏi trạm sạc.     │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Xem % pin và quãng đường còn lại trên xe               │
│   2. Mở app/bản đồ, tìm các trạm dọc tuyến                  │
│   3. So từng trạm: loại cổng, công suất, trụ trống          │
│   4. Tự tính pin khi đến trạm và thời gian sạc              │
│   5. Đến trạm; hết trụ thì tìm lại hoặc gọi tổng đài        │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3-5                   │
│ ⏱ ___ phút/chuyến (chưa có số công bố, cần đo thực tế)      │
│ ⏱ Báo chí: nhiều trạm ở Hà Nội kín chỗ giờ cao điểm.        │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1: LLM hiểu yêu  │
│   cầu tự do của tài xế. Bước 3-4: rule và API chọn trạm,    │
│   LLM chỉ giải thích phương án, không tự chọn trạm.         │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   - Thời gian lập phương án sạc: ___ phút ──> dưới 1 phút   │
│   - Trạm đề xuất đúng cổng, trong tầm pin: 100% trên bộ     │
│      test                                                   │
│   - Đến nơi hết trụ mà không được báo trước: giảm 50% so    │
│      với baseline (cần đo)                                  │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [x] LLM  [ ] Agent │
│ Rule: tầm pin, loại cổng, chọn trạm. LLM: hiểu yêu cầu tự   │
│ do và giải thích dễ hiểu.                                   │
└─────────────────────────────────────────────────────────────┘
```

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #4                                       │
│                                                             │
│ Bài toán (1 câu): Phản ánh viết tự do của cư dân trên App   │
│   Vinhomes Resident phải được đọc, phân loại và chuyển thủ  │
│   công đến đúng bộ phận thuộc Ban Quản lý tòa nhà.          │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên tiếp nhận (Tổng đài, Lễ tân, │
│   Ban Quản lý) mất thời gian phân loại; cư dân chờ lâu hơn  │
│   khi phản ánh bị chuyển sai.                               │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Cư dân gửi phản ánh (app, hotline, email, trực tiếp)   │
│   2. Nhân viên đọc, xác định loại việc và mức độ khẩn       │
│   3. Chuyển đến bộ phận xử lý phù hợp                       │
│   4. Bộ phận xử lý; nhân viên đốc thúc tối thiểu 5 ngày/lần │
│   5. Phản hồi kết quả và khảo sát cư dân                    │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-3                   │
│ ⏱ Chuẩn Vinhomes: tối đa 4 giờ làm việc (điện thoại), 24    │
│    giờ (email). Kênh app: chưa có số công bố.               │
│ ⏱ ___ phút/lượt (cần đo từ log thực tế)                     │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2: LLM trả về    │
│   loại sự vụ, mức độ khẩn, bộ phận đề xuất và độ tự tin.    │
│   Bước 3: rule định tuyến; độ tự tin thấp thì chuyển người  │
│   duyệt.                                                    │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   - Từ lúc gửi đến khi vào đúng hàng đợi: tối đa 4 giờ làm  │
│      việc ──> dưới 1 phút (ca AI tự tin)                    │
│   - Đúng bộ phận ngay lần đầu: ≥ 90%                        │
│   - Ca an toàn tính mạng bị bỏ sót: 0 trên bộ test          │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [x] LLM  [ ] Agent │
│ Rule: tra tòa nhà, từ khóa khẩn cấp. LLM: nội dung tự do.   │
└─────────────────────────────────────────────────────────────┘
```

```text
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #5                                       │
│                                                             │
│ Bài toán (1 câu): Review về Vinpearl nằm rải rác trên       │
│   Booking.com, Agoda và Google Maps nên quản lý khó phát    │
│   hiện kịp các phàn nàn nghiêm trọng.                       │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [x] Khác: Vinpearl         │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên theo dõi review (đọc thủ     │
│   công nhiều kênh); quản lý khách sạn (biết sự cố muộn).    │
│                                                             │
│ Workflow thủ công hiện tại (5 bước):                        │
│   1. Mở từng kênh review theo từng khách sạn                │
│   2. Đọc review mới, có thể bằng nhiều ngôn ngữ             │
│   3. Đánh giá mức nghiêm trọng, ghi vào bảng tổng hợp       │
│   4. Gửi phàn nàn khẩn cho quản lý khách sạn                │
│   5. Quản lý xử lý sự cố và phản hồi trên từng kênh         │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 1-3                   │
│ ⏱ ___ phút/khách sạn/ngày (cần đo thực tế)                  │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2-3: LLM xác     │
│   định chủ đề, mức khẩn, tóm tắt tiếng Việt và độ tự tin.   │
│   Bước 1 và 4 dùng API và rule. AI không tự trả lời khách.  │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   - Từ lúc review xuất hiện đến khi quản lý nhận: ___ giờ   │
│      ──> dưới 1 giờ                                         │
│   - Phát hiện đúng review khẩn (recall): ≥ 95%              │
│   - Cảnh báo khẩn là đúng (precision): ≥ 80%                │
│                                                             │
│ Quick Architecture: [ ] No AI  [x] Rule  [x] LLM  [ ] Agent │
│ Rule: điểm thấp, từ khóa an toàn, gửi đúng khách sạn.       │
│ LLM: hiểu nội dung tự do, nhiều ngôn ngữ.                   │
└─────────────────────────────────────────────────────────────┘
```

---

# 🗳️ Quyết định lựa chọn

Chọn **Card #2 (VinFast — Trợ lý lập phương án sạc)** để Deep-Dive.

**Vì sao chọn #2:** quyết định chính dựa trên dữ liệu có cấu trúc (mức pin, loại cổng, tình trạng trụ), nên đúng sai kiểm tra được bằng rule trên bộ test ngay cả khi chưa có log thật. Tác động xảy ra trong lúc tài xế đang di chuyển. #2 cũng chưa có baseline, và điều này sẽ được tính đến khi ra quyết định ở Phase 5.

## Lý do loại các thẻ khác

* **Card #4 (Vinhomes — Phân loại phản ánh cư dân):** Yêu cầu không bỏ sót ca an toàn tính mạng chỉ chứng minh được khi có đủ log phản ánh đã gắn nhãn, mà nhóm chưa có. Trong khi đó, danh mục chọn sẵn trên app kết hợp rule theo từ khóa có thể giải quyết phần lớn việc định tuyến mà chưa cần LLM, nên nên thử cách đơn giản này trước. Mốc 4 giờ làm việc là thời hạn tối đa, không phải thời gian thực tế, nên chưa cho biết phần tiết kiệm thật.
* **Card #5 (Vinpearl — Phân tích review khách sạn):** Đây là tác vụ theo dõi sau sự việc: khi review xuất hiện thì sự cố đã xảy ra, nên giá trị của việc biết sớm thấp hơn hỗ trợ tài xế ngay trên đường. Giải pháp phụ thuộc vào điều khoản và quyền truy cập dữ liệu của Booking.com, Agoda và Google Maps, và nhu cầu này có thể được đáp ứng bằng công cụ quản lý danh tiếng có sẵn thay vì tự xây.
