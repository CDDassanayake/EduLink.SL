import enum
import uuid
from datetime import datetime
from sqlalchemy import String, Text, DateTime, Enum as SQLEnum, ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class ConversationType(str, enum.Enum):
    STUDENT_TEACHER = "STUDENT_TEACHER"
    TEACHER_TEACHER = "TEACHER_TEACHER"
    STUDENT_STUDENT = "STUDENT_STUDENT"


class Conversation(Base):
    """Conversations between users"""
    __tablename__ = "conversations"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, default=uuid.uuid4
    )
    type: Mapped[ConversationType] = mapped_column(
        SQLEnum(ConversationType), nullable=False
    )
    participant_ids: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Conversation(id={self.id}, type={self.type})>"


class Message(Base):
    """Messages within conversations"""
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, default=uuid.uuid4
    )
    conversation_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    sender_id: Mapped[str] = mapped_column(String(36), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    read_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, index=True)

    def __repr__(self) -> str:
        return f"<Message(id={self.id}, conversation_id={self.conversation_id})>"
