from pydantic import BaseModel, ConfigDict
from typing import Optional


class ReviewCreate(BaseModel):
    booking_id: str
    rating: int  # 1 to 5
    comment: Optional[str] = None


class ReviewResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    booking_id: str
    student_id: str
    teacher_id: str
    rating: int
    comment: Optional[str] = None
    is_visible: bool = True
    created_at: str
