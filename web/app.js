const form = document.querySelector("#incident-form");
const panel = document.querySelector(".decision-panel");
const result = document.querySelector("#result");
const emptyResult = document.querySelector("#empty-result");
const submitButton = document.querySelector("#dispatch-button");
const statusBadge = document.querySelector("#decision-status");

const latInput = document.querySelector("#latitude");
const lonInput = document.querySelector("#longitude");
const destInput = document.querySelector("#destination");
const destLatInput = document.querySelector("#destination_lat");
const destLonInput = document.querySelector("#destination_lon");
const radiusSlider = document.querySelector("#radius-slider");
const radiusLabel = document.querySelector("#radius-value-label");
const landmarkSelect = document.querySelector("#landmark-select");
const locationStatus = document.querySelector("#location-status");

const actionLabels = {
  recommend_station: "Đề xuất trạm sạc",
  dispatch_mobile_charger: "Điều xe sạc lưu động",
  dispatch_emergency_rescue: "Cứu hộ khẩn cấp",
  ask_for_information: "Yêu cầu thêm dữ liệu",
  manual_review: "Kiểm tra thủ công",
};

const riskLabels = {
  dispatch_emergency_rescue: "Khẩn cấp",
  dispatch_mobile_charger: "Nguy cấp (<5%)",
  manual_review: "Cần xác minh",
  ask_for_information: "Thiếu dữ liệu",
  recommend_station: "An toàn kiểm soát",
};

function text(id, value) {
  const el = document.querySelector(`#${id}`);
  if (el) el.textContent = value ?? "—";
}

function formatConnectors(station) {
  const connectors = station?.connectors || [];
  if (Array.isArray(connectors) && connectors.length > 0) {
    if (typeof connectors[0] === "object") {
      return connectors.map((c) => `${c.type} (${c.power_kw}kW)`).join(" · ");
    }
    return connectors.join(" · ");
  }
  return "CCS2 · Type 2";
}

// -------------------------------------------------------------
// Interactive Map Manager (Leaflet with Offline Canvas Fallback)
// -------------------------------------------------------------
class MapManager {
  constructor() {
    this.map = null;
    this.hasLeaflet = typeof window.L !== "undefined";
    this.clickMode = "origin"; // "origin" or "dest"
    this.stations = [];
    this.userMarker = null;
    this.destMarker = null;
    this.radiusCircle = null;
    this.routeLine = null;
    this.stationMarkers = [];
    this.selectedStation = null;

    this.init();
  }

  init() {
    const mapEl = document.querySelector("#leaflet-map");
    const canvasEl = document.querySelector("#canvas-radar-container");

    if (this.hasLeaflet) {
      try {
        this.map = L.map("leaflet-map").setView([21.0285, 105.8542], 12);
        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          maxZoom: 19,
          attribution: "© OpenStreetMap contributors",
        }).addTo(this.map);

        this.map.on("click", (e) => this.handleMapClick(e.latlng.lat, e.latlng.lng));
      } catch (err) {
        console.warn("Leaflet tile error, switching to Canvas fallback:", err);
        this.hasLeaflet = false;
      }
    }

    if (!this.hasLeaflet) {
      if (mapEl) mapEl.hidden = true;
      if (canvasEl) canvasEl.hidden = false;
      this.initCanvasFallback();
    }

    this.setupToolbar();
  }

  setupToolbar() {
    const btnOrigin = document.querySelector("#btn-pick-origin");
    const btnDest = document.querySelector("#btn-pick-dest");
    const btnReset = document.querySelector("#btn-reset-map");
    const indicator = document.querySelector("#map-mode-indicator");

    if (btnOrigin && btnDest) {
      btnOrigin.addEventListener("click", () => {
        this.clickMode = "origin";
        btnOrigin.classList.add("is-active");
        btnDest.classList.remove("is-active");
        if (indicator) indicator.textContent = "Chế độ: Nhấp bản đồ để đặt vị trí xe";
      });

      btnDest.addEventListener("click", () => {
        this.clickMode = "dest";
        btnDest.classList.add("is-active");
        btnOrigin.classList.remove("is-active");
        if (indicator) indicator.textContent = "Chế độ: Nhấp bản đồ để đặt điểm đến";
      });
    }

    if (btnReset) {
      btnReset.addEventListener("click", () => this.fitAll());
    }
  }

  handleMapClick(lat, lng) {
    if (this.clickMode === "origin") {
      latInput.value = lat.toFixed(4);
      lonInput.value = lng.toFixed(4);
      this.setUserLocation(lat, lng);
    } else {
      destLatInput.value = lat.toFixed(4);
      destLonInput.value = lng.toFixed(4);
      destInput.value = `GPS ${lat.toFixed(4)}, ${lng.toFixed(4)}`;
      this.setDestination(lat, lng, `Tọa độ ${lat.toFixed(4)}, ${lng.toFixed(4)}`);
    }
  }

  setStations(stations) {
    this.stations = stations || [];
    if (this.hasLeaflet && this.map) {
      this.stationMarkers.forEach((m) => this.map.removeLayer(m));
      this.stationMarkers = [];

      this.stations.forEach((st) => {
        if (st.latitude != null && st.longitude != null) {
          const isSelected = this.selectedStation && this.selectedStation.id === st.id;
          const marker = L.circleMarker([st.latitude, st.longitude], {
            radius: isSelected ? 10 : 7,
            fillColor: isSelected ? "#073d36" : "#18a58f",
            color: "#ffffff",
            weight: 2,
            opacity: 1,
            fillOpacity: 0.9,
          });

          marker.bindPopup(`
            <div style="font-family: sans-serif; font-size: 13px;">
              <strong style="color: #073d36;">${st.name}</strong><br/>
              <span>Cổng trống: <b>${st.available_ports ?? "Chưa rõ"}</b></span><br/>
              <small style="color: #647470;">${st.address || ""}</small>
            </div>
          `);

          marker.addTo(this.map);
          this.stationMarkers.push(marker);
        }
      });
    } else {
      this.drawCanvas();
    }
  }

  setUserLocation(lat, lng) {
    const radiusKm = parseFloat(radiusSlider?.value || "15");
    if (this.hasLeaflet && this.map) {
      if (this.userMarker) this.map.removeLayer(this.userMarker);
      if (this.radiusCircle) this.map.removeLayer(this.radiusCircle);

      const carIcon = L.divIcon({
        html: `<div style="background:#087667; color:white; width:30px; height:30px; border-radius:50%; display:grid; place-items:center; font-size:16px; border:2px solid white; box-shadow:0 0 10px rgba(8,118,103,.5);">🚗</div>`,
        className: "",
        iconSize: [30, 30],
        iconAnchor: [15, 15],
      });

      this.userMarker = L.marker([lat, lng], { icon: carIcon }).addTo(this.map);
      this.userMarker.bindPopup("<b>Vị trí xe hiện tại</b>");

      this.radiusCircle = L.circle([lat, lng], {
        radius: radiusKm * 1000,
        color: "#18a58f",
        fillColor: "#18a58f",
        fillOpacity: 0.08,
        dashArray: "6, 8",
        weight: 1.5,
      }).addTo(this.map);
    } else {
      this.drawCanvas();
    }
  }

  setDestination(lat, lng, name) {
    if (this.hasLeaflet && this.map) {
      if (this.destMarker) this.map.removeLayer(this.destMarker);

      const destIcon = L.divIcon({
        html: `<div style="background:#bf3c42; color:white; width:30px; height:30px; border-radius:50%; display:grid; place-items:center; font-size:16px; border:2px solid white; box-shadow:0 0 10px rgba(191,60,66,.5);">🎯</div>`,
        className: "",
        iconSize: [30, 30],
        iconAnchor: [15, 15],
      });

      this.destMarker = L.marker([lat, lng], { icon: destIcon }).addTo(this.map);
      this.destMarker.bindPopup(`<b>Điểm đến:</b> ${name}`);
    } else {
      this.drawCanvas();
    }
  }

  updateRadius(radiusKm) {
    if (this.radiusCircle) {
      this.radiusCircle.setRadius(radiusKm * 1000);
    }
    if (!this.hasLeaflet) {
      this.drawCanvas();
    }
  }

  drawRoute(origin, station, destination) {
    this.selectedStation = station;
    this.setStations(this.stations);

    if (this.hasLeaflet && this.map) {
      if (this.routeLine) this.map.removeLayer(this.routeLine);

      const points = [];
      if (origin && origin.lat != null && origin.lon != null) points.push([origin.lat, origin.lon]);
      if (station && station.latitude != null && station.longitude != null) points.push([station.latitude, station.longitude]);
      if (destination && destination.latitude != null && destination.longitude != null) points.push([destination.latitude, destination.longitude]);

      if (points.length >= 2) {
        this.routeLine = L.polyline(points, {
          color: "#087667",
          weight: 4,
          opacity: 0.85,
          dashArray: "8, 6",
        }).addTo(this.map);

        this.map.fitBounds(L.latLngBounds(points).pad(0.25));
      }
    } else {
      this.drawCanvas();
    }
  }

  fitAll() {
    if (this.hasLeaflet && this.map) {
      const allPoints = [];
      if (this.userMarker) allPoints.push(this.userMarker.getLatLng());
      if (this.destMarker) allPoints.push(this.destMarker.getLatLng());
      this.stations.forEach((s) => {
        if (s.latitude != null && s.longitude != null) allPoints.push([s.latitude, s.longitude]);
      });
      if (allPoints.length) {
        this.map.fitBounds(L.latLngBounds(allPoints).pad(0.2));
      } else {
        this.map.setView([21.0285, 105.8542], 12);
      }
    } else {
      this.drawCanvas();
    }
  }

  // --- Canvas Offline Fallback Renderer ---
  initCanvasFallback() {
    const canvas = document.querySelector("#radar-canvas");
    if (!canvas) return;
    canvas.addEventListener("click", (e) => {
      const rect = canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerLat = 21.0285;
      const centerLon = 105.8542;
      const scale = 0.0006;
      const clickedLat = centerLat - (y - canvas.height / 2) * scale;
      const clickedLon = centerLon + (x - canvas.width / 2) * scale;
      this.handleMapClick(clickedLat, clickedLon);
    });
    this.drawCanvas();
  }

  drawCanvas() {
    const canvas = document.querySelector("#radar-canvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;
    ctx.clearRect(0, 0, w, h);

    // Background & grid
    ctx.fillStyle = "#07231f";
    ctx.fillRect(0, 0, w, h);

    ctx.strokeStyle = "rgba(24, 165, 143, 0.15)";
    ctx.lineWidth = 1;
    for (let r = 50; r <= 350; r += 50) {
      ctx.beginPath();
      ctx.arc(w / 2, h / 2, r, 0, Math.PI * 2);
      ctx.stroke();
    }
    ctx.beginPath();
    ctx.moveTo(w / 2, 0); ctx.lineTo(w / 2, h);
    ctx.moveTo(0, h / 2); ctx.lineTo(w, h / 2);
    ctx.stroke();

    const centerLat = 21.0285;
    const centerLon = 105.8542;
    const scale = 1400; // pixels per degree

    function toScreen(lat, lon) {
      return {
        x: w / 2 + (lon - centerLon) * scale,
        y: h / 2 - (lat - centerLat) * scale,
      };
    }

    // Stations
    this.stations.forEach((st) => {
      if (st.latitude != null && st.longitude != null) {
        const pt = toScreen(st.latitude, st.longitude);
        ctx.fillStyle = "#18a58f";
        ctx.beginPath();
        ctx.arc(pt.x, pt.y, 6, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = "#edf7f5";
        ctx.font = "10px sans-serif";
        ctx.fillText(st.name.replace("Trạm mô phỏng ", ""), pt.x + 8, pt.y + 3);
      }
    });

    // Origin
    const uLat = parseFloat(latInput?.value);
    const uLon = parseFloat(lonInput?.value);
    if (!isNaN(uLat) && !isNaN(uLon)) {
      const uPt = toScreen(uLat, uLon);
      ctx.fillStyle = "#f0a72e";
      ctx.beginPath();
      ctx.arc(uPt.x, uPt.y, 8, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 11px sans-serif";
      ctx.fillText("🚗 Xe", uPt.x + 10, uPt.y + 4);

      // Radius
      const rKm = parseFloat(radiusSlider?.value || "15");
      const rPx = (rKm / 111) * scale;
      ctx.strokeStyle = "rgba(240, 167, 46, 0.4)";
      ctx.setLineDash([5, 5]);
      ctx.beginPath();
      ctx.arc(uPt.x, uPt.y, rPx, 0, Math.PI * 2);
      ctx.stroke();
      ctx.setLineDash([]);
    }

    // Destination
    const dLat = parseFloat(destLatInput?.value);
    const dLon = parseFloat(destLonInput?.value);
    if (!isNaN(dLat) && !isNaN(dLon)) {
      const dPt = toScreen(dLat, dLon);
      ctx.fillStyle = "#bf3c42";
      ctx.beginPath();
      ctx.arc(dPt.x, dPt.y, 8, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "#ffffff";
      ctx.font = "bold 11px sans-serif";
      ctx.fillText("🎯 Đích", dPt.x + 10, dPt.y + 4);
    }
  }
}

const mapMgr = new MapManager();

// -------------------------------------------------------------
// UI Logic & Form Event Listeners
// -------------------------------------------------------------
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
  text("action-node", action === "recommend_station" ? "TRẠM SẠC" : "ĐIỀU PHỐI");
  text("route-tag-node", station?.route_tag || "LỘ TRÌNH");
  text("action-value", actionLabels[action] || action);
  text("risk-value", riskLabels[action] || (flags.length ? "Cần lưu ý" : "Có kiểm soát"));

  const rangeLimit = context.demo_range_limit_km ?? context.conservative_range_km;
  text("range-value", rangeLimit != null ? `${rangeLimit} km · lab limit` : "Không áp dụng");

  // Detour display
  const detourFact = document.querySelector("#detour-fact");
  if (station && station.detour_km != null && (context.destination || context.destination_lat)) {
    detourFact.hidden = false;
    text("detour-value", `+${Number(station.detour_km).toFixed(2)} km (${station.route_tag || "Tiện đường"})`);
  } else {
    detourFact.hidden = true;
  }

  text("reason-value", data.reason);
  text("message-value", data.message);

  // Recommended Station Card
  const stationCard = document.querySelector("#station-card");
  stationCard.hidden = !station;
  if (station) {
    text("station-name", station.name);
    text("station-distance", `${Number(station.distance_km).toFixed(2)} km`);
    text("station-ports", station.available_ports != null ? `${station.available_ports} cổng trống` : "Chưa rõ chỗ trống");
    text("station-connectors", formatConnectors(station));
    text("station-address", station.address || "Khu vực trạm mô phỏng Hà Nội");

    const tagBadge = document.querySelector("#station-tag");
    if (tagBadge) {
      tagBadge.textContent = station.route_tag || "Tiện đường nhất";
      tagBadge.className = `route-tag-badge ${station.route_tag === "Ngược đường" ? "is-danger" : ""}`;
    }

    // Google Maps Navigation Button
    const gmapsBtn = document.querySelector("#google-maps-link");
    if (gmapsBtn && (data.google_maps_url || context.google_maps_url)) {
      gmapsBtn.href = data.google_maps_url || context.google_maps_url;
      gmapsBtn.hidden = false;
      const sub = document.querySelector("#gmaps-subtext");
      if (sub && context.destination_name) {
        sub.textContent = `Lộ trình: Xe → ${station.name} → ${context.destination_name}`;
      }
    } else if (gmapsBtn) {
      gmapsBtn.hidden = true;
    }
  }

  // Render Nearby Stations in radius
  renderNearbyStations(data.nearby_stations || [], station);

  // Draw Route on Map
  mapMgr.drawRoute(
    { lat: context.latitude, lon: context.longitude },
    station,
    context.destination || { latitude: context.destination_lat, longitude: context.destination_lon }
  );

  document.querySelector("#approval-check").checked = false;
}

function renderNearbyStations(stations, currentRecommended) {
  const container = document.querySelector("#nearby-cards");
  const section = document.querySelector("#nearby-section");
  const countLabel = document.querySelector("#nearby-count");

  if (!stations || stations.length <= 1) {
    section.hidden = true;
    return;
  }

  section.hidden = false;
  countLabel.textContent = stations.length;
  container.replaceChildren();

  stations.forEach((st) => {
    const isChosen = currentRecommended && currentRecommended.id === st.id;
    const card = document.createElement("div");
    card.className = `nearby-card ${isChosen ? "is-selected" : ""}`;

    const tagClass = st.route_tag === "Ngược đường" ? "is-danger" : "";
    const detourText = st.detour_km != null ? ` · Lệch +${st.detour_km} km` : "";

    card.innerHTML = `
      <div class="nearby-card-top">
        <span class="nearby-card-title">${st.name}</span>
        <span class="route-tag-badge ${tagClass}">${st.route_tag || "Phù hợp"}</span>
      </div>
      <div class="nearby-card-meta">
        <span>📍 ${Number(st.distance_km).toFixed(2)} km${detourText}</span>
        <span>⚡ ${st.available_ports ?? 0} cổng trống</span>
      </div>
    `;

    card.addEventListener("click", () => {
      document.querySelectorAll(".nearby-card").forEach((c) => c.classList.remove("is-selected"));
      card.classList.add("is-selected");
      // Update selected station in station-card and route line
      text("station-name", st.name);
      text("station-distance", `${Number(st.distance_km).toFixed(2)} km`);
      text("station-ports", st.available_ports != null ? `${st.available_ports} cổng trống` : "Chưa rõ chỗ trống");
      text("station-connectors", formatConnectors(st));
      text("station-address", st.address || "Khu vực trạm mô phỏng Hà Nội");

      const gmapsBtn = document.querySelector("#google-maps-link");
      if (gmapsBtn) {
        const oLat = latInput.value, oLon = lonInput.value;
        const dLat = destLatInput.value, dLon = destLonInput.value;
        if (dLat && dLon) {
          gmapsBtn.href = `https://www.google.com/maps/dir/?api=1&origin=${oLat},${oLon}&destination=${dLat},${dLon}&waypoints=${st.latitude},${st.longitude}&travelmode=driving`;
        } else {
          gmapsBtn.href = `https://www.google.com/maps/dir/?api=1&origin=${oLat},${oLon}&destination=${st.latitude},${st.longitude}&travelmode=driving`;
        }
      }

      mapMgr.drawRoute(
        { lat: parseFloat(latInput.value), lon: parseFloat(lonInput.value) },
        st,
        { latitude: parseFloat(destLatInput.value), longitude: parseFloat(destLonInput.value) }
      );
    });

    container.appendChild(card);
  });
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

// -------------------------------------------------------------
// Metadata Loader
// -------------------------------------------------------------
async function loadMetadata() {
  try {
    const response = await fetch("/api/meta", { cache: "no-store" });
    if (!response.ok) throw new Error("Không kết nối được máy chủ.");
    const meta = await response.json();

    const select = document.querySelector("#vehicle-model");
    select.replaceChildren(new Option("Chọn dòng xe", ""));
    meta.vehicle_models.forEach((model) => select.add(new Option(model.label, model.value)));

    // Load landmarks
    if (meta.landmarks && landmarkSelect) {
      landmarkSelect.replaceChildren(new Option("-- Chọn điểm đến mẫu --", ""));
      meta.landmarks.forEach((lm) => {
        const opt = new Option(lm.name, lm.name);
        opt.dataset.lat = lm.lat;
        opt.dataset.lon = lm.lon;
        landmarkSelect.add(opt);
      });
    }

    // Feed stations to map
    if (meta.stations) {
      mapMgr.setStations(meta.stations);
    }

    text("runtime-label", meta.runtime_mode === "gemini_guarded" ? "Gemini 2.5 + guardrail" : "Offline · tất định");
    text("data-notice-text", meta.data_notice);
    text("data-count", `${meta.station_records} bản ghi mô phỏng`);
  } catch (error) {
    const select = document.querySelector("#vehicle-model");
    select.replaceChildren(new Option("Không nạp được dữ liệu", ""));
    text("runtime-label", "Mất kết nối");
  }
}

// -------------------------------------------------------------
// Geolocation API Handler
// -------------------------------------------------------------
const btnGeo = document.querySelector("#btn-geolocation");
if (btnGeo) {
  btnGeo.addEventListener("click", () => {
    if (!navigator.geolocation) {
      locationStatus.hidden = false;
      locationStatus.textContent = "Trình duyệt không hỗ trợ Geolocation.";
      return;
    }

    locationStatus.hidden = false;
    locationStatus.textContent = "Đang lấy tín hiệu GPS từ thiết bị…";
    btnGeo.disabled = true;

    navigator.geolocation.getCurrentPosition(
      (pos) => {
        btnGeo.disabled = false;
        const lat = pos.coords.latitude;
        const lon = pos.coords.longitude;
        latInput.value = lat.toFixed(4);
        lonInput.value = lon.toFixed(4);
        locationStatus.textContent = `✅ Đã lấy GPS: ${lat.toFixed(4)}, ${lon.toFixed(4)} (±${Math.round(pos.coords.accuracy)}m)`;
        mapMgr.setUserLocation(lat, lon);
        if (mapMgr.map) mapMgr.map.setView([lat, lon], 13);
      },
      (err) => {
        btnGeo.disabled = false;
        let msg = "Không thể lấy GPS.";
        if (err.code === 1) msg = "Quyền truy cập vị trí bị từ chối. Vui lòng bật cấp quyền vị trí trình duyệt hoặc nhấp lên bản đồ.";
        else if (err.code === 2) msg = "Vị trí không khả dụng. Bạn có thể nhấp trực tiếp lên bản đồ.";
        else if (err.code === 3) msg = "Hết thời gian chờ GPS.";
        locationStatus.textContent = `⚠️ ${msg}`;
      },
      { timeout: 8000, enableHighAccuracy: true }
    );
  });
}

// -------------------------------------------------------------
// Radius Slider Handler
// -------------------------------------------------------------
if (radiusSlider) {
  radiusSlider.addEventListener("input", () => {
    const val = radiusSlider.value;
    if (radiusLabel) radiusLabel.textContent = `${val} km`;
    mapMgr.updateRadius(parseFloat(val));
  });
}

// -------------------------------------------------------------
// Landmark Destination Selection
// -------------------------------------------------------------
if (landmarkSelect) {
  landmarkSelect.addEventListener("change", () => {
    const selected = landmarkSelect.selectedOptions[0];
    if (selected && selected.value) {
      destInput.value = selected.value;
      const lat = parseFloat(selected.dataset.lat);
      const lon = parseFloat(selected.dataset.lon);
      destLatInput.value = !isNaN(lat) ? lat : "";
      destLonInput.value = !isNaN(lon) ? lon : "";
      if (!isNaN(lat) && !isNaN(lon)) {
        mapMgr.setDestination(lat, lon, selected.value);
      }
    }
  });
}

// Coordinate inputs change handler to update map
[latInput, lonInput].forEach((input) => {
  input.addEventListener("change", () => {
    const lat = parseFloat(latInput.value);
    const lon = parseFloat(lonInput.value);
    if (!isNaN(lat) && !isNaN(lon)) {
      mapMgr.setUserLocation(lat, lon);
    }
  });
});

// -------------------------------------------------------------
// Form Submission Handler
// -------------------------------------------------------------
form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!form.reportValidity()) return;

  submitButton.disabled = true;
  submitButton.querySelector("span:first-child").textContent = "Đang tối ưu lộ trình & guardrail…";
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
    submitButton.querySelector("span:first-child").textContent = "Đánh giá & Tìm trạm tiện đường";
    panel.setAttribute("aria-busy", "false");
  }
});

// -------------------------------------------------------------
// Sample Buttons
// -------------------------------------------------------------
document.querySelector("#fill-sample").addEventListener("click", () => {
  const models = document.querySelector("#vehicle-model");
  models.value = [...models.options].some((opt) => opt.value === "VF8") ? "VF8" : models.options[1]?.value || "";
  document.querySelector("#battery").value = "25";
  latInput.value = "21.0300";
  lonInput.value = "105.7800";
  destInput.value = "VinUni - Ocean Park Gia Lâm";
  destLatInput.value = "20.9880";
  destLonInput.value = "105.9520";
  radiusSlider.value = "15";
  radiusLabel.textContent = "15 km";
  document.querySelector("#message").value = "Xe đang ở khu vực Cầu Giấy di chuyển về VinUni Ocean Park. Cần tìm trạm sạc tiện đường đi, tránh đi vòng.";
  mapMgr.setUserLocation(21.0300, 105.7800);
  mapMgr.setDestination(20.9880, 105.9520, "VinUni - Ocean Park");
  mapMgr.updateRadius(15);
  form.querySelector("select").focus();
});

document.querySelector("#fill-sample-noi-bai")?.addEventListener("click", () => {
  const models = document.querySelector("#vehicle-model");
  models.value = [...models.options].some((opt) => opt.value === "VFE34") ? "VFE34" : models.options[1]?.value || "";
  document.querySelector("#battery").value = "18";
  latInput.value = "21.0450";
  lonInput.value = "105.8200";
  destInput.value = "Sân bay Quốc tế Nội Bài";
  destLatInput.value = "21.2185";
  destLonInput.value = "105.8040";
  radiusSlider.value = "20";
  radiusLabel.textContent = "20 km";
  document.querySelector("#message").value = "Đang đi đón khách ở sân bay Nội Bài, pin còn 18%. Tìm trạm sạc nhanh trên lộ trình đi lên sân bay.";
  mapMgr.setUserLocation(21.0450, 105.8200);
  mapMgr.setDestination(21.2185, 105.8040, "Sân bay Nội Bài");
  mapMgr.updateRadius(20);
  form.querySelector("select").focus();
});

loadMetadata();
