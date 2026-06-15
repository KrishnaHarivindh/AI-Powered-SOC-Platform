from fastapi import APIRouter

from app.api.v1.routes import alerts, events, health

api_router = APIRouter()
api_router.include_router(alerts.router, tags=["alerts"])
api_router.include_router(events.router, tags=["events"])
api_router.include_router(health.router, tags=["health"])
