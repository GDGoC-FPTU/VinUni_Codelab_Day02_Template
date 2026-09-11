<<<<<<< HEAD
# Phase 3 — DEEP-DIVE (Báo cáo Phân tích Chuyên sâu)

**Bài toán lựa chọn:** Phân loại và định tuyến tự động ticket khiếu nại của khách hàng.
**Công ty:** Xanh SM (Tham chiếu từ Card #3 trong file Problem Scan)

## 3.1. Current-State Workflow Mapping

**Mô tả quy trình hiện tại trước khi dùng AI (Quy trình thủ công xử lý Ticket khiếu nại):**

**Chi tiết các bước:**
1. **Tiếp nhận:** Hệ thống ghi nhận ticket khiếu nại từ khách hàng (qua App/Web/Call). Output: Mã ticket thô và nội dung. (Hệ thống thực hiện - 0 phút).
2. **🔄 Handoff 1:** Ticket mới được đưa vào hàng đợi chờ xử lý của nhân viên CSKH (Tier 1).
3. **Đọc và Phân tích:** Nhân viên CSKH mở ticket, đọc toàn bộ nội dung mô tả sự việc của khách hàng. 
   - *Input:* Nội dung chữ hoặc ghi âm. 
   - *Output:* Hiểu được vấn đề là gì (Thái độ tài xế, Lỗi app, Quên đồ, Lỗi thanh toán...). (Nhân viên CSKH thực hiện - 1.5 phút).
4. **🔴 Bottleneck - Phân loại & Mức độ:** Nhân viên CSKH đối chiếu nội dung với ma trận lỗi của công ty để xác định chính xác danh mục khiếu nại và độ ưu tiên (SLA xử lý). 
   - *Input:* Sự hiểu biết về vấn đề. 
   - *Output:* Tag danh mục, Tag độ ưu tiên được chọn trong hệ thống. (Nhân viên CSKH thực hiện - 1 phút). *Bước này dễ bị nhầm lẫn do mỗi nhân viên có cảm quan đánh giá khác nhau, đặc biệt khi quá tải.*
5. **🔄 Handoff 2:** Chuyển giao ticket đã phân loại cho bộ phận chuyên môn liên quan (Vận hành, Kế toán, Công nghệ, v.v.).
6. **Xử lý & Đóng vé:** Bộ phận chuyên môn tiếp nhận, xử lý vấn đề, sau đó báo lại bộ phận CSKH để phản hồi kết quả cho khách và đóng vé. (Bộ phận chuyên môn thực hiện - 5-15 phút, không tính vào thời gian phân loại).

**Tổng kết Quy trình Hiện tại (Phần Phân loại & Định tuyến):**
- **Tổng thời gian mỗi lượt:** Trung bình **2.5 - 3 phút/ticket**.
- **Điểm chuyển giao (🔄 Handoff):** Giữa hệ thống tiếp nhận với NV CSKH, và giữa NV CSKH với bộ phận xử lý chuyên môn.
- **Điểm nghẽn (🔴 Bottleneck):** Bước 3 & 4 (Đọc hiểu nội dung và Phân loại). Trong các khung giờ cao điểm, lượng vé tăng vọt khiến hàng đợi dài, nhân viên bị áp lực dẫn đến tốc độ chậm và nguy cơ phân loại sai cao.

---

## 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên Chăm sóc khách hàng (CSKH) tuyến đầu (Tier 1). |
| **2. Current Workflow** | Nhân viên mở từng ticket, đọc nội dung khiếu nại, tự phân tích suy luận và chọn danh mục lỗi, mức độ ưu tiên từ một menu hệ thống, sau đó bấm chuyển tiếp cho phòng ban tương ứng xử lý. |
| **3. Bottleneck** | Bước đọc hiểu nội dung ngôn ngữ tự nhiên (unstructured text) của khách hàng và ánh xạ nó với đúng quy định/phân loại của công ty. Thao tác lặp đi lặp lại hàng ngàn lần mỗi ngày, tốn thời gian và dễ sai sót. |
| **4. Business Impact** | - Khách hàng phải chờ lâu hơn để được giải quyết (vi phạm SLA tiếp nhận).<br>- Tốn chi phí nhân sự CSKH cho việc phân loại thủ công thay vì tập trung giải quyết vấn đề khó.<br>- Vé phân loại sai (vd: khiếu nại thái độ tài xế lại chuyển cho bộ phận kỹ thuật App) gây ping-pong giữa các phòng ban, làm tăng Thời gian xử lý (Turnaround Time) và giảm Chỉ số hài lòng (CSAT). |
| **5. Success Metric** | - 85% vé khiếu nại được phân loại và định tuyến tự động trong thời gian dưới 10s.<br>- Độ chính xác (Accuracy) của việc phân loại đạt >90% (tương đương hoặc hơn con người). |
| **6. Operational Boundary** | - **Được phép:** AI tự động đọc hiểu text/transcript, gán thẻ tag danh mục, đánh giá thái độ (sentiment) của khách.<br>- **TUYỆT ĐỐI không được:** AI không được tự ý gửi email/tin nhắn phản hồi hứa hẹn bồi thường tiền bạc cho khách, không được tự ý thao tác hủy chuyến hay khóa tài khoản tài xế.<br>- **Điểm cần duyệt:** Những ticket mà AI phân tích có độ tự tin (confidence score) thấp hơn 75% hoặc chứa từ khóa nhạy cảm (pháp lý, an toàn) phải được giữ lại cho con người duyệt. |

---

## 3.3. Future-State Flow & AI Fit

**Xác định mức AI Fit (AI-Fit Matrix):**
- [ ] Rule / State-Machine
- [x] LLM Feature *(Sử dụng khả năng Natural Language Understanding của LLM để phân tích văn bản và phân loại vào các danh mục định sẵn).*
- [ ] Agentic Loop

**Sơ đồ Future-State Flow:**

1. **Tiếp nhận:** Khách hàng gửi khiếu nại lên App/Web.
2. 🔵 **AI Step (LLM Classification):** Ngay khi ticket sinh ra, hệ thống gọi API tới LLM. LLM đọc nội dung khiếu nại, phân tích đánh giá sắc thái (Sentiment) và phân loại theo danh mục có sẵn.
   - *Output:* Category Tag, Priority Score, Confidence Score.
3. **Phân luồng tự động dựa trên độ tự tin (Confidence):**
   - **Luồng 1 (Confidence >= 75%):** Hệ thống tự động gắn thẻ và định tuyến thẳng đến bộ phận chuyên môn phù hợp. *(Bỏ qua hoàn toàn bước đọc và phân loại thủ công của NV CSKH Tier 1).*
   - **Luồng 2 (Confidence < 75% hoặc có yếu tố rủi ro cao) — ↩️ Fallback:** Đẩy ticket vào hàng đợi duyệt thủ công.
4. 🟢 **Human Step (HITL):** Nhân viên CSKH xem xét các vé thuộc Luồng Fallback. Tại đây, LLM đã đưa ra trước *gợi ý phân loại*, nhân viên chỉ việc đọc nhanh để xác nhận (Approve) hoặc sửa đổi (Correct). Dữ liệu sau khi sửa sẽ được lưu làm phản hồi giúp cải thiện mô hình.
5. **🔄 Handoff 2:** Chuyển giao ticket đã phân loại (từ Luồng 1 hoặc sau bước HITL) tới bộ phận chuyên môn.
6. **Xử lý & Đóng vé:** Bộ phận chuyên môn xử lý như bình thường.
=======
# 02 — Deep-Dive Report: AI Vehicle Health & Predictive Maintenance

## Executive summary

Đề xuất phát hiện sớm rủi ro sức khỏe xe VinFast từ telemetry, DTC, lịch sử dịch vụ và outcome sửa chữa đã gán nhãn. Hệ thống tạo **risk score + evidence + bản nháp khuyến nghị**, không tự chẩn đoán an toàn, sửa/điều khiển xe hay tự đặt lịch. Quyết định: **NOT YET production; GO offline pilot có kiểm soát**.

## 1. Current-state workflow

| Bước | Người/hệ thống | Hoạt động | Thời gian cần đo | Rủi ro/bottleneck |
|---:|---|---|---:|---|
| 1 | Xe/backend | Ghi telemetry, DTC và cảnh báo. | near-real-time đến theo lô | Mất kết nối, thiếu dữ liệu, schema/version không đồng nhất. |
| 2 | Chủ xe/CSKH | Chủ xe thấy cảnh báo hoặc gọi hỗ trợ; CSKH tạo ticket. | 2–5 phút | 🔄 Handoff; mô tả thiếu bối cảnh. |
| 3 | Kỹ thuật viên triage | Đọc DTC, lịch sử và xu hướng thông số để ưu tiên. | 10–20 phút (giả định) | 🔴 Dữ liệu nhiều chiều, khó thấy trend tiến triển. |
| 4 | Cố vấn dịch vụ | Liên hệ chủ xe, đề xuất kiểm tra/đặt lịch theo SOP. | 5–10 phút | 🔄 Không cam kết chẩn đoán/ETA khi chưa xác minh. |
| 5 | Xưởng | Kiểm tra thực tế, sửa chữa, ghi root cause/outcome. | tùy lỗi | Nhãn feedback chưa chuẩn khiến ML học sai. |

VinFast công bố chẩn đoán lỗi từ xa và thông báo tới ứng dụng/trung tâm dịch vụ; điều này là bối cảnh công khai, không chứng minh sẵn dataset predictive-maintenance hoàn chỉnh. [Nguồn](https://vinfastauto.com/vn_vi/tinh-nang-moi-cham-soc-khach-hang-tu-dong-vf-e34)

## 2. Problem statement — 6 fields

| Field | Nội dung |
|---|---|
| Actor / Operator | Kỹ thuật viên triage, cố vấn dịch vụ, reliability engineer; chủ xe chỉ nhận thông báo sau duyệt. |
| Current Workflow | Con người đọc DTC/cảnh báo cùng lịch sử xe, sau đó theo dõi, hướng dẫn, đặt lịch hoặc escalate theo SOP. |
| Bottleneck | Telemetry có thể báo trend bất thường trước một rule ngưỡng; không thể đọc sâu mọi xe mỗi ngày. |
| Business Impact | Có thể giảm sự cố bất ngờ, xe nằm xưởng và thời gian triage; chưa gán giá trị tiền tệ khi chưa có dữ liệu nội bộ. |
| Success Metric | Recall ≥90% cho “inspect within 24h”; false-positive ≤15%; lead time trung vị ≥24h trước event xác nhận; 100% alert có evidence/audit ID. |
| Operational Boundary | Chỉ risk triage/draft. Không ra lệnh dừng xe, xóa DTC, cập nhật firmware, điều khiển từ xa, tự đặt lịch hay kết luận “xe an toàn”. Policy DTC mức cao luôn override model và escalate theo SOP. |

## 3. Future-state flow & AI fit

1. **Data-quality gate (Rule):** kiểm tra consent, schema, freshness, firmware version và missingness. Không đạt → `needs_human_review`, không scoring.
2. **Safety policy (Rule):** DTC/điều kiện có severity cao đã được kỹ sư duyệt → escalation theo SOP, không chờ ML.
3. **Risk model (time-series ML):** dữ liệu hợp lệ tạo anomaly score và risk trong horizon xác định, với feature/model version đã phê duyệt.
4. **Evidence builder:** nêu feature thay đổi, độ mới dữ liệu, DTC liên quan và case lịch sử đã ẩn danh; không nói là root cause.
5. **LLM explanation:** chuyển evidence cấu trúc thành JSON/draft; không suy diễn raw telemetry hoặc khuyến nghị ngoài policy.
6. **🟢 Human-in-the-loop:** kỹ thuật viên chấp nhận/sửa/bác bỏ alert; cố vấn dịch vụ mới gửi thông báo/đề xuất lịch.
7. **Feedback loop:** outcome kiểm tra/sửa chữa được chuẩn hóa thành nhãn; review bias/drift trước retrain.
8. **↩️ Fallback:** model timeout, data stale, out-of-distribution hay conflict → chỉ hiện dữ liệu gốc/checklist và route SOP thủ công.

| Thành phần | Loại | Lý do |
|---|---|---|
| Consent, schema, DTC severity, quyền hành động | Rule/state machine | Policy rõ, cần audit và độ tin cậy cao. |
| Anomaly/risk prediction | Time-series ML | Pattern đa biến theo thời gian, rule đơn giản khó bao phủ. |
| Tóm tắt cho người dùng/kỹ thuật viên | LLM feature | Hữu ích cho ngôn ngữ, bị giới hạn bởi evidence. |
| Đặt lịch, điều khiển xe, retrain | Không dùng agent | Quá rủi ro cho pilot. |

## 4. Data, model và evaluation plan

| Hạng mục | Thiết kế pilot |
|---|---|
| Dữ liệu | Telemetry pseudonymized: timestamp, model/version, DTC, battery/thermal/charging signals do kỹ sư duyệt, odometer, service outcome; tách PII/GPS chính xác. |
| Nhãn | Kỹ thuật viên xác nhận: no-issue, inspect-soon, inspect-24h, safety escalation; lưu lý do và SOP version. |
| Split | Time-based theo xe để tránh leakage; đánh giá riêng theo model/firmware/mùa. |
| Baseline | Rule theo DTC/threshold hiện hữu; chỉ dùng model nếu cải thiện recall/lead-time ở false-positive chấp nhận được. |
| Red-team | Telemetry thiếu/giả, model-version lạ, yêu cầu xóa lỗi/khẳng định xe an toàn, prompt injection trong ghi chú dịch vụ. |
| Monitoring | Drift, missingness, calibration, alert volume, acceptance rate, false negative hậu kiểm; kill switch về baseline rule. |

## 5. Readiness & decision

- [ ] Dataset có consent, data contract và nhãn outcome đáng tin: **chưa xác nhận**.
- [ ] Owner kỹ thuật phê duyệt feature/DTC, SOP escalation và quyền truy cập: **chưa xác nhận**.
- [x] Có thể giới hạn rủi ro bằng rule override, HITL, audit và kill switch.
- [ ] Baseline rule và tiêu chí rollback đã ký duyệt: **cần thiết lập**.

### Quyết định: NOT YET production; GO offline pilot

Chỉ pilot khi có data governance, nhãn chất lượng, baseline rõ và review kỹ thuật. Production cần KPI offline, shadow mode, safety review và bằng chứng không tăng false negative nghiêm trọng. [Ứng dụng VinFast đã công bố theo dõi/cảnh báo trạng thái xe](https://vinfastauto.com/vn_vi/quan-ly-xe-o-to-dien-qua-ung-dung-vinfast), nhưng đề xuất không giả định quyền truy cập hệ thống nội bộ.
>>>>>>> e7eabe7bddd44bf8100dba65595b10552b6e4c07
