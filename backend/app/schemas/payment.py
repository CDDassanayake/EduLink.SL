from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from decimal import Decimal
from app.models.payment import PaymentStatus, ListingPlan, ListingPaymentStatus


class PaymentCheckoutRequest(BaseModel):
    tutor_id: str
    listing_id: str
    session_start: datetime
    session_end: datetime
    booking_type: str  # 'SINGLE' or 'MONTHLY'
    package_weeks: Optional[int] = None


class PaymentCheckoutResponse(BaseModel):
    client_secret: str
    payment_intent_id: str
    amount: Decimal


class ListingPaymentRequest(BaseModel):
    listing_id: str
    plan: ListingPlan


class ListingPaymentResponse(BaseModel):
    client_secret: str
    payment_intent_id: str
    amount: Decimal


class PaymentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    booking_id: str
    student_id: str
    teacher_id: str
    gross_amount: Decimal
    platform_fee: Decimal
    teacher_payout_amount: Decimal
    currency: str
    status: PaymentStatus
    refund_amount: Optional[Decimal] = None
    created_at: datetime


class WebhookEvent(BaseModel):
    data: dict
