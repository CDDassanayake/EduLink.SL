from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.api.deps import get_db, get_current_user
from app.models.user import User
from app.models.review import Review
from app.models.booking import Booking
from app.schemas.review import ReviewCreate, ReviewResponse

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post("/", response_model=ReviewResponse, status_code=status.HTTP_201_CREATED)
async def create_review(
    review_data: ReviewCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Submit a review for a teacher.
    Only students can submit reviews, and only for attended bookings.
    """
    # Verify user is a student
    if current_user.role != "STUDENT":
        raise HTTPException(status_code=403, detail="Only students can submit reviews")

    # Verify booking exists and belongs to the student
    booking_query = select(Booking).where(
        Booking.id == review_data.booking_id,
        Booking.student_id == current_user.id
    )
    booking_result = await db.execute(booking_query)
    booking = booking_result.scalar_one_or_none()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    # Verify booking is attended (can only review attended sessions)
    if booking.status != "ATTENDED":
        raise HTTPException(
            status_code=400,
            detail="Can only review attended sessions"
        )

    # Check if review already exists for this booking
    existing_review_query = select(Review).where(
        Review.booking_id == review_data.booking_id
    )
    existing_review_result = await db.execute(existing_review_query)
    existing_review = existing_review_result.scalar_one_or_none()

    if existing_review:
        raise HTTPException(
            status_code=400,
            detail="Review already submitted for this booking"
        )

    # Validate rating
    if not 1 <= review_data.rating <= 5:
        raise HTTPException(
            status_code=400,
            detail="Rating must be between 1 and 5"
        )

    # Create review
    review = Review(
        booking_id=review_data.booking_id,
        student_id=current_user.id,
        teacher_id=booking.teacher_id,
        rating=review_data.rating,
        comment=review_data.comment,
        is_visible=True
    )

    db.add(review)
    await db.commit()
    await db.refresh(review)

    return ReviewResponse(
        id=str(review.id),
        booking_id=review.booking_id,
        student_id=review.student_id,
        teacher_id=review.teacher_id,
        rating=review.rating,
        comment=review.comment,
        is_visible=review.is_visible,
        created_at=review.created_at.isoformat()
    )


@router.get("/teacher/{teacher_id}", response_model=list[ReviewResponse])
async def get_teacher_reviews(
    teacher_id: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Get all visible reviews for a specific teacher.
    Public endpoint (no authentication required).
    """
    reviews_query = select(Review).where(
        Review.teacher_id == teacher_id,
        Review.is_visible == True
    ).order_by(Review.created_at.desc())

    result = await db.execute(reviews_query)
    reviews = result.scalars().all()

    return [
        ReviewResponse(
            id=str(review.id),
            booking_id=review.booking_id,
            student_id=review.student_id,
            teacher_id=review.teacher_id,
            rating=review.rating,
            comment=review.comment,
            is_visible=review.is_visible,
            created_at=review.created_at.isoformat()
        )
        for review in reviews
    ]


@router.get("/teacher/{teacher_id}/average")
async def get_teacher_average_rating(
    teacher_id: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Get average rating for a teacher.
    Public endpoint (no authentication required).
    """
    avg_query = select(func.avg(Review.rating)).where(
        Review.teacher_id == teacher_id,
        Review.is_visible == True
    )

    count_query = select(func.count(Review.id)).where(
        Review.teacher_id == teacher_id,
        Review.is_visible == True
    )

    avg_result = await db.execute(avg_query)
    count_result = await db.execute(count_query)

    avg_rating = avg_result.scalar()
    review_count = count_result.scalar()

    return {
        "average_rating": round(avg_rating, 2) if avg_rating else None,
        "review_count": review_count
    }
