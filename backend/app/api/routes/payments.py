from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from decimal import Decimal
import stripe
from datetime import datetime, timedelta

from app.api.deps import get_db, get_current_user
from app.models.user import User, UserRole
from app.models.listing import TeacherListing, ListingStatus
from app.models.payment import ListingPayment, ListingPlan, ListingPaymentStatus
from app.schemas.payment import ListingPaymentRequest, ListingPaymentResponse
from app.config import settings

router = APIRouter(prefix="/payments", tags=["payments"])

# Initialize Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Listing plan pricing (in LKR)
LISTING_PLANS = {
    ListingPlan.BASIC: {"amount": Decimal("500.00"), "days": 30},
    ListingPlan.STANDARD: {"amount": Decimal("1200.00"), "days": 90},
    ListingPlan.PREMIUM: {"amount": Decimal("2000.00"), "days": 180},
}


@router.post("/listing-checkout", response_model=ListingPaymentResponse)
async def create_listing_payment_checkout(
    payment_data: ListingPaymentRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Create a Stripe checkout session for listing payment.
    Requires authentication and TEACHER role.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can pay for listings")
    
    # Get the listing
    query = select(TeacherListing).where(TeacherListing.id == payment_data.listing_id)
    result = await db.execute(query)
    listing = result.scalar_one_or_none()
    
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    
    if listing.teacher_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only pay for your own listings")
    
    # Check if listing already has a paid payment
    existing_payment = await db.execute(
        select(ListingPayment).where(
            ListingPayment.listing_id == payment_data.listing_id,
            ListingPayment.status == ListingPaymentStatus.PAID
        )
    )
    existing = existing_payment.scalar_one_or_none()
    if existing:
        print(f"DEBUG: Found existing paid payment: {existing.id} for listing {payment_data.listing_id}")
        # Temporarily disable for testing
        # raise HTTPException(status_code=400, detail="Listing already paid for")
    
    # Get plan details
    plan_details = LISTING_PLANS.get(payment_data.plan)
    if not plan_details:
        raise HTTPException(status_code=400, detail="Invalid plan")
    
    amount = plan_details["amount"]
    days_active = plan_details["days"]
    
    # Convert to cents for Stripe (LKR uses cents)
    amount_cents = int(amount * 100)
    
    try:
        # Create Stripe PaymentIntent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount_cents,
            currency="lkr",
            metadata={
                "listing_id": str(payment_data.listing_id),
                "teacher_id": str(current_user.id),
                "plan": payment_data.plan.value,
                "days_active": str(days_active),
                "payment_type": "listing"
            }
        )
        
        # Create ListingPayment record
        listing_payment = ListingPayment(
            listing_id=payment_data.listing_id,
            teacher_id=current_user.id,
            plan=payment_data.plan,
            amount=amount,
            days_active=days_active,
            stripe_payment_intent=payment_intent.id,
            status=ListingPaymentStatus.PENDING
        )
        
        db.add(listing_payment)
        await db.commit()
        
        return ListingPaymentResponse(
            client_secret=payment_intent.client_secret,
            payment_intent_id=payment_intent.id,
            amount=amount
        )
    except stripe.error.StripeError as e:
        print(f"Stripe error: {type(e).__name__}: {str(e)}")
        print(f"Stripe key used: {settings.STRIPE_SECRET_KEY[:10]}...")
        raise HTTPException(status_code=400, detail=f"Stripe error: {str(e)}")


@router.post("/webhook")
async def stripe_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    """
    Handle Stripe webhooks for payment events.
    """
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    # Handle payment_intent.succeeded event
    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        metadata = payment_intent["metadata"]
        
        payment_type = metadata.get("payment_type")
        
        if payment_type == "listing":
            await handle_listing_payment_success(payment_intent, metadata, db)
        elif payment_type == "booking":
            await handle_booking_payment_success(payment_intent, metadata, db)
    
    return {"status": "success"}


async def handle_listing_payment_success(payment_intent: dict, metadata: dict, db: AsyncSession):
    """Handle successful listing payment"""
    listing_id = metadata.get("listing_id")
    payment_intent_id = payment_intent["id"]
    
    # Get the payment record
    query = select(ListingPayment).where(
        ListingPayment.stripe_payment_intent == payment_intent_id
    )
    result = await db.execute(query)
    listing_payment = result.scalar_one_or_none()
    
    if not listing_payment:
        return
    
    # Update payment status
    listing_payment.status = ListingPaymentStatus.PAID
    
    # Get the listing and activate it
    query = select(TeacherListing).where(TeacherListing.id == listing_id)
    result = await db.execute(query)
    listing = result.scalar_one_or_none()
    
    if listing:
        listing.status = ListingStatus.ACTIVE
        listing.expires_at = datetime.utcnow() + timedelta(days=listing_payment.days_active)
    
    await db.commit()


async def handle_booking_payment_success(payment_intent: dict, metadata: dict, db: AsyncSession):
    """Handle successful booking payment (to be implemented)"""
    # TODO: Implement booking payment success handling
    pass


@router.get("/history")
async def get_payment_history(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get current user's payment history.
    """
    if current_user.role == UserRole.TEACHER:
        query = select(ListingPayment).where(
            ListingPayment.teacher_id == current_user.id
        ).order_by(ListingPayment.created_at.desc())
    else:
        query = select(ListingPayment).where(
            ListingPayment.teacher_id == current_user.id
        ).order_by(ListingPayment.created_at.desc())
    
    result = await db.execute(query)
    payments = result.scalars().all()
    
    return [
        {
            "id": str(payment.id),
            "listing_id": str(payment.listing_id),
            "plan": payment.plan.value,
            "amount": float(payment.amount),
            "status": payment.status.value,
            "created_at": payment.created_at.isoformat()
        }
        for payment in payments
    ]
