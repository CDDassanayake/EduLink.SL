import enum
import uuid
from datetime import datetime
from decimal import Decimal
from sqlalchemy import String, Numeric, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class PaymentStatus(str, enum.Enum):
    PENDING = "PENDING"
    CAPTURED = "CAPTURED"
    REFUNDED = "REFUNDED"
    PARTIALLY_REFUNDED = "PARTIALLY_REFUNDED"
    FAILED = "FAILED"


class ListingPlan(str, enum.Enum):
    BASIC = "BASIC"
    STANDARD = "STANDARD"
    PREMIUM = "PREMIUM"


class ListingPaymentStatus(str, enum.Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    FAILED = "FAILED"


class Payment(Base):
    """Student session payments"""
    __tablename__ = "payments"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, default=uuid.uuid4
    )
    booking_id: Mapped[str] = mapped_column(String(36), nullable=False)
    student_id: Mapped[str] = mapped_column(String(36), nullable=False)
    teacher_id: Mapped[str] = mapped_column(String(36), nullable=False)
    gross_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    platform_fee: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    teacher_payout_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(3), default="LKR")
    stripe_payment_intent: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    stripe_transfer_id: Mapped[str | None] = mapped_column(String(100), nullable=True)
    status: Mapped[PaymentStatus] = mapped_column(
        SQLEnum(PaymentStatus), default=PaymentStatus.PENDING
    )
    refund_amount: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Payment(id={self.id}, booking_id={self.booking_id}, status={self.status})>"


class ListingPayment(Base):
    """Teacher listing payments"""
    __tablename__ = "listing_payments"

    id: Mapped[uuid.UUID] = mapped_column(
        String(36), primary_key=True, default=uuid.uuid4
    )
    listing_id: Mapped[str] = mapped_column(String(36), nullable=False)
    teacher_id: Mapped[str] = mapped_column(String(36), nullable=False)
    plan: Mapped[ListingPlan] = mapped_column(SQLEnum(ListingPlan), nullable=False)
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    days_active: Mapped[int] = mapped_column(nullable=False)
    stripe_payment_intent: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    status: Mapped[ListingPaymentStatus] = mapped_column(
        SQLEnum(ListingPaymentStatus), default=ListingPaymentStatus.PENDING
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<ListingPayment(id={self.id}, listing_id={self.listing_id}, plan={self.plan})>"
