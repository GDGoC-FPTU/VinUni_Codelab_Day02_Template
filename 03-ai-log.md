# 03 — AI Log & Reflection

## Mục đích sử dụng AI

Tôi sử dụng AI như một thought-partner để brainstorm các điểm nghẽn của VinFast, Xanh SM, Vinhomes, Vinmec và Vinpearl; sau đó dùng AI để phản biện metric, ranh giới vận hành và lựa chọn giữa Rule, LLM và Agent.

## AI đã hỗ trợ gì?

- Gợi ý các quy trình lặp lại hoặc tốn thời gian.
- Đề xuất cách cấu trúc Quick Problem Card.
- Chỉ ra rằng bài toán điều phối sự cố sạc có thể dùng LLM Feature nhưng không nên giao quyền tự trị cho Agent.
- Gợi ý các tình huống adversarial như pin 2%, trạm cách 8 km và yêu cầu bỏ qua bước phê duyệt.

## Sai sót hoặc rủi ro phát hiện được

Trong quá trình brainstorm, một số con số như “80 sự cố/ngày”, “20 giờ công/ngày” và “15% doanh thu” chỉ là giả định minh họa, không phải dữ liệu đã xác minh. Tôi không trình bày chúng như sự thật production; báo cáo ghi rõ cần kiểm tra bằng log vận hành.

Một rủi ro khác là LLM có thể nghe theo yêu cầu “gửi ngay” hoặc đề xuất trạm xa khi chỉ đọc thấy khoảng cách mà không cân nhắc mức pin. Vì vậy, chỉ dựa vào câu chữ trong prompt là chưa đủ.

## Cách tôi sửa prompt và ranh giới

Tôi chuyển các yêu cầu an toàn thành quy tắc cụ thể:

1. Mọi output phải bắt đầu bằng `[DRAFT_ONLY]`.
2. Pin dưới 5% là trạng thái critical.
3. Trong trạng thái critical, trạm xa hơn 5 km bị cấm.
4. Hành động thay thế là `dispatch_mobile_charger`.
5. Thiếu dữ liệu an toàn phải chuyển sang `request_human_review`.
6. Điều phối viên luôn phải duyệt trước khi gửi.

Ngoài system prompt, code còn có lớp kiểm tra hậu xử lý để không phụ thuộc hoàn toàn vào việc LLM tuân thủ. Khi không có API key hoặc Gemini lỗi, chương trình trả về fallback an toàn thay vì đoán.

## Bài học

AI hữu ích trong việc mở rộng không gian ý tưởng và phản biện nhanh, nhưng metric, dữ liệu nền, rủi ro và quyền hạn vận hành vẫn cần con người xác minh. Tôi chọn quyết định **NOT YET** vì prototype kỹ thuật chưa thay thế được việc xác lập baseline và kiểm thử với dữ liệu thực tế.

