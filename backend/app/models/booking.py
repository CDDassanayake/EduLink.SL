import enum
import uuid
from datetime import datetime, time, date
from sqlalchemy import String, Integer, Boolean, Text, DateTime, Time, Date, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class BookingStatus(str, enum.Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    ATTENDED = "ATTENDED"
    CANCELLED = "CANCELLED"
    DISPUTED = "DISPUTED"


class BookingType(str, enum.Enum):
    SINGLE = "SINGLE"
    MONTHLY = "MONTHLY"


class AvailabilitySlot(Base):
    """Teacher availability slots"""
    __tablename__ = "availability_slots"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, default=uuid.uuid4
    )
    teacher_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    day_of_week: Mapped[int] = mapped_column(Integer, nullable=False)  # 0=Mon, 6=Sun
    start_time: Mapped[time] = mapped_column(Time, nullable=False)
    end_time: Mapped[time] = mapped_column(Time, nullable=False)
    is_recurring: Mapped[bool] = mapped_column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"<AvailabilitySlot(id={self.id}, teacher_id={self.teacher_id}, day={self.day_of_week})>"


class BlockedDate(Base):
    """Teacher blocked dates"""
    __tablename__ = "blocked_dates"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, default=uuid.uuid4
    )
    teacher_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    blocked_date: Mapped[date] = mapped_column(Date, nullable=False)
    reason: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def __repr__(self) -> str:
        return f"<BlockedDate(id={self.id}, teacher_id={self.teacher_id}, date={self.blocked_date})>"


class Booking(Base):
    """Student bookings"""
    __tablename__ = "bookings"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, default=uuid.uuid4
    )
    student_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    teacher_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    listing_id: Mapped[str] = mapped_column(String(36), nullable=False)
    session_start: Mapped[datetime] = mapped_column(DateTime, nullable=False, index=True)
    session_end: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    booking_type: Mapped[BookingType] = mapped_column(
        SQLEnum(BookingType), nullable=False
    )
    package_weeks: Mapped[int | None] = mapped_column(Integer, nullable=True)
    status: Mapped[BookingStatus] = mapped_column(
        SQLEnum(BookingStatus), default=BookingStatus.PENDING
    )
    cancelled_by: Mapped[str | None] = mapped_column(String(36), nullable=True)
    cancel_reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    cancelled_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    can_review: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Booking(id={self.id}, student_id={self.student_id}, status={self.status})>"
