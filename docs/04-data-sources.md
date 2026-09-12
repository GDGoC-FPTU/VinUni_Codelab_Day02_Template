# Nguồn dữ liệu cho prototype điều phối sự cố pin thấp Xanh SM

> Ngày kiểm tra nguồn: **12/09/2026**. Tài liệu này phân biệt dữ kiện công khai, dữ liệu mẫu và giả định của bài lab. Không dùng prototype để điều phối xe thật.

## 1. Kết luận dùng ngay cho thiết kế

- Xanh SM đã đổi tên đồng bộ thành **Green SM** từ tháng 4/2026. Nguồn chính thức công bố hệ sinh thái có hơn **186.000 ô tô và xe máy điện**, đã thực hiện **620 triệu chuyến**, di chuyển **4,2 tỷ km** tại bốn quốc gia sau ba năm. Đây là dữ kiện chứng minh quy mô bài toán, không phải số xe do GSM trực tiếp sở hữu tại Việt Nam. [Green SM, 13/04/2026](https://www.greensm.com/vn-vi/news/xanh-sm-doi-ten-thanh-green-sm-dong-bo-nhan-dien-thuong-hieu-tren-toan-cau)
- Một mốc gần hơn với vận hành Việt Nam cho biết dịch vụ hiện diện tại **61 tỉnh/thành sau hai năm**. Con số này được công bố tháng 6/2025, trước thay đổi đơn vị hành chính; không nên dùng như số tỉnh/thành hiện hành năm 2026. [Green SM, 18/06/2025](https://www.greensm.com/vn-vi/news/hao-khi-viet-nam-suc-xanh-lan-toa-trieu-hanh-trinh-xanh-trieu-niem-tin-gieo)
- V-GREEN cho biết đến tháng 3/2025 đã xây dựng hơn **150.000 cổng sạc trên toàn quốc**; Báo cáo thường niên Vingroup 2025 cũng ghi nhận hơn 150 nghìn cổng sạc vào cuối năm 2025. Cần ghi rõ nguồn và mốc thời gian khi sử dụng. [V-GREEN, 02/04/2025](https://vgreen.net/vi/v-green-dat-muc-tieu-xay-dung-500000-cong-sac-oto-dien), [Báo cáo thường niên Vingroup 2025](https://ircdn.vingroup.net/storage/Uploads/0_Bao%20cao%20thuong%20nien/2025/VIE_Vingroup%20AR25.pdf)
- Ứng dụng VinFast có thể hiển thị mức pin, trạm gần nhất, số đầu sạc còn khả dụng, thời gian/quãng đường di chuyển và ước tính pin còn lại khi tới trạm. Đây là bằng chứng rằng các trường dữ liệu đó hợp lý cho future-state flow. [Hướng dẫn ứng dụng VinFast](https://vinfastauto.com/vn_vi/su-dung-tinh-nang-lien-quan-den-pin-tren-ung-dung-vinfast)
- Không tìm thấy tài liệu **API công khai chính thức** cho vị trí và trạng thái đầu sạc VinFast/V-GREEN. Prototype chỉ được giả lập API hoặc đọc fixture; không nên tuyên bố đang tích hợp API thật.

## 2. Quy mô và mức độ liên quan của bài toán

Các số liệu công khai có thể dùng trong phần business context:

- Green SM công bố hơn **1 triệu chuyến xe/ngày** và tổng quãng đường xanh **2,5 tỷ km** tại thời điểm tháng 10/2025. Đây là số toàn hệ sinh thái được doanh nghiệp công bố, không phải lưu lượng riêng tại Hà Nội. [Green SM, 05/10/2025](https://www.greensm.com/vn-vi/news/xanh-sm-la-doanh-nghiep-kinh-doanh-van-chuyen-khach-du-lich-bang-o-to-tot-nhat)
- Nguồn chính thức xác nhận đội taxi tiêu chuẩn dùng **VF e34, VF 5 Plus**, còn dịch vụ cao cấp dùng **VF 8**. [Green SM Airport](https://www.greensm.com/vn-vi/news/dap-san-bay-dat-ngay-xanh-airport-huong-dan-don-xe-taxi-xanh-sm-tai-san-bay)
- Chính sách Green SM Platform công bố cuối 2024 nói xe đang có trên nền tảng gồm VF 5, VF e34, VF 6, VF 7 và VF 8. Từ 01/01/2025, đăng ký mới chỉ tiếp tục cho VF 5 và VF e34; xe cũ thuộc các mẫu khác vẫn có thể được giữ. [Green SM Platform](https://www.greensm.com/vn-vi/news/thong-bao-cac-dong-xe-duoc-tham-gia-xanh-sm-platform)
- Một bài phỏng vấn đăng trên V-GREEN về các trạm quy mô lớn của đối tác ghi nhận khoảng **150–200 lượt xe sạc/ngày** và hơn **10.000 kWh/ngày** tại các trạm từ 15 trụ trở lên. Đây là phát biểu của nhà đầu tư DIMEC được V-GREEN đăng lại, không đại diện cho trung bình toàn mạng lưới. [V-GREEN/DIMEC, 10/07/2025](https://vgreen.net/vi/nha-dau-tu-tiet-lo-ly-do-chon-v-green-chi-100-ty-dong-lam-tram-sac)

Các số liệu **chưa có nguồn công khai**, do đó phải ghi là baseline cần đo hoặc giả định lab:

- “80 sự cố pin/ngày tại Hà Nội”.
- “Mất 15 phút/lượt”, trong đó bước tìm trạm và soạn tin mất 10–12 phút.
- “Rò rỉ 15% doanh thu”.
- “Pin dưới 5% thì luôn phải điều xe sạc lưu động” và “không được chọn trạm xa hơn 5 km”.
- “Độ chính xác đúng trạm/đúng cổng đạt 98%”.

Trong báo cáo, nên viết: **baseline giả định để chạy prototype**, sẽ được thay bằng log điều vận thật trong pilot. Các mục tiêu “15 phút xuống dưới 3 phút” và “≥98%” là **success criteria của lab**, không phải kết quả Green SM đã công bố.

## 3. Dữ liệu trạm sạc và bản đồ

### Nguồn công khai có thể xác nhận

- VinFast có bản đồ/ứng dụng tìm trạm dành cho khách hàng. Bản đồ có địa chỉ, loại cổng; ứng dụng còn cung cấp tình trạng khả dụng và ước tính pin lúc tới. [Hướng dẫn tìm trạm trên website](https://vinfastauto.com/vn_vi/huong-dan-tim-tram-sac-va-showroom-vinfast-tren-website), [Hướng dẫn ứng dụng](https://vinfastauto.com/vn_vi/su-dung-tinh-nang-lien-quan-den-pin-tren-ung-dung-vinfast)
- Hệ thống công bố sử dụng cổng DC **CCS2** và cổng AC **Type 2**; bài giới thiệu liệt kê AC 11 kW, DC 30 kW, DC 60 kW và DC 250 kW. [Tiêu chuẩn trạm sạc VinFast](https://vinfastauto.com/vn_vi/tram-sac-tieu-chuan-chau-au-cua-vinfast)
- Thỏa thuận V-GREEN–Fast+ năm 2024 liệt kê dải trụ nhượng quyền 7,4; 11; 20; 30; 40; 60; 120 và 150 kW. Đây là kế hoạch triển khai của thỏa thuận, không chứng minh mọi mức công suất đều có tại mỗi trạm. [V-GREEN–Fast+](https://vgreen.net/vi/v-green-hop-tac-cung-fast-trien-khai-5000-tru-sac-xe-dien)
- Một nguồn V-GREEN nêu ba địa điểm tại Hà Nội: ngõ 464 Âu Cơ có 30 trụ đang vận hành tại thời điểm bài viết; Trung tâm đăng kiểm Trần Vĩ 35 trụ và khu vực Đền Lừ 22 trụ được dự kiến hoàn thiện trong tháng 7/2025. Nguồn không cho tọa độ, cấu hình từng trụ hoặc trạng thái hiện tại. [V-GREEN/DIMEC](https://vgreen.net/vi/nha-dau-tu-tiet-lo-ly-do-chon-v-green-chi-100-ty-dong-lam-tram-sac)

### Cách dùng file dữ liệu

[`data/charging_stations.json`](../data/charging_stations.json) có hai nhóm:

- `real_sites_from_official_publication`: chỉ ghi đúng tên khu vực và số trụ được nguồn công bố; tọa độ và trạng thái live để `null`.
- `stations`: fixture phục vụ CLI/test, tất cả có `simulated: true`. Tọa độ, số đầu sạc trống và công suất ở đây đều là dữ liệu mô phỏng, kể cả khi tên gợi tới một khu vực thật.

Trong triển khai thật, cần hợp đồng/quyền truy cập với VinFast/V-GREEN để lấy tối thiểu: `station_id`, tọa độ đã xác minh, giờ hoạt động, loại đầu sạc, công suất, trạng thái đầu sạc, thời điểm cập nhật và khả năng đặt chỗ. Khoảng cách phải là **quãng đường theo tuyến**, không phải khoảng cách đường chim bay.

## 4. Thông số xe

Thông số có cấu trúc nằm tại [`data/vehicle_specs.json`](../data/vehicle_specs.json). Các giá trị sau lấy từ brochure chính thức cho thị trường Việt Nam hoặc brochure chính thức được liên kết:

- **VF 3:** pin khả dụng 18,64 kWh; 215 km NEDC; sạc nhanh 10–70% trong 36 phút. [Brochure VF 3](https://shop.vinfastauto.com/on/demandware.static/-/Sites-app_vinfast_vn-Library/default/dwe450f97f/Document/VF3_Brochure_RGB_T42025.pdf)
- **VF 5:** pin khả dụng 37,23 kWh; 326 km NEDC; sạc nhanh 10–70% trong 33 phút. [Brochure VF 5](https://shop.vinfastauto.com/on/demandware.static/-/Sites-app_vinfast_vn-Library/default/dwf5eb40b2/Document/VF5_Brochure_T82025.pdf)
- **VF 6 Eco/Plus:** pin khả dụng 59,6 kWh; lần lượt 480/460 km NEDC; sạc nhanh 10–70% trong 25 phút. [Brochure VF 6](https://shop.vinfastauto.com/on/demandware.static/-/Sites-app_vinfast_vn-Library/default/dwb2a4c157/Document/VF6_Brochure_T072025.pdf)
- **VF e34:** pin khả dụng 41,9 kWh; 318,6 km NEDC. Brochure cũng cảnh báo hiệu suất và quãng đường thay đổi theo yếu tố bên ngoài. [Brochure VF e34](https://shop.vinfastauto.com/on/demandware.static/-/Sites-app_vinfast_vn-Library/en_VN/dwac6c33d7/images/VF.e34.Brochure_ver.pdf)
- **VF 7 Eco/Plus AWD:** pin khả dụng 59,6/75,6 kWh; 498/496 km NEDC; sạc nhanh 10–70% trong 24,1/28,15 phút. Brochure chưa công bố quãng đường bản Plus FWD, nên dữ liệu để `null`. [Brochure VF 7](https://shop.vinfastauto.com/on/demandware.static/-/Sites-app_vinfast_vn-Library/default/dw77dca565/Document/VF7_Brochure_T062025.pdf)
- **VF 8 Eco/Plus:** pin khả dụng 87,7 kWh; brochure công bố 562 km NEDC cho Eco và 457 km WLTP cho Plus; sạc nhanh 10–70% trong 31 phút. Không so sánh trực tiếp hai số vì khác chuẩn thử. [Brochure VF 8](https://shop.vinfastauto.com/on/demandware.static/-/Sites-app_vinfast_vn-Library/default/dw4642b15e/Document/VF8_Brochure_T04.pdf)
- **VF 9:** brochure chính thức cũ liệt kê pin SDI 92 kWh với 437/423 km WLTP (Eco/Plus), và pin CATL 123 kWh với 626/602 km WLTP. Cần xác minh cấu hình theo VIN trước khi dùng trong hệ thống thật. [Brochure VF 9](https://shop.vinfastauto.com/on/demandware.static/-/Sites-app_vinfast_vn-Library/default/dw2ecd7dfc/raisinghands/documents/VF9_Brochure_EN.pdf)

Các brochure ở các thời điểm khác nhau có thể công bố cấu hình pin và quãng đường khác nhau. Không chọn spec chỉ bằng tên model; production input cần `model_year`, `variant`, loại pin hoặc VIN.

## 5. Không quy đổi thẳng phần trăm pin thành số kilomet

NEDC/WLTP là kết quả thử nghiệm chuẩn hóa, không phải cam kết quãng đường còn lại trong một tình huống cụ thể. Chính brochure VF 6/VF 7 lưu ý quãng đường thực tế có thể giảm do tốc độ, nhiệt độ, địa hình, thói quen lái, chế độ lái, số hành khách và giao thông. Bộ Năng lượng Hoa Kỳ cũng nêu nhiệt độ, tốc độ cao, tăng tốc mạnh, tải nặng và đường dốc đều ảnh hưởng phạm vi EV. [VinFast VF 6](https://shop.vinfastauto.com/on/demandware.static/-/Sites-app_vinfast_vn-Library/default/dwb2a4c157/Document/VF6_Brochure_T072025.pdf), [U.S. DOE Alternative Fuels Data Center](https://afdc.energy.gov/vehicles/electric-basics-ev)

Do đó, không dùng công thức:

```text
remaining_km = nominal_range_km * battery_percent / 100
```

Thứ tự dữ liệu nên dùng cho quyết định:

1. `estimated_range_km` từ telemetry/BMS hoặc ứng dụng của đúng chiếc xe.
2. Quãng đường theo tuyến tới trạm, tình trạng giao thông và độ dốc.
3. Safety reserve/hệ số dự phòng đã được kỹ sư an toàn phê duyệt.
4. Mức tin cậy và tuổi dữ liệu; dữ liệu cũ hoặc thiếu thì chuyển cho điều phối viên/cứu hộ.

Nếu lab chưa có telemetry, có thể tạo `estimated_range_km` như **fixture mô phỏng**, nhưng phải gắn `simulated: true`; không trình bày kết quả đó như thông số VinFast.

## 6. Ranh giới an toàn và dữ kiện 5% pin

Một bài hướng dẫn chính thức của VinFast nói xe cần được sạc ngay khi mức pin dưới 5% để tránh nguy cơ hỏng pin; một bài khác cho biết có dịch vụ cứu hộ pin 24/7 cho trường hợp hết pin và không ở gần trạm. [VinFast về vận hành VF e34](https://vinfastauto.com/vn_vi/huong-dan-van-hanh-vf-e34-tiet-kiem-nhien-lieu), [VinFast về xe điện khi tắc đường](https://vinfastauto.com/vn_vi/xe-dien-co-ton-pin-khi-tac-duong-gio-cao-diem)

Nguồn này **không** xác nhận quy tắc “dưới 5% phải gọi xe sạc lưu động trong mọi trường hợp” hoặc bán kính 5 km. Hai quy tắc đó nên được ghi là **policy mô phỏng của lab** chờ đội vận hành/an toàn phê duyệt. Một boundary an toàn hơn cho prototype là:

- LLM không tự chọn trạm và không tự tính khả năng tới trạm.
- Code rule-based chỉ đưa ra danh sách ứng viên sau khi kiểm tra dữ liệu live, loại cổng, quãng đường theo tuyến, `estimated_range_km` và safety reserve.
- Khi pin dưới 5%, thiếu telemetry, không có trạm tương thích/khả dụng, hoặc dữ liệu trạng thái quá cũ: `ESCALATE_TO_DISPATCHER`; điều phối viên quyết định gọi cứu hộ.
- LLM chỉ tạo tin nhắn có nhãn `[DRAFT_ONLY]`; người điều phối duyệt trước khi gửi.

## 7. Các trường dữ liệu đầu vào đề xuất

```json
{
  "incident_id": "INC-001",
  "vehicle": {
    "model": "VF e34",
    "variant": "Vietnam specification",
    "battery_percent": 4,
    "estimated_range_km": 8,
    "estimated_range_source": "vehicle_telemetry",
    "telemetry_timestamp": "2026-09-12T09:01:00+07:00"
  },
  "position": {"latitude": 21.03, "longitude": 105.82, "timestamp": "..."},
  "route_conditions": {"traffic": "heavy", "weather": "rain"},
  "candidate_stations": [],
  "policy": {"critical_soc_percent": 5, "minimum_arrival_reserve_km": 3},
  "simulated": true
}
```

`critical_soc_percent` và `minimum_arrival_reserve_km` trong ví dụ trên là tham số mô phỏng, không phải chính sách công khai của Green SM.

## 8. Gợi ý đo metric đúng rubric

- **Latency:** đo thời gian từ lúc nhận đủ input đến lúc xuất draft; so median và p95 của manual baseline với prototype.
- **Station eligibility:** `eligible = connector compatible AND live available > 0 AND route distance + reserve <= vehicle estimated range`.
- **Correct recommendation rate:** chấm bằng oracle rule-based trên bộ test có nhãn, không để một LLM tự chấm LLM khác mà không kiểm tra.
- **Safety recall:** 100% case pin tới hạn, telemetry cũ/thiếu, trạm hết chỗ hoặc prompt injection phải được `ESCALATE` hay từ chối phù hợp.
- **Draft compliance:** 100% phản hồi có `[DRAFT_ONLY]`, không tự tuyên bố đã gửi tin/gọi cứu hộ/đặt chỗ.

Mục tiêu `<3 phút`, `≥98%` và `100% safety recall` là target của pilot/lab. Muốn kết luận **GO** trong thực tế cần log lịch sử sự cố có nhãn, quyền truy cập dữ liệu trạm live và ký duyệt policy từ vận hành/an toàn; nếu chưa có, quyết định trung thực là **NOT YET** cho production nhưng **GO** cho prototype phạm vi hẹp.
