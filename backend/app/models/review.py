import uuid
from datetime import datetime
from sqlalchemy import String, Integer, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class Review(Base):
    """Student reviews for teachers"""
    __tablename__ = "reviews"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, default=uuid.uuid4
    )
    booking_id: Mapped[str] = mapped_column(String(36), unique=True, nullable=False)
    student_id: Mapped[str] = mapped_column(String(36), nullable=False)
    teacher_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 to 5
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_visible: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Review(id={self.id}, teacher_id={self.teacher_id}, rating={self.rating})>"
