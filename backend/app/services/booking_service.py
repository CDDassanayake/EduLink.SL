from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime
from typing import Optional
from app.schemas.booking import BookingCreate, BookingResponse
from app.models.booking import Booking, BookingStatus, BookingType
from app.models.listing import TeacherListing
from app.models.user import User
from app.models.payment import Payment
from app.config import settings
import stripe


class BookingService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_booking(
        self,
        student_id: str,
        booking_data: BookingCreate
    ) -> tuple[Booking, str]:
        """
        Create a new booking with Stripe payment intent.
        Returns (booking, stripe_client_secret)
        """
        # Verify listing exists and is active
        listing_query = select(TeacherListing).where(
            TeacherListing.id == booking_data.listing_id
        )
        listing_result = await self.db.execute(listing_query)
        listing = listing_result.scalar_one_or_none()

        if not listing:
            raise ValueError("Listing not found")

        if listing.teacher_id != booking_data.tutor_id:
            raise ValueError("Listing does not belong to tutor")

        # Calculate price
        if booking_data.booking_type == BookingType.SINGLE:
            gross_amount = listing.hourly_rate
        elif booking_data.booking_type == BookingType.MONTHLY:
            # 4 sessions per month with 10% discount
            gross_amount = listing.hourly_rate * 4 * 0.9
        else:
            gross_amount = listing.hourly_rate

        platform_fee = gross_amount * 0.10
        teacher_payout = gross_amount - platform_fee

        # Create Stripe PaymentIntent
        try:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            payment_intent = stripe.PaymentIntent.create(
                amount=int(gross_amount * 100),  # Convert to cents
                currency='lkr',
                metadata={
                    'booking_type': booking_data.booking_type.value,
                    'listing_id': booking_data.listing_id,
                    'student_id': student_id,
                    'teacher_id': booking_data.tutor_id
                }
            )
        except Exception as e:
            raise ValueError(f"Failed to create payment intent: {str(e)}")

        # Create booking with PENDING status
        booking = Booking(
            student_id=student_id,
            teacher_id=booking_data.tutor_id,
            listing_id=booking_data.listing_id,
            session_start=booking_data.session_start,
            session_end=booking_data.session_end,
            booking_type=booking_data.booking_type,
            package_weeks=booking_data.package_weeks,
            status=BookingStatus.PENDING,
            can_review=False
        )

        self.db.add(booking)
        await self.db.commit()
        await self.db.refresh(booking)

        return booking, payment_intent.client_secret

    async def confirm_booking(self, payment_intent_id: str) -> Booking:
        """
        Confirm booking after successful payment.
        Called by Stripe webhook.
        """
        # Find booking by payment intent (need to add payment_intent_id to booking model or use payment table)
        # For now, we'll use the payment table
        payment_query = select(Payment).where(
            Payment.stripe_payment_intent == payment_intent_id
        )
        payment_result = await self.db.execute(payment_query)
        payment = payment_result.scalar_one_or_none()

        if not payment:
            raise ValueError("Payment not found")

        # Update booking status
        booking_query = select(Booking).where(Booking.id == payment.booking_id)
        booking_result = await self.db.execute(booking_query)
        booking = booking_result.scalar_one_or_none()

        if not booking:
            raise ValueError("Booking not found")

        booking.status = BookingStatus.CONFIRMED
        await self.db.commit()
        await self.db.refresh(booking)

        return booking

    async def cancel_booking(
        self,
        booking_id: str,
        student_id: str,
        reason: Optional[str] = None
    ) -> Booking:
        """
        Cancel a booking with refund calculation.
        """
        booking_query = select(Booking).where(Booking.id == booking_id)
        booking_result = await self.db.execute(booking_query)
        booking = booking_result.scalar_one_or_none()

        if not booking:
            raise ValueError("Booking not found")

        if booking.student_id != student_id:
            raise ValueError("You can only cancel your own bookings")

        if booking.status != BookingStatus.CONFIRMED:
            raise ValueError("Only confirmed bookings can be cancelled")

        # Calculate refund based on cancellation rules
        hours_until_session = (booking.session_start - datetime.utcnow()).total_seconds() / 3600

        if hours_until_session >= 24:
            refund_amount = 1.0  # 100% refund
        else:
            refund_amount = 0.6  # 60% refund

        # Process refund via Stripe (TODO: implement)
        # For now, just update status
        booking.status = BookingStatus.CANCELLED
        booking.cancelled_by = student_id
        booking.cancel_reason = reason
        booking.cancelled_at = datetime.utcnow()

        await self.db.commit()
        await self.db.refresh(booking)

        return booking

    async def mark_attended(self, booking_id: str, teacher_id: str) -> Booking:
        """
        Mark a booking as attended by the teacher.
        """
        booking_query = select(Booking).where(Booking.id == booking_id)
        booking_result = await self.db.execute(booking_query)
        booking = booking_result.scalar_one_or_none()

        if not booking:
            raise ValueError("Booking not found")

        if booking.teacher_id != teacher_id:
            raise ValueError("You can only mark your own bookings as attended")

        if booking.status != BookingStatus.CONFIRMED:
            raise ValueError("Only confirmed bookings can be marked as attended")

        booking.status = BookingStatus.ATTENDED
        booking.can_review = True

        await self.db.commit()
        await self.db.refresh(booking)

        return booking
