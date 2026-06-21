from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import time
from decimal import Decimal
from app.models.listing import TeachingMode, ClassType, ListingStatus, SubjectCategory


class SubjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    name: str
    category: SubjectCategory


class TutorListingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    teacher_id: str
    subject_id: str
    mode: TeachingMode
    class_type: ClassType
    hourly_rate: Decimal
    description: Optional[str] = None
    trial_available: bool = False
    trial_rate: Optional[Decimal] = None
    max_group_size: Optional[int] = None
    status: ListingStatus


class TutorSearchResponse(BaseModel):
    id: str
    full_name: str
    profile_photo_url: Optional[str] = None
    merit_score: int
    average_rating: Optional[float] = None
    review_count: int = 0
    listings: List[TutorListingResponse]


class TutorProfileResponse(TutorSearchResponse):
    bio: Optional[str] = None
    years_experience: Optional[int] = None
    verification_status: str
    city: Optional[str] = None


class AvailabilitySlotCreate(BaseModel):
    day_of_week: int
    start_time: time
    end_time: time
    is_recurring: bool = True


class AvailabilitySlotResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    teacher_id: str
    day_of_week: int
    start_time: time
    end_time: time
    is_recurring: bool


class BlockedDateCreate(BaseModel):
    blocked_date: str  # YYYY-MM-DD
    reason: Optional[str] = None


class BlockedDateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    teacher_id: str
    blocked_date: str
    reason: Optional[str] = None
