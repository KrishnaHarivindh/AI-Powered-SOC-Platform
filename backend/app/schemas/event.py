from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.models.security_event import EventStatus, Severity


class EventIngest(BaseModel):
    source_ip: str = Field(min_length=3, max_length=64)
    event_type: str = Field(min_length=2, max_length=120)
    severity: Severity
    timestamp: datetime | None = None
    raw_log: dict | None = None


class EventRead(BaseModel):
    id: UUID
    timestamp: datetime
    source_ip: str
    event_type: str
    severity: Severity
    raw_log: dict
    status: EventStatus

    model_config = ConfigDict(from_attributes=True)
