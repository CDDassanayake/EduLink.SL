from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from decimal import Decimal
from app.models.booking import BookingType, BookingStatus


class BookingCreate(BaseModel):
    tutor_id: str
    listing_id: str
    session_start: datetime
    session_end: datetime
    booking_type: BookingType
    package_weeks: Optional[int] = None


class BookingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    student_id: str
    teacher_id: str
    listing_id: str
    session_start: datetime
    session_end: datetime
    booking_type: BookingType
    package_weeks: Optional[int] = None
    status: BookingStatus
    cancelled_by: Optional[str] = None
    cancel_reason: Optional[str] = None
    cancelled_at: Optional[datetime] = None
    can_review: bool = False
    created_at: datetime


class BookingCancel(BaseModel):
    reason: Optional[str] = None
