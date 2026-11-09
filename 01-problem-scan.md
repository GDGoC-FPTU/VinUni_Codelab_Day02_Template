# Problem Scan — Vin Smart Future (Vinhomes / Vinmec)

**Bài làm cá nhân — Phase 1 và Phase 2**

---

# 🔍 Phase 1 — SCAN: Tìm kiếm cơ hội (Cá nhân)

| # | Mã | Subsidiary | Lens chính | Mô tả ngắn bài toán |
|---|---|---|---|---|
| 1 | VH-01 | **Vinhomes** | Stakeholder Pain | Tự động hỗ trợ phân loại phản ánh cư dân đa kênh, nhận diện yêu cầu có dấu hiệu khẩn cấp và đề xuất chuyển đúng bộ phận xử lý. |
| 2 | VM-01 | **Vinmec** | Repetitive | Kiểm tra hồ sơ bảo lãnh viện phí/bảo hiểm, phát hiện thiếu chứng từ và sai lệch thông tin trước khi nhân viên gửi hồ sơ. |
| 3 | VM-02 | **Vinmec** | AI-upgrade | Dự đoán nguy cơ bệnh nhân bỏ hẹn, đề xuất nhắc lịch có chọn lọc và hỗ trợ lấp khung giờ đã được xác nhận trống. |
| 4 | VH-02 | **Vinhomes** | Time-consuming | Tối ưu điều phối yêu cầu sửa chữa, hỗ trợ phân công kỹ thuật viên phù hợp chuyên môn, chuẩn bị vật tư và sắp lịch xử lý. |
| 5 | VH-03 | **Vinhomes** | Stakeholder Pain | Rút ngắn xử lý đăng ký cư dân, khách, thẻ ra vào và thẻ xe bằng cách kiểm tra tính đầy đủ, nhất quán của hồ sơ trước khi người có thẩm quyền phê duyệt. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards (Cá nhân)

Tôi chọn **#1 — VH-01**, **#2 — VM-01** và **#3 — VM-02** để phân tích: phân loại phản ánh, kiểm tra chứng từ và dự báo bỏ hẹn.

## Card #1 — VH-01 — Xử lý phản ánh cư dân đa kênh

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                                        │
│                                                                              │
│ Bài toán: Phân loại phản ánh cư dân, nhận diện dấu hiệu khẩn cấp và chuyển   │
│ đúng bộ phận xử lý.                                                          │
│ Công ty thành viên: [x] Vinhomes                                             │
│ Lens: Stakeholder Pain                                                       │
│                                                                              │
│ Ai đang đau? Nhân viên CSKH/ban quản lý quá tải; cư dân phải chờ hoặc trình  │
│ bày lại phản ánh.                                                            │
│                                                                              │
│ Workflow thủ công hiện tại (5 bước):                                         │
│ 1. Tiếp nhận phản ánh và tạo ticket (1 phút).                                │
│ → 2. Đọc nội dung, xác minh địa điểm, đối chiếu ticket cũ (3 phút).          │
│ → 3. Phân loại sự cố, xác định ưu tiên và bộ phận xử lý (3 phút).            │
│ → 4. Chuyển ticket, ghi hạn phản hồi và gửi xác nhận (1 phút).               │
│ → 5. Theo dõi xử lý và xác nhận đóng ticket (thời gian đo riêng).            │
│                                                                              │
│ Bước nào tốn nhất? Bước 2–3: 6 phút/ticket.                                  │
│ Tổng thời gian tiếp nhận–phân loại–chuyển: 8 phút/ticket; chưa gồm thời gian │
│ sửa chữa và theo dõi đến khi đóng.                                           │
│                                                                              │
│ AI hỗ trợ ở bước 2–3: Trích xuất thông tin, phát hiện khả năng trùng lặp, đề │
│ xuất phân loại và gắn cờ khẩn cấp. Rule tính hạn SLA.                        │
│                                                                              │
│ Metric mục tiêu:                                                             │
│ • Giảm thời gian thao tác từ 8 xuống ≤ 4,8 phút/ticket (40%), gồm thời gian  │
│ người duyệt.                                                                 │
│ • Đề xuất đúng bộ phận ≥ 95% trên tập kiểm thử được gán nhãn.                │
│ • Nhận diện ≥ 95% tình huống có dấu hiệu khẩn cấp trên tập kiểm thử được gán │
│ nhãn.                                                                        │
│                                                                              │
│ Quick Architecture: [ ] No AI [x] Rule [x] LLM [ ] Agent                     │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Tác động và giá trị dự kiến — kịch bản giả định:**

- Với **3.900 ticket/tháng**, giảm thao tác từ **8 xuống 4,8 phút/ticket** giúp thu hồi **3,2 phút/ticket**, tương đương **208 giờ/tháng**: `3.900 × (8 − 4,8) ÷ 60`.
- Giả định chi phí lao động **100.000 đồng/giờ**, giá trị thời gian thu hồi là **20,8 triệu đồng/tháng**. Đây là năng lực nhân sự có thể dành cho các yêu cầu khác, chưa phải lợi nhuận hay khoản tiền chắc chắn cắt giảm.
- Tác động bổ sung: giảm chuyển sai bộ phận, xử lý lại và vi phạm SLA; cư dân ít phải nhắc lại hoặc chờ chuyển tiếp. Chưa quy đổi thành tiền vì thiếu baseline.

**Cách kiểm chứng:** Đo thời gian thao tác gồm cả duyệt/sửa đề xuất AI; đối chiếu tỷ lệ chuyển sai, xử lý lại và quá hạn SLA trước–sau pilot với nhóm ticket tương đồng. Chỉ tính giá trị trên ticket thực sự được hỗ trợ và trừ chi phí mô hình, tích hợp, vận hành khi đánh giá hiệu quả kinh tế.

**Ranh giới và fallback:** AI đề xuất phân loại và phản hồi nháp; nhân viên duyệt trước khi chuyển/gửi. Không tự đóng ticket. Thiếu thông tin hoặc không đủ căn cứ thì chuyển người xử lý.

---

## Card #2 — VM-01 — Kiểm tra hồ sơ bảo hiểm, bảo lãnh viện phí

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                                        │
│                                                                              │
│ Bài toán: Phát hiện thiếu chứng từ và sai lệch thông tin trong hồ sơ bảo     │
│ lãnh viện phí trước khi gửi.                                                 │
│ Công ty thành viên: [x] Vinmec                                               │
│ Lens: Repetitive                                                             │
│                                                                              │
│ Ai đang đau? Nhân viên bảo lãnh viện phí/tiếp đón kiểm tra lặp lại; bệnh     │
│ nhân phải chờ bổ sung hồ sơ.                                                 │
│                                                                              │
│ Workflow thủ công hiện tại (5 bước):                                         │
│ 1. Tiếp nhận giấy tờ, xác định checklist theo đối tác (1 phút).              │
│ → 2. Đọc thẻ bảo hiểm, giấy tờ cá nhân và chứng từ liên quan (5 phút).       │
│ → 3. Đối chiếu chứng từ với dữ liệu bệnh viện và checklist (4 phút).         │
│ → 4. Ghi nhận sai lệch và lập danh sách cần bổ sung (1 phút).                │
│ → 5. Nhân viên duyệt, gửi hồ sơ hoặc yêu cầu bổ sung (1 phút).               │
│                                                                              │
│ Bước nào tốn nhất? Bước 2–3: 9 phút/hồ sơ.                                   │
│ Tổng thời gian kiểm tra nội bộ: 12 phút/hồ sơ; không gồm thời gian chờ bổ    │
│ sung hoặc chờ bên bảo hiểm phản hồi.                                         │
│                                                                              │
│ AI hỗ trợ ở bước 2–4: OCR/Document AI trích xuất dữ liệu; rule kiểm tra      │
│ thiếu/sai lệch; LLM giải thích cảnh báo và soạn checklist bổ sung nháp.      │
│                                                                              │
│ Metric mục tiêu:                                                             │
│ • Giảm thời gian kiểm tra từ 12 xuống ≤ 6,6 phút/hồ sơ (45%), gồm thời gian  │
│ người duyệt.                                                                 │
│ • Phát hiện ≥ 95% lỗi thiếu/sai thuộc checklist trên tập kiểm thử được gán   │
│ nhãn.                                                                        │
│ • Giảm ≥ 30% tương đối tỷ lệ hồ sơ bị yêu cầu bổ sung do lỗi kiểm tra trong  │
│ phạm vi hệ thống so với baseline đo trước pilot.                             │
│                                                                              │
│ Quick Architecture: [ ] No AI [x] Rule [x] LLM [ ] Agent                     │
│ Kết hợp OCR/Document AI; rule làm lõi kiểm tra.                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Tác động và giá trị dự kiến — kịch bản giả định:**

- Giả định **150 hồ sơ/ngày × 26 ngày = 3.900 hồ sơ/tháng**. Giảm thời gian rà soát nội bộ từ **12 xuống 6,6 phút/hồ sơ** giúp thu hồi **351 giờ/tháng**: `3.900 × (12 − 6,6) ÷ 60`.
- Với đơn giá lao động giả định **110.000 đồng/giờ**, giá trị thời gian thu hồi tương đương **38,61 triệu đồng/tháng**, trước chi phí OCR, mô hình, tích hợp và vận hành; chưa phải lợi nhuận ròng.
- Tác động bổ sung: giảm lượt bổ sung hồ sơ, sai chứng từ và nguy cơ chậm thanh toán do lỗi hồ sơ. Chưa định giá các lợi ích này khi chưa có dữ liệu về tần suất, nguyên nhân và chi phí xử lý lại.

**Cách kiểm chứng:** Đo riêng thời gian nhân viên rà soát và sửa kết quả AI; theo dõi tỷ lệ hồ sơ đầy đủ ngay lần đầu và tỷ lệ phải bổ sung do lỗi thuộc checklist. Chỉ tính phần thao tác nội bộ có thể tác động, tách khỏi thời gian chờ bệnh nhân hoặc công ty bảo hiểm; không lấy toàn bộ thời gian xử lý bảo lãnh làm thời gian AI tiết kiệm.

**Ranh giới và fallback:** Hệ thống không tự duyệt/từ chối bảo lãnh hoặc cam kết chi trả. Nhân viên xác nhận trước khi gửi; chứng từ mờ, thông tin thiếu hoặc quy định chưa rõ được chuyển kiểm tra thủ công.

---

## Card #3 — VM-02 — Dự đoán bỏ hẹn và lấp lịch khám trống

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                                        │
│                                                                              │
│ Bài toán: Ưu tiên xác nhận lịch có nguy cơ bỏ hẹn và tìm bệnh nhân phù hợp   │
│ cho khung giờ đã trống.                                                      │
│ Công ty thành viên: [x] Vinmec                                               │
│ Lens: AI-upgrade                                                             │
│                                                                              │
│ Ai đang đau? Nhân viên đặt lịch/CSKH phải xác nhận dàn trải; phòng khám mất  │
│ công suất; bệnh nhân chờ bỏ lỡ lịch phù hợp.                                 │
│                                                                              │
│ Workflow thủ công hiện tại (5 bước):                                         │
│ 1. Xuất danh sách lịch khám sắp tới.                                         │
│ → 2. Gọi/nhắn xác nhận, ghi nhận hủy hoặc đổi lịch.                          │
│ → 3. Cập nhật các khung giờ đã được xác nhận trống.                          │
│ → 4. Lọc danh sách chờ, kiểm tra điều kiện và liên hệ bệnh nhân.             │
│ → 5. Bệnh nhân đồng ý; nhân viên xác nhận và cập nhật lịch.                  │
│                                                                              │
│ Bước nào tốn nhất? Bước 2: 3 phút/lịch được liên hệ; bước 4: 5 phút/slot     │
│ trống cần xử lý. Hai chỉ số đo riêng.                                        │
│                                                                              │
│ AI hỗ trợ trước bước 2: ML dự báo nguy cơ bỏ hẹn để ưu tiên liên hệ. Bước 4: │
│ rule ghép lịch theo chuyên khoa, thời gian và điều kiện đặt lịch.            │
│                                                                              │
│ Metric mục tiêu:                                                             │
│ • Giảm bỏ hẹn từ baseline giả định 10% xuống ≤ 8% trong pilot có nhóm so     │
│ sánh tương đồng.                                                             │
│ • Lấp ≥ 20% slot đã xác nhận trống, đủ thời gian liên hệ và có bệnh nhân chờ │
│ phù hợp.                                                                     │
│ • Giảm thời gian tìm và xác nhận người thay thế từ 5 xuống ≤ 3 phút/slot đủ  │
│ điều kiện được xử lý.                                                        │
│                                                                              │
│ Quick Architecture: [ ] No AI [x] Rule [ ] LLM [ ] Agent                     │
│ Kết hợp Predictive ML để dự báo; rule để ghép lịch.                          │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Tác động và giá trị dự kiến — kịch bản giả định:**

- **300 lịch/ngày × 26 ngày = 7.800 lịch/tháng**. Giả định bỏ hẹn **10%**, công suất có nguy cơ không sử dụng là **780 slot/tháng**.
- Nếu phục hồi được **20% của 780 slot** và bệnh nhân thay thế thực sự đến khám, số lượt khám tăng thêm là **156 lượt/tháng**. Với biên đóng góp giả định **300.000 đồng/lượt**, giá trị tối đa trong kịch bản này là **46,8 triệu đồng/tháng**, trước chi phí can thiệp và công nghệ.
- Giả định **20 phút/slot**, 156 lượt tương đương **52 giờ công suất khám được sử dụng lại**. Đây là công suất phục hồi, không phải giờ lao động cắt giảm.
- Tác động bổ sung: bệnh nhân trong danh sách chờ có thêm cơ hội khám sớm; nhân viên ưu tiên liên hệ thay vì xác nhận dàn trải. Mức phục hồi **20%** là mục tiêu cần kiểm chứng tại đơn vị, chưa phải hiệu quả đã đạt.

**Cách kiểm chứng:** Pilot so sánh dự báo kết hợp nhắc lịch với nhắc lịch tiêu chuẩn; đo lượt khám thực tế tăng thêm và chi phí trên mỗi lượt phục hồi. Kết quả thực tế tính theo `slot đủ điều kiện × tỷ lệ lấp lại × tỷ lệ đến khám × biên đóng góp`, trừ chi phí can thiệp và công nghệ. Kịch bản 46,8 triệu đồng chỉ đạt khi có đủ slot có thể lấp và bệnh nhân thay thế đến khám; không cộng trùng lợi ích giảm bỏ hẹn và lấp lịch trên cùng một lượt khám.

**Ranh giới và fallback:** Điểm rủi ro chỉ dùng để ưu tiên liên hệ. Không tự hủy hoặc đặt chồng lịch; chỉ đặt lại khi slot đã trống và bệnh nhân đồng ý. Khi mô hình chưa đủ tin cậy, dùng nhắc lịch tiêu chuẩn và danh sách chờ theo rule.
