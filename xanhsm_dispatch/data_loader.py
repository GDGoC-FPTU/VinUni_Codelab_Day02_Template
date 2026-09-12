"""Load and normalize the public/simulated data used by the prototype."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _first(mapping: dict[str, Any], *keys: str, default: Any = None) -> Any:
    for key in keys:
        value = mapping.get(key)
        if value is not None:
            return value
    return default


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (tuple, set)):
        return list(value)
    if isinstance(value, str):
        return [part.strip() for part in value.split(",") if part.strip()]
    return [value]


def _records(payload: Any, keys: Iterable[str]) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if isinstance(payload, dict):
        for key in keys:
            if isinstance(payload.get(key), list):
                return [item for item in payload[key] if isinstance(item, dict)]
    return []


def normalize_station(raw: dict[str, Any]) -> dict[str, Any]:
    location = raw.get("location") if isinstance(raw.get("location"), dict) else {}
    gps = raw.get("gps") if isinstance(raw.get("gps"), dict) else {}
    connectors = _as_list(
        _first(
            raw,
            "connectors",
            "connector_types",
            "ports",
            "port_types",
            "charging_ports",
            "connector_type",
        )
    )
    normalized_connectors: list[str] = []
    connector_options: list[dict[str, Any]] = []
    for connector in connectors:
        if isinstance(connector, dict):
            connector_type = _first(connector, "type", "name", "connector", "standard")
            if connector_type:
                normalized_type = str(connector_type).upper().replace(" ", "")
                normalized_connectors.append(normalized_type)
                connector_options.append({
                    "type": normalized_type,
                    "power_kw": _first(connector, "power_kw", "max_power_kw"),
                    "available": _first(connector, "available", "available_ports", default=None),
                })
            continue
        if connector:
            normalized_type = str(connector).upper().replace(" ", "")
            normalized_connectors.append(normalized_type)
            connector_options.append({"type": normalized_type, "power_kw": None, "available": None})

    status = str(_first(raw, "status", "operating_status", default="unknown")).lower()
    available = _first(
        raw,
        "available_ports",
        "available_chargers",
        "available_connectors",
        "available_slots",
        default=None,
    )
    if available is None:
        option_availability = [option["available"] for option in connector_options if option["available"] is not None]
        if option_availability:
            try:
                available = sum(int(value) for value in option_availability)
            except (TypeError, ValueError):
                available = None
    try:
        available = int(available) if available is not None else None
    except (TypeError, ValueError):
        available = None

    return {
        "id": str(_first(raw, "id", "station_id", "code", default="unknown")),
        "name": str(_first(raw, "name", "station_name", "title", default="Trạm sạc")),
        "address": str(_first(raw, "address", "formatted_address", default="Chưa có địa chỉ")),
        "latitude": _first(raw, "latitude", "lat", default=_first(location, "latitude", "lat", default=_first(gps, "latitude", "lat"))),
        "longitude": _first(raw, "longitude", "lon", "lng", default=_first(location, "longitude", "lon", "lng", default=_first(gps, "longitude", "lon", "lng"))),
        "distance_km": _first(raw, "distance_km", "distance", default=None),
        "connectors": normalized_connectors,
        "connector_options": connector_options,
        "compatible_models": [str(x).upper().replace(" ", "") for x in _as_list(raw.get("compatible_models"))],
        "power_kw": _first(
            raw,
            "power_kw",
            "max_power_kw",
            "charging_power_kw",
            default=max(
                (float(option["power_kw"]) for option in connector_options if option["power_kw"] is not None),
                default=None,
            ),
        ),
        "available_ports": available,
        "status": status,
        "simulated": bool(raw.get("simulated", False)),
        "source_url": raw.get("source_url"),
    }


def normalize_vehicle(raw: dict[str, Any]) -> dict[str, Any]:
    model = str(_first(raw, "model", "vehicle_model", "name", default="UNKNOWN"))
    connectors = _as_list(
        _first(raw, "connectors", "connector_types", "compatible_connectors", "charging_port", "connector_type")
    )
    range_km = _first(
        raw,
        "official_range_km",
        "nominal_range_km",
        "range_km",
        "wltp_range_km",
        "nedc_range_km",
        "max_range_km",
        default=None,
    )
    if isinstance(range_km, dict):
        range_km = _first(range_km, "value", "max", "official")
    try:
        range_km = float(range_km) if range_km is not None else None
    except (TypeError, ValueError):
        range_km = None
    try:
        safety_factor = float(raw.get("safety_factor", 0.65))
    except (TypeError, ValueError):
        safety_factor = 0.65
    power_values = _as_list(
        _first(raw, "allowed_power_modes_kw", "charging_power_modes_kw", "supported_power_kw")
    )
    allowed_power_modes: list[float] = []
    for value in power_values:
        try:
            allowed_power_modes.append(float(value))
        except (TypeError, ValueError):
            continue
    return {
        "model": model.upper().replace(" ", "").replace("-", ""),
        "display_name": model,
        "connectors": [str(x).upper().replace(" ", "") for x in connectors],
        "official_range_km": range_km,
        "official_range_standard": _first(raw, "official_range_standard", "range_standard"),
        "safety_factor": min(max(safety_factor, 0.3), 0.9),
        "allowed_power_modes_kw": allowed_power_modes,
        "source_url": _first(raw, "source_url", "source"),
        "simulated": bool(raw.get("simulated", False)),
    }


class DataRepository:
    """Best-effort loader; absent or malformed files produce empty datasets."""

    STATION_FILES = ("charging_stations.json", "stations.json")
    VEHICLE_FILES = ("vehicle_specs.json", "vehicles.json")

    def __init__(self, data_dir: str | Path | None = None) -> None:
        self.data_dir = Path(data_dir) if data_dir else PROJECT_ROOT / "data"
        self.warnings: list[str] = []
        self.sources: list[str] = []

    def _load_first(self, names: tuple[str, ...]) -> Any:
        for name in names:
            path = self.data_dir / name
            if not path.exists():
                continue
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
                self.sources.append(str(path))
                return payload
            except (OSError, json.JSONDecodeError) as exc:
                self.warnings.append(f"Không đọc được {path.name}: {exc}")
        self.warnings.append(f"Thiếu dữ liệu: {' hoặc '.join(names)}")
        return []

    def load(self) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        station_payload = self._load_first(self.STATION_FILES)
        vehicle_payload = self._load_first(self.VEHICLE_FILES)
        station_records = _records(
            station_payload,
            ("simulated_lab_stations", "stations", "charging_stations", "data"),
        )
        vehicle_records = _records(vehicle_payload, ("vehicles", "vehicle_specs", "models", "data"))
        if isinstance(vehicle_payload, dict):
            connector_reference = vehicle_payload.get("connector_reference", {})
            default_connectors = [
                connector_reference.get("public_ac"),
                connector_reference.get("public_dc"),
            ]
            default_connectors = [value for value in default_connectors if value]
            if default_connectors:
                vehicle_records = [
                    {**item, "connectors": item.get("connectors") or default_connectors}
                    for item in vehicle_records
                ]
        stations = [normalize_station(item) for item in station_records]
        vehicles = [normalize_vehicle(item) for item in vehicle_records]
        return stations, vehicles
