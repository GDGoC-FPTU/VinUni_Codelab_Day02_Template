# 02 — Báo cáo Deep-Dive: Phân loại & Điều hướng phản ánh cư dân Vinhomes

> Lab 02 — AI Product Scoping (Vin Smart Future)
>
> **Phạm vi:** Phân loại + điều hướng + soạn phản hồi cho phản ánh của cư dân Vinhomes.
>
> **Mức độ bằng chứng:** Ý tưởng / phạm vi prototype. Các volume và thời gian vận hành bên dưới được đánh dấu **[GIẢ ĐỊNH]** vì bộ tài liệu lab không cung cấp log nội bộ đã xác minh của Vinhomes.
>
> **Điểm được xác minh từ nguồn công khai:** Vinhomes Resident là một nền tảng cư dân thực tế và Vinhomes đã công bố việc sử dụng ứng dụng ở quy mô đáng kể. Tuy nhiên, workflow triage và các KPI vận hành của giải pháp này vẫn là **đề xuất scoping**, không phải mô tả hệ thống nội bộ đã được Vinhomes xác nhận.

---

# Phase 3 — DEEP-DIVE

## 3.1 Quy trình hiện tại Mapping

### Quy trình hiện tại

```text
┌──────────────────────────┐
│ 1. Cư dân gửi phản ánh   │
│    trên App              │
│    ⏱ [GIẢ ĐỊNH] 1 phút   │
└────────────┬─────────────┘
             │
             │ 🔄 Handoff: App → hàng đợi CSKH
             ▼
┌──────────────────────────┐
│ 2. CSKH mở & đọc ticket  │
│    ⏱ [GIẢ ĐỊNH] 2 phút   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────────┐
│ 3. Phân loại vấn đề          │
│    🔴 BOTTLENECK             │
│    ⏱ [GIẢ ĐỊNH] 2 phút      │
└────────────┬─────────────────┘
             │ 🔄 Handoff
             ▼
┌──────────────────────────────┐
│ 4. Xác định tòa nhà/nhóm     │
│    🔴 BOTTLENECK             │
│    ⏱ [GIẢ ĐỊNH] 2 phút      │
└────────────┬─────────────────┘
             │
             ▼
┌──────────────────────────┐
│ 5. Điều hướng + soạn     │
│    phản hồi ban đầu      │
│    ⏱ [GIẢ ĐỊNH] 1 phút   │
└──────────────────────────┘

Thời gian xử lý thủ công ước tính:
≈ 8 phút/ticket [GIẢ ĐỊNH]
```

### Mức độ bằng chứng của từng bước

| Thành phần | Trạng thái bằng chứng | Căn cứ |
|---|---|---|
| Vinhomes Resident là kênh phục vụ cư dân | ✅ Được hỗ trợ bởi nguồn công khai | Vinhomes Annual Report 2024; Vinhomes Investor Presentation |
| Có “support requests” trên ứng dụng | ✅ Có bằng chứng lịch sử công khai | Vinhomes Investor Presentation 3Q2020 ghi >22.000 yêu cầu hỗ trợ trong ứng dụng |
| CSKH đọc → phân loại → điều hướng | ⚠️ **Mô hình scoping** | Không có log/workflow nội bộ trong bộ tài liệu lab |
| 8 phút/ticket | ⚠️ **[GIẢ ĐỊNH]** | Chưa có baseline thực tế |
| Các bước và thứ tự cụ thể | ⚠️ **[GIẢ ĐỊNH]** | Cần phỏng vấn stakeholder hoặc quan sát quy trình |

Vinhomes từng mô tả Vinhomes Resident là một nền tảng toàn diện cho cư dân và là cầu nối giữa cư dân với Ban Quản lý. Tài liệu của Vinhomes cũng nhắc tới các nhóm vận hành như Chăm sóc khách hàng, Kỹ thuật, An ninh và House Keeping. Điều này hỗ trợ **bối cảnh khái niệm** cho việc có một luồng tiếp nhận → điều hướng tới nhóm xử lý; nó **không chứng minh** rằng workflow nội bộ hiện tại chính xác từng bước như mô hình ở trên. [Nguồn: Vinhomes; xem Danh mục nguồn.]

### Bottleneck chính

Điểm kém hiệu quả cốt lõi được **đặt giả thuyết** không đơn thuần là “viết phản hồi”, mà là **chuyển ngôn ngữ tự nhiên, không có cấu trúc của cư dân thành category + team phụ trách + thông tin ticket đủ nhất quán**.

Các ví dụ dưới đây chỉ nhằm minh họa, không phải log vận hành của Vinhomes:

- “Đèn hành lang tầng 12 bị hư” → facility/điện.
- “Xe tôi bị chặn ở hầm” → bãi xe/an ninh/quyền ra vào.
- “Phí này sao tháng này lại tăng?” → phí/quản lý.
- “Nhà bên cạnh khoan đêm” → hàng xóm/tiếng ồn/quy định cộng đồng.

---

## 3.2 Problem Statement — 6 Fields

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | CSKH / điều phối viên tiếp nhận phản ánh của cư dân và ban quản lý tòa nhà. **[Mô hình scoping]** |
| **2. Current Workflow** | Cư dân gửi ticket → CSKH đọc nội dung → phân loại → xác định tòa nhà/bộ phận phụ trách → chuyển ticket và soạn phản hồi. **[Mô hình scoping; cần validation]** |
| **3. Bottleneck** | Phân loại intent, trích xuất entity (tòa nhà, khu vực, thời gian, vấn đề) và xác định queue/team phụ trách. **[Giả thuyết cần test]** |
| **4. Business Impact** | Ticket triage chậm làm tăng thời gian chờ và nguy cơ chuyển sai team. **[GIẢ ĐỊNH]** baseline 8 phút/ticket; cần xác nhận từ logs trước pilot. |
| **5. Success Metric** | (a) median triage time <2 phút; (b) routing accuracy ≥95% trên tập test có ground truth; (c) 100% ticket nhạy cảm hoặc có tác động cao được chuyển HITL; (d) JSON schema validity 100% trong prototype test. **Các giá trị là target/acceptance criteria của prototype, không phải KPI đã công bố của Vinhomes.** |
| **6. Operational Boundary** | AI chỉ được classify/extract/recommend/draft. AI **không** được tự phê duyệt khoản phí, kết luận tranh chấp, cam kết bồi thường, thay đổi dữ liệu cư dân, hoặc tự gửi phản hồi ra ngoài. Ticket nhạy cảm hoặc confidence thấp phải chuyển HITL/manual fallback. **[Thiết kế an toàn của nhóm]** |

---

## 3.3 Độ phù hợp với AI

### Ma trận độ phù hợp AI

| Lựa chọn | Mức phù hợp | Lý do |
|---|---|---|
| Rule / State-Machine | **Lớp bắt buộc** | Các mapping cố định, policy, blacklist/allowlist và escalation cần lớp quyết định xác định. |
| **LLM Feature** | **Chính** | Mạnh ở hiểu ngôn ngữ tự nhiên, chuẩn hóa, trích xuất và soạn thảo. |
| Agentic Loop | **Không cần** | Workflow đã có các bước cố định; thực thi tự trị nhiều bước làm tăng rủi ro mà chưa tạo thêm giá trị rõ ràng. |

### Kiến trúc đề xuất

**Hybrid: Rule + LLM Feature + HITL**

1. **Pre-check / rules:** kiểm tra schema, required fields, từ khóa nhạy cảm và các tuyến xử lý xác định trước.
2. **LLM:** phân loại issue, trích xuất entity, tạo draft ngắn gọn.
3. **Policy layer:** loại output vi phạm boundary.
4. **HITL:** CSKH xác nhận route + draft.
5. **Hệ thống:** chỉ sau khi con người phê duyệt mới thực hiện thao tác nghiệp vụ tiếp theo.

### Future-State Flow

```text
┌──────────────────────┐
│ 1. Nhận ticket       │
│    từ App             │
└──────────┬───────────┘
           │
           ▼
┌────────────────────────────┐
│ 2. Pre-check / Rules       │
│    - kiểm tra schema       │
│    - kiểm tra nhạy cảm     │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ 3. 🔵 LLM Feature          │
│    - phân loại             │
│    - trích xuất            │
│    - đề xuất queue         │
│    - soạn draft             │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ 4. 🔎 Policy / Boundary    │
│    Kiểm tra output         │
└────────────┬───────────────┘
             │
        ┌────┴────┐
        │         │
        ▼         ▼
   Confidence    Nhạy cảm /
      cao        không chắc chắn
        │         │
        │         ▼
        │   🟢 HITL / CSKH review
        │         │
        └────┬────┘
             ▼
┌────────────────────────────┐
│ 5. 🟢 Con người xác nhận   │
│    route + draft            │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ 6. Hoàn tất thao tác       │
│    nghiệp vụ trong hệ thống │
└────────────────────────────┘

↩️ Fallback:
Nếu LLM lỗi / output không hợp lệ /
confidence thấp → quay về route thủ công.
```

### Vì sao chọn LLM Feature thay vì Agent?

Đây là **kết luận thiết kế của nhóm**, phù hợp với nguyên tắc “Problem First, AI Second” của Lab: workflow được giả định có cấu trúc rõ, nên chỉ cần dùng LLM ở nơi ngôn ngữ tự nhiên gây khó cho rule-based thuần túy; routing và policy vẫn nên được kiểm soát bằng luật/hệ thống. [Nguồn nội bộ Lab: `03-inspiration-kit.md`; `01-worksheet.md`.]

---

# Phase 5 — EVALUATE

## AI Readiness Checklist

| # | Tiêu chí | Đánh giá | Ghi chú |
|---|---|---|---|
| 1 | Có dữ liệu mẫu/logs sạch để test? | ⚠️ **Chưa xác nhận** | Bộ tài liệu lab không cung cấp log Vinhomes. Cần dataset đã ẩn danh + ground truth. |
| 2 | Rủi ro khi AI sai có nằm trong tầm kiểm soát? | ✅ **Có thể kiểm soát** | Có HITL, policy layer, schema validation và manual fallback. **Đây là đánh giá thiết kế, cần test thực tế.** |
| 3 | Stakeholders sẵn sàng thay đổi workflow? | ⚠️ **Chưa xác nhận** | Cần xác nhận với CSKH/ban quản lý trước pilot. |

## Quyết định cuối cùng

### ✅ **NOT YET — Cần tích lũy thêm dữ liệu/xác lập baseline**

### Justification

Bài toán có **AI fit khá rõ**, scope nhỏ và có thể thiết kế ranh giới vận hành chặt chẽ. Tuy nhiên, theo đúng tiêu chí lab, hiện chưa có dữ liệu/log nội bộ Vinhomes để chứng minh baseline, routing accuracy, volume, hoặc mức cải thiện thực tế.

Vì vậy quyết định phù hợp hơn là **NOT YET**, thay vì GO dựa trên các con số giả định. Sau khi có dataset đã ẩn danh, ground truth và baseline triage time, có thể chạy một prototype offline để kiểm tra:

- routing accuracy;
- intent classification quality;
- mức độ đầy đủ của entity extraction;
- tỷ lệ case phải chuyển HITL;
- tỷ lệ output JSON hợp lệ;
- thời gian xử lý so với baseline thủ công.

> **Kết luận:** Problem rõ + AI fit hợp lý + boundary kiểm soát được, nhưng **thiếu evidence thực tế để biện minh cho GO**. Do đó **NOT YET** là quyết định trung thực hơn trong giai đoạn scoping.

---

# Danh mục nguồn tham chiếu

1. **Nguồn nội bộ Lab — `01-worksheet.md`**: yêu cầu workflow mapping, 6-field Problem Statement, AI Fit, Future Flow, HITL, Fallback và Evaluate.
2. **Nguồn nội bộ Lab — `02-deliverable-example.md`**: chuẩn chất lượng đầu ra và cách thể hiện một case Deep-Dive hoàn chỉnh; dùng để tham chiếu cấu trúc, không coi là bằng chứng cho Vinhomes.
3. **Nguồn nội bộ Lab — `03-inspiration-kit.md`**: use case “Phân loại & Điều hướng phản ánh cư dân” và nguyên tắc Problem First, AI Second.
4. **Vinhomes Annual Report 2024**: Vinhomes Resident có khoảng 130.000 tài khoản, >86% căn hộ sử dụng và ~97% active monthly. https://gcp-cdn.vinhomes.vn/cms-data/VIE_Vinhomes%20AR%202024_250411_compressed.pdf
5. **Vinhomes Investor Presentation 3Q2020**: hơn 22.000 in-app support requests trong giai đoạn được báo cáo. https://gcp-cdn.vinhomes.vn/cms-data/2020-10-29-VHM-3Q20-Earnings-Presensentation-vUP.pdf
6. **Vinhomes — “Những lá thư cảm ơn…”**: mô tả Vinhomes Resident là cầu nối với Ban Quản lý và đề cập các nhóm CSKH, Kỹ thuật, An ninh, House Keeping. https://vinhomes.vn/vi/nhung-la-thu-cam-on-tu-cu-dan-va-dich-vu-tu-trai-tim-vinhomes

> **Quy ước đọc báo cáo:** “✅ Nguồn xác nhận” = có bằng chứng từ nguồn được dẫn; “⚠️ Mô hình scoping” = nhóm đang đề xuất workflow; “[GIẢ ĐỊNH]” = số liệu tạm thời, phải được xác thực trước pilot/production.
