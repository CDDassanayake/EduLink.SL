# EduLink SL

A full-stack tutor booking marketplace for Sri Lankan O/L, A/L, and university students. Connect students with verified tutors, manage bookings, process payments, and provide AI-powered career guidance.

## 🌟 Features

### For Students
- **Search Tutors**: Find tutors by subject, city, stream (O/L, A/L), teaching mode, and price
- **Book Sessions**: Single sessions or monthly packages with flexible scheduling
- **Secure Payments**: Integrated Stripe payment processing
- **Real-time Messaging**: Chat with tutors before and after bookings
- **AI Career Guidance**: AI-powered chatbot for career advice and university guidance
- **Reviews & Ratings**: Rate tutors after completed sessions
- **Booking Management**: View upcoming sessions, cancel with refund protection

### For Teachers
- **Verification System**: Submit documents for admin verification before posting
- **Class Listings**: Create and manage subject listings with pricing
- **Schedule Management**: Set availability slots and block specific dates
- **Earnings Dashboard**: Track income and payout history
- **Student Communication**: Message students to coordinate sessions
- **Merit System**: Build reputation through positive session outcomes
- **Weekly Payouts**: Automated payouts via Stripe Connect

### For Admins
- **Teacher Verification**: Review and approve/reject teacher applications
- **Platform Analytics**: View KPIs and platform statistics
- **User Management**: Manage user accounts and permissions
- **Dispute Resolution**: Handle booking disputes and refunds

## 🛠 Tech Stack

### Frontend
- **Framework**: SvelteKit 2.x with Svelte 5.x (runes)
- **Language**: TypeScript 5.x (strict mode)
- **Styling**: Tailwind CSS 3.x
- **Components**: shadcn-svelte
- **State Management**: Svelte 5 runes ($state, $derived, $effect)
- **API Client**: Svelte Query (TanStack)
- **Validation**: Zod 3.x

### Backend
- **Framework**: FastAPI 0.111+ (async throughout)
- **Language**: Python 3.12
- **Validation**: Pydantic v2
- **ORM**: SQLAlchemy 2.x (async)
- **Database**: PostgreSQL 16
- **Cache**: Redis 7
- **Authentication**: FastAPI-Users 13.x (JWT)
- **Background Tasks**: Celery 5.x
- **Payments**: Stripe
- **AI**: LangChain + OpenAI
- **File Storage**: Cloudinary
- **Real-time**: WebSocket with Redis pub/sub

### Infrastructure
- **Containerization**: Docker Compose
- **Database Migrations**: Alembic
- **API Documentation**: FastAPI auto-generated Swagger/ReDoc

## 📁 Project Structure

```
edulink-sl/
├── frontend/                    # SvelteKit application
│   ├── src/
│   │   ├── lib/
│   │   │   ├── components/     # Reusable components
│   │   │   ├── stores/         # Svelte 5 rune stores
│   │   │   ├── api/            # API client functions
│   │   │   └── schemas/        # Zod validation schemas
│   │   └── routes/
│   │       ├── (student)/      # Student routes
│   │       ├── (teacher)/      # Teacher routes
│   │       ├── (admin)/        # Admin routes
│   │       └── auth/           # Authentication
│   └── package.json
│
└── backend/                     # FastAPI application
    ├── app/
    │   ├── models/             # SQLAlchemy ORM models
    │   ├── schemas/            # Pydantic schemas
    │   ├── api/routes/         # API endpoints
    │   ├── services/           # Business logic
    │   ├── websocket/          # WebSocket manager
    │   └── workers/            # Celery tasks
    ├── alembic/                # Database migrations
    └── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- Node.js 18+
- Docker and Docker Compose
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/edulink-sl.git
cd edulink-sl
```

### 2. Start Infrastructure

```bash
docker-compose up -d
```

This starts PostgreSQL and Redis containers.

### 3. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys (Stripe, OpenAI, Cloudinary, etc.)

# Run database migrations
alembic upgrade head

# Seed subjects table
python -m app.seed

# Start the server
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

API Documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 4. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

### 5. Start Celery Worker (Optional)

In a new terminal:

```bash
cd backend
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
celery -A app.workers.celery_app worker --loglevel=info
```

## 🔐 Environment Variables

### Backend (.env)

```env
# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/edulink

# Redis
REDIS_URL=redis://localhost:6379/0

# Authentication
SECRET_KEY=your-secret-key-here

# Stripe
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# OpenAI
OPENAI_API_KEY=sk-...

# Cloudinary
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Email (Resend)
RESEND_API_KEY=re_...
```

### Frontend (.env)

```env
VITE_API_URL=http://localhost:8000/api/v1
```

## 📚 API Documentation

### Authentication Endpoints

- `POST /api/v1/auth/register` - Create account
- `POST /api/v1/auth/login` - Login
- `GET /api/v1/auth/me` - Get current user
- `POST /api/v1/auth/refresh` - Refresh token

### Tutor Endpoints

- `GET /api/v1/tutors` - Search tutors with filters
- `GET /api/v1/tutors/{id}/profile` - Get tutor profile
- `GET /api/v1/tutors/{id}/availability` - Get availability slots

### Booking Endpoints

- `POST /api/v1/bookings` - Create booking
- `GET /api/v1/bookings` - Get user's bookings
- `PATCH /api/v1/bookings/{id}/cancel` - Cancel booking

### Payment Endpoints

- `POST /api/v1/payments/checkout` - Create payment intent
- `POST /api/v1/payments/webhook` - Stripe webhook

### Admin Endpoints

- `GET /api/v1/admin/verifications` - Get teacher verifications
- `PATCH /api/v1/admin/verifications/{id}/approve` - Approve teacher
- `PATCH /api/v1/admin/verifications/{id}/reject` - Reject teacher

For complete API documentation, visit `http://localhost:8000/docs` when the backend is running.

## 👥 User Roles

### Student
- Browse and search tutors
- Book sessions (single or monthly packages)
- Pay via Stripe
- Chat with tutors
- Submit reviews
- Use AI career guidance

### Teacher
- Submit verification documents
- Create class listings
- Set availability schedule
- Manage bookings
- Track earnings
- Receive weekly payouts

### Admin
- Review teacher verifications
- Approve/reject applications
- View platform analytics
- Manage users
- Resolve disputes

## 🔧 Development

### Database Migrations

```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

### Running Tests

```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm run test
```

### Code Style

- **Frontend**: Follow Svelte 5 patterns with runes
- **Backend**: Follow FastAPI async patterns
- Use TypeScript strict mode

## 🌐 Deployment

### Backend

```bash
# Build Docker image
docker build -t edulink-backend .

# Run container
docker run -p 8000:8000 edulink-backend
```

### Frontend

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📧 Support

For support, email support@edulink.lk or open an issue on GitHub.
