import enum
import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import String, Numeric, Boolean, Text, Integer, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class SubjectCategory(str, enum.Enum):
    OL = "OL"
    AL_SCIENCE = "AL_SCIENCE"
    AL_ARTS = "AL_ARTS"
    AL_COMMERCE = "AL_COMMERCE"
    AL_TECHNOLOGY = "AL_TECHNOLOGY"
    UNIVERSITY = "UNIVERSITY"
    LANGUAGE = "LANGUAGE"
    OTHER = "OTHER"


class TeachingMode(str, enum.Enum):
    ONLINE = "ONLINE"
    IN_PERSON = "IN_PERSON"
    HOME_VISIT = "HOME_VISIT"
    FLEXIBLE = "FLEXIBLE"


class ClassType(str, enum.Enum):
    INDIVIDUAL = "INDIVIDUAL"
    GROUP = "GROUP"


class ListingStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    EXPIRED = "EXPIRED"


class Subject(Base):
    """Subject catalog - seeded data"""
    __tablename__ = "subjects"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    category: Mapped[SubjectCategory] = mapped_column(
        SQLEnum(SubjectCategory), nullable=False
    )
    display_order: Mapped[int] = mapped_column(Integer, default=0)

    def __repr__(self) -> str:
        return f"<Subject(id={self.id}, name={self.name}, category={self.category})>"


class TeacherListing(Base):
    """Teacher listings - one per subject per teacher"""
    __tablename__ = "teacher_listings"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    teacher_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False, index=True
    )
    subject_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), nullable=False)
    mode: Mapped[TeachingMode] = mapped_column(
        SQLEnum(TeachingMode), nullable=False
    )
    class_type: Mapped[ClassType] = mapped_column(SQLEnum(ClassType), nullable=False)
    hourly_rate: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    trial_available: Mapped[bool] = mapped_column(Boolean, default=False)
    trial_rate: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    max_group_size: Mapped[int | None] = mapped_column(Integer, nullable=True)
    status: Mapped[ListingStatus] = mapped_column(
        SQLEnum(ListingStatus), default=ListingStatus.INACTIVE
    )
    expires_at: Mapped[datetime | None] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<TeacherListing(id={self.id}, teacher_id={self.teacher_id}, status={self.status})>"
