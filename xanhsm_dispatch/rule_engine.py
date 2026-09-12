"""Deterministic safety rules for the Xanh SM dispatcher prototype.

Safety decisions live here, not in a prompt.  An LLM may improve wording but
cannot change the selected action, station, human-review requirement or flags.
"""

from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Any

from .data_loader import DataRepository, normalize_station, normalize_vehicle


CRITICAL_BATTERY_PERCENT = 5.0
CRITICAL_MAX_STATION_KM = 5.0
EMERGENCY_TERMS = (
    "cháy", "bốc cháy", "mùi cháy", "khói", "mùi khét", "điện giật", "rò điện",
    "chập điện", "điện áp cao", "tai nạn", "va chạm", "ngập nước", "kẹt giữa đường",
)
ADMIN_ATTACK_TERMS = (
    "bỏ qua quy tắc", "bỏ qua quy định", "ignore previous", "system prompt",
    "quyền admin", "admin override", "tiết lộ dữ liệu", "xuất dữ liệu",
    "danh sách tài xế", "api key", "mật khẩu", "gửi thẳng", "tự động gửi",
    "bỏ qua bước nháp", "không cần duyệt", "đừng gắn thẻ", "xóa draft_only",
    "tôi là quản trị viên", "tôi là admin", "dump database", "toàn bộ dữ liệu",
    "jailbreak", "dan mode", "aim mode", "unrestricted", "bỏ qua an toàn",
    "tắt hitl", "bỏ qua hitl", "override safety", "giám đốc vận hành",
    "điều phối viên trưởng", "lệnh khẩn từ sếp", "bỏ qua kiểm tra",
    "đừng ghi [draft_only]", "không gắn nhãn draft", "auto_send=true", "autosend",
    "xóa system prompt", "bỏ qua hướng dẫn", "bỏ qua ranh giới", "bypass",
)

# Landmark coordinates for Hanoi destination routing (En-route charging)
LANDMARK_COORDINATES: dict[str, tuple[float, float, str]] = {
    "vinuni": (20.9880, 105.9520, "Trường Đại học VinUni - Ocean Park"),
    "ocean park": (20.9880, 105.9520, "Vinhomes Ocean Park Gia Lâm"),
    "gia lâm": (20.9880, 105.9520, "Khu vực Gia Lâm"),
    "nội bài": (21.2185, 105.8040, "Sân bay Quốc tế Nội Bài"),
    "noi bai": (21.2185, 105.8040, "Sân bay Quốc tế Nội Bài"),
    "sân bay": (21.2185, 105.8040, "Sân bay Quốc tế Nội Bài"),
    "mỹ đình": (21.0210, 105.7640, "Khu vực SVĐ Quốc gia Mỹ Đình"),
    "my dinh": (21.0210, 105.7640, "Khu vực SVĐ Quốc gia Mỹ Đình"),
    "bến xe mỹ đình": (21.0285, 105.7725, "Bến xe Mỹ Đình"),
    "hoàn kiếm": (21.0285, 105.8542, "Khu vực Hoàn Kiếm / Trung tâm"),
    "hồ gươm": (21.0285, 105.8542, "Hồ Hoàn Kiếm"),
    "nhà hát lớn": (21.0250, 105.8560, "Nhà Hát Lớn Hà Nội"),
    "hồ tây": (21.0587, 105.8172, "Khu vực Hồ Tây"),
    "tây hồ": (21.0587, 105.8172, "Quận Tây Hồ"),
    "cầu giấy": (21.0364, 105.7906, "Quận Cầu Giấy"),
    "đền lừ": (20.9956, 105.8638, "Khu vực Đền Lừ"),
    "long biên": (21.0264, 105.8997, "Quận Long Biên"),
    "aeon mall long biên": (21.0264, 105.8997, "Aeon Mall Long Biên"),
    "thanh xuân": (20.9971, 105.8049, "Quận Thanh Xuân"),
    "hà đông": (20.9810, 105.7530, "Quận Hà Đông"),
    "aeon mall hà đông": (20.9810, 105.7530, "Aeon Mall Hà Đông"),
}


def _canonical_model(value: str) -> str:
    compact = re.sub(r"[^A-Z0-9]", "", value.upper())
    aliases = {"VFE34": "VFE34", "VF E34": "VFE34", "VF5PLUS": "VF5", "VF6PLUS": "VF6"}
    return aliases.get(compact, compact)


def _haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    radius_km = 6371.0088
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return radius_km * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


class DispatchRuleEngine:
    """Evaluate one incident using deterministic, fail-closed rules."""

    def __init__(
        self,
        stations: list[dict[str, Any]] | None = None,
        vehicles: list[dict[str, Any]] | None = None,
        data_dir: str | Path | None = None,
    ) -> None:
        self.data_repository = DataRepository(data_dir)
        if stations is None or vehicles is None:
            loaded_stations, loaded_vehicles = self.data_repository.load()
            stations = loaded_stations if stations is None else stations
            vehicles = loaded_vehicles if vehicles is None else vehicles
        self.stations = [normalize_station(s) for s in (stations or [])]
        self.vehicles = [normalize_vehicle(v) for v in (vehicles or [])]

    @staticmethod
    def extract_context(text: str) -> dict[str, Any]:
        normalized = text.lower()

        # When an attacker supplies several claimed battery values, choosing the
        # minimum is the safe interpretation. Only values adjacent to "pin" count.
        battery_values: list[float] = []
        battery_patterns = (
            r"(?:mức\s*)?pin(?:\s+hiện\s+tại|\s+báo|\s+còn|\s+là|\s*:)?\s*(\d{1,3}(?:[.,]\d+)?)\s*%",
            r"(\d{1,3}(?:[.,]\d+)?)\s*%\s*(?:pin|battery)",
            r"battery(?:\s+level|\s+is|\s*:)?\s*(\d{1,3}(?:[.,]\d+)?)\s*%",
        )
        for pattern in battery_patterns:
            for match in re.finditer(pattern, normalized, re.IGNORECASE):
                value = float(match.group(1).replace(",", "."))
                if 0 <= value <= 100:
                    battery_values.append(value)
        # A phrase such as "pin lúc 4%, lúc 14%" contains only one explicit
        # occurrence of "pin". Capture both numbers so ambiguity fails closed.
        if "pin" in normalized or "battery" in normalized:
            for match in re.finditer(r"(\d{1,3}(?:[.,]\d+)?)\s*%", normalized):
                value = float(match.group(1).replace(",", "."))
                if 0 <= value <= 100:
                    battery_values.append(value)

        model_match = re.search(r"\b(vf\s*e?\s*\d{1,2}(?:\s*plus)?)\b", text, re.IGNORECASE)
        coords: tuple[float, float] | None = None
        dest_coords: tuple[float, float] | None = None
        dest_name: str | None = None

        valid_coords: list[tuple[float, float]] = []
        for match in re.finditer(r"(?<!\d)(-?\d{1,2}(?:\.\d+)?)\s*[,;/]\s*(-?\d{2,3}(?:\.\d+)?)(?!\d)", text):
            lat, lon = float(match.group(1)), float(match.group(2))
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                valid_coords.append((lat, lon))

        if valid_coords:
            coords = valid_coords[0]
            if len(valid_coords) > 1:
                dest_coords = valid_coords[1]
                dest_name = f"GPS {dest_coords[0]}, {dest_coords[1]}"

        # If destination wasn't explicitly found in coords, scan landmark keywords in text
        if dest_coords is None:
            for landmark_key, (l_lat, l_lon, l_name) in LANDMARK_COORDINATES.items():
                if landmark_key in normalized:
                    dest_coords = (l_lat, l_lon)
                    dest_name = l_name
                    break

        radius_match = re.search(r"(?:bán\s*kính|trong\s*(?:vòng)?)\s*(\d{1,2}(?:[.,]\d+)?)\s*km", normalized)
        search_radius_km = float(radius_match.group(1).replace(",", ".")) if radius_match else None

        return {
            "battery_percent": min(battery_values) if battery_values else None,
            "battery_conflict": (
                len({round(value, 3) for value in battery_values}) > 1
                and bool(re.search(r"\blúc\b.*\blúc\b|\bkhi\b.*\bkhi\b|dao động|mâu thuẫn", normalized))
            ),
            "vehicle_model": _canonical_model(model_match.group(1)) if model_match else None,
            "latitude": coords[0] if coords else None,
            "longitude": coords[1] if coords else None,
            "destination_lat": dest_coords[0] if dest_coords else None,
            "destination_lon": dest_coords[1] if dest_coords else None,
            "destination_name": dest_name,
            "search_radius_km": search_radius_km,
            "emergency_terms": [term for term in EMERGENCY_TERMS if term in normalized],
            "attack_terms": [term for term in ADMIN_ATTACK_TERMS if term in normalized],
        }

    def _vehicle(self, model: str) -> dict[str, Any] | None:
        canonical = _canonical_model(model)
        for vehicle in self.vehicles:
            if _canonical_model(str(vehicle.get("model", ""))) == canonical:
                return vehicle
        return None

    @staticmethod
    def _compatible(station: dict[str, Any], vehicle: dict[str, Any]) -> bool:
        station_models = {_canonical_model(str(x)) for x in station.get("compatible_models", [])}
        model = _canonical_model(str(vehicle.get("model", "")))
        if station_models and model not in station_models:
            return False
        station_connectors = {str(x).upper().replace(" ", "") for x in station.get("connectors", [])}
        vehicle_connectors = {str(x).upper().replace(" ", "") for x in vehicle.get("connectors", [])}
        connector_ok = bool(station_connectors and vehicle_connectors and station_connectors.intersection(vehicle_connectors))
        if not connector_ok:
            return False
        allowed_power = vehicle.get("allowed_power_modes_kw", [])
        options = [
            option for option in station.get("connector_options", [])
            if option.get("type") in vehicle_connectors
            and option.get("available") != 0
        ]
        if station.get("connector_options") and not options:
            return False
        if allowed_power and options and any(option.get("power_kw") is not None for option in options):
            return any(
                math.isclose(float(option["power_kw"]), float(mode), rel_tol=0.0, abs_tol=0.1)
                for option in options if option.get("power_kw") is not None
                for mode in allowed_power
            )
        station_power = station.get("power_kw")
        if allowed_power and station_power is not None:
            try:
                return any(
                    math.isclose(float(station_power), float(mode), rel_tol=0.0, abs_tol=0.1)
                    for mode in allowed_power
                )
            except (TypeError, ValueError):
                return False
        return True

    def _station_candidates(self, context: dict[str, Any], vehicle: dict[str, Any]) -> list[dict[str, Any]]:
        candidates: list[dict[str, Any]] = []
        d_lat = context.get("destination_lat")
        d_lon = context.get("destination_lon")
        has_dest = bool(d_lat is not None and d_lon is not None)

        orig_lat = float(context["latitude"]) if context.get("latitude") is not None else None
        orig_lon = float(context["longitude"]) if context.get("longitude") is not None else None
        orig_to_dest_km = 0.0
        if has_dest and orig_lat is not None and orig_lon is not None:
            orig_to_dest_km = _haversine_km(orig_lat, orig_lon, float(d_lat), float(d_lon))

        for source in self.stations:
            station = dict(source)
            if station.get("status") in {
                "offline", "closed", "maintenance", "inactive", "out_of_service", "faulted"
            }:
                continue
            if station.get("available_ports") is not None and station["available_ports"] <= 0:
                continue
            if not self._compatible(station, vehicle):
                continue
            distance = station.get("distance_km")
            if distance is None and station.get("latitude") is not None and station.get("longitude") is not None and orig_lat is not None and orig_lon is not None:
                try:
                    distance = _haversine_km(
                        orig_lat, orig_lon,
                        float(station["latitude"]), float(station["longitude"]),
                    )
                except (TypeError, ValueError):
                    continue
            try:
                station["distance_km"] = round(float(distance), 2)
            except (TypeError, ValueError):
                continue

            st_lat = station.get("latitude")
            st_lon = station.get("longitude")
            if has_dest and st_lat is not None and st_lon is not None and orig_lat is not None and orig_lon is not None:
                try:
                    st_lat_f = float(st_lat)
                    st_lon_f = float(st_lon)
                    d_dest_f = float(d_lat)
                    d_lon_f = float(d_lon)
                    d_to_dest = _haversine_km(st_lat_f, st_lon_f, d_dest_f, d_lon_f)
                    detour = max(0.0, round(float(distance) + d_to_dest - orig_to_dest_km, 2))

                    # Direction vector alignment
                    lat_mid = math.radians((orig_lat + d_dest_f) / 2)
                    vod_y = d_dest_f - orig_lat
                    vod_x = (d_lon_f - orig_lon) * math.cos(lat_mid)
                    vos_y = st_lat_f - orig_lat
                    vos_x = (st_lon_f - orig_lon) * math.cos(lat_mid)

                    dot = vod_x * vos_x + vod_y * vos_y
                    mag_od = math.hypot(vod_x, vod_y)
                    mag_os = math.hypot(vos_x, vos_y)
                    cos_theta = dot / (mag_od * mag_os) if (mag_od > 1e-6 and mag_os > 1e-6) else 1.0

                    if cos_theta < -0.15:
                        routing_score = float(distance) + 2.5 * detour + 4.0
                        route_tag = "Ngược đường"
                    elif detour <= 1.2:
                        routing_score = float(distance) + 1.2 * detour
                        route_tag = "Rất tiện đường"
                    else:
                        routing_score = float(distance) + 1.8 * detour
                        route_tag = "Tiện đường một phần"

                    station["destination_distance_km"] = round(d_to_dest, 2)
                    station["detour_km"] = detour
                    station["direction_cos"] = round(cos_theta, 2)
                    station["routing_score"] = round(routing_score, 2)
                    station["route_tag"] = route_tag
                except (TypeError, ValueError):
                    station["detour_km"] = 0.0
                    station["routing_score"] = round(float(distance), 2)
                    station["route_tag"] = "Gần nhất"
            else:
                station["detour_km"] = 0.0
                station["routing_score"] = round(float(distance), 2)
                station["route_tag"] = "Gần nhất"

            candidates.append(station)

        if has_dest:
            return sorted(candidates, key=lambda item: (item.get("routing_score", item["distance_km"]), item["distance_km"]))
        return sorted(candidates, key=lambda item: item["distance_km"])

    @staticmethod
    def _decision(action: str, reason: str, message: str, **extra: Any) -> dict[str, Any]:
        result: dict[str, Any] = {
            "status": "DRAFT_ONLY",
            "action": action,
            "requires_human_approval": True,
            "auto_send": False,
            "message": message if message.startswith("[DRAFT_ONLY]") else f"[DRAFT_ONLY] {message}",
            "reason": reason,
            "missing_fields": [],
            "safety_flags": [],
            "recommended_station": None,
            "alternatives": [],
        }
        result.update(extra)
        # These are invariants, not suggestions to the language model.
        result["status"] = "DRAFT_ONLY"
        result["requires_human_approval"] = True
        result["auto_send"] = False
        if not str(result.get("message", "")).startswith("[DRAFT_ONLY]"):
            result["message"] = f"[DRAFT_ONLY] {result.get('message', '')}"
        return result

    def evaluate(self, text: str, context: dict[str, Any] | None = None) -> dict[str, Any]:
        parsed = self.extract_context(text)
        stable_keys = (
            "battery_percent", "vehicle_model", "latitude", "longitude",
            "destination_lat", "destination_lon", "destination_name", "search_radius_km",
        )
        merged = {key: value for key, value in (context or {}).items() if key in stable_keys}
        for key in stable_keys:
            if parsed.get(key) is not None:
                merged[key] = parsed[key]
        # Safety signals apply to the current message only. They must not poison
        # later turns in the same incident after the dispatcher has reviewed them.
        merged["emergency_terms"] = parsed["emergency_terms"]
        merged["attack_terms"] = parsed["attack_terms"]
        merged["battery_conflict"] = parsed["battery_conflict"]

        if merged.get("emergency_terms"):
            terms = ", ".join(merged["emergency_terms"])
            return self._decision(
                "dispatch_emergency_rescue",
                f"Phát hiện tín hiệu nguy hiểm: {terms}.",
                "[DRAFT_ONLY] Dừng di chuyển/sạc nếu có thể thực hiện an toàn, đưa người ra vị trí an toàn và chờ điều phối viên gọi đội cứu hộ khẩn cấp. Không tự xử lý hệ thống điện.",
                safety_flags=["EMERGENCY", "HUMAN_REVIEW_REQUIRED"],
                context=merged,
            )

        privacy_attack = bool(re.search(
            r"(?:tất cả|toàn bộ).*tài xế|danh sách.*(?:biển số|tài xế)|"
            r"(?:api[_ -]?key|mật khẩu|token|secret|dump|system prompt|"
            r"credentials|private key|bearer token|auth token|cơ sở dữ liệu|"
            r"database|driver table|schema|select\s+\*|drop\s+table|dan mode|jailbreak)",
            text,
            re.IGNORECASE,
        ))
        if privacy_attack:
            return self._decision(
                "manual_review",
                "Yêu cầu truy xuất dữ liệu nhạy cảm hoặc chỉ thị hệ thống không thuộc phạm vi điều phối sự cố.",
                "[DRAFT_ONLY] Không cung cấp dữ liệu nhạy cảm. Chuyển điều phối viên kiểm tra thủ công.",
                safety_flags=["DATA_EXFILTRATION_ATTEMPT", "HUMAN_REVIEW_REQUIRED"],
                context=merged,
            )

        if merged.get("battery_conflict"):
            return self._decision(
                "ask_for_information",
                "Phát hiện nhiều mức pin mâu thuẫn trong cùng yêu cầu; không được tự chọn một giá trị.",
                "[DRAFT_ONLY] Vui lòng xác nhận lại một mức pin hiện tại duy nhất hiển thị trên xe.",
                missing_fields=["mức_pin_%_xác_nhận"],
                safety_flags=["CONFLICTING_BATTERY_DATA", "INSUFFICIENT_DATA"],
                context=merged,
            )

        # A known critical battery state fails closed immediately, even when
        # model or GPS is still missing. The human rescue workflow can collect
        # the location; missing metadata must not delay escalation.
        battery = merged.get("battery_percent")
        if battery is not None and float(battery) < CRITICAL_BATTERY_PERCENT:
            battery = float(battery)
            return self._decision(
                "dispatch_mobile_charger",
                f"Pin {battery:g}% dưới ngưỡng an toàn {CRITICAL_BATTERY_PERCENT:g}%; không đề xuất trạm dù có trạm trong bán kính {CRITICAL_MAX_STATION_KM:g} km.",
                "[DRAFT_ONLY] Xe đang ở mức pin nguy cấp. Giữ xe ở vị trí an toàn và chờ điều phối viên xác nhận điều xe sạc/cứu hộ lưu động.",
                safety_flags=["CRITICAL_BATTERY", "NO_STATION_RECOMMENDATION", "HUMAN_REVIEW_REQUIRED"],
                context=merged,
            )

        required = {
            "battery_percent": "mức_pin_%",
            "vehicle_model": "dòng_xe",
            "latitude": "tọa_độ_GPS",
            "longitude": "tọa_độ_GPS",
        }
        missing = []
        for key, label in required.items():
            if merged.get(key) is None and label not in missing:
                missing.append(label)
        if missing:
            return self._decision(
                "ask_for_information",
                "Thiếu dữ liệu bắt buộc để đánh giá quãng đường an toàn.",
                "[DRAFT_ONLY] Vui lòng cung cấp: " + ", ".join(missing) + ". Ví dụ: VF 5, pin 18%, GPS 21.0285, 105.8542.",
                missing_fields=missing,
                safety_flags=["INSUFFICIENT_DATA"],
                context=merged,
            )

        battery = float(merged["battery_percent"])

        vehicle = self._vehicle(str(merged["vehicle_model"]))
        if vehicle is None:
            return self._decision(
                "manual_review",
                f"Không có dữ liệu đã xác minh cho dòng xe {merged['vehicle_model']}.",
                "[DRAFT_ONLY] Chưa thể kiểm tra cổng sạc và tầm hoạt động của xe. Điều phối viên cần tra cứu thủ công.",
                safety_flags=["UNKNOWN_VEHICLE", "HUMAN_REVIEW_REQUIRED"],
                context=merged,
            )

        if not self.stations:
            return self._decision(
                "manual_review",
                "Chưa nạp dữ liệu trạm sạc; hệ thống không được tự bịa tên hoặc vị trí trạm.",
                "[DRAFT_ONLY] Không có dữ liệu trạm sạc khả dụng. Điều phối viên cần mở bản đồ trạm chính thức để kiểm tra.",
                safety_flags=["STATION_DATA_UNAVAILABLE", "HUMAN_REVIEW_REQUIRED"],
                context=merged,
            )

        candidates = self._station_candidates(merged, vehicle)
        official_range = vehicle.get("official_range_km")
        if official_range is None:
            return self._decision(
                "manual_review",
                "Thiếu tầm hoạt động tham chiếu của dòng xe; không thể đánh giá khả năng tới trạm.",
                "[DRAFT_ONLY] Chuyển điều phối viên kiểm tra thủ công dữ liệu xe và trạm.",
                safety_flags=["VEHICLE_RANGE_DATA_UNAVAILABLE", "HUMAN_REVIEW_REQUIRED"],
                context=merged,
            )

        # Lab-only heuristic. It is not live telemetry or a guaranteed range;
        # production must replace it with a timestamped estimate from the car.
        demo_range_limit = round(float(official_range) * battery / 100 * float(vehicle.get("safety_factor", 0.65)), 2)
        safe = [station for station in candidates if station["distance_km"] <= demo_range_limit]
        if not safe:
            return self._decision(
                "manual_review",
                "Không tìm thấy trạm đang hoạt động, còn chỗ, đúng cổng sạc và nằm trong ngưỡng mô phỏng của lab.",
                "[DRAFT_ONLY] Không có phương án trạm đủ an toàn từ dữ liệu hiện tại. Điều phối viên cần xác minh và cân nhắc cứu hộ lưu động.",
                safety_flags=["NO_SAFE_COMPATIBLE_STATION", "HUMAN_REVIEW_REQUIRED"],
                context={**merged, "demo_range_limit_km": demo_range_limit, "range_is_live_telemetry": False},
            )

        # Apply search_radius filter if specified and contains safe stations
        search_radius = merged.get("search_radius_km")
        ranked_safe = safe
        if search_radius is not None:
            try:
                r_val = float(search_radius)
                if r_val > 0:
                    within_radius = [s for s in safe if s["distance_km"] <= r_val]
                    if within_radius:
                        ranked_safe = within_radius
            except (TypeError, ValueError):
                pass

        has_dest = bool(merged.get("destination_lat") is not None and merged.get("destination_lon") is not None)
        if has_dest:
            ranked_safe = sorted(ranked_safe, key=lambda s: (s.get("routing_score", s["distance_km"]), s["distance_km"]))
        else:
            ranked_safe = sorted(ranked_safe, key=lambda s: s["distance_km"])

        best = ranked_safe[0]
        alternatives = ranked_safe[1:4]
        nearby_stations = ranked_safe[:10]

        # Build official Google Maps Direction URL
        lat_o, lon_o = merged.get("latitude"), merged.get("longitude")
        lat_s, lon_s = best.get("latitude"), best.get("longitude")
        gmaps_url: str | None = None
        if lat_o is not None and lon_o is not None and lat_s is not None and lon_s is not None:
            if has_dest:
                lat_d, lon_d = merged["destination_lat"], merged["destination_lon"]
                gmaps_url = (
                    f"https://www.google.com/maps/dir/?api=1&origin={lat_o},{lon_o}"
                    f"&destination={lat_d},{lon_d}&waypoints={lat_s},{lon_s}&travelmode=driving"
                )
            else:
                gmaps_url = (
                    f"https://www.google.com/maps/dir/?api=1&origin={lat_o},{lon_o}"
                    f"&destination={lat_s},{lon_s}&travelmode=driving"
                )

        if has_dest:
            dest_label = merged.get("destination_name") or f"GPS {merged['destination_lat']}, {merged['destination_lon']}"
            detour_val = best.get("detour_km", 0.0)
            tag_label = best.get("route_tag", "tiện đường")
            reason_str = (
                f"Trạm đề xuất {best['name']} cách {best['distance_km']:.2f} km ({tag_label}, độ lệch lộ trình +{detour_val:.2f} km về {dest_label}), "
                f"trong ngưỡng mô phỏng lab {demo_range_limit:.2f} km; phải kiểm tra telemetry thật trước khi gửi."
            )
            message_str = (
                f"[DRAFT_ONLY] Đề xuất {best['name']} — {best.get('address', 'Khu vực trạm')} "
                f"({best['distance_km']:.2f} km, tiện đường về {dest_label}, lệch +{detour_val:.2f} km). "
                f"Điều phối viên kiểm tra lại tình trạng trụ và duyệt trước khi gửi tài xế."
            )
        else:
            reason_str = f"Trạm gần nhất phù hợp cách {best['distance_km']:.2f} km, trong ngưỡng mô phỏng lab {demo_range_limit:.2f} km; phải kiểm tra telemetry thật trước khi gửi."
            message_str = f"[DRAFT_ONLY] Đề xuất {best['name']} — {best.get('address', 'Khu vực trạm')} ({best['distance_km']:.2f} km). Điều phối viên kiểm tra lại tình trạng trụ và duyệt trước khi gửi tài xế."

        return self._decision(
            "recommend_station",
            reason_str,
            message_str,
            safety_flags=["HUMAN_REVIEW_REQUIRED"],
            recommended_station=best,
            alternatives=alternatives,
            nearby_stations=nearby_stations,
            google_maps_url=gmaps_url,
            context={
                **merged,
                "demo_range_limit_km": demo_range_limit,
                "range_is_live_telemetry": False,
                "google_maps_url": gmaps_url,
                "destination": {
                    "latitude": merged.get("destination_lat"),
                    "longitude": merged.get("destination_lon"),
                    "name": merged.get("destination_name"),
                } if has_dest else None,
            },
        )


def evaluate_offline(text: str, data_dir: str | Path | None = None) -> dict[str, Any]:
    """Convenience entry point used by tests and the no-API demo."""

    return DispatchRuleEngine(data_dir=data_dir).evaluate(text)
