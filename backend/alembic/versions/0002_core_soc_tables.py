"""core soc tables

Revision ID: 0002_core_soc
Revises: 0001_initial
Create Date: 2026-06-13
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "0002_core_soc"
down_revision: Union[str, None] = "0001_initial"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    severity = postgresql.ENUM("low", "medium", "high", "critical", name="severity")
    event_status = postgresql.ENUM("open", "reviewed", "closed", name="eventstatus")
    alert_status = postgresql.ENUM("open", "acknowledged", "closed", name="alertstatus")
    severity.create(op.get_bind(), checkfirst=True)
    event_status.create(op.get_bind(), checkfirst=True)
    alert_status.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "security_events",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("timestamp", sa.DateTime(timezone=True), nullable=False),
        sa.Column("source_ip", sa.String(64), nullable=False),
        sa.Column("event_type", sa.String(120), nullable=False),
        sa.Column("severity", severity, nullable=False),
        sa.Column("raw_log", postgresql.JSONB(), nullable=False),
        sa.Column("status", event_status, nullable=False),
    )
    op.create_index("ix_security_events_source_ip", "security_events", ["source_ip"])
    op.create_index("ix_security_events_event_type", "security_events", ["event_type"])
    op.create_index("ix_security_events_severity", "security_events", ["severity"])

    op.create_table(
        "alerts",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("event_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("security_events.id"), nullable=False),
        sa.Column("title", sa.String(220), nullable=False),
        sa.Column("severity", severity, nullable=False),
        sa.Column("status", alert_status, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_alerts_event_id", "alerts", ["event_id"])
    op.create_index("ix_alerts_severity", "alerts", ["severity"])

    op.create_table(
        "audit_logs",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("action", sa.String(120), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_audit_logs_action", "audit_logs", ["action"])


def downgrade() -> None:
    op.drop_index("ix_audit_logs_action", table_name="audit_logs")
    op.drop_table("audit_logs")
    op.drop_index("ix_alerts_severity", table_name="alerts")
    op.drop_index("ix_alerts_event_id", table_name="alerts")
    op.drop_table("alerts")
    op.drop_index("ix_security_events_severity", table_name="security_events")
    op.drop_index("ix_security_events_event_type", table_name="security_events")
    op.drop_index("ix_security_events_source_ip", table_name="security_events")
    op.drop_table("security_events")
    postgresql.ENUM(name="alertstatus").drop(op.get_bind(), checkfirst=True)
    postgresql.ENUM(name="eventstatus").drop(op.get_bind(), checkfirst=True)
    postgresql.ENUM(name="severity").drop(op.get_bind(), checkfirst=True)
