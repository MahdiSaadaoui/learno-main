# Rapport Technique - Learno

This report summarizes the technical architecture and implementation of the Learno platform.

## 1. Project Context

Learno is a multi-service smart classroom platform with four user-facing roles:

- Student
- Teacher
- Guardian
- School/Admin

The platform combines web dashboards, backend APIs, AI-based session processing, and IoT/sensor data streams.

## 2. Global Architecture

```text
Frontend (Next.js dashboards)
        |
        v
Backend API (Express + Prisma + Socket.IO)
   |           |
   |           +--> Realtime channels
   |
   +--> PostgreSQL
   +--> AI service (FastAPI)
   +--> Sensor ingest (IoT endpoints/websocket)
```

## 3. Main Components

### 3.1 Frontend (`learno-web/learn`)

- Built with Next.js 16 + React 19
- Role-based route groups for student, teacher, guardian, and admin
- Unified API client with auth token refresh flow
- Realtime dashboard badges and updates via Socket.IO
- Student adaptive visual support using condition-driven theme variables

### 3.2 Backend (`learno-web/backend`)

- Express 5 REST API + Socket.IO
- Prisma ORM for PostgreSQL
- JWT auth + RBAC + Zod request validation
- Session lifecycle orchestration with AI service
- Admin analytics and live session monitoring
- Environment telemetry ingestion with fallback demo data

### 3.3 AI Service (`learno-ai`)

- FastAPI-based processing service
- Session start/stop processing pipeline
- Generates analysis payloads and lesson/advice outputs
- Sends webhook events back to backend

### 3.4 IoT Service (`learno-iot`)

- Sensor data source for classroom environment metrics
- Provides telemetry consumed by backend ingest job

## 4. Backend Internal Design

Backend documentation is split into:

- Operational README: `learno-web/backend/README.md`
- Full architecture/layers/security: `learno-web/backend/all.md`

The backend follows layered design:

1. API/transport layer
2. Middleware/policy layer
3. Domain modules layer
4. Integration layer
5. Data layer
6. Realtime layer
7. Background jobs layer

## 5. Security Strategy

Implemented controls include:

- Access JWT verification
- Refresh token lifecycle (cookie + DB hash)
- Role-based authorization guards
- Validation with Zod schemas
- Webhook secret checks for AI callbacks
- Socket authentication via JWT handshake
- Centralized error handling

## 6. Realtime and Monitoring

- Socket rooms for user, conversation, class, and session scopes
- Realtime alerts/messages/session updates to dashboards
- Admin live environment section updated from telemetry events

## 7. Demo Readiness

To support demo videos without physical IoT hardware:

- backend environment ingest supports synthetic telemetry fallback
- admin dashboard now displays deterministic demo environment values for live sessions when no real sensor reading exists

This keeps live admin monitoring visible even when IoT stream is absent.

## 8. Build and Execution

Typical local run order:

1. PostgreSQL + backend config
2. Backend (`npm run dev`)
3. AI service (`uvicorn api:app --reload --port 8000`)
4. Frontend (`npm run dev`)

Main endpoints:

- Frontend: `http://localhost:3000`
- Backend API health: `http://localhost:4000/api/health`
- Legacy frontend: `http://localhost:4000/app`

## 9. Documentation Index

- Root overview: `README.md`
- Frontend: `learno-web/learn/README.md`
- Backend: `learno-web/backend/README.md`
- Backend full architecture: `learno-web/backend/all.md`
- AI service: `learno-ai/README.md`
- Legacy frontend: `learno-web/frontend/README.md`

---

This technical report is intentionally high-level. Detailed backend internals are centralized in `learno-web/backend/all.md`.
