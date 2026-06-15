from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.security_event import Severity
from app.schemas.event import EventIngest, EventRead
from app.services.event_service import ingest_event, list_events

router = APIRouter(prefix="/events")


@router.post("/ingest", response_model=EventRead)
def ingest(payload: EventIngest, db: Annotated[Session, Depends(get_db)]):
    return ingest_event(db, payload)


@router.get("", response_model=list[EventRead])
def read_events(
    db: Annotated[Session, Depends(get_db)],
    severity: Severity | None = Query(default=None),
    source_ip: str | None = Query(default=None),
):
    return list_events(db, severity=severity, source_ip=source_ip)
