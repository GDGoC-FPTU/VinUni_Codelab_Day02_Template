# 02 — Deep-Dive Report

## 1. Use Case

**Vinhomes — Phân loại và điều hướng phản ánh cư dân bằng AI**

Mục tiêu là dùng AI để hỗ trợ nhân viên tiếp nhận phản ánh tự nhiên của cư dân, xác định intent/category, trích xuất thông tin cần thiết và đề xuất bộ phận xử lý. AI không tự quyết định các trường hợp nhạy cảm.

> Các số liệu thời gian, volume và metric trong báo cáo này là **giả định cho bài lab/prototype** vì các file nguồn không cung cấp dữ liệu vận hành nội bộ đã xác minh.

---

## 2. Current-State Workflow Mapping

```text
Cư dân gửi phản ánh
        |
        v
[1] Nhân viên nhận ticket
    ~1 phút
        |
        v
[2] Đọc và hiểu nội dung
    ~3 phút
        |
        v
[3] Xác định category + bộ phận
    ~3 phút  🔴 BOTTLENECK
        |
        v
[4] Chuyển ticket
    ~1 phút
        |
        v
[5] Bộ phận xử lý
```

**Tổng giả định:** ~8 phút/ticket.

### Handoff

- Cư dân → hệ thống ticket.
- CSKH → bộ phận vận hành.
- Bộ phận tiếp nhận → nhân viên xử lý chuyên môn.

### Bottleneck

Bước 2–3: nhân viên phải đọc ngôn ngữ tự nhiên và tự suy luận category/bộ phận.

---

## 3. Problem Statement — 6 Fields

| Field | Nội dung |
|---|---|
| **1. Actor / Operator** | Nhân viên CSKH/ban quản lý tiếp nhận phản ánh của cư dân. |
| **2. Current Workflow** | Nhân viên đọc ticket, hiểu nội dung, xác định loại phản ánh, chọn bộ phận phụ trách rồi chuyển ticket. |
| **3. Bottleneck** | Phân loại và routing thủ công, đặc biệt với nội dung dài, mơ hồ hoặc có nhiều vấn đề cùng lúc. |
| **4. Business Impact** | Với baseline giả định 8 phút/ticket, khối lượng lớn có thể tạo tải đáng kể cho CSKH và làm chậm SLA xử lý ban đầu. |
| **5. Success Metric** | Giảm thời gian phân loại/routing xuống <1 phút/ticket; routing accuracy ≥95% trên tập test; 100% case nhạy cảm được chuyển HITL. |
| **6. Operational Boundary** | AI được phép phân loại, trích xuất thông tin và đề xuất routing. AI không được tự đưa ra quyết định pháp lý, tài chính, tranh chấp hoặc cam kết xử lý với cư dân. Các case không chắc chắn phải fallback về người. |

---

## 4. Rule vs LLM vs Agent

| Phương án | Ưu điểm | Nhược điểm | Đánh giá |
|---|---|---|---|
| Rule-based | Dễ kiểm thử, deterministic | Khó bao phủ ngôn ngữ tự nhiên và cách diễn đạt đa dạng | Tốt cho routing cuối |
| LLM Feature | Hiểu ngữ nghĩa, phân loại và trích xuất tốt | Có thể hallucinate, cần guardrails | **Phù hợp nhất** |
| Agentic Loop | Có thể tự thực hiện nhiều bước | Phức tạp và rủi ro không cần thiết | Không cần |

**Quyết định:** LLM làm lớp hiểu ngôn ngữ + Rule/Policy làm lớp kiểm soát routing.

---

## 5. Future-State Flow

```text
Cư dân gửi phản ánh
        |
        v
[1] Ticket Intake
        |
        v
[2] 🔵 AI classify + extract
        |
        v
[3] 🔵 Confidence / policy check
        |
   +----+----+
   |         |
 High      Low / Sensitive
   |         |
   v         v
[4] 🟢 HITL review    ↩️ Fallback
   |                   Nhân viên xử lý tay
   v
[5] Rule-based routing
   |
   v
[6] Chuyển bộ phận
```

### AI Step

LLM nhận nội dung ticket và trả JSON có schema cố định:

- category
- urgency
- extracted_entities
- suggested_department
- confidence
- requires_human_review
- reason

### Human-in-the-loop

Nhân viên duyệt kết quả trước khi ticket được chuyển tự động, đặc biệt khi confidence thấp hoặc category thuộc nhóm nhạy cảm.

### Fallback

Fallback về quy trình hiện tại nếu:
- model lỗi;
- output không đúng schema;
- confidence dưới ngưỡng;
- phát hiện nội dung nhạy cảm;
- thiếu thông tin quan trọng.

---

## 6. Operational Boundary

### AI được phép

1. Đọc nội dung ticket.
2. Phân loại intent.
3. Trích xuất thông tin.
4. Đề xuất bộ phận.
5. Tạo lý do ngắn gọn cho đề xuất.

### AI không được phép

1. Tự đưa ra kết luận pháp lý.
2. Tự xác nhận mức bồi thường/phí.
3. Tự cam kết thời gian giải quyết.
4. Tự xử lý tranh chấp quyền lợi.
5. Tự bỏ qua HITL khi confidence thấp.
6. Tự gửi phản hồi nhạy cảm cho cư dân.

---

# 7. Phase 5 — EVALUATE

## AI Readiness Checklist

| Câu hỏi | Đánh giá |
|---|---|
| Có dữ liệu mẫu/logs sạch để test? | **NOT YET** — cần tập ticket đã gán nhãn |
| Rủi ro AI sai có kiểm soát được? | **YES** — HITL + confidence threshold + fallback |
| Stakeholders sẵn sàng thay đổi workflow? | **CẦN XÁC NHẬN** qua pilot với CSKH |

## Quyết định

### **NOT YET — Cần tích lũy thêm dữ liệu/xác lập baseline**

Lý do:

1. Use case có AI fit tốt vì input là ngôn ngữ tự nhiên.
2. Rủi ro có thể kiểm soát bằng HITL và rule-based routing.
3. Tuy nhiên, bài lab không cung cấp dataset ticket thực tế đã gán nhãn.
4. Chưa thể tuyên bố accuracy ≥95% nếu chưa có test set.
5. Cần xây baseline rule-based trước, sau đó benchmark LLM.

### Điều kiện để chuyển sang GO

- Có tối thiểu một tập dữ liệu ticket đại diện đã được con người gán nhãn.
- Có taxonomy/category thống nhất.
- Có baseline rule-based.
- Có metric và test set cố định.
- Có pilot với HITL.
- Có cơ chế audit/log kết quả AI.

**Kết luận:** Đây là bài toán **có tiềm năng GO cho prototype**, nhưng quyết định ở thời điểm scoping là **NOT YET** cho production vì thiếu bằng chứng dữ liệu/baseline.
