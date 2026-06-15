from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.alert import Alert
from app.schemas.alert import AlertRead

router = APIRouter(prefix="/alerts")


@router.get("", response_model=list[AlertRead])
def read_alerts(db: Annotated[Session, Depends(get_db)]):
    return list(db.scalars(select(Alert).order_by(Alert.created_at.desc())))
