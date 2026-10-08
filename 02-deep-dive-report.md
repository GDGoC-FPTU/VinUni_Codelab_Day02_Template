# 02 — Deep-Dive Report (Nhóm)

> Vin Smart Future — AI Product Scoping Lab
> **Bài toán chọn Deep-Dive:** Xanh SM — AI hỗ trợ tổng đài tài xế, tách xử lý 2 nhóm case riêng biệt: **(a) Khẩn cấp** (an toàn/tai nạn) và **(b) Huỷ cuốc** (từ Quick Problem Card #3).

---

## 🏗️ Phase 3 — DEEP-DIVE

### 3.1. Current-State Workflow Mapping

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │     │ Bước 3       │     │ Bước 4       │
│ Tài xế gửi   │     │ Yêu cầu xếp  │     │ Nhân viên đọc│     │ Nhân viên xác│
│ yêu cầu vào  │ ──→ │ vào hàng đợi │ ──→ │ tin theo thứ │ ──→ │ định case    │
│ kênh chat    │ 🔄  │ chung (FIFO) │     │ tự đến       │     │ thuộc nhóm   │
│ chung trên App│    │ — không phân │     │              │     │ nào: (a) hay │
│              │     │ biệt loại case│    │              │     │ (b)          │
│ Ai: Tài xế   │     │ Ai: Hệ thống │     │ Ai: Nhân viên│     │ Ai: Nhân viên│
│ ⏱ tức thời   │     │ ⏱ chờ TB     │     │ ⏱ 2 phút 🔴  │     │ ⏱ 1 phút 🔴  │
│              │     │ 3-5 phút     │     │ (đọc tin cũ  │     │ (phân loại   │
│              │     │              │     │ trước)       │     │ sau khi đọc) │
│ In: Nội dung │     │ In: Tin nhắn │     │ In: Nội dung │     │ In: Nội dung │
│ yêu cầu      │     │ thô          │     │ tin nhắn     │     │ đã đọc       │
│ Out: Tin nhắn│     │ Out: Vị trí  │     │ Out: Hiểu nội│     │ Out: Nhãn (a)│
│ vào hệ thống │     │ trong hàng đợi│    │ dung         │     │ Khẩn cấp hoặc│
│              │     │              │     │              │     │ (b) Huỷ cuốc │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
                                                                       │
                                              ┌────────────────────────┴───────────────────────┐
                                              ▼                                                  ▼
                                    ┌──────────────────┐                              ┌──────────────────┐
                                    │ Bước 5a — Nhóm (a)│                              │ Bước 5b — Nhóm (b)│
                                    │ 🔄 Escalate cho   │                              │ Xử lý huỷ cuốc    │
                                    │ đội an toàn        │                              │ thủ công: cập nhật│
                                    │ Ai: Nhân viên      │                              │ hệ thống/hoàn phí │
                                    │ ⏱ 1 phút           │                              │ Ai: Nhân viên      │
                                    │                    │                              │ ⏱ 3-4 phút 🔴     │
                                    └──────────────────┘                              └──────────────────┘
🔴 = Bottleneck   🔄 = Handoff
⏱ Nhóm (a) Khẩn cấp: trung bình ~7 phút/lượt để phát hiện + escalate.
⏱ Nhóm (b) Huỷ cuốc: trung bình ~5-6 phút/lượt (đọc + phân loại + xử lý thủ công).
```

---

### 3.2. Problem Statement (6-field) & Metrics

| Field | Nội dung chi tiết |
|---|---|
| **1. Actor / Operator** | Nhân viên trực tổng đài hỗ trợ tài xế (Driver Support) tại Trung tâm Điều hành Xanh SM. |
| **2. Current Workflow** | Tài xế gửi mọi loại yêu cầu vào cùng một kênh chat hỗ trợ trên App, gồm 2 nhóm bản chất khác nhau: **(a) Case khẩn cấp** (tai nạn, va chạm, mất an toàn) và **(b) Yêu cầu huỷ cuốc** thông thường (khách không xuất hiện, sự cố xe nhẹ...). Nhân viên xử lý tuần tự theo thứ tự đến (FIFO); chỉ khi đọc xong nội dung mới xác định được case thuộc nhóm (a) hay (b), rồi mới xử lý theo đúng quy trình riêng của từng nhóm. Không có công cụ phân loại/định tuyến tự động. |
| **3. Bottleneck** | Bước đọc và phân loại case vào nhóm (a)/(b) (bước 3-4): vì xử lý tuần tự theo FIFO, một case khẩn cấp (nhóm a) gửi đến sau nhiều yêu cầu huỷ cuốc (nhóm b) sẽ bị "chôn" trong hàng đợi; đồng thời khối lượng lớn case huỷ cuốc (nhóm b) — vốn có thể xử lý theo policy rõ ràng — vẫn chiếm nhiều thời gian xử lý thủ công lặp lại của nhân viên. |
| **4. Business Impact** | Nhóm (a): trung bình mỗi ca khẩn cấp mất 5-7 phút mới được phát hiện và escalate đúng đội xử lý, ảnh hưởng an toàn tài xế/hành khách, nguy cơ vi phạm SLA an toàn nội bộ (~15-20 ca/ngày tại Hà Nội). Nhóm (b): hàng trăm yêu cầu huỷ cuốc/ngày tốn ~5-6 phút xử lý thủ công mỗi case, chiếm phần lớn thời gian của đội hỗ trợ, gián tiếp kéo dài thời gian phát hiện case khẩn cấp. |
| **5. Success Metric** | Nhóm (a) Khẩn cấp: giảm thời gian phát hiện + escalate từ ~7 phút xuống dưới 30 giây, độ chính xác phân loại ≥ 95% (Recall ưu tiên hơn Precision).<br>Nhóm (b) Huỷ cuốc: tự động xử lý ≥ 70% case theo đúng policy mà không cần nhân viên can thiệp trực tiếp (Efficiency). |
| **6. Operational Boundary** | AI được phép đọc và phân loại mọi yêu cầu vào đúng nhóm (a) Khẩn cấp hoặc (b) Huỷ cuốc theo thời gian thực. Với nhóm (a): chỉ được đẩy cảnh báo lên đầu hàng đợi, **CẤM** tự soạn/gửi phản hồi hay tự đóng case (bắt buộc HITL). Với nhóm (b): chỉ được tự động xử lý khi case khớp đúng policy rõ ràng (ví dụ khách không xuất hiện sau X phút chờ); **CẤM** tự huỷ cuốc trong trường hợp mơ hồ/có tranh chấp — phải chuyển cho nhân viên xử lý. |

---

### 3.3. Future-State Flow & AI Fit

* **AI Fit:** Chọn **Agentic Loop** — vì hệ thống không dừng ở một bước phân loại đơn thuần mà phải: (1) phân loại case vào đúng nhóm (a)/(b), (2) với nhóm (b) tự thực hiện hành động xử lý theo policy nếu đủ điều kiện, và (3) với nhóm (a) định tuyến ưu tiên kèm cảnh báo — mỗi nhóm có một chuỗi hành động và ranh giới HITL khác nhau. Không dùng thuần Rule-based vì cách tài xế mô tả case rất đa dạng về ngôn ngữ.
* **Quy trình tương lai (Future-State):**

```text
┌──────────────┐     ┌──────────────┐
│ Bước 1       │     │ Bước 2       │
│ Tài xế gửi   │     │ 🔵 AI đọc &  │
│ yêu cầu vào  │ ──→ │ phân loại vào│
│ kênh chat    │     │ nhóm (a)/(b) │
│              │     │ real-time    │
└──────────────┘     └──────┬───────┘
                             │
             ┌───────────────┴───────────────┐
             ▼                                ▼
   ┌──────────────────┐            ┌──────────────────────┐
   │ Nhóm (a) Khẩn cấp │            │ Nhóm (b) Huỷ cuốc     │
   │ 🔵 Đẩy lên đầu    │            │ 🔵 Kiểm tra khớp      │
   │ hàng đợi + cảnh   │            │ policy huỷ cuốc rõ    │
   │ báo đỏ            │            │ ràng?                 │
   └────────┬──────────┘            └──────┬─────────┬─────┘
            ▼                          Có  ▼         ▼ Không/mơ hồ
   ┌──────────────────┐      ┌──────────────────┐  ┌──────────────────┐
   │ 🟢 Nhân viên      │      │ 🔵 AI tự động xử  │  │ 🟢 Nhân viên xử   │
   │ (HITL) xác nhận &  │      │ lý (cập nhật hệ   │  │ lý thủ công như   │
   │ xử lý ngay case    │      │ thống/hoàn phí)   │  │ cũ                │
   └──────────────────┘      └──────────────────┘  └──────────────────┘

↩️ Fallback: Nếu AI không chắc chắn (confidence thấp) ở bước phân loại, hoặc
lỗi hệ thống, case tự động chuyển về hàng đợi thủ công cho nhân viên xử lý
như quy trình cũ — không mất dữ liệu, không tự ý hành động khi không chắc.
```

---

## 🏁 Phase 5 — EVALUATE

### AI Readiness Checklist:
1. [x] Chúng tôi có sẵn dữ liệu mẫu/logs sạch để test? — Có log lịch sử chat hỗ trợ tài xế (cả case khẩn cấp lẫn huỷ cuốc) từ hệ thống hiện tại để dùng làm test case và tinh chỉnh prompt/policy.
2. [x] Rủi ro khi AI sai có nằm trong tầm kiểm soát (qua HITL hoặc Fallback)? — Có. Nhóm (a) luôn bắt buộc nhân viên xác nhận trước khi đóng case; nhóm (b) AI chỉ tự hành động khi khớp policy rõ ràng, còn lại chuyển về người xử lý.
3. [ ] Stakeholders sẵn sàng thay đổi quy trình làm việc cũ? — Cần đào tạo lại nhân viên trực tổng đài để quen với việc AI tự xử lý một phần case huỷ cuốc và ưu tiên theo cảnh báo AI thay vì FIFO thuần túy.

### Quyết định cuối cùng của Ban Giám Đốc Vin Smart Future:
[x] **GO (Bắt đầu xây dựng Prototype):** Bắt đầu phát triển với scope hẹp — ưu tiên hoàn thiện nhóm (a) Khẩn cấp trước (rủi ro an toàn cao, giá trị rõ), sau đó mở rộng tự động hoá nhóm (b) Huỷ cuốc.
[ ] **NOT YET (Cần tích lũy thêm dữ liệu/xác lập baseline):**
[ ] **NO-GO (Không khả thi / Rule-based tốt hơn):**

**Justification (Lý giải quyết định dựa trên bằng chứng kỹ thuật và chi phí):**
> Bài toán có tác động rõ ràng và đo lường được ở cả hai nhóm case (an toàn cho nhóm khẩn cấp, hiệu suất vận hành cho nhóm huỷ cuốc). Kiến trúc Agentic Loop tuy phức tạp hơn LLM đơn thuần nhưng vẫn kiểm soát được rủi ro nhờ ranh giới rõ ràng theo từng nhóm: HITL bắt buộc cho mọi case khẩn cấp, và AI chỉ tự hành động với case huỷ cuốc khớp policy tường minh — mọi trường hợp mơ hồ đều có fallback về quy trình thủ công cũ. Chi phí triển khai thấp vì tận dụng log chat có sẵn để test cả hai nhóm case trước khi mở rộng.
