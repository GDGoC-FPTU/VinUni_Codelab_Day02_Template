"""Offline safety tests for the Xanh SM dispatcher rule engine.

These tests deliberately exercise the deterministic rule layer, not Gemini.  They
therefore run without an API key, network access, or a live charging-station API.
The LLM is only allowed to phrase a draft after these rules have made the safety
decision.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import pytest

from xanhsm_dispatch.rule_engine import DispatchRuleEngine


ROOT = Path(__file__).resolve().parents[1]
CASE_FILE = ROOT / "data" / "test_cases.json"


def _load_suite() -> dict[str, Any]:
    with CASE_FILE.open(encoding="utf-8") as stream:
        return json.load(stream)


SUITE = _load_suite()
CASES = SUITE["cases"]
CASES_BY_ID = {case["id"]: case for case in CASES}


def _case_id(case: dict[str, Any]) -> str:
    return case["id"]


def _normalise_vehicle(vehicle: dict[str, Any] | None) -> list[dict[str, Any]]:
    """Add harmless aliases so fixtures tolerate either common data spelling."""
    if not vehicle:
        return []
    record = dict(vehicle)
    if "connector_type" in record:
        record.setdefault("connector", record["connector_type"])
        record.setdefault("port_type", record["connector_type"])
    # Range is a controlled fixture value, not a claim about the real vehicle.
    # It keeps routing tests focused on the boundary named by each case.
    record.setdefault("official_range_km", 400)
    record.setdefault("simulated", True)
    record.setdefault("id", record.get("model"))
    record.setdefault("name", record.get("model"))
    return [record]


def _normalise_stations(stations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for station in stations:
        record = dict(station)
        connectors = record.get("connector_types", [])
        if connectors:
            record.setdefault("connector_type", connectors[0])
            record.setdefault("connectors", connectors)
        record.setdefault("available", record.get("status") == "available")
        record.setdefault("available_ports", 1 if record["available"] else 0)
        record.setdefault("max_power_kw", record.get("power_kw"))
        records.append(record)
    return records


def _evaluate(case: dict[str, Any]) -> dict[str, Any]:
    """Run one case through the public, deterministic interface."""
    case_input = case["input"]
    engine = DispatchRuleEngine(
        stations=_normalise_stations(case_input.get("candidate_stations", [])),
        vehicles=_normalise_vehicle(case_input.get("vehicle")),
    )
    result = engine.evaluate(case_input["message"])
    assert isinstance(result, dict), "Rule engine output must be a structured dict"
    return result


def _station_id(result: dict[str, Any]) -> str | None:
    station = result.get("recommended_station")
    if station is None:
        return None
    if isinstance(station, str):
        return station
    for key in ("id", "station_id", "code"):
        if station.get(key) is not None:
            return str(station[key])
    return None


def _normalise_missing(values: Any) -> set[str]:
    aliases = {
        "location": "gps",
        "coordinates": "gps",
        "current_location": "gps",
        "tọa_độ_gps": "gps",
        "vehicle": "vehicle_model",
        "model": "vehicle_model",
        "dòng_xe": "vehicle_model",
        "battery": "battery_percent",
        "soc": "battery_percent",
        "mức_pin_%": "battery_percent",
        "mức_pin_%_xác_nhận": "battery_percent",
    }
    if not isinstance(values, list):
        return set()
    return {aliases.get(str(value).lower(), str(value).lower()) for value in values}


def test_case_file_has_required_coverage() -> None:
    assert len(CASES) >= 20
    assert len(CASES_BY_ID) == len(CASES), "Every test id must be unique"

    categories = {case["category"] for case in CASES}
    required = {
        "normal",
        "battery_boundary",
        "critical_battery",
        "station_over_5km",
        "incompatible_connector",
        "incompatible_power",
        "missing_gps",
        "missing_vehicle_model",
        "prompt_injection",
        "bypass_draft_only",
        "fake_admin",
        "data_exfiltration",
        "ambiguous_description",
    }
    assert required <= categories


@pytest.mark.parametrize("case", CASES, ids=_case_id)
def test_expected_action(case: dict[str, Any]) -> None:
    result = _evaluate(case)
    assert result.get("action") == case["expected_action"]


@pytest.mark.parametrize("case", CASES, ids=_case_id)
def test_every_output_is_draft_and_requires_human_approval(
    case: dict[str, Any],
) -> None:
    result = _evaluate(case)
    message = result.get("message", "")

    assert result.get("status") == "DRAFT_ONLY"
    assert isinstance(message, str) and message.startswith("[DRAFT_ONLY]")
    assert result.get("requires_human_approval") is True
    assert result.get("auto_send") is False


@pytest.mark.parametrize(
    "case",
    [case for case in CASES if case["category"] in {"critical_battery", "station_over_5km"}],
    ids=_case_id,
)
def test_critical_battery_never_gets_a_station(case: dict[str, Any]) -> None:
    battery = case["input"].get("vehicle", {}).get("battery_percent")
    if battery is None or battery >= 5:
        pytest.skip("This distance case is not below the critical threshold")

    result = _evaluate(case)
    assert result["action"] == "dispatch_mobile_charger"
    assert result.get("recommended_station") is None


def test_exactly_five_percent_is_not_treated_as_below_five() -> None:
    result = _evaluate(CASES_BY_ID["BOUNDARY-05"])
    assert result["action"] == "recommend_station"
    assert _station_id(result) == "HN-2KM"


@pytest.mark.parametrize(
    "case",
    [case for case in CASES if "recommended_station_id" in case["expected_safety_assertions"]],
    ids=_case_id,
)
def test_recommended_station_matches_expected_fixture(case: dict[str, Any]) -> None:
    result = _evaluate(case)
    expected = case["expected_safety_assertions"]["recommended_station_id"]
    assert _station_id(result) == expected


@pytest.mark.parametrize(
    "case",
    [case for case in CASES if case["expected_safety_assertions"].get("forbidden_station_ids")],
    ids=_case_id,
)
def test_incompatible_station_is_never_selected(case: dict[str, Any]) -> None:
    result = _evaluate(case)
    forbidden = set(case["expected_safety_assertions"]["forbidden_station_ids"])
    assert _station_id(result) not in forbidden


@pytest.mark.parametrize(
    "case",
    [case for case in CASES if case["expected_safety_assertions"].get("recommended_station_must_be_null")],
    ids=_case_id,
)
def test_cases_that_require_refusal_or_escalation_have_no_station(
    case: dict[str, Any],
) -> None:
    assert _evaluate(case).get("recommended_station") is None


@pytest.mark.parametrize(
    "case",
    [case for case in CASES if case["expected_safety_assertions"].get("required_missing_fields")],
    ids=_case_id,
)
def test_missing_or_ambiguous_input_is_not_guessed(case: dict[str, Any]) -> None:
    result = _evaluate(case)
    required = set(case["expected_safety_assertions"]["required_missing_fields"])
    actual = _normalise_missing(result.get("missing_fields"))
    assert result["action"] == "ask_for_information"
    assert required <= actual
    assert result.get("recommended_station") is None


@pytest.mark.parametrize(
    "case",
    [case for case in CASES if case["category"] == "data_exfiltration"],
    ids=_case_id,
)
def test_data_exfiltration_does_not_leak_secrets_or_personal_data(
    case: dict[str, Any],
) -> None:
    result = _evaluate(case)
    rendered = json.dumps(result, ensure_ascii=False)

    assert result["action"] == "manual_review"
    assert not re.search(r"AIza[0-9A-Za-z_-]{20,}", rendered)
    assert not re.search(r"(?:api[_ -]?key|token|secret)\s*[=:]\s*[\"']?\w{8,}", rendered, re.I)
    assert not re.search(r"\b0\d{8,10}\b", rendered)
    assert not re.search(r"\b\d{2}[A-Z]-\d{3,5}(?:\.\d{2})?\b", rendered)


@pytest.mark.parametrize(
    "case",
    [case for case in CASES if case["category"] in {"prompt_injection", "bypass_draft_only", "fake_admin"}],
    ids=_case_id,
)
def test_adversarial_authority_claims_cannot_disable_boundaries(
    case: dict[str, Any],
) -> None:
    result = _evaluate(case)
    assert result["status"] == "DRAFT_ONLY"
    assert result["message"].startswith("[DRAFT_ONLY]")
    assert result["requires_human_approval"] is True
    assert result["auto_send"] is False


@pytest.mark.parametrize(
    "case",
    [case for case in CASES if case["category"] == "physical_emergency"],
    ids=_case_id,
)
def test_physical_hazard_escalates_without_driving_recommendation(
    case: dict[str, Any],
) -> None:
    result = _evaluate(case)
    assert result["action"] == "dispatch_emergency_rescue"
    assert result.get("recommended_station") is None
