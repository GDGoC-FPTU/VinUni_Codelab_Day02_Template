# 02 — Deep-Dive Report: QR Parking Assistant

## Executive Summary

QR Parking Assistant là web app không bắt buộc cài đặt. Khách quét QR tại cổng, thang máy hoặc cột mốc để hệ thống biết vị trí bắt đầu. Camera/cảm biến cung cấp trạng thái ô; rule engine lọc ô không hợp lệ; routing tính tuyến; session store ghi nhớ nơi xe đã đỗ. LLM chỉ hiểu yêu cầu tự nhiên và diễn giải hướng dẫn. Nhân viên có quyền override, còn người lái chịu trách nhiệm quan sát và điều khiển xe.

**Quyết định:** **NOT YET cho production; GO cho pilot một tầng/khu trong shadow mode**, vì chưa có dữ liệu thật chứng minh độ chính xác và độ trễ occupancy.

## 1. Scope MVP

### User stories

1. **Khi đến:** Khách quét QR tại cổng để nhận tuyến tới ô phù hợp và vừa được xác nhận còn trống.
2. **Sau khi đỗ:** Khách bấm “Tôi đã đỗ” hoặc quét QR tại cột/zone để lưu tầng, zone, spot và thời gian.
3. **Khi ra về:** Khách quét QR gần thang máy/sảnh để nhận tuyến đi bộ tới xe đã lưu.

### Trong phạm vi

- Xe ô tô con tại một tầng/khu pilot.
- QR tĩnh gắn với `anchor_id` đã có trong bản đồ; QR không chứa dữ liệu cá nhân.
- Trạng thái `available`, `occupied`, `reserved`, `blocked`, `unknown`.
- Nhu cầu: ô thường, EV charging, accessible, gần một nhóm thang máy.
- Đề xuất zone/ô và hướng dẫn từng chặng ở tốc độ bãi xe.
- Re-route khi ô bị chiếm hoặc lối đi bị chặn.
- Lưu vị trí xe theo session ẩn danh và tự xóa sau khi xe ra khỏi bãi/qua thời hạn.

### Ngoài phạm vi

- Giữ chỗ chắc chắn hoặc thu phí đặt chỗ.
- Tự lái, điều khiển vô lăng/phanh hoặc ra lệnh cho barrier.
- Dẫn xe đi ngược chiều, qua lối đóng hoặc vùng dành cho nhân viên.
- Xác minh quyền sử dụng chỗ accessible chỉ bằng lời khai của AI.
- Cam kết chỗ vẫn trống khi xe đến.
- Theo dõi khách lâu dài hoặc chia sẻ vị trí xe cho người chưa xác minh session.

### Chức năng ưu tiên

| Mức | Chức năng | Lý do |
|---|---|---|
| Must | Quét QR xác định vị trí | Không cần GPS chính xác trong tầng hầm, không cần cài app. |
| Must | Tìm zone/ô trống phù hợp | Giải quyết pain chính. |
| Must | Lưu và tìm lại xe | Tạo hành trình trọn vẹn lúc đến và lúc về. |
| Must | Re-route/fallback | Bắt buộc vì trạng thái ô thay đổi theo thời gian thực. |
| Should | Lọc EV/accessible/gần thang máy | Hữu ích nhưng phải có policy rules. |
| Should | Hướng dẫn âm thanh ngắn | Giảm thao tác màn hình khi đang lái. |
| Could | Nhắc thời gian đỗ/giờ đóng cửa | Tiện ích, không ảnh hưởng safety. |
| Won't now | Reservation/thanh toán/tự lái | Tăng độ phức tạp và rủi ro, không cần cho MVP. |

## 2. Current-State Workflow

> Các thời gian là giả thuyết cần đo lại bằng timestamp cổng vào, camera và khảo sát khách.

| Bước | Actor/System | Hoạt động | Thời gian | Handoff/Bottleneck |
|---:|---|---|---:|---|
| 1 | Barrier/ticket system | Ghi nhận xe vào bãi | 0,5 phút | 🔄 Hệ thống → người lái |
| 2 | Người lái | Xem biển số chỗ còn lại theo tầng | 1 phút | Dữ liệu quá tổng quát |
| 3 | Người lái | Chạy vào zone được chọn | 2–4 phút | Có thể dồn xe |
| 4 | Người lái | Quan sát từng dãy để tìm ô | 4–8 phút | 🔴 Không biết ô cụ thể |
| 5 | Người lái | Phát hiện ô đã bị chiếm/chặn | 2–4 phút | 🔴 Dữ liệu chậm/tranh chỗ |
| 6 | Người lái ↔ nhân viên | Hỏi và nhận chỉ dẫn | 2 phút | 🔄 Handoff thủ công |
| 7 | Người lái | Đi đến ô khác và đỗ | 2–4 phút | Điểm xung đột giao thông |

**Tổng thời gian tìm chỗ giả thuyết:** 8–15 phút trong cao điểm; lâu hơn nếu phải đổi tầng.

### Root causes

1. Biển chỉ hiển thị tổng số, không phản ánh nhu cầu cụ thể.
2. Occupancy có thể cập nhật chậm hoặc sai do che khuất/cảm biến lỗi.
3. Nhiều xe có thể nhận cùng một gợi ý nếu không có cơ chế phân phối.
4. Route không biết lối một chiều, khu chặn tạm thời hoặc điểm ùn.
5. Không có fallback rõ khi mất camera/network.

## 3. Problem Statement 6-field

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Người lái xe là user; nhân viên điều phối bãi xe là operator và có quyền override. |
| **2. Current Workflow** | Khách xem biển tầng, tự chạy qua các dãy, quay lại khi ô bị chiếm, sau đó phải tự chụp/nhớ cột và lúc về có thể hỏi bảo vệ để tìm xe. |
| **3. Bottleneck** | Thiếu trạng thái ô theo thời gian gần thực; không biết chính xác vị trí trong tầng hầm; không có liên kết giữa hành trình tìm ô và hành trình quay lại xe. |
| **4. Business Impact** | Tăng thời gian chờ, quãng đường chạy trong bãi, ùn tại giao cắt, workload điều phối và trải nghiệm tiêu cực. Chưa có số tài chính được xác minh. |
| **5. Success Metric** | Scan-to-guidance <10 giây; median search time <5 phút; ≥95% recommendation precision; occupancy freshness ≤10 giây; ≥95% phiên lưu vị trí dẫn đúng zone; 0 route safety violation. |
| **6. Operational Boundary** | AI chỉ gợi ý, không bảo đảm/giữ ô và không điều khiển xe. Chỉ dùng ô có dữ liệu đủ mới và confidence đạt ngưỡng. Accessible/EV/reserved spaces được lọc bằng rule. Nhân viên override và fallback về biển/điều phối hiện tại. |

## 4. AI Fit

| Thành phần | Công nghệ phù hợp | Vì sao |
|---|---|---|
| Xác định ô trống | Camera CV hoặc parking sensor | Đây là bài toán perception, không phải LLM. |
| Kiểm tra ô hợp lệ | Rule engine | Reserved, EV, accessible và closed area là hard constraints. |
| Chọn ô và tuyến | Ranking + graph routing | Tối ưu khoảng cách, độ tươi dữ liệu và hướng lưu thông. |
| Hiểu “gần thang máy, có sạc” | LLM/NLU | Chuyển yêu cầu tự nhiên thành constraints có cấu trúc. |
| Giải thích/re-route | LLM template có grounding | Tạo hướng dẫn dễ hiểu từ route đã được engine xác nhận. |
| Xác định vị trí trong bãi | QR anchor | Ổn định hơn GPS trong tầng hầm; QR ánh xạ tới node trên bản đồ. |
| Ghi nhớ vị trí xe | Session store | Bài toán lưu/truy xuất dữ liệu, không cần LLM. |
| Agentic loop | Không chọn | Không cần cho MVP và tăng rủi ro hành động. |

**Kiến trúc chọn:** `CV/Sensor + Rules + Ranking/Routing + LLM Feature`.

## 5. Data Contract

```json
{
  "vehicle_session_id": "anonymous-session-id",
  "intent": "FIND_SPOT",
  "qr_anchor_id": "QR-B1-ENTRY-EAST",
  "current_node": "B1_ENTRY_EAST",
  "preferences": {"spot_type": "standard", "destination_zone": "elevator_A"},
  "candidate_spots": [
    {
      "spot_id": "B1-A-023",
      "state": "available",
      "confidence": 0.98,
      "last_updated_seconds": 4,
      "spot_type": "standard",
      "route_id": "R-102"
    }
  ]
}
```

Khi khách xác nhận đã đỗ, session store chỉ lưu dữ liệu tối thiểu:

```json
{
  "vehicle_session_id": "anonymous-session-id",
  "parked_spot_id": "B1-A-023",
  "parked_anchor_id": "QR-B1-A-COLUMN-02",
  "parked_at": "timestamp",
  "expires_at": "timestamp"
}
```

Authoritative sources là occupancy service, map/routing engine và policy rules. LLM không được tự tạo `spot_id`, trạng thái hoặc tuyến.

## 6. Future-State Flow

```text
Quét QR cổng / khách chọn nhu cầu
              │
              ▼
Camera/sensor cập nhật occupancy
              │
              ▼
Validate freshness + confidence + map status
       │ valid                     │ invalid/missing
       ▼                           ▼
Rule filter spot type       ↩ Fallback: biển + nhân viên
       │
       ▼
Ranking/routing chọn candidate an toàn
       │
       ▼
LLM tạo [DRAFT_ONLY] hướng dẫn grounded theo route
       │
       ▼
Hiển thị bằng hình/âm thanh ngắn, không gây mất tập trung
       │
       ├── ô vẫn trống → khách đỗ → xác nhận/quét QR cột → lưu session
       └── ô bị chiếm → re-route hoặc fallback

KHI RA VỀ:
Quét QR gần thang máy → xác minh session → lấy vị trí đã lưu
→ routing tuyến đi bộ → dẫn tới zone/xe → xóa session khi xe ra bãi
```

## 7. Ranking Logic

Chỉ xét candidate đã vượt hard rules. Score minh họa:

```text
score = 0.40 × normalized_distance
      + 0.25 × congestion_cost
      + 0.20 × occupancy_uncertainty
      + 0.15 × destination_distance
```

`one-way`, `closed`, `reserved`, `EV-only` và `accessible` là hard rules, không đánh đổi bằng score.

## 8. Operational Boundaries & Fallback

AI được phép chuyển yêu cầu thành preference, diễn giải candidate/route do backend cung cấp, nêu uncertainty, yêu cầu re-route và truy xuất vị trí xe trong đúng session đã xác minh.

AI bị cấm bịa ô/route, tuyên bố giữ chỗ, hướng vào lối cấm, dùng sai spot type, tạo tương tác dài khi xe đang chạy, điều khiển xe/barrier hoặc tiết lộ vị trí xe khi session không hợp lệ.

| Tình huống | Hành vi bắt buộc |
|---|---|
| Occupancy quá 10 giây | Không gợi ý ô cụ thể; hướng tới zone và cảnh báo dữ liệu cũ. |
| Confidence thấp | Loại candidate hoặc yêu cầu nhân viên xác nhận. |
| Tỷ lệ dữ liệu thiếu >5% trong zone | Tạm tắt AI guidance cho zone đó. |
| Hai xe cùng candidate | Allocation service cấp candidate khác; không tuyên bố reservation. |
| Network/CV unavailable | Quay về biển điện tử và nhân viên điều phối. |
| Route bị đóng | Recompute route; nếu không có tuyến hợp lệ thì fallback. |
| QR rách/không đọc được | Cho nhập mã anchor ngắn hoặc hỏi nhân viên; không tự đoán vị trí. |
| Không có vị trí xe đã lưu | Không bịa vị trí; cho nhập tầng/zone nhớ được hoặc chuyển nhân viên. |
| Session hết hạn/không hợp lệ | Yêu cầu xác minh theo quy trình bãi xe; không hiển thị vị trí xe. |

## 9. Evaluation

| Metric | Proposed gate |
|---|---:|
| Occupancy precision/recall | ≥95% |
| State freshness p95 | ≤10 giây |
| Route safety violations | 0 |
| JSON schema validity | 100% |
| Adversarial boundary pass rate | 100% |
| Median entry-to-park time | <5 phút |
| Quãng đường chạy tìm | Giảm ≥30% so với control |
| QR scan-to-guidance p95 | <10 giây |
| Saved-location retrieval đúng zone | ≥95% |

Pilot A/B cần so sánh các khung giờ tương đồng và theo dõi cả re-route, override, near-miss; không chỉ đo satisfaction.

## 10. Risk Register

| Rủi ro | Mức độ | Mitigation |
|---|---|---|
| False available | Cao | Freshness gate, confidence threshold, re-route nhanh. |
| Chỉ dẫn gây mất tập trung | Cao | Audio ngắn, visual tối giản, không tương tác dài khi xe chạy. |
| Ùn do nhiều xe cùng route | Cao | Allocation/rate limit và congestion-aware ranking. |
| Vi phạm accessible/EV policy | Cao | Hard rules ngoài LLM, audit log. |
| Camera che khuất/drift | Trung bình–cao | Sensor fusion, monitoring theo camera/zone. |
| Privacy biển số/hành trình | Cao | Session ID ẩn danh, retention tối thiểu, access control. |
| QR bị tráo hoặc dẫn tới link giả | Cao | QR ký số/deep-link allowlist, tem chống bóc và kiểm tra định kỳ. |
| Lộ link session | Cao | Token ngắn hạn, không chứa spot trong URL, xác minh trước khi tìm xe. |

## 11. AI Readiness & Decision

- [ ] Có ground-truth occupancy đủ sạch ở khu pilot.
- [ ] Map số có one-way, closed aisle và spot type đã xác thực.
- [x] Có thể giữ rủi ro trong tầm kiểm soát bằng rule, HITL và fallback.
- [ ] Nhân viên vận hành đã xác nhận workflow, baseline và override process.

### Quyết định: NOT YET

Chưa đủ bằng chứng để triển khai production. Cho phép **GO một proof-of-concept/shadow pilot ở một tầng**, với điều kiện hoàn thiện map, đo baseline, kiểm thử CV/sensor, privacy review và diễn tập mất mạng. Chỉ chuyển sang live guidance khi đạt gate về precision, freshness và không có route safety violation.
