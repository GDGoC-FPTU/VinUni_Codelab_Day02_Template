### Phase 1
# 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Vinhomes (BQL tòa nhà) | Lặp lại (Repetitive) | Điều phối yêu cầu bảo trì - sửa chữa (work order) từ cư dân qua app/hotline: nhân viên phải đọc, phân loại, gán kỹ thuật viên thủ công. Ước tính 1 BQL toà ~30-50 ticket/ngày, mỗi ticket tốn 8-10 phút xử lý thủ công → ~5-7 giờ nhân sự/ngày/tòa; tỷ lệ gán sai chuyên môn kỹ thuật viên ~15-20% gây phát sinh thời gian chờ xử lý lại (rework). |
| 2 | Vinhomes (Kế toán - Vận hành phí DV) | Tốn thời gian (Time-consuming) | Đối soát phí dịch vụ, phí gửi xe, phí điện nước với hệ thống thanh toán/ngân hàng đối tác hàng tháng: xử lý thủ công trên Excel do sai lệch số công tơ, giao dịch trùng, chiết khấu ưu đãi. Ước tính mỗi kỳ đối soát tốn 3-5 ngày công/kế toán viên/tòa nhà, tỷ lệ sai lệch phát hiện sau đối soát ~2-3% giá trị hóa đơn → khiếu nại cư dân và thất thoát công nợ. |
| 3 | Vinhomes (Tổng đài CSKH cư dân) | AI có thể tốt hơn (AI-upgrade) | Trả lời phản ánh/khiếu nại cư dân (tiếng ồn, an ninh, tiện ích, phí DV) qua hotline/app còn theo kịch bản cứng, thời gian phản hồi trung bình (First Response Time) 4-8 giờ với case không khẩn cấp. Ước tính 20-30% cư dân đánh giá "chưa hài lòng" do phản hồi chậm hoặc không đúng trọng tâm, ảnh hưởng trực tiếp tới điểm NPS/CSAT của khu đô thị. |
| 4 | Vinhomes (Phòng quản lý cư dân - Onboarding) | Tốn thời gian (Time-consuming) | Thủ tục đăng ký sửa chữa/cải tạo căn hộ và làm thẻ ra vào cho cư dân mới đòi hỏi kiểm tra hồ sơ, quy định PCCC, phê duyệt qua nhiều phòng ban thủ công qua email/giấy tờ. Ước tính thời gian xử lý trung bình 5-7 ngày làm việc/hồ sơ, trong khi SLA cam kết là 2-3 ngày → tồn đọng hồ sơ chờ duyệt chiếm ~25% khối lượng công việc phòng hành chính. |
| 5 | Vinhomes (An ninh - Bãi đỗ xe & kiểm soát ra vào) | Pain từ người khác (Stakeholder Pain) | Bảo vệ/lễ tân liên tục nhận phàn nàn từ cư dân và khách về tình trạng ùn tắc tại cổng ra vào giờ cao điểm do nhận diện biển số/thẻ xe thủ công hoặc lỗi thiết bị. Ước tính thời gian chờ trung bình giờ cao điểm 3-5 phút/xe, gây ùn ứ hàng chục xe, phát sinh ~10-15 lượt khiếu nại/tháng/khu đô thị lớn liên quan tới an ninh - bãi đỗ. |

---

`
### Phase 2
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                        │
│                                                                │
│ Bài toán: Điều phối work order bảo trì-sửa chữa từ cư dân     │
│ chưa tối ưu, gây gán sai kỹ thuật viên và chậm SLA.           │
│ Công ty thành viên: [x] Vinhomes                              │
│                                                                │
│ Ai đau: Nhân viên trực BQL (phải phân loại thủ công) +        │
│ Kỹ thuật viên (nhận việc sai chuyên môn) + Cư dân (chờ lâu)   │
│                                                                │
│ Workflow thủ công hiện tại:                                   │
│  1. Cư dân gửi yêu cầu (app/hotline, mô tả tự do)             │
│    ──> 2. NV trực đọc, đoán loại sự cố (điện/nước/khóa...)   │
│    ──> 3. NV tra bảng phân công, chọn KTV rảnh                │
│    ──> 4. Gọi/nhắn KTV xác nhận nhận việc                     │
│    ──> 5. Cập nhật trạng thái ticket thủ công                 │
│                                                                │
│ Bước tốn thời gian/lỗi nhất: Bước 2-3 (phân loại + chọn KTV)  │
│ ⏱ ~4-5 phút/ticket, tỷ lệ gán sai chuyên môn ~15-20%          │
│                                                                │
│ AI hỗ trợ ở bước nào: Bước 2 (auto-classify mô tả sự cố)      │
│ và bước 3 (gợi ý KTV theo skill+workload, không phải tự động  │
│ quyết định)                                                   │
│                                                                │
│ Metric: Giảm thời gian phân loại+gán việc từ 4-5 phút         │
│ ──> dưới 30 giây; giảm tỷ lệ gán sai từ 15-20% ──> dưới 5%    │
│                                                                │
│ Quick Architecture: [x] Rule (structured dropdown + matching  │
│ engine) — LLM chỉ hỗ trợ khi mô tả là free-text chưa chuẩn hóa│
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                         │
│                                                                │
│ Bài toán: Phản hồi khiếu nại cư dân qua tổng đài/app còn      │
│ chậm và rập khuôn, gây giảm điểm CSAT/NPS.                    │
│ Công ty thành viên: [x] Vinhomes                              │
│                                                                │
│ Ai đau: Cư dân (chờ 4-8 giờ mới có phản hồi) + Nhân viên      │
│ CSKH (quá tải case lặp lại, đơn giản)                         │
│                                                                │
│ Workflow thủ công hiện tại:                                   │
│  1. Cư dân gửi phản ánh (app/hotline)                         │
│    ──> 2. Case vào hàng chờ chung, không phân loại ưu tiên    │
│    ──> 3. NV CSKH đọc, tra cứu quy định/case tương tự         │
│    ──> 4. Soạn phản hồi thủ công                              │
│    ──> 5. Gửi + đóng case                                     │
│                                                                │
│ Bước tốn thời gian/lỗi nhất: Bước 3-4 (tra cứu + soạn)        │
│ ⏱ ~10-15 phút/case với case đơn giản (hỏi phí, giờ mở cửa...) │
│                                                                │
│ AI hỗ trợ ở bước nào: Bước 3-4 — RAG chatbot trả lời case     │
│ đơn giản/lặp lại tự động, escalate case phức tạp cho người    │
│                                                                │
│ Metric: Giảm thời gian phản hồi trung bình (FRT) từ 4-8 giờ   │
│ ──> dưới 15 phút cho case đơn giản; giảm 40% case chạm tay NV │
│                                                                │
│ Quick Architecture: [x] LLM (RAG trên FAQ + quy định nội quy) │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                         │
│                                                                │
│ Bài toán: Ùn tắc tại cổng ra vào giờ cao điểm do nhận diện    │
│ biển số/thẻ xe thủ công hoặc lỗi thiết bị.                    │
│ Công ty thành viên: [x] Vinhomes                              │
│                                                                │
│ Ai đau: Bảo vệ/lễ tân (bị phàn nàn trực tiếp) + Cư dân/khách  │
│ (chờ 3-5 phút/xe giờ cao điểm)                                │
│                                                                │
│ Workflow thủ công hiện tại:                                   │
│  1. Xe tới cổng ──> 2. Bảo vệ kiểm tra thẻ/quẹt thẻ           │
│    ──> 3. Nếu lỗi đọc thẻ/biển số, kiểm tra thủ công bằng mắt│
│    ──> 4. Gọi xác minh qua bộ đàm nếu nghi ngờ                │
│    ──> 5. Mở barrier                                          │
│                                                                │
│ Bước tốn thời gian/lỗi nhất: Bước 3 (lỗi đọc biển số/thẻ)     │
│ ⏱ ~2-3 phút xử lý lỗi/lượt, dồn ứ khi tần suất lỗi cao        │
│                                                                │
│ AI hỗ trợ ở bước nào: Bước 2-3 — Computer Vision nhận diện    │
│ biển số + đối chiếu database cư dân tự động                  │
│                                                                │
│ Metric: Giảm thời gian trung bình qua cổng từ 3-5 phút        │
│ ──> dưới 10 giây/xe giờ cao điểm; giảm 80% số vụ xử lý lỗi tay│
│                                                                │
│ Quick Architecture: [x] AI (CV/ANPR) kết hợp [x] Rule         │
│ (matching database + fallback logic khi confidence thấp)     │
└─────────────────────────────────────────────────────────────┘