# 01 — Problem Scan & Quick Cards

> Phase 1 (SCAN) và Phase 2 (QUICK-ASSESS) của Lab 02 — AI Product Scoping (Vin Smart Future).

---

## 🔍 Phase 1 — SCAN

Dùng 4 lenses (Lặp lại · Tốn thời gian · AI-upgrade · Stakeholder Pain) quét vận hành của các công ty thành viên.

| # | Subsidiary | Lens | Mô tả ngắn bài toán |
| :-: | :--- | :--- | :--- |
| 1 | **Vinhomes** | Lặp lại | Nhân viên đọc và phân loại phản ánh của cư dân theo chủ đề. |
| 2 | **Xanh SM** | Stakeholder Pain | Tài xế báo điểm đón không chính xác, cần chuyển phản ánh đến đúng bộ phận. |
| 3 | **VinFast** | Lặp lại | Nhân viên tổng hợp câu hỏi thường gặp về lịch bảo dưỡng. |
| 4 | **Vinmec** | Tốn thời gian | Nhân viên hành chính phân loại yêu cầu đặt lịch khám. |
| 5 | **Vinmec** | Lặp lại | *VinTriage* — trợ lý phân luồng triệu chứng thông minh. |

---

## 🃏 Phase 2 — QUICK-ASSESS

Top 3 từ bảng SCAN: **#1 (Vinhomes — phản ánh cư dân), #2 (Xanh SM — điểm đón sai), #4 (Vinmec — yêu cầu
đặt lịch).** Ba bài cùng dạng *đọc văn bản tự do → phân loại → chuyển đúng nơi* ở ba công ty khác nhau, nên
so sánh trực tiếp được với nhau.

> ⚠️ Các con số trong thẻ (phút/lượt, tỉ lệ, thời gian chờ) là **ước tính để scoping**, chưa có số đo thực tế —
> cần xác minh trước khi dùng làm baseline.

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Phản ánh của cư dân (mất nước, hỏng đèn,  │
│ thang máy, ồn ào, vệ sinh, phí dịch vụ...) gửi qua nhiều    │
│ kênh được CSKH đọc, phân loại theo chủ đề và chuyển bộ phận │
│ hoàn toàn thủ công.                                         │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [X] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? CSKH/lễ tân BQL tòa nhà (người phân    │
│ loại); cư dân (chờ xử lý); tổ kỹ thuật, vệ sinh, an ninh    │
│ (nhận việc sai bộ phận).                                    │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Cư dân gửi phản ánh qua App Vinhomes Resident /        │
│      hotline / Zalo / quầy lễ tân ──>                       │
│   2. CSKH đọc, gọi lại cư dân nếu thiếu thông tin ──>       │
│   3. Gán chủ đề + mức ưu tiên theo kinh nghiệm ──>          │
│   4. Chuyển bộ phận qua nhóm Zalo/email ──>                 │
│   5. Nhắn xác nhận cho cư dân                               │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-4 (~8 trong 12 phút │
│ công mỗi phản ánh; cư dân chờ 2-4 giờ mới tới đúng bộ phận; │
│ khoảng 15-20% bị chuyển nhầm, phải chuyển lại).             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4: LLM đọc nội │
│ dung tự do → trả JSON gồm chủ đề, mức ưu tiên, bộ phận, căn │
│ hộ/vị trí, thông tin còn thiếu; CSKH bấm duyệt hoặc sửa. Ca │
│ khẩn cấp (cháy, rò gas, kẹt thang máy) đi qua rule từ khóa  │
│ trước, không chờ LLM.                                       │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   • Thời gian từ lúc nhận đến lúc tới đúng bộ phận: 2-4 giờ │
│     → ≤ 15 phút.                                            │
│   • Công CSKH: 12 → ≤ 3 phút/phản ánh.                      │
│   • Phân loại đúng ≥ 90% trên bộ test 300 phản ánh đã gán   │
│     nhãn.                                                   │
│   • Chuyển nhầm 15-20% → ≤ 5%.                              │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [X] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Tài xế báo điểm đón trên app không chính  │
│ xác (sai vị trí, chỗ cấm dừng, nhầm lối vào) nhưng phản ánh │
│ không được chuyển tới đúng bộ phận để sửa.                  │
│ Công ty thành viên: [ ] VinFast  [X] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Tài xế (đón sai chỗ, mất thời gian,    │
│ khách hủy chuyến); CSKH tài xế (đọc và chuyển phản ánh);    │
│ đội Bản đồ & Sản phẩm (nhận việc rời rạc).                  │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Tài xế báo qua app / hotline / nhóm Zalo đội xe ──>    │
│   2. CSKH đọc, hỏi lại địa chỉ hoặc mã chuyến ──>           │
│   3. Đoán lỗi do bản đồ, GPS, app hay khách đặt sai ──>     │
│   4. Chuyển đội Bản đồ / Sản phẩm / CSKH khách ──>          │
│   5. Phản hồi tài xế (thường bị bỏ qua)                     │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2-4 (~5 phút/phản     │
│ ánh; nhiều tài xế báo cùng một điểm thành nhiều phiếu rời,  │
│ đội Bản đồ không thấy điểm nào lỗi nhiều nhất).             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4: LLM đọc lời │
│ tài xế → nguyên nhân, bộ phận, địa chỉ/mã chuyến; rule gom  │
│ các báo cáo trùng theo tọa độ chuyến thành một phiếu. CSKH  │
│ duyệt trước khi chuyển.                                     │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   • Thời gian tới đúng bộ phận: ~1 ngày → ≤ 1 giờ.          │
│   • ≥ 80% báo cáo trùng được gộp đúng vào một phiếu.        │
│   • Điểm đón bị báo ≥ 3 lần được sửa trong ≤ 7 ngày.        │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [X] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #4                                       │
│                                                             │
│ Bài toán (1 câu): Yêu cầu đặt lịch khám gửi qua hotline,    │
│ website, app, fanpage được nhân viên hành chính đọc và chọn │
│ chuyên khoa, cơ sở bằng tay, dễ xếp nhầm chuyên khoa.       │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [X] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên hành chính / tổng đài đặt    │
│ lịch; người bệnh (chờ xác nhận, có khi đến nhầm phòng khám  │
│ phải đổi lịch).                                             │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Người bệnh gửi yêu cầu kèm mô tả triệu chứng ──>       │
│   2. Nhân viên đọc, chọn chuyên khoa và cơ sở ──>           │
│   3. Tra lịch trống của bác sĩ ──>                          │
│   4. Gọi điện xác nhận lịch                                 │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (~4-6 phút/yêu cầu; │
│ mô tả mơ hồ dễ chọn sai chuyên khoa, người bệnh phải đổi    │
│ lịch).                                                      │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2: LLM trích     │
│ thông tin (cơ sở, ngày mong muốn, bảo hiểm) và gợi ý chuyên │
│ khoa để nhân viên chọn. KHÔNG chẩn đoán, không tư vấn điều  │
│ trị. Từ khóa nguy cấp (đau ngực, khó thở, co giật) → rule   │
│ chuyển cấp cứu/hotline ngay.                                │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
│   • Thời gian xử lý mỗi yêu cầu: 4-6 → ≤ 2 phút.            │
│   • Gợi ý chuyên khoa đúng ≥ 90% trên 300 yêu cầu đã gán    │
│     nhãn.                                                   │
│   • 100% yêu cầu có từ khóa nguy cấp được chuyển trong ≤ 1  │
│     phút.                                                   │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [X] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Thẻ được chọn để Deep-Dive: **Card #1 — Phân loại phản ánh cư dân Vinhomes**

| Bài | Quyết định | Lý do |
| :-: | :--- | :--- |
| **#1** | ✅ Chọn | Điểm nghẽn là **đọc văn bản tự do** (tiếng Việt không dấu, viết tắt, một tin nói nhiều việc) rồi gán nhãn — đúng thế mạnh của LLM, rule từ khóa làm không xuể. Khối lượng lớn, lặp lại mỗi ngày. Rủi ro thấp vì AI **chỉ gán nhãn và đề xuất bộ phận**, không tự trả lời cư dân; CSKH vẫn duyệt. |
| #2 | Để sau | Cũng hợp LLM, nhưng phần lớn giá trị nằm ở việc **gom báo cáo theo tọa độ** — việc của rule/bản đồ, không cần LLM. Kết quả cuối còn phụ thuộc đội Bản đồ có sửa điểm đón hay không, nằm ngoài tầm của bài phân loại. |
| #4 | Để sau | Dữ liệu sức khỏe nhạy cảm; ranh giới "gợi ý chuyên khoa" rất dễ trượt sang chẩn đoán. Cần bác sĩ thẩm định bộ nhãn và quy trình pháp lý trước khi thử. |
| #3 | Không lên thẻ | Lịch bảo dưỡng là bảng cố định theo km / thời gian → trang FAQ tĩnh hoặc tra cứu theo rule là đủ (No AI / Rule); LLM chỉ thêm giá trị nhỏ. |
| #5 | Không lên thẻ | Phân luồng triệu chứng là quyết định y khoa; sai có thể nguy hiểm tính mạng. Cần quy trình lâm sàng và phê duyệt chuyên môn, vượt phạm vi lab. |

> **Trả lời phản biện trong bài mẫu** (bài mẫu loại Card #4 "Vinhomes CSKH" vì sợ AI trả lời sai về phí, tranh chấp): phạm vi của nhóm **không cho AI trả lời cư dân**. AI chỉ phân loại và chuyển tuyến; phản ánh về phí dịch vụ và tranh chấp luôn được đẩy cho người có thẩm quyền duyệt.

Báo cáo phân tích sâu: [02-deep-dive-report.md](02-deep-dive-report.md).
