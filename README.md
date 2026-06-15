# AI-Powered SOC Platform

![CI](https://github.com/KrishnaHarivindh/AI-Powered-SOC-Platform/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/github/license/KrishnaHarivindh/AI-Powered-SOC-Platform)
![Last Commit](https://img.shields.io/github/last-commit/KrishnaHarivindh/AI-Powered-SOC-Platform)
![Language](https://img.shields.io/github/languages/top/KrishnaHarivindh/AI-Powered-SOC-Platform)

Mini enterprise SIEM and Security Operations Center platform inspired by Splunk, Elastic, Microsoft Sentinel, and IBM QRadar.

## Overview

AI-Powered SOC Platform is a full-stack cybersecurity analytics project for ingesting security events, monitoring alerts, and presenting operational visibility through a modern dashboard. It is built as a portfolio-ready foundation for security event management, alert triage, and SOC workflow automation.

## Core Capabilities

- Security event ingestion API
- Event search and listing endpoints
- Alert management foundation
- FastAPI backend with versioned API structure
- React and TypeScript dashboard shell
- PostgreSQL data layer with SQLAlchemy
- Alembic database migrations
- Docker Compose environment
- Health-check endpoint for service readiness

## Tech Stack

**Backend:** Python, FastAPI, SQLAlchemy, Alembic  
**Frontend:** React, TypeScript, Vite  
**Database:** PostgreSQL  
**DevOps:** Docker Compose  
**Domain:** SIEM, SOC operations, cybersecurity analytics

## Project Structure

```text
AI-Powered-SOC-Platform/
  backend/              FastAPI services, APIs, models, migrations
  frontend/             React TypeScript dashboard
  docs/                 Architecture and project documentation
  docker-compose.yml    Local infrastructure setup
  .env.example          Environment template
```

## Backend Setup

```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8001
```

Health API:

```text
http://127.0.0.1:8001/api/v1/health
```

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://127.0.0.1:5174
```

## API Surface

- `POST /api/v1/events/ingest`
- `GET /api/v1/events`
- `GET /api/v1/alerts`
- `GET /api/v1/health`

## Database Migrations

```bash
cd backend
python -m alembic upgrade head
```

## Roadmap

- Rule-based alert correlation
- AI-assisted alert summarization
- MITRE ATT&CK mapping
- Threat timeline visualization
- Analyst case management
- Dashboard metrics and incident reporting

## Portfolio Note

This project demonstrates backend API design, frontend dashboard engineering, database modeling, Docker-based local infrastructure, and cybersecurity product thinking.
