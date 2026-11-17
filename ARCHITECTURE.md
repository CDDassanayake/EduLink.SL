# EduLink SL — System Architecture & Workflow Document
**Version 1.0 | For AI-assisted development (Windsurf / Cursor / Claude)**

> **How to use this document:** Place `ARCHITECTURE.md` in your project root. At the start of every Windsurf session, begin with: *"Read ARCHITECTURE.md thoroughly before writing any code. Follow every convention defined in it exactly."*

---

## 1. SYSTEM OVERVIEW

EduLink SL is a full-stack tutor booking marketplace for Sri Lankan O/L, A/L, and university students. Three distinct user types (Student, Teacher, Admin) each have completely separate UI pipelines and API permissions. The system handles verified tutor listings, slot-based session booking, Stripe payments, real-time messaging, merit-based accountability, and an AI career guidance chatbot.

---

## 2. TECHNOLOGY STACK (exact versions — do not substitute)

```
FRONTEND
├── SvelteKit          2.x        (file-based routing, SSR, +layout.svelte)
├── Svelte             5.x        (use runes: $state, $derived, $effect)
├── TypeScript         5.x        (strict mode enabled — no 'any' allowed)
├── Tailwind CSS       3.x        (utility classes only, no @apply)
├── shadcn-svelte      latest     (component library — use for all UI primitives)
├── Svelte Query       (TanStack) (all API data fetching and caching)
└── Zod                3.x        (frontend form validation schemas)

BACKEND
├── Python             3.12
├── FastAPI            0.111+     (async throughout — no sync route handlers)
├── Pydantic           v2         (all schemas use model_config)
├── SQLAlchemy         2.x async  (use async_session, not Session)
├── Alembic            latest     (all schema changes via migrations only)
├── asyncpg            latest     (PostgreSQL async driver)
├── FastAPI-Users      13.x       (auth, JWT, OAuth — do not roll custom auth)
├── Redis              (via redis.asyncio)
├── Celery             5.x        (background jobs — email, reminders, payouts)
├── stripe             latest     (official Stripe Python SDK)
├── langchain          latest     (AI career chat — ConversationChain)
├── openai             latest     (OpenAI API client)
└── cloudinary         latest     (file/image uploads)

INFRASTRUCTURE
├── PostgreSQL         16
├── Redis              7
└── Docker Compose     (local dev — spins up postgres + redis)
```

---

## 3. PROJECT FOLDER STRUCTURE

```
edulink-sl/
│
├── ARCHITECTURE.md              ← THIS FILE — always read first
├── docker-compose.yml
├── .env.example
│
├── frontend/                    ← SvelteKit application
│   ├── src/
│   │   ├── app.html
│   │   ├── app.d.ts
│   │   ├── lib/
│   │   │   ├── components/
│   │   │   │   ├── ui/          ← shadcn-svelte components (auto-generated)
│   │   │   │   ├── layout/
│   │   │   │   │   ├── PublicNav.svelte
│   │   │   │   │   ├── AuthSidebar.svelte
│   │   │   │   │   └── AppTopbar.svelte
│   │   │   │   ├── tutor/
│   │   │   │   │   ├── TutorCard.svelte
│   │   │   │   │   ├── TutorListCard.svelte
│   │   │   │   │   └── AvailabilityGrid.svelte
│   │   │   │   ├── booking/
│   │   │   │   │   ├── BookingPanel.svelte
│   │   │   │   │   └── BookingCard.svelte
│   │   │   │   ├── messaging/
│   │   │   │   │   ├── ConversationList.svelte
│   │   │   │   │   └── ChatWindow.svelte
│   │   │   │   └── charts/
│   │   │   │       └── BarChart.svelte
│   │   │   ├── stores/
│   │   │   │   ├── auth.svelte.ts      ← $state rune store for current user
│   │   │   │   ├── websocket.svelte.ts ← WebSocket connection store
│   │   │   │   └── notifications.svelte.ts
│   │   │   ├── api/
│   │   │   │   ├── client.ts           ← base fetch wrapper with auth headers
│   │   │   │   ├── auth.ts
│   │   │   │   ├── tutors.ts
│   │   │   │   ├── bookings.ts
│   │   │   │   ├── messages.ts
│   │   │   │   └── payments.ts
│   │   │   ├── schemas/
│   │   │   │   └── index.ts            ← Zod validation schemas (mirrors Pydantic)
│   │   │   └── utils/
│   │   │       ├── dates.ts
│   │   │       └── currency.ts         ← LKR formatting helpers
│   │   └── routes/
│   │       ├── +layout.svelte          ← root layout (loads auth state)
│   │       ├── +layout.ts              ← root load function
│   │       ├── +page.svelte            ← Landing page (index)
│   │       ├── find-tutors/
│   │       │   └── +page.svelte
│   │       ├── streams/
│   │       │   └── +page.svelte
│   │       ├── career-guidance/
│   │       │   └── +page.svelte
│   │       ├── auth/
│   │       │   ├── login/+page.svelte
│   │       │   └── register/+page.svelte
│   │       ├── tutor/
│   │       │   └── [id]/+page.svelte   ← dynamic tutor profile
│   │       ├── (student)/              ← route group — requires student role
│   │       │   ├── +layout.svelte      ← student sidebar layout
│   │       │   ├── +layout.ts          ← guard: redirect if not student
│   │       │   ├── dashboard/+page.svelte
│   │       │   ├── bookings/+page.svelte
│   │       │   ├── messages/+page.svelte
│   │       │   ├── ai-chat/+page.svelte
│   │       │   └── book/[tutorId]/+page.svelte
│   │       ├── (teacher)/              ← route group — requires teacher role
│   │       │   ├── +layout.svelte      ← teacher sidebar layout
│   │       │   ├── +layout.ts          ← guard: redirect if not teacher
│   │       │   ├── dashboard/+page.svelte
│   │       │   ├── verification/+page.svelte
│   │       │   ├── post-class/+page.svelte
│   │       │   ├── schedule/+page.svelte
│   │       │   ├── messages/+page.svelte
│   │       │   └── earnings/+page.svelte
│   │       └── (admin)/                ← route group — requires admin role
│   │           ├── +layout.svelte
│   │           ├── +layout.ts          ← guard: redirect if not admin
│   │           ├── dashboard/+page.svelte
│   │           └── verifications/+page.svelte
│   ├── static/
│   ├── svelte.config.js
│   ├── tailwind.config.ts
│   ├── vite.config.ts
│   └── package.json
│
└── backend/                     ← FastAPI application
    ├── app/
    │   ├── main.py              ← FastAPI app init, CORS, router includes
    │   ├── config.py            ← Pydantic BaseSettings — reads from .env
    │   ├── database.py          ← async engine + session factory
    │   │
    │   ├── models/              ← SQLAlchemy ORM models (one file per domain)
    │   │   ├── __init__.py
    │   │   ├── user.py          ← User, TeacherProfile
    │   │   ├── listing.py       ← Subject, TeacherListing
    │   │   ├── booking.py       ← AvailabilitySlot, BlockedDate, Booking
    │   │   ├── payment.py       ← Payment, ListingPayment
    │   │   ├── review.py        ← Review
    │   │   ├── merit.py         ← MeritEvent
    │   │   ├── message.py       ← Conversation, Message
    │   │   └── notification.py  ← Notification
    │   │
    │   ├── schemas/             ← Pydantic v2 request/response schemas
    │   │   ├── auth.py
    │   │   ├── tutor.py
    │   │   ├── booking.py
    │   │   ├── payment.py
    │   │   ├── review.py
    │   │   └── message.py
    │   │
    │   ├── api/
    │   │   ├── deps.py          ← shared dependencies (get_current_user, get_db)
    │   │   └── routes/
    │   │       ├── auth.py
    │   │       ├── tutors.py
    │   │       ├── bookings.py
    │   │       ├── payments.py
    │   │       ├── reviews.py
    │   │       ├── messages.py
    │   │       ├── ai_chat.py
    │   │       └── admin.py
    │   │
    │   ├── services/            ← business logic (called by routes, never by each other)
    │   │   ├── booking_service.py
    │   │   ├── payment_service.py
    │   │   ├── merit_service.py
    │   │   ├── notification_service.py
    │   │   └── ai_service.py
    │   │
    │   ├── websocket/
    │   │   └── manager.py       ← ConnectionManager using Redis pub/sub
    │   │
    │   └── workers/             ← Celery tasks
    │       ├── celery_app.py
    │       ├── email_tasks.py
    │       └── payout_tasks.py
    │
    ├── alembic/
    │   ├── versions/
    │   └── env.py
    ├── tests/
    ├── requirements.txt
    ├── Dockerfile
    └── .env.example
```

---

## 4. USER ROLES & PERMISSIONS

```
ROLE          ACCESS LEVEL      INITIAL STATE AFTER REGISTER
─────────────────────────────────────────────────────────────
STUDENT       Authenticated     Active immediately after email verify
TEACHER       Authenticated     Locked — must complete verification first
ADMIN         Authenticated     Created manually by superadmin only

PERMISSION MATRIX
                         STUDENT   TEACHER   ADMIN
Browse public pages        ✓         ✓         ✓
View tutor profile         ✓         ✓         ✓
Book a session             ✓         ✗         ✗
Post a class listing       ✗         ✓         ✗
Manage own schedule        ✗         ✓         ✗
View own earnings          ✗         ✓         ✗
Send/receive messages      ✓         ✓         ✗
Use AI career chat         ✓         ✗         ✗
Approve verifications      ✗         ✗         ✓
View platform analytics    ✗         ✗         ✓
Manage all users           ✗         ✗         ✓
```

---

## 5. AUTHENTICATION FLOW

```
REGISTRATION
─────────────────────────────────────────────────────────────
1. POST /api/v1/auth/register
   Body: { email, password, full_name, role, city, phone }

2. FastAPI-Users creates User record with is_verified=False
   A verification email is sent via Celery task → Resend API

3. User clicks verification link → GET /api/v1/auth/verify?token=xxx
   is_verified set to True

4. If role=TEACHER → teacher_verification_status='PENDING'
   Teacher is redirected to /teacher/verification on first login
   Teacher CANNOT access /teacher/dashboard until status='APPROVED'

5. If role=STUDENT → active immediately, redirect to /student/dashboard

LOGIN
─────────────────────────────────────────────────────────────
1. POST /api/v1/auth/login
   Body: { username (email), password }
   Returns: { access_token, token_type: 'bearer' }
   access_token expires in 30 minutes

2. POST /api/v1/auth/refresh
   Body: { refresh_token }
   Returns: new access_token

3. Frontend stores access_token in memory (NOT localStorage)
   Stores refresh_token in httpOnly cookie

4. All authenticated requests include header:
   Authorization: Bearer <access_token>

ROLE DETECTION & REDIRECT
─────────────────────────────────────────────────────────────
GET /api/v1/auth/me returns:
  { id, email, full_name, role, city, is_verified,
    teacher_verification_status }    ← only present if role=TEACHER

SvelteKit root +layout.ts calls /auth/me on every page load.
Stores result in auth.svelte.ts store.
Route group +layout.ts files check role and redirect:
  (student)/+layout.ts → if role !== 'STUDENT' → redirect /auth/login
  (teacher)/+layout.ts → if role !== 'TEACHER' → redirect /auth/login
                       → if status !== 'APPROVED' → redirect /teacher/verification
  (admin)/+layout.ts   → if role !== 'ADMIN' → redirect /auth/login
```

---

## 6. SYSTEM WORKFLOWS

### 6.1 Student Booking Flow (complete end-to-end)

```
STEP 1 — Discovery (public, no auth required)
  Student visits /find-tutors
  GET /api/v1/tutors?subject=physics&city=colombo&stream=AL_SCIENCE&mode=online
  Server returns paginated list of TeacherListing records
  UI shows tutor cards with name, merit, rating, price, tags

STEP 2 — Profile view (requires authentication)
  Student clicks "View profile"
  SvelteKit checks auth store → if no token → redirect /auth/login?redirect=/tutor/[id]
  After login → redirect back to /tutor/[id]
  GET /api/v1/tutors/{tutor_id}/profile
  GET /api/v1/tutors/{tutor_id}/availability?week=2025-06-23
  Returns availability slots, booked slots, and teacher details

STEP 3 — Select slot
  Student selects date → time slot → session type (SINGLE | MONTHLY)
  Client calculates price:
    SINGLE:  listing.hourly_rate × 1
    MONTHLY: listing.hourly_rate × 4 × 0.90   (10% discount)
  Platform fee: session_total × 0.10

STEP 4 — Create Stripe Checkout (payment intent)
  POST /api/v1/payments/checkout
  Body: { tutor_id, listing_id, slot_datetime, session_type }
  Server creates Stripe PaymentIntent with metadata
  Returns: { client_secret, payment_intent_id }
  Frontend uses Stripe.js Elements to collect card details
  Student clicks "Confirm & Pay"

STEP 5 — Stripe webhook confirms payment
  Stripe calls POST /api/v1/payments/webhook (signed)
  Event: payment_intent.succeeded
  Server:
    1. Creates Booking record (status=CONFIRMED)
    2. Marks slot as BOOKED in AvailabilitySlot
    3. Creates Payment record with platform_fee
    4. Sends confirmation email via Celery
    5. Sends in-app notification to teacher
    6. Schedules 24h and 1h reminder emails via Celery beat

STEP 6 — Session takes place
  Teacher marks session ATTENDED via PATCH /api/v1/bookings/{id}/attend
  This:
    1. Changes booking status to ATTENDED
    2. Adds +5 merit to teacher
    3. Unlocks review ability for student (booking.can_review = True)
    4. Queues teacher payout in Celery (weekly settlement)

STEP 7 — Review (optional, 7-day window)
  Student submits review ONLY if booking.status == 'ATTENDED'
  POST /api/v1/reviews
  Body: { booking_id, rating (1-5), comment }
  Server validates booking.student_id == current_user.id
  Updates teacher's average rating via SQL AVG recalculation

CANCELLATION RULES (enforced server-side)
  hours_until_session >= 24h → refund 100%,  merit delta: -3  (student) / -5 (teacher)
  hours_until_session < 24h  → refund 60%,   merit delta: -10 (student) / -15 (teacher)
  Refund processed via Stripe Refunds API
  Merit delta applied via POST /api/v1/merit/apply (internal, not public)
```

### 6.2 Teacher Listing Flow (complete end-to-end)

```
STEP 1 — Register as teacher
  POST /api/v1/auth/register with role='TEACHER'
  Redirect → /teacher/verification

STEP 2 — Submit verification documents
  Teacher uploads NIC front, NIC back, degree certificate
  Files uploaded to Cloudinary via POST /api/v1/teachers/documents
  Returns Cloudinary URLs stored in TeacherProfile.document_urls (JSON array)
  Teacher selects subjects they want to teach
  PATCH /api/v1/teachers/profile
  Body: { subjects, bio, years_experience, teaching_mode, preferred_language }
  teacher_verification_status remains 'PENDING'

STEP 3 — Admin reviews (see Admin flow 6.4)
  Admin approves → teacher_verification_status = 'APPROVED'
  Email sent to teacher → they can now access /teacher/dashboard

STEP 4 — Post a class listing
  Teacher goes to /teacher/post-class
  Fills form: subject, stream, class_type, mode, hourly_rate, description, trial_available
  Selects plan: BASIC (30 days / LKR 500), STANDARD (90 days / LKR 1200), PREMIUM (180 days / LKR 2000)
  POST /api/v1/listings (creates listing, status='INACTIVE' until paid)
  Returns: { listing_id, selected_plan, amount_due }

STEP 5 — Pay for listing
  POST /api/v1/payments/listing-checkout
  Body: { listing_id, plan }
  Returns Stripe PaymentIntent client_secret
  Teacher completes payment

STEP 6 — Listing goes live
  Stripe webhook: payment_intent.succeeded
  Server:
    1. Creates ListingPayment record
    2. Sets listing.status = 'ACTIVE'
    3. Sets listing.expires_at = now + plan_days
    4. Listing appears in /find-tutors search results immediately

STEP 7 — Manage schedule
  Teacher sets weekly availability via PUT /api/v1/schedule
  Body: { slots: [{ day_of_week, start_time, end_time, is_recurring }] }
  Teacher can block specific dates via POST /api/v1/schedule/block
  Body: { date, reason }

STEP 8 — Receive bookings and conduct sessions
  When student books → teacher gets notification
  Teacher views today's schedule on dashboard
  After session → PATCH /api/v1/bookings/{id}/attend
  Earnings accumulate → weekly payout via Stripe Connect
```

### 6.3 Real-time Messaging Flow

```
CONNECTION
  User authenticates → receives JWT access_token
  Frontend opens WebSocket:
    ws://api.edulink.lk/ws/chat?token=<access_token>
  ConnectionManager validates token → extracts user_id
  Adds connection to Redis pub/sub channel: user:{user_id}

SEND MESSAGE
  User types message → clicks send
  WebSocket sends JSON:
    { type: 'message', conversation_id: 'uuid', content: 'Hello' }
  
  Server (websocket/manager.py):
    1. Saves Message to PostgreSQL
    2. Publishes to Redis channel: conversation:{conversation_id}
    3. All users subscribed to that conversation receive the message
    4. Redis pub/sub delivers to other user's WebSocket connection

  Other user's browser receives:
    { type: 'message', conversation_id, sender_id, content, created_at }
  
  Frontend appends message to chat window

UNREAD COUNT
  On connect, server publishes unread_count to user channel
  Frontend updates notification badge
  On message open → PATCH /api/v1/messages/{conversation_id}/read
  Decrements unread count in Redis

CONVERSATION TYPES
  STUDENT_TEACHER:  created when student first messages a teacher from profile page
  TEACHER_TEACHER:  teachers can message each other
  STUDENT_STUDENT:  students can message each other
  All conversation types use same WebSocket, same Message model
```

### 6.4 Admin Verification Flow

```
Admin goes to /admin/verifications
GET /api/v1/admin/verifications?status=PENDING
Returns list of TeacherProfile records with PENDING status

Admin reviews documents (Cloudinary links open in new tab)
Admin actions:

  APPROVE:
    PATCH /api/v1/admin/verifications/{teacher_id}/approve
    Server:
      1. Sets teacher_verification_status = 'APPROVED'
      2. Sends approval email to teacher via Celery
      3. Teacher can now access full teacher portal

  REJECT:
    PATCH /api/v1/admin/verifications/{teacher_id}/reject
    Body: { reason }
    Server:
      1. Sets teacher_verification_status = 'REJECTED'
      2. Sends rejection email with reason to teacher via Celery

  REQUEST MORE DOCUMENTS:
    POST /api/v1/admin/verifications/{teacher_id}/request-docs
    Body: { message }
    Sends email with specific document request to teacher
```

---

## 7. DATABASE SCHEMA

### Complete table definitions with relationships

```sql
-- USERS (FastAPI-Users managed)
users
  id                  UUID PK DEFAULT gen_random_uuid()
  email               VARCHAR(255) UNIQUE NOT NULL
  hashed_password     VARCHAR(255)
  full_name           VARCHAR(255) NOT NULL
  role                ENUM('STUDENT','TEACHER','ADMIN') NOT NULL
  city                VARCHAR(100)
  phone               VARCHAR(20)
  profile_photo_url   VARCHAR(500)
  merit_score         INTEGER DEFAULT 100
  is_active           BOOLEAN DEFAULT TRUE
  is_verified         BOOLEAN DEFAULT FALSE
  is_superuser        BOOLEAN DEFAULT FALSE
  created_at          TIMESTAMPTZ DEFAULT NOW()
  updated_at          TIMESTAMPTZ DEFAULT NOW()

-- TEACHER PROFILES (1:1 with users where role=TEACHER)
teacher_profiles
  id                          UUID PK
  user_id                     UUID FK → users.id UNIQUE
  bio                         TEXT
  years_experience            INTEGER
  document_urls               JSONB   -- array of Cloudinary URLs
  verification_status         ENUM('PENDING','APPROVED','REJECTED') DEFAULT 'PENDING'
  verification_note           TEXT    -- admin rejection reason
  stripe_connect_account_id   VARCHAR(100)
  listing_active              BOOLEAN DEFAULT FALSE
  updated_at                  TIMESTAMPTZ DEFAULT NOW()

-- SUBJECTS (seeded data)
subjects
  id            UUID PK
  name          VARCHAR(100) NOT NULL
  category      ENUM('OL','AL_SCIENCE','AL_ARTS','AL_COMMERCE',
                     'AL_TECHNOLOGY','UNIVERSITY','LANGUAGE','OTHER')
  display_order INTEGER DEFAULT 0

-- TEACHER LISTINGS (one per subject per teacher)
teacher_listings
  id                UUID PK
  teacher_id        UUID FK → users.id
  subject_id        UUID FK → subjects.id
  mode              ENUM('ONLINE','IN_PERSON','HOME_VISIT','FLEXIBLE')
  class_type        ENUM('INDIVIDUAL','GROUP')
  hourly_rate       NUMERIC(10,2) NOT NULL
  description       TEXT
  trial_available   BOOLEAN DEFAULT FALSE
  trial_rate        NUMERIC(10,2)
  max_group_size    INTEGER         -- NULL for individual
  status            ENUM('ACTIVE','INACTIVE','EXPIRED') DEFAULT 'INACTIVE'
  expires_at        TIMESTAMPTZ
  created_at        TIMESTAMPTZ DEFAULT NOW()
  INDEX: (teacher_id, subject_id, status)

-- AVAILABILITY SLOTS
availability_slots
  id            UUID PK
  teacher_id    UUID FK → users.id
  day_of_week   SMALLINT  -- 0=Mon, 6=Sun
  start_time    TIME NOT NULL
  end_time      TIME NOT NULL
  is_recurring  BOOLEAN DEFAULT TRUE

-- BLOCKED DATES
blocked_dates
  id            UUID PK
  teacher_id    UUID FK → users.id
  blocked_date  DATE NOT NULL
  reason        VARCHAR(255)

-- BOOKINGS
bookings
  id              UUID PK
  student_id      UUID FK → users.id
  teacher_id      UUID FK → users.id
  listing_id      UUID FK → teacher_listings.id
  session_start   TIMESTAMPTZ NOT NULL
  session_end     TIMESTAMPTZ NOT NULL
  booking_type    ENUM('SINGLE','MONTHLY')
  package_weeks   INTEGER         -- NULL for SINGLE
  status          ENUM('PENDING','CONFIRMED','ATTENDED','CANCELLED','DISPUTED')
                  DEFAULT 'PENDING'
  cancelled_by    UUID FK → users.id  -- NULL if not cancelled
  cancel_reason   TEXT
  cancelled_at    TIMESTAMPTZ
  can_review      BOOLEAN DEFAULT FALSE  -- TRUE after ATTENDED
  created_at      TIMESTAMPTZ DEFAULT NOW()
  INDEX: (teacher_id, session_start, status)
  INDEX: (student_id, status)

-- PAYMENTS (student pays for session)
payments
  id                      UUID PK
  booking_id              UUID FK → bookings.id
  student_id              UUID FK → users.id
  teacher_id              UUID FK → users.id
  gross_amount            NUMERIC(10,2)
  platform_fee            NUMERIC(10,2)   -- 10% of gross
  teacher_payout_amount   NUMERIC(10,2)   -- gross - platform_fee
  currency                VARCHAR(3) DEFAULT 'LKR'
  stripe_payment_intent   VARCHAR(100) UNIQUE
  stripe_transfer_id      VARCHAR(100)
  status                  ENUM('PENDING','CAPTURED','REFUNDED',
                               'PARTIALLY_REFUNDED','FAILED')
                          DEFAULT 'PENDING'
  refund_amount           NUMERIC(10,2)
  created_at              TIMESTAMPTZ DEFAULT NOW()

-- LISTING PAYMENTS (teacher pays to post listing)
listing_payments
  id                      UUID PK
  listing_id              UUID FK → teacher_listings.id
  teacher_id              UUID FK → users.id
  plan                    ENUM('BASIC','STANDARD','PREMIUM')
  amount                  NUMERIC(10,2)
  days_active             INTEGER
  stripe_payment_intent   VARCHAR(100) UNIQUE
  status                  ENUM('PENDING','PAID','FAILED') DEFAULT 'PENDING'
  created_at              TIMESTAMPTZ DEFAULT NOW()

-- REVIEWS
reviews
  id          UUID PK
  booking_id  UUID FK → bookings.id UNIQUE  -- one review per booking
  student_id  UUID FK → users.id
  teacher_id  UUID FK → users.id
  rating      SMALLINT NOT NULL  -- 1 to 5
  comment     TEXT
  is_visible  BOOLEAN DEFAULT TRUE
  created_at  TIMESTAMPTZ DEFAULT NOW()
  INDEX: (teacher_id, is_visible)

-- MERIT EVENTS
merit_events
  id          UUID PK
  user_id     UUID FK → users.id
  booking_id  UUID FK → bookings.id  -- NULL for platform bonuses
  delta       INTEGER NOT NULL  -- positive or negative
  reason      VARCHAR(255) NOT NULL
  created_at  TIMESTAMPTZ DEFAULT NOW()

-- CONVERSATIONS
conversations
  id               UUID PK
  type             ENUM('STUDENT_TEACHER','TEACHER_TEACHER','STUDENT_STUDENT')
  participant_ids  UUID[]  -- always exactly 2 participants
  created_at       TIMESTAMPTZ DEFAULT NOW()

-- MESSAGES
messages
  id               UUID PK
  conversation_id  UUID FK → conversations.id
  sender_id        UUID FK → users.id
  content          TEXT NOT NULL
  read_at          TIMESTAMPTZ  -- NULL if unread
  created_at       TIMESTAMPTZ DEFAULT NOW()
  INDEX: (conversation_id, created_at DESC)

-- NOTIFICATIONS
notifications
  id          UUID PK
  user_id     UUID FK → users.id
  type        VARCHAR(50)   -- 'BOOKING_CONFIRMED','BOOKING_REMINDER', etc.
  title       VARCHAR(255)
  body        TEXT
  is_read     BOOLEAN DEFAULT FALSE
  link        VARCHAR(255)  -- frontend route to navigate to on click
  created_at  TIMESTAMPTZ DEFAULT NOW()
```

---

## 8. API ENDPOINTS (complete reference)

```
BASE URL: http://localhost:8000/api/v1
DOCS:     http://localhost:8000/docs  (FastAPI auto-generated Swagger)

AUTH
  POST  /auth/register          Create account
  POST  /auth/login             Get JWT tokens
  POST  /auth/refresh           Refresh access token
  GET   /auth/verify            Email verification
  GET   /auth/me                Current user info
  PATCH /auth/me                Update profile

TUTORS (public read, auth required for profile details)
  GET   /tutors                 Search with filters
                                Query: subject_id, city, stream, mode,
                                       min_rating, max_price, available_today
  GET   /tutors/{id}/profile    Full tutor profile (auth required)
  GET   /tutors/{id}/availability  Weekly slots
                                Query: week=YYYY-MM-DD (Monday of week)
  GET   /tutors/{id}/reviews    Paginated reviews

TEACHER MANAGEMENT (teacher role only)
  GET   /teacher/profile        Own profile
  PUT   /teacher/profile        Update bio, rates, subjects
  POST  /teacher/documents      Upload verification docs to Cloudinary
  GET   /teacher/listings       Own listings
  POST  /teacher/listings       Create new listing (status=INACTIVE until paid)
  PATCH /teacher/listings/{id}  Update listing
  DELETE /teacher/listings/{id} Delete listing
  GET   /teacher/bookings       Upcoming + past bookings
  PATCH /teacher/bookings/{id}/attend  Mark session as attended
  GET   /teacher/earnings       Earnings summary + breakdown
  GET   /teacher/payouts        Payout history

SCHEDULE (teacher role only)
  GET   /schedule               Current week availability
  PUT   /schedule               Set recurring availability slots
  POST  /schedule/block         Block a specific date
  DELETE /schedule/block/{id}   Unblock a date

BOOKINGS (student role only)
  POST  /bookings               Create booking (triggers payment intent)
  GET   /bookings               Student's bookings
  GET   /bookings/{id}          Single booking detail
  PATCH /bookings/{id}/cancel   Cancel booking

PAYMENTS
  POST  /payments/checkout            Student session checkout
  POST  /payments/listing-checkout    Teacher listing payment
  POST  /payments/webhook             Stripe webhook (verify signature)
  GET   /payments/history             Payment history for current user
  POST  /payments/refund/{booking_id} Request refund

REVIEWS (student role only, verified bookings)
  POST  /reviews                Submit review
  GET   /reviews/teacher/{id}   Get tutor's reviews (public)

MESSAGES
  GET   /conversations          List conversations for current user
  POST  /conversations          Start new conversation
  GET   /conversations/{id}/messages  Message history
  PATCH /conversations/{id}/read      Mark conversation as read
  WS    /ws/chat                WebSocket connection

AI CHAT (student role only)
  POST  /ai/chat                Send message, get AI response
  GET   /ai/chat/history        Get conversation history
  DELETE /ai/chat/history       Clear conversation memory

ADMIN (admin role only)
  GET   /admin/analytics        Platform KPIs
  GET   /admin/verifications    Pending/all teacher verifications
  PATCH /admin/verifications/{id}/approve
  PATCH /admin/verifications/{id}/reject
  POST  /admin/verifications/{id}/request-docs
  GET   /admin/users            All users
  PATCH /admin/users/{id}/suspend
  GET   /admin/disputes         Open disputes
  PATCH /admin/disputes/{id}/resolve
  GET   /admin/reviews          All reviews
  DELETE /admin/reviews/{id}    Remove review
```

---

## 9. SVELTE 5 PATTERNS (follow exactly — do not use Svelte 4 syntax)

```typescript
// STORES — use $state rune, not writable()
// src/lib/stores/auth.svelte.ts
let user = $state<User | null>(null);
let isLoading = $state(true);

export function getAuthStore() {
  return {
    get user() { return user; },
    get isLoading() { return isLoading; },
    set(newUser: User | null) { user = newUser; },
    setLoading(val: boolean) { isLoading = val; }
  };
}

// COMPONENTS — use $props() not export let
// src/lib/components/tutor/TutorCard.svelte
<script lang="ts">
  import type { TutorListing } from '$lib/types';
  let { tutor, onBook }: { tutor: TutorListing; onBook?: () => void } = $props();
  let isHovered = $state(false);
  let priceFormatted = $derived(`LKR ${tutor.hourly_rate.toLocaleString()}/hr`);
</script>

// ROUTE GUARDS — in +layout.ts files
// src/routes/(student)/+layout.ts
import { redirect } from '@sveltejs/kit';
export const load = async ({ parent }) => {
  const { user } = await parent();
  if (!user) throw redirect(302, '/auth/login');
  if (user.role !== 'STUDENT') throw redirect(302, '/auth/login');
  return {};
};

// API CLIENT — always use this wrapper
// src/lib/api/client.ts
export async function apiClient<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const token = getAccessToken(); // from memory store
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
  });
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || 'Request failed');
  }
  return response.json();
}
```

---

## 10. FASTAPI PATTERNS (follow exactly)

```python
# ROUTE HANDLER PATTERN
# app/api/routes/bookings.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_current_active_user, get_db, require_student
from app.schemas.booking import BookingCreate, BookingResponse
from app.services.booking_service import BookingService
from app.models.user import User

router = APIRouter(prefix="/bookings", tags=["bookings"])

@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(
    booking_data: BookingCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_student),   # enforces STUDENT role
):
    service = BookingService(db)
    booking = await service.create_booking(
        student_id=current_user.id,
        booking_data=booking_data
    )
    return booking

# SERVICE PATTERN
# app/services/booking_service.py
class BookingService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_booking(self, student_id: UUID, booking_data: BookingCreate):
        # 1. Check slot is not already booked (with SELECT FOR UPDATE)
        # 2. Create Stripe PaymentIntent
        # 3. Create Booking with status=PENDING
        # 4. Return booking + stripe client_secret

# PYDANTIC SCHEMA PATTERN
# app/schemas/booking.py
from pydantic import BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class BookingCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tutor_id: UUID
    listing_id: UUID
    slot_datetime: datetime
    session_type: Literal['SINGLE', 'MONTHLY']

# DEPENDENCY PATTERN
# app/api/deps.py
async def require_teacher(
    current_user: User = Depends(get_current_active_user)
) -> User:
    if current_user.role != 'TEACHER':
        raise HTTPException(status_code=403, detail="Teacher access required")
    if current_user.teacher_profile.verification_status != 'APPROVED':
        raise HTTPException(status_code=403, detail="Account not yet verified")
    return current_user
```

---

## 11. ENVIRONMENT VARIABLES

```bash
# backend/.env  (never commit this file)

# Database
DATABASE_URL=postgresql+asyncpg://edulink:password@localhost:5432/edulink_db

# Redis
REDIS_URL=redis://localhost:6379/0

# Auth
SECRET_KEY=your-secret-key-minimum-32-chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Google OAuth (optional)
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=

# Stripe
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
STRIPE_CONNECT_CLIENT_ID=ca_...

# OpenAI
OPENAI_API_KEY=sk-...

# Cloudinary
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=

# Email (Resend)
RESEND_API_KEY=re_...
FROM_EMAIL=noreply@edulink.lk

# App
FRONTEND_URL=http://localhost:5173
ENVIRONMENT=development   # development | production
```

```bash
# frontend/.env.local  (never commit this file)
PUBLIC_API_URL=http://localhost:8000/api/v1
PUBLIC_WS_URL=ws://localhost:8000
PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_...
```

---

## 12. DOCKER COMPOSE (local development)

```yaml
# docker-compose.yml
version: '3.9'
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: edulink_db
      POSTGRES_USER: edulink
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

---

## 13. DEVELOPMENT SETUP SEQUENCE

```bash
# 1 — Clone repository
git clone https://github.com/YOUR_USERNAME/edulink-sl.git
cd edulink-sl

# 2 — Start infrastructure
docker-compose up -d

# 3 — Backend setup
cd backend
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # Fill in your keys
alembic upgrade head               # Run all migrations
python -m app.seed                 # Seed subjects table
uvicorn app.main:app --reload --port 8000

# 4 — Frontend setup (new terminal)
cd frontend
npm install
cp .env.example .env.local         # Fill in your keys
npm run dev                        # Starts on http://localhost:5173

# 5 — Celery worker (new terminal, for email/jobs)
cd backend
celery -A app.workers.celery_app worker --loglevel=info

# Verify setup
# Backend docs:  http://localhost:8000/docs
# Frontend:      http://localhost:5173
```

---

## 14. BUSINESS RULES (enforce server-side, never trust client)

```
MERIT SYSTEM
  Teacher marks attended       → student: no change, teacher: +5
  Student cancels ≥24h before  → student: -3,  teacher: 0,   refund: 100%
  Student cancels <24h before  → student: -10, teacher: +3,  refund: 60%
  Teacher cancels ≥24h before  → student: 0,   teacher: -5,  refund: 100%
  Teacher cancels <24h before  → student: 0,   teacher: -15, refund: 100%
  Student no-show              → student: -15, teacher: +5,  refund: 0%
  Teacher no-show              → student: 0,   teacher: -20, refund: 100%
  merit_score < 40 (student)   → blocked from creating new bookings
  merit_score < 60 (teacher)   → listing demoted in search ranking

PLATFORM COMMISSION
  Student session payment      → 10% retained by platform
  Weekly payout to teacher     → gross_session_total × 0.90
  Listing fee                  → 100% platform revenue (non-refundable)

REVIEW RULES
  Only allowed if booking.status == 'ATTENDED'
  One review per booking (enforced by UNIQUE constraint)
  7-day window from session_end to submit review
  Tutor avg_rating = recalculated after every new review

SLOT CONFLICT PREVENTION
  When creating booking → use SELECT FOR UPDATE on the slot
  Two concurrent requests for same slot → second one gets 409 Conflict
  Implemented in BookingService.create_booking() as a transaction

TEACHER VERIFICATION
  Teacher cannot create listings until verification_status == 'APPROVED'
  Documents stored in Cloudinary (not local filesystem)
  Admin sees document links in verification queue
  Rejection reason stored and emailed to teacher
```

---

## 15. WINDSURF / AI CODING ASSISTANT PROMPTING GUIDE

### Starting each session

Always begin with:
```
Read ARCHITECTURE.md in the project root. Do not write any code until you 
have read the entire document. Follow every convention defined in it exactly:
- Use Svelte 5 runes ($state, $derived, $effect) not Svelte 4 stores
- Use async SQLAlchemy 2 patterns, not sync
- Use Pydantic v2 model_config, not class Config
- All file paths must match the folder structure in section 3
- Use the exact route patterns shown in sections 9 and 10
```

### Effective task breakdown (build in this order)

```
Phase 1 — Backend foundation (build first, test with /docs)
  Task 1:  "Set up FastAPI project with folder structure from section 3"
  Task 2:  "Create all SQLAlchemy models from the schema in section 7"
  Task 3:  "Set up Alembic and generate initial migration"
  Task 4:  "Set up FastAPI-Users auth with JWT and the User model"
  Task 5:  "Implement GET /api/v1/tutors search endpoint with filters"
  Task 6:  "Implement the booking creation flow with slot conflict prevention"
  Task 7:  "Integrate Stripe payment intent creation and webhook handler"
  Task 8:  "Set up WebSocket ConnectionManager with Redis pub/sub"
  Task 9:  "Implement Celery tasks for email reminders"
  Task 10: "Implement the AI chat endpoint using LangChain + OpenAI"

Phase 2 — Frontend (build after backend is working)
  Task 1:  "Set up SvelteKit with TypeScript, Tailwind, shadcn-svelte"
  Task 2:  "Create auth store and root layout with role-based redirect"
  Task 3:  "Build the public landing page and find-tutors page"
  Task 4:  "Build the student dashboard and bookings pages"
  Task 5:  "Build the tutor profile page with booking panel"
  Task 6:  "Build the real-time messaging UI using WebSocket store"
  Task 7:  "Build the teacher dashboard, post-class, and schedule pages"
  Task 8:  "Build the admin verifications queue"
```

### Task prompt template (use this exact format)

```
Context: Working on EduLink SL (see ARCHITECTURE.md).
Task: [specific thing to build]
File(s) to create/edit: [exact path from architecture]
Dependencies: [what must exist first]
Do not: [list anti-patterns to avoid]
Reference: [section number in ARCHITECTURE.md]
```
