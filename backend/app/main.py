from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

# Create FastAPI app
app = FastAPI(
    title="EduLink SL API",
    description="Tutor booking marketplace for Sri Lankan students",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers (will be uncommented as routes are implemented)
from app.api.routes import auth, tutors, bookings, payments, reviews, messages, ai_chat, admin

app.include_router(auth.router, prefix="/api/v1")
app.include_router(tutors.router, prefix="/api/v1/tutors", tags=["tutors"])
app.include_router(bookings.router, prefix="/api/v1/bookings", tags=["bookings"])
app.include_router(payments.router, prefix="/api/v1/payments", tags=["payments"])
app.include_router(reviews.router, prefix="/api/v1/reviews", tags=["reviews"])
app.include_router(messages.router, prefix="/api/v1/messages", tags=["messages"])
app.include_router(ai_chat.router, prefix="/api/v1/ai", tags=["ai"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["admin"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "EduLink SL API", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
