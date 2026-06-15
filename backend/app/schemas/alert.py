from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.alert import AlertStatus
from app.models.security_event import Severity


class AlertRead(BaseModel):
    id: UUID
    event_id: UUID
    title: str
    severity: Severity
    status: AlertStatus
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
