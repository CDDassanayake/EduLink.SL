from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from app.api.deps import get_db, get_current_user
from app.models.user import User, UserRole
from app.models.booking import Booking, BookingStatus
from app.schemas.booking import BookingCreate, BookingResponse, BookingCancel
from app.services.booking_service import BookingService

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(
    booking_data: BookingCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new booking with Stripe payment.
    Requires authentication and STUDENT role.
    """
    if current_user.role != UserRole.STUDENT:
        raise HTTPException(status_code=403, detail="Only students can create bookings")

    booking_service = BookingService(db)
    booking, client_secret = await booking_service.create_booking(
        str(current_user.id),
        booking_data
    )

    # Return booking with client_secret for frontend
    return BookingResponse(
        id=str(booking.id),
        student_id=str(booking.student_id),
        teacher_id=str(booking.teacher_id),
        listing_id=str(booking.listing_id),
        session_start=booking.session_start,
        session_end=booking.session_end,
        booking_type=booking.booking_type,
        package_weeks=booking.package_weeks,
        status=booking.status,
        cancelled_by=str(booking.cancelled_by) if booking.cancelled_by else None,
        cancel_reason=booking.cancel_reason,
        cancelled_at=booking.cancelled_at,
        can_review=booking.can_review,
        created_at=booking.created_at
    )


@router.get("/", response_model=list[BookingResponse])
async def get_bookings(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get bookings for the current user.
    Students see their bookings, teachers see bookings they received.
    """
    if current_user.role == UserRole.STUDENT:
        query = select(Booking).where(Booking.student_id == current_user.id)
    elif current_user.role == UserRole.TEACHER:
        query = select(Booking).where(Booking.teacher_id == current_user.id)
    else:
        raise HTTPException(status_code=403, detail="Invalid role")

    result = await db.execute(query)
    bookings = result.scalars().all()

    return [
        BookingResponse(
            id=str(b.id),
            student_id=str(b.student_id),
            teacher_id=str(b.teacher_id),
            listing_id=str(b.listing_id),
            session_start=b.session_start,
            session_end=b.session_end,
            booking_type=b.booking_type,
            package_weeks=b.package_weeks,
            status=b.status,
            cancelled_by=str(b.cancelled_by) if b.cancelled_by else None,
            cancel_reason=b.cancel_reason,
            cancelled_at=b.cancelled_at,
            can_review=b.can_review,
            created_at=b.created_at
        )
        for b in bookings
    ]


@router.get("/{booking_id}", response_model=BookingResponse)
async def get_booking(
    booking_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get a specific booking.
    User can only view their own bookings (as student or teacher).
    """
    query = select(Booking).where(Booking.id == booking_id)
    result = await db.execute(query)
    booking = result.scalar_one_or_none()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    if (current_user.role == UserRole.STUDENT and booking.student_id != current_user.id) or \
       (current_user.role == UserRole.TEACHER and booking.teacher_id != current_user.id):
        raise HTTPException(status_code=403, detail="You can only view your own bookings")

    return BookingResponse(
        id=str(booking.id),
        student_id=str(booking.student_id),
        teacher_id=str(booking.teacher_id),
        listing_id=str(booking.listing_id),
        session_start=booking.session_start,
        session_end=booking.session_end,
        booking_type=booking.booking_type,
        package_weeks=booking.package_weeks,
        status=booking.status,
        cancelled_by=str(booking.cancelled_by) if booking.cancelled_by else None,
        cancel_reason=booking.cancel_reason,
        cancelled_at=booking.cancelled_at,
        can_review=booking.can_review,
        created_at=booking.created_at
    )


@router.patch("/{booking_id}/cancel", response_model=BookingResponse)
async def cancel_booking(
    booking_id: str,
    cancel_data: BookingCancel,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Cancel a booking.
    Only students can cancel their own bookings.
    """
    if current_user.role != UserRole.STUDENT:
        raise HTTPException(status_code=403, detail="Only students can cancel bookings")

    booking_service = BookingService(db)
    booking = await booking_service.cancel_booking(
        booking_id,
        str(current_user.id),
        cancel_data.reason
    )

    return BookingResponse(
        id=str(booking.id),
        student_id=str(booking.student_id),
        teacher_id=str(booking.teacher_id),
        listing_id=str(booking.listing_id),
        session_start=booking.session_start,
        session_end=booking.session_end,
        booking_type=booking.booking_type,
        package_weeks=booking.package_weeks,
        status=booking.status,
        cancelled_by=str(booking.cancelled_by) if booking.cancelled_by else None,
        cancel_reason=booking.cancel_reason,
        cancelled_at=booking.cancelled_at,
        can_review=booking.can_review,
        created_at=booking.created_at
    )


@router.patch("/{booking_id}/attend", response_model=BookingResponse)
async def mark_attended(
    booking_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Mark a booking as attended.
    Only teachers can mark their own bookings as attended.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can mark bookings as attended")

    booking_service = BookingService(db)
    booking = await booking_service.mark_attended(booking_id, str(current_user.id))

    return BookingResponse(
        id=str(booking.id),
        student_id=str(booking.student_id),
        teacher_id=str(booking.teacher_id),
        listing_id=str(booking.listing_id),
        session_start=booking.session_start,
        session_end=booking.session_end,
        booking_type=booking.booking_type,
        package_weeks=booking.package_weeks,
        status=booking.status,
        cancelled_by=str(booking.cancelled_by) if booking.cancelled_by else None,
        cancel_reason=booking.cancel_reason,
        cancelled_at=booking.cancelled_at,
        can_review=booking.can_review,
        created_at=booking.created_at
    )
