const form = document.querySelector("#incident-form");
const panel = document.querySelector(".decision-panel");
const result = document.querySelector("#result");
const emptyResult = document.querySelector("#empty-result");
const submitButton = document.querySelector("#dispatch-button");
const statusBadge = document.querySelector("#decision-status");

const actionLabels = {
  recommend_station: "Đề xuất trạm",
  dispatch_mobile_charger: "Điều xe sạc lưu động",
  dispatch_emergency_rescue: "Cứu hộ khẩn cấp",
  ask_for_information: "Yêu cầu thêm dữ liệu",
  manual_review: "Kiểm tra thủ công",
};

const riskLabels = {
  dispatch_emergency_rescue: "Khẩn cấp",
  dispatch_mobile_charger: "Cao",
  manual_review: "Cần xác minh",
  ask_for_information: "Thiếu dữ liệu",
  recommend_station: "Có kiểm soát",
};

function text(id, value) {
  document.querySelector(`#${id}`).textContent = value ?? "—";
}

function formatConnectors(station) {
  const connectors = station?.connectors || [];
  return connectors.length ? connectors.join(" · ") : "Cổng chưa rõ";
}

function showResult(data) {
  const action = data.action || "manual_review";
  const context = data.context || {};
  const station = data.recommended_station;
  const flags = data.safety_flags || [];
  const isDanger = action === "dispatch_emergency_rescue" || action === "dispatch_mobile_charger";

  emptyResult.hidden = true;
  result.hidden = false;
  statusBadge.textContent = isDanger ? "Cần xử lý ngay" : "Chờ người duyệt";
  statusBadge.className = `decision-status ${isDanger ? "is-danger" : "is-ready"}`;
  text("battery-node", context.battery_percent != null ? `${context.battery_percent}%` : "—%");
  text("action-node", action === "recommend_station" ? "TRẠM" : "XỬ LÝ");
  text("action-value", actionLabels[action] || action);
  text("risk-value", riskLabels[action] || (flags.length ? "Cần lưu ý" : "Có kiểm soát"));
  const rangeLimit = context.demo_range_limit_km ?? context.conservative_range_km;
  text("range-value", rangeLimit != null ? `${rangeLimit} km · mô phỏng` : "Không áp dụng");
  text("reason-value", data.reason);
  text("message-value", data.message);

  const stationCard = document.querySelector("#station-card");
  stationCard.hidden = !station;
  if (station) {
    text("station-name", station.name);
    text("station-distance", `${Number(station.distance_km).toFixed(2)} km`);
    text("station-ports", station.available_ports != null ? `${station.available_ports} cổng trống` : "Chưa rõ chỗ trống");
    text("station-connectors", formatConnectors(station));
    text("station-address", station.address || "Chưa có địa chỉ mô phỏng");
  }
  document.querySelector("#approval-check").checked = false;
}

function showError(message) {
  emptyResult.hidden = false;
  result.hidden = true;
  emptyResult.querySelector("p").textContent = message;
  statusBadge.textContent = "Không thể đánh giá";
  statusBadge.className = "decision-status is-danger";
  panel.classList.remove("shake");
  void panel.offsetWidth;
  panel.classList.add("shake");
}

async function loadMetadata() {
  try {
    const response = await fetch("/api/meta", { cache: "no-store" });
    if (!response.ok) throw new Error("Không kết nối được máy chủ.");
    const meta = await response.json();
    const select = document.querySelector("#vehicle-model");
    select.replaceChildren(new Option("Chọn dòng xe", ""));
    meta.vehicle_models.forEach((model) => select.add(new Option(model.label, model.value)));
    text("runtime-label", meta.runtime_mode === "gemini_guarded" ? "Gemini + guardrail" : "Offline · tất định");
    text("data-notice-text", meta.data_notice);
    text("data-count", `${meta.station_records} bản ghi mô phỏng`);
  } catch (error) {
    const select = document.querySelector("#vehicle-model");
    select.replaceChildren(new Option("Không nạp được dữ liệu", ""));
    text("runtime-label", "Mất kết nối");
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!form.reportValidity()) return;
  submitButton.disabled = true;
  submitButton.querySelector("span:first-child").textContent = "Đang áp dụng guardrail…";
  panel.setAttribute("aria-busy", "true");

  const payload = Object.fromEntries(new FormData(form).entries());
  try {
    const response = await fetch("/api/dispatch", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Dữ liệu chưa hợp lệ.");
    showResult(data);
  } catch (error) {
    showError(error.message || "Không kết nối được máy chủ. Hãy chạy lại web_server.py.");
  } finally {
    submitButton.disabled = false;
    submitButton.querySelector("span:first-child").textContent = "Đánh giá phương án";
    panel.setAttribute("aria-busy", "false");
  }
});

document.querySelector("#fill-sample").addEventListener("click", () => {
  const models = document.querySelector("#vehicle-model");
  models.value = [...models.options].some((option) => option.value === "VF5") ? "VF5" : models.options[1]?.value || "";
  document.querySelector("#battery").value = "18";
  document.querySelector("#latitude").value = "21.0285";
  document.querySelector("#longitude").value = "105.8542";
  document.querySelector("#message").value = "Xe đang đỗ an toàn. Hãy tìm trạm phù hợp gần nhất để điều phối viên kiểm tra.";
  form.querySelector("select").focus();
});

loadMetadata();
