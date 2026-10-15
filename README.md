# OweU

Splitting payments with friends: scan a receipt, assign each item
to the people who had it and see who owes what. 

## Tech stack
- **Backend:** Python, FastAPI, SQLAlchemy, Alembic
- **Database:** PostgreSQL
- **Frontend:** React, TypeScript, Vite

## Running locally

### Database
    cp .env.example .env
    docker compose up -d

### Backend
    cd backend
    uv sync
    uv run fastapi dev app/main.py

### Frontend
    cd frontend
    npm install
    npm run dev

## Status
Early development.
