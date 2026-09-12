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
)


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
        for match in re.finditer(r"(?<!\d)(-?\d{1,2}(?:\.\d+)?)\s*[,;/]\s*(-?\d{2,3}(?:\.\d+)?)(?!\d)", text):
            lat, lon = float(match.group(1)), float(match.group(2))
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                coords = (lat, lon)
                break

        return {
            "battery_percent": min(battery_values) if battery_values else None,
            "battery_conflict": (
                len({round(value, 3) for value in battery_values}) > 1
                and bool(re.search(r"\blúc\b.*\blúc\b|\bkhi\b.*\bkhi\b|dao động|mâu thuẫn", normalized))
            ),
            "vehicle_model": _canonical_model(model_match.group(1)) if model_match else None,
            "latitude": coords[0] if coords else None,
            "longitude": coords[1] if coords else None,
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
            if distance is None and station.get("latitude") is not None and station.get("longitude") is not None:
                try:
                    distance = _haversine_km(
                        float(context["latitude"]), float(context["longitude"]),
                        float(station["latitude"]), float(station["longitude"]),
                    )
                except (TypeError, ValueError):
                    continue
            try:
                station["distance_km"] = round(float(distance), 2)
            except (TypeError, ValueError):
                continue
            candidates.append(station)
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
        stable_keys = ("battery_percent", "vehicle_model", "latitude", "longitude")
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
            r"(?:api[_ -]?key|mật khẩu|token|secret|dump database|system prompt)",
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

        best = safe[0]
        alternatives = safe[1:3]
        return self._decision(
            "recommend_station",
            f"Trạm gần nhất phù hợp cách {best['distance_km']:.2f} km, trong ngưỡng mô phỏng lab {demo_range_limit:.2f} km; phải kiểm tra telemetry thật trước khi gửi.",
            f"[DRAFT_ONLY] Đề xuất {best['name']} — {best['address']} ({best['distance_km']:.2f} km). Điều phối viên kiểm tra lại tình trạng trụ và duyệt trước khi gửi tài xế.",
            safety_flags=["HUMAN_REVIEW_REQUIRED"],
            recommended_station=best,
            alternatives=alternatives,
            context={**merged, "demo_range_limit_km": demo_range_limit, "range_is_live_telemetry": False},
        )


def evaluate_offline(text: str, data_dir: str | Path | None = None) -> dict[str, Any]:
    """Convenience entry point used by tests and the no-API demo."""

    return DispatchRuleEngine(data_dir=data_dir).evaluate(text)
