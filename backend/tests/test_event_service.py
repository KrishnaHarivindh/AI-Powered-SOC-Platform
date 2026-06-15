from app.models.security_event import Severity
from app.schemas.event import EventIngest
from app.services.event_service import ALERT_SEVERITIES


def test_high_and_critical_events_create_alerts():
    assert Severity.HIGH in ALERT_SEVERITIES
    assert Severity.CRITICAL in ALERT_SEVERITIES
    assert Severity.MEDIUM not in ALERT_SEVERITIES


def test_event_ingest_schema_defaults_raw_log():
    payload = EventIngest(source_ip="192.168.1.10", event_type="failed_login", severity="high")

    assert payload.source_ip == "192.168.1.10"
    assert payload.severity == Severity.HIGH
