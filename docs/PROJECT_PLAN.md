# AI-Powered SOC Platform Plan

## Phase 1: Foundation

- FastAPI backend
- React TypeScript frontend
- PostgreSQL configuration
- SQLAlchemy database layer
- Alembic migrations
- Docker Compose
- Health API
- SOC dashboard shell

## Phase 2: Core SOC

- `security_events`
- `alerts`
- `audit_logs`
- CSV/JSON log ingestion
- Event filtering
- Alert creation

## Phase 3: Threat Detection

- `rule_engine.py`
- Failed login detection
- Brute force detection
- Privilege escalation detection
- Port scanning detection
- Suspicious IP detection

## Phase 4: AI Incident Analysis

- `incident_analyzer.py`
- Severity classification
- Attack type classification
- Recommended response
- Incident summary

## Phase 5: Dashboard

- Total events
- Alert severity counts
- Top source IPs
- Recent incidents
- Threat timeline
