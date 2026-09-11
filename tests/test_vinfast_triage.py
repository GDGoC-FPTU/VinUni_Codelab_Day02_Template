"""Offline regression checks; these do not evaluate Gemini behavior."""
import importlib.util
import json
from pathlib import Path
import pytest

spec = importlib.util.spec_from_file_location('triage', Path(__file__).resolve().parents[1] / 'starter-code/vinfast_triage_prototype.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

def case():
    return dict(intent='vehicle_fault', severity='SAFETY_REVIEW_REQUIRED', summary='Customer reports battery warning.', missing_information=[], recommended_queue='EMERGENCY_TECHNICAL_SUPPORT', human_review_required=True, customer_response_type='SAFE_ESCALATION_ONLY', confidence=0.9)

@pytest.mark.parametrize('raw', ['{}', '[]', '```json\n{}\n```', '{"intent":"vehicle_fault","intent":"other_service"}'])
def test_reject_invalid_json(raw):
    with pytest.raises(ValueError):
        m.parse_output(raw)

@pytest.mark.parametrize('value', [True, 'low', float('nan'), 1.1, -0.1])
def test_reject_invalid_confidence(value):
    data = case(); data['confidence'] = value
    with pytest.raises(ValueError):
        m.parse_output(json.dumps(data))

def test_safety_must_escalate_and_require_human():
    data = m.parse_output(json.dumps(case()))
    assert not m.check_boundaries(data, 0)
    data['human_review_required'] = False
    data['recommended_queue'] = 'SERVICE_INTAKE'
    assert len(m.check_boundaries(data, 0)) == 2

@pytest.mark.parametrize('index', [1, 2, 3])
def test_reject_wrong_route_for_each_attack(index):
    data = case(); data['recommended_queue'] = 'SERVICE_INTAKE'
    assert m.check_boundaries(data, index)

def test_missing_information_contract():
    data = case()
    data.update(intent='insufficient_information', severity='UNKNOWN', recommended_queue='SERVICE_INTAKE', customer_response_type='REQUEST_INFORMATION', confidence=0.2, missing_information=['vehicle_model_or_vin','symptom','vehicle_current_state'])
    assert not m.check_boundaries(data, 3)
    data['missing_information'].pop()
    assert m.check_boundaries(data, 3)

def test_no_key_does_not_claim_boundary_result(monkeypatch, capsys):
    monkeypatch.delenv('GEMINI_API_KEY', raising=False)
    monkeypatch.delenv('GOOGLE_API_KEY', raising=False)
    assert m.main() == 2
    assert 'no API call made' in capsys.readouterr().out
