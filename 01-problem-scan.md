
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
| # | Subsidiary | Lens | Mô tả ngắn bài toán |
|---|------------|------|---------------------|
| 1 | **VinFast** | AI-upgrade | Nhân viên kỹ thuật phải tra cứu nhiều tài liệu hướng dẫn sửa chữa để xác định nguyên nhân và quy trình xử lý phù hợp với từng mã lỗi của xe. |
| 2 | **Xanh SM** | Stakeholder Pain | Tài xế gặp khó khăn khi tìm điểm đón khách chính xác tại các khu vực đông người như trung tâm thương mại, sân bay hoặc bệnh viện, dẫn đến khách phải chờ hoặc gọi lại cho tài xế. |
| 3 | **Vinhomes** | Repetitive | Nhân viên vận hành phải tiếp nhận, phân loại và chuyển các yêu cầu bảo trì từ cư dân như hỏng đèn, điều hòa, thang máy hoặc rò rỉ nước đến đúng bộ phận phụ trách. |
| 4 | **Vinmec** | Time-consuming | Nhân viên y tế phải tổng hợp và kiểm tra lịch sử thuốc, kết quả xét nghiệm và thông tin điều trị của bệnh nhân trước mỗi lần khám hoặc tái khám. |
| 5 | **VinFast** | Stakeholder Pain | Bộ phận chăm sóc khách hàng khó xác định mức độ ưu tiên của các yêu cầu bảo hành khi khách mô tả sự cố không rõ ràng, khiến các trường hợp nghiêm trọng có thể phải chờ xử lý lâu. |

---

# 🃏 Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                        │
│                                                             │
│ Bài toán (1 câu): Nhân viên kỹ thuật VinFast mất thời gian  │
│ tra cứu nhiều tài liệu hướng dẫn sửa chữa để xác định       │
│ nguyên nhân và quy trình xử lý phù hợp với từng mã lỗi xe. │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên kỹ thuật / đội hỗ trợ sửa    │
│ chữa                                                        │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Nhận mã lỗi từ khách hàng hoặc hệ thống ──> 2. Tra cứu │
│      tài liệu kỹ thuật và hướng dẫn sửa chữa                │
│   3. So sánh với các trường hợp tương tự đã xử lý ──> 4.    │
│      Chọn quy trình xử lý phù hợp ──> 5. Gửi hướng dẫn cho  │
│      bộ phận thực hiện hoặc khách hàng                       │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Tìm kiếm và đối chiếu tài │
│ liệu để xác định nguyên nhân và quy trình xử lý (⏱ 15-25    │
│ phút/lượt)                                                   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Tóm tắt tài liệu, gợi  │
│ ý nguyên nhân khả dĩ, đề xuất quy trình xử lý và khuyến nghị │
│ phụ tùng/bước kiểm tra tiếp theo                              │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian xác    │
│ định nguyên nhân từ 20 phút xuống dưới 5 phút/lượt; tăng độ │
│ chính xác phân loại lỗi từ 75% lên 90%                        │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                        │
│                                                             │
│ Bài toán (1 câu): Tài xế Xanh SM gặp khó khăn khi tìm điểm  │
│ đón khách chính xác tại các khu vực đông người, làm khách   │
│ phải chờ hoặc gọi lại nhiều lần.                             │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Tài xế Xanh SM và khách hàng sử dụng    │
│ dịch vụ                                                      │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Nhận vị trí khách cần đón ──> 2. Tìm điểm đón phù hợp  │
│      ở khu vực đông người                                     │
│   3. Kiểm tra lưu lượng giao thông, chỗ đỗ và an toàn ──> 4. │
│      Gửi vị trí cho khách ──> 5. Điều chỉnh nếu khách không   │
│      tìm thấy điểm đón                                         │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Xác định điểm đón tối ưu   │
│ tại khu vực đông người và thời điểm có nhiều biến động (⏱ 5- │
│ 10 phút/lượt)                                                │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Đề xuất điểm đón gần  │
│ nhất, an toàn và dễ nhận diện dựa trên vị trí, lưu lượng     │
│ người, thời tiết và dữ liệu lịch sử                            │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm số lần khách     │
│ chờ quá 5 phút từ 30% xuống dưới 10%; tăng tỷ lệ điểm đón  │
│ chính xác lên trên 95%                                        │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                        │
│                                                             │
│ Bài toán (1 câu): Nhân viên y tế Vinmec phải tổng hợp và    │
│ kiểm tra lịch sử thuốc, kết quả xét nghiệm và thông tin điều │
│ trị của bệnh nhân trước mỗi lần khám hoặc tái khám.          │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [x] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Nhân viên y tế / bác sĩ phụ trách /     │
│ đội hỗ trợ hồ sơ bệnh án                                      │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Nhận lịch hẹn khám hoặc tái khám ──> 2. Truy xuất dữ   │
│      liệu hồ sơ bệnh án, thuốc, xét nghiệm và lịch sử điều   │
│      trị                                                       │
│   3. Kiểm tra thông tin thiếu sót, trùng lặp hoặc mâu thuẫn  │
│      trong hồ sơ ──> 4. Tóm tắt nội dung quan trọng cho bác   │
│      sĩ ──> 5. Chuẩn bị cuộc khám và đưa ra kế hoạch tiếp    │
│      theo                                                      │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Tổng hợp dữ liệu đa nguồn  │
│ và rút trích thông tin quan trọng cho quyết định khám (⏱ 10- │
│ 15 phút/lượt)                                                │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Tóm tắt hồ sơ bệnh    │
│ án, phát hiện tương tác thuốc, cảnh báo thông tin quan trọng  │
│ và gợi ý các xét nghiệm hoặc điều trị cần ưu tiên             │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian chuẩn │
│ bị hồ sơ trước khám từ 15 phút xuống dưới 3 phút/lượt; tăng  │
│ tỷ lệ phát hiện sai sót thông tin hoặc tương tác thuốc lên   │
│ trên 85%                                                     │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **🤖 AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*