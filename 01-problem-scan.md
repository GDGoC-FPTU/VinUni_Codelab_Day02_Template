# 🔍 Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **🤖 AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### 📝 List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **VinFast** | AI có thể tốt hơn | Tự động đề xuất lịch trình sạc tối ưu và trạm sạc trống phù hợp với loại cổng sạc (CCS2/GBT) của từng dòng xe điện (VF5, VF8, VF9). |
| 2 |  **VinFast** |Lặp lại | So khớp dữ liệu sạc điện hằng tuần từ hàng nghìn trụ sạc liên kết ngoài với hóa đơn thực tế gửi về hệ thống tài chính. |
| 3 | **Xanh SM** |Tốn thời gian | Tối ưu hóa điểm đón taxi điện Xanh SM dựa trên phân tích ngôn ngữ tự nhiên từ tin nhắn tài xế và tọa độ GPS thực tế. |
| 4 | **Vinhomes** | Lặp lại | Phân loại tự động các khiếu nại (ví dụ: mất nước, hỏng đèn, ồn ào) gửi qua App Vinhomes Resident đến đúng ban quản lý từng tòa nhà. |
| 5 | **VinFast** | AI có thể tốt hơn | Khách hàng mô tả tiếng Việt (ví dụ: *"xe đi qua gờ giảm tốc kêu cụp cụp ở bánh trước"*), hệ thống tự động phân loại mã lỗi kỹ thuật ban đầu. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên(số 1, số 2 và số 4) và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #_1_                                     │
│                                                             │
│ Bài toán (1 câu): Gợi ý trạm sạc trống và còn hoạt động phù |
|hợp với từng dòng xe điện (VF5, VF8, VF9) và chỉ đường đến trụ
|đó, tránh trụ ở trạng 
|thái bảo trì                               
│ Công ty thành viên: [X] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? _Người dùng xe________________________ │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Ước lượng quãng đường đi được dựa trên dung lượng pin  |
|──> 2. Tìm và chọn trạm sạc trên bản đồ
|──> 3. Tìm quãng đường phù hợp với giao thông để đến trạm
|──> 4. Di chuyển xe đến trạm sạc, nếu trạm lỗi thì đổi trạm
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? 1, 2, 3 (⏱ ~15 - 30 phút/lượt)│
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1: có thể
| tính toán khoảng cách đến trụ sạc gần nhất dựa trên dung 
|lượng đã tiêu hao, bước 3 vì chúng có thể tìm quãng đường phù| 
 hợp nhất với giao thông lúc đó                               │
│                                                             │
│ Đo thành công bằng gì (Metric có số)?                       │
|   * Tỉ lệ đến đúng trụ, trụ ở trong đúng trạng thái: 50%
|   * Thời gian từ lúc quyết định sạc đến lúc bắt đầu sạc: giảm từ 35% trở lên
│
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [] LLM  [X] Agent  |
|  (Kết hợp nhiều dữ liệu để ước lượng quãng đường còn lại và 
dựa vào tình hình giao thông để tìm ra đường ngắn nhất, giao thông 
thoáng nhất đến trụ) 
└─────────────────────────────────────────────────────────────┘
```

```
┌──────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                        │
│                                                              │
│ Bài toán (1 câu): Tự động đối soát dữ liệu phiên sạc hằng    │
│   tuần từ hàng nghìn trụ đối tác với hóa đơn họ gửi về, chỉ  │
│   đẩy các dòng sai lệch cho người xử lý.                     │
│ Công ty thành viên: [X] VinFast  [ ] Xanh SM  [ ] Vinhomes   │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________   │
│                                                              │
│ Ai đang đau (Actor)? Nhân viên đối soát / kế toán (chính);   │
│   đối tác vận hành trụ sạc.                                  │
│                                                              │
│ Workflow thủ công hiện tại (5 bước):                         │
│   1. Xuất log phiên sạc từ hệ thống                          │
│   ──> 2. Thu hóa đơn đối tác (PDF/ Giấy, mỗi bên một mẫu)    │
│   ──> 3. Chuẩn hóa tay, dò khớp bằng Excel theo mã trụ /     │
│          ngày / kWh / số tiền                                │
│   ──> 4. Tra từng dòng lệch, email đối tác xác nhận          │
│   ──> 5. Chốt số, chuyển tài chính thanh toán                │
│                                                              │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3–4                    │
│   (⏱ giả định ~5–10 phút/dòng lệch – cần đo baseline)       │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                        │
│   • B2: đọc hóa đơn nhiều mẫu → bảng chuẩn                   │
│   • B4: gom nhóm nguyên nhân lệch, soạn email cho đối tác    │
│                                                              │
│ Đo thành công bằng gì (Metric có số)?                        │
│   • Tỷ lệ dòng khớp tự động (%) – mục tiêu đề xuất ≥ 95%     │
│   • Số sai lệch (VND) phát hiện / lọt qua sau khi chốt       │
│                                                              │
│ Quick Architecture: [ ] No AI  [X] Rule  [X] LLM  [ ] Agent  │
└──────────────────────────────────────────────────────────────┘
```
```
┌──────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                        │
│                                                              │
│ Bài toán (1 câu): Tự động phân loại khiếu nại cư dân gửi qua │
│   App theo tòa nhà, loại vấn đề, mức khẩn và chuyển đúng ban │
│   quản lý xử lý.                                             │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [X] Vinhomes   │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________   │
│                                                              │
│ Ai đang đau (Actor)? Cư dân đã gửi khiếu nại;                │
│   nhân viên  phân luồng ; ban quản lý tòa nhà.               │
│                                                              │
│ Workflow thủ công hiện tại (5 bước):                         │
│   1. Cư dân gửi khiếu nại  (dạng chữ + ảnh)                  │
│   ──> 2. Nhân viên đọc, xác định tòa + loại vấn đề           │
│   ──> 3. Chuyển cho phòng\ban được nhắc tới trong khiếu nại  │
│   ──> 4. Chuyển sai → bị trả lại → phân loại lại             │
│   ──> 5. Xử lý, phản hồi cư dân                              │
│                                                              │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 và 4                 │
│   (⏱ giả định ~2–5 phút/khiếu nại, cộng vài giờ trễ mỗi lần  │
│    chuyển sai – cần đo baseline)                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào?                        │
│   • B2: đọc nội dung + ảnh → loại vấn đề, mức khẩn, vị trí   │
│   • B5: gợi ý câu trả lời mẫu cho ban quản lý                │
│                                                              │
│ Đo thành công bằng gì (Metric có số)?                        │
│   • Độ chính xác phân loại (%) – mục tiêu đề xuất ≥ 90%      │
│   • Tỷ lệ bị chuyển lại (%)                                  │
│   • Thời gian từ lúc gửi → đúng bộ phận nhận (phút)          │
│   • % khiếu nại khẩn được xử lý đúng                         │
│                                                              │
│ Quick Architecture: [ ] No AI  [X] Rule  [X] LLM  [ ] Agent  │
└──────────────────────────────────────────────────────────────┘
```