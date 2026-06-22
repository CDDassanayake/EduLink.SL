# EduLink SL Backend

FastAPI backend for the EduLink SL tutor booking marketplace.

## Tech Stack

- Python 3.12
- FastAPI 0.111+
- Pydantic v2
- SQLAlchemy 2.x (async)
- PostgreSQL 16
- Redis 7
- FastAPI-Users (auth)
- Celery (background tasks)
- Stripe (payments)
- LangChain + OpenAI (AI chat)
- Cloudinary (file uploads)

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI app initialization
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database connection
│   ├── models/              # SQLAlchemy ORM models
│   ├── schemas/             # Pydantic schemas
│   ├── api/
│   │   ├── deps.py          # Shared dependencies
│   │   └── routes/          # API route handlers
│   ├── services/            # Business logic
│   ├── websocket/           # WebSocket manager
│   └── workers/             # Celery tasks
├── alembic/                 # Database migrations
├── tests/                   # Test suite
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration
└── .env.example             # Environment variables template
```

## Setup Instructions

### 1. Start Infrastructure

From the project root:

```bash
docker-compose up -d
```

This starts PostgreSQL and Redis containers.

### 2. Create Virtual Environment

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and fill in your API keys:
- Stripe keys
- OpenAI API key
- Cloudinary credentials
- Resend API key
- Generate a secure SECRET_KEY

### 5. Run Database Migrations

```bash
alembic upgrade head
```

### 6. Seed Subjects Table

```bash
python -m app.seed
```

### 7. Start the Server

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

### 8. Start Celery Worker (Optional, for background tasks)

In a new terminal:

```bash
cd backend
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
celery -A app.workers.celery_app worker --loglevel=info
```

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Running Tests

```bash
pytest
```

## Development Notes

- All database operations use async SQLAlchemy 2 patterns
- All route handlers are async
- Use Pydantic v2 with `model_config = ConfigDict(from_attributes=True)`
- Follow the patterns defined in `ARCHITECTURE.md`

## Database Migrations

To create a new migration:

```bash
alembic revision --autogenerate -m "description"
```

To apply migrations:

```bash
alembic upgrade head
```

To rollback:

```bash
alembic downgrade -1
```
