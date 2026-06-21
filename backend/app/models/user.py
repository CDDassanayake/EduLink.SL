import enum
import uuid
from datetime import datetime
from sqlalchemy import String, Boolean, Integer, Enum as SQLEnum, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class UserRole(str, enum.Enum):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    ADMIN = "ADMIN"


class VerificationStatus(str, enum.Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class User(Base):
    """User model - managed by FastAPI-Users"""
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole), nullable=False, default=UserRole.STUDENT
    )
    city: Mapped[str | None] = mapped_column(String(100), nullable=True)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    profile_photo_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    merit_score: Mapped[int] = mapped_column(Integer, default=100)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email}, role={self.role})>"


class TeacherProfile(Base):
    """Teacher profile - 1:1 with users where role=TEACHER"""
    __tablename__ = "teacher_profiles"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[str] = mapped_column(
        String(36), unique=True, nullable=False, index=True
    )
    bio: Mapped[str | None] = mapped_column(Text, nullable=True)
    years_experience: Mapped[int | None] = mapped_column(Integer, nullable=True)
    document_urls: Mapped[str | None] = mapped_column(Text, nullable=True)  # JSONB as string
    verification_status: Mapped[VerificationStatus] = mapped_column(
        SQLEnum(VerificationStatus), default=VerificationStatus.PENDING
    )
    verification_note: Mapped[str | None] = mapped_column(Text, nullable=True)
    stripe_connect_account_id: Mapped[str | None] = mapped_column(String(100), nullable=True)
    listing_active: Mapped[bool] = mapped_column(Boolean, default=False)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<TeacherProfile(id={self.id}, user_id={self.user_id}, status={self.verification_status})>"
