from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.models.audit_log import AuditLog
from app.models.security_event import SecurityEvent, Severity
from app.schemas.event import EventIngest


ALERT_SEVERITIES = {Severity.HIGH, Severity.CRITICAL}


def ingest_event(db: Session, payload: EventIngest) -> SecurityEvent:
    raw_log = payload.raw_log or payload.model_dump(mode="json")
    event = SecurityEvent(
        timestamp=payload.timestamp,
        source_ip=payload.source_ip,
        event_type=payload.event_type,
        severity=payload.severity,
        raw_log=raw_log,
    )
    db.add(event)
    db.flush()

    if event.severity in ALERT_SEVERITIES:
        db.add(Alert(event_id=event.id, title=f"{event.severity.upper()} {event.event_type}", severity=event.severity))

    db.add(AuditLog(action="EVENT_INGEST", description=f"Ingested {event.event_type} from {event.source_ip}"))
    db.commit()
    db.refresh(event)
    return event


def list_events(db: Session, severity: Severity | None = None, source_ip: str | None = None) -> list[SecurityEvent]:
    query = select(SecurityEvent).order_by(SecurityEvent.timestamp.desc())
    if severity:
        query = query.where(SecurityEvent.severity == severity)
    if source_ip:
        query = query.where(SecurityEvent.source_ip == source_ip)
    return list(db.scalars(query))
