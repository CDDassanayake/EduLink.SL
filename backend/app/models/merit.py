import uuid
from datetime import datetime
from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class MeritEvent(Base):
    """Merit score change events"""
    __tablename__ = "merit_events"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    booking_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    delta: Mapped[int] = mapped_column(Integer, nullable=False)  # positive or negative
    reason: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<MeritEvent(id={self.id}, user_id={self.user_id}, delta={self.delta})>"
