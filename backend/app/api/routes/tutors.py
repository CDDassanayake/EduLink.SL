from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from typing import Optional
from datetime import datetime, timedelta
from app.api.deps import get_db, get_current_user
from app.models.user import User, UserRole
from app.models.listing import TeacherListing, Subject, TeachingMode, ListingStatus, ClassType
from app.models.booking import AvailabilitySlot, BlockedDate
from app.schemas.tutor import (
    TutorSearchResponse,
    TutorProfileResponse,
    TutorListingResponse,
    AvailabilitySlotResponse,
    SubjectResponse,
    AvailabilitySlotCreate,
    BlockedDateCreate,
    BlockedDateResponse
)

router = APIRouter(prefix="/tutors", tags=["tutors"])


@router.get("/", response_model=list[TutorSearchResponse])
async def search_tutors(
    subject_id: Optional[str] = Query(None, description="Filter by subject ID"),
    city: Optional[str] = Query(None, description="Filter by city"),
    stream: Optional[str] = Query(None, description="Filter by stream (OL, AL_SCIENCE, etc.)"),
    mode: Optional[TeachingMode] = Query(None, description="Filter by teaching mode"),
    min_rating: Optional[float] = Query(None, ge=0, le=5, description="Minimum rating"),
    max_price: Optional[float] = Query(None, ge=0, description="Maximum hourly rate"),
    available_today: Optional[bool] = Query(False, description="Only show tutors available today"),
    db: AsyncSession = Depends(get_db)
):
    """
    Search tutors with filters.
    Returns paginated list of TeacherListing records with teacher details.
    """
    try:
        # Build base query for active listings with teacher and subject info
        query = (
            select(TeacherListing, User)
            .join(User, User.id == TeacherListing.teacher_id)
            .where(TeacherListing.status == ListingStatus.ACTIVE)
            .where(User.role == UserRole.TEACHER)
        )
        
        # Apply filters
        if subject_id:
            query = query.where(TeacherListing.subject_id == subject_id)
        
        if city:
            query = query.where(User.city.ilike(f"%{city}%"))
        
        if stream:
            # Join with Subject to filter by category
            query = query.join(Subject, Subject.id == TeacherListing.subject_id)
            query = query.where(Subject.category == stream)
        
        if mode:
            query = query.where(TeacherListing.mode == mode)
        
        if max_price:
            query = query.where(TeacherListing.hourly_rate <= max_price)
        
        # Execute query
        result = await db.execute(query)
        rows = result.all()
        
        # Group by teacher and build response
        tutors_dict = {}
        for listing, user in rows:
            teacher_id = str(user.id)
            
            # Skip if doesn't meet rating requirement
            if min_rating and user.merit_score and user.merit_score < min_rating * 20:  # Convert rating to merit score
                continue
            
            if teacher_id not in tutors_dict:
                tutors_dict[teacher_id] = {
                    "id": teacher_id,
                    "full_name": user.full_name,
                    "profile_photo_url": user.profile_photo_url,
                    "merit_score": user.merit_score or 0,
                    "average_rating": (user.merit_score / 20.0) if user.merit_score else 0.0,  # Convert merit to rating
                    "review_count": 0,  # TODO: Calculate from reviews table
                    "listings": []
                }
            
            tutors_dict[teacher_id]["listings"].append(
                TutorListingResponse.model_validate(listing)
            )
        
        # Filter by availability today if requested
        if available_today:
            today = datetime.now().date()
            available_tutors = {}
            
            for teacher_id, tutor_data in tutors_dict.items():
                # Check if teacher has availability for today
                day_of_week = today.weekday()
                availability_query = (
                    select(AvailabilitySlot)
                    .where(AvailabilitySlot.teacher_id == teacher_id)
                    .where(AvailabilitySlot.day_of_week == day_of_week)
                )
                
                # Check if today is not blocked
                blocked_query = (
                    select(BlockedDate)
                    .where(BlockedDate.teacher_id == teacher_id)
                    .where(BlockedDate.blocked_date == today)
                )
                
                availability_result = await db.execute(availability_query)
                blocked_result = await db.execute(blocked_query)
                
                has_availability = availability_result.first() is not None
                is_blocked = blocked_result.first() is not None
                
                if has_availability and not is_blocked:
                    available_tutors[teacher_id] = tutor_data
            
            tutors_dict = available_tutors
        
        return list(tutors_dict.values())
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{tutor_id}/profile", response_model=TutorProfileResponse)
async def get_tutor_profile(
    tutor_id: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Get full tutor profile (auth required).
    Returns detailed tutor information with all active listings.
    """
    # Get teacher with profile
    query = (
        select(User)
        .where(User.id == tutor_id)
        .where(User.role == UserRole.TEACHER)
    )
    
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=404, detail="Tutor not found")
    
    # Get teacher's active listings
    listings_query = (
        select(TeacherListing)
        .where(TeacherListing.teacher_id == tutor_id)
        .where(TeacherListing.status == ListingStatus.ACTIVE)
    )
    
    listings_result = await db.execute(listings_query)
    listings = listings_result.scalars().all()
    
    # Get teacher profile (if exists)
    from app.models.user import TeacherProfile
    profile_query = select(TeacherProfile).where(TeacherProfile.user_id == tutor_id)
    profile_result = await db.execute(profile_query)
    profile = profile_result.scalar_one_or_none()
    
    # Build response
    response_data = {
        "id": str(user.id),
        "full_name": user.full_name,
        "profile_photo_url": user.profile_photo_url,
        "merit_score": user.merit_score,
        "average_rating": user.merit_score / 20.0 if user.merit_score else 0.0,
        "review_count": 0,  # TODO: Calculate from reviews table
        "listings": [TutorListingResponse.model_validate(l) for l in listings],
        "bio": profile.bio if profile else None,
        "years_experience": profile.years_experience if profile else None,
        "verification_status": profile.verification_status if profile else "PENDING",
        "city": user.city
    }
    
    return TutorProfileResponse(**response_data)


@router.get("/{tutor_id}/availability", response_model=list[AvailabilitySlotResponse])
async def get_tutor_availability(
    tutor_id: str,
    week: Optional[str] = Query(None, description="Monday of week in YYYY-MM-DD format"),
    db: AsyncSession = Depends(get_db)
):
    """
    Get weekly availability slots.
    Query: week=YYYY-MM-DD (Monday of week)
    Returns availability slots, booked slots, and teacher details.
    """
    # Get all recurring availability slots for the teacher
    query = select(AvailabilitySlot).where(AvailabilitySlot.teacher_id == tutor_id)
    result = await db.execute(query)
    slots = result.scalars().all()
    
    # Get blocked dates for the week if week is specified
    blocked_dates = []
    if week:
        try:
            week_start = datetime.strptime(week, "%Y-%m-%d").date()
            week_end = week_start + timedelta(days=6)
            
            blocked_query = (
                select(BlockedDate)
                .where(BlockedDate.teacher_id == tutor_id)
                .where(BlockedDate.blocked_date >= week_start)
                .where(BlockedDate.blocked_date <= week_end)
            )
            blocked_result = await db.execute(blocked_query)
            blocked_dates = blocked_result.scalars().all()
        except ValueError:
            pass  # Invalid date format, ignore week filter
    
    return [AvailabilitySlotResponse.model_validate(slot) for slot in slots]


@router.get("/{tutor_id}/reviews")
async def get_tutor_reviews(
    tutor_id: str,
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=50),
    db: AsyncSession = Depends(get_db)
):
    """
    Get paginated reviews for a tutor.
    """
    # TODO: Implement reviews retrieval from reviews table
    # For now, return empty list
    return {
        "reviews": [],
        "total": 0,
        "page": page,
        "per_page": per_page,
        "average_rating": 0.0
    }


# Teacher listing management endpoints (require authentication)

@router.post("/listings", response_model=TutorListingResponse, status_code=status.HTTP_201_CREATED)
async def create_listing(
    subject_id: str,
    mode: TeachingMode,
    class_type: ClassType,
    hourly_rate: float,
    description: Optional[str] = None,
    trial_available: bool = False,
    trial_rate: Optional[float] = None,
    max_group_size: Optional[int] = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Create a new teacher listing.
    Requires authentication and TEACHER role.
    Listing starts as INACTIVE and requires admin approval.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can create listings")
    
    # Verify subject exists
    subject_query = select(Subject).where(Subject.id == subject_id)
    subject_result = await db.execute(subject_query)
    subject = subject_result.scalar_one_or_none()
    
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    
    # Create listing
    listing = TeacherListing(
        teacher_id=current_user.id,
        subject_id=subject.id,
        mode=mode,
        class_type=class_type,
        hourly_rate=hourly_rate,
        description=description,
        trial_available=trial_available,
        trial_rate=trial_rate,
        max_group_size=max_group_size,
        status=ListingStatus.INACTIVE  # Requires admin approval
    )
    
    db.add(listing)
    await db.commit()
    await db.refresh(listing)
    
    return TutorListingResponse.model_validate(listing)


@router.get("/my-listings", response_model=list[TutorListingResponse])
async def get_my_listings(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get current user's listings.
    Requires authentication and TEACHER role.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can view their listings")
    
    query = select(TeacherListing).where(TeacherListing.teacher_id == current_user.id)
    result = await db.execute(query)
    listings = result.scalars().all()
    
    return [TutorListingResponse.model_validate(l) for l in listings]


@router.put("/listings/{listing_id}", response_model=TutorListingResponse)
async def update_listing(
    listing_id: str,
    mode: Optional[TeachingMode] = None,
    class_type: Optional[ClassType] = None,
    hourly_rate: Optional[float] = None,
    description: Optional[str] = None,
    trial_available: Optional[bool] = None,
    trial_rate: Optional[float] = None,
    max_group_size: Optional[int] = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Update a teacher listing.
    Requires authentication and TEACHER role.
    Only the listing owner can update.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can update listings")
    
    query = select(TeacherListing).where(TeacherListing.id == listing_id)
    result = await db.execute(query)
    listing = result.scalar_one_or_none()
    
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    
    if listing.teacher_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only update your own listings")
    
    # Update fields if provided
    if mode is not None:
        listing.mode = mode
    if class_type is not None:
        listing.class_type = class_type
    if hourly_rate is not None:
        listing.hourly_rate = hourly_rate
    if description is not None:
        listing.description = description
    if trial_available is not None:
        listing.trial_available = trial_available
    if trial_rate is not None:
        listing.trial_rate = trial_rate
    if max_group_size is not None:
        listing.max_group_size = max_group_size
    
    await db.commit()
    await db.refresh(listing)
    
    return TutorListingResponse.model_validate(listing)


@router.delete("/listings/{listing_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_listing(
    listing_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a teacher listing.
    Requires authentication and TEACHER role.
    Only the listing owner can delete.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can delete listings")
    
    query = select(TeacherListing).where(TeacherListing.id == listing_id)
    result = await db.execute(query)
    listing = result.scalar_one_or_none()
    
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    
    if listing.teacher_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only delete your own listings")
    
    await db.delete(listing)
    await db.commit()


# Availability management endpoints

@router.post("/availability", response_model=AvailabilitySlotResponse, status_code=status.HTTP_201_CREATED)
async def create_availability_slot(
    slot_data: AvailabilitySlotCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Create an availability slot.
    Requires authentication and TEACHER role.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can create availability slots")
    
    slot = AvailabilitySlot(
        teacher_id=current_user.id,
        day_of_week=slot_data.day_of_week,
        start_time=slot_data.start_time,
        end_time=slot_data.end_time,
        is_recurring=slot_data.is_recurring
    )
    
    db.add(slot)
    await db.commit()
    await db.refresh(slot)
    
    return AvailabilitySlotResponse.model_validate(slot)


@router.get("/my-availability", response_model=list[AvailabilitySlotResponse])
async def get_my_availability(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get current user's availability slots.
    Requires authentication and TEACHER role.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can view their availability")
    
    query = select(AvailabilitySlot).where(AvailabilitySlot.teacher_id == current_user.id)
    result = await db.execute(query)
    slots = result.scalars().all()
    
    return [AvailabilitySlotResponse.model_validate(s) for s in slots]


@router.delete("/availability/{slot_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_availability_slot(
    slot_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Delete an availability slot.
    Requires authentication and TEACHER role.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can delete availability slots")
    
    query = select(AvailabilitySlot).where(AvailabilitySlot.id == slot_id)
    result = await db.execute(query)
    slot = result.scalar_one_or_none()
    
    if not slot:
        raise HTTPException(status_code=404, detail="Availability slot not found")
    
    if slot.teacher_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only delete your own availability slots")
    
    await db.delete(slot)
    await db.commit()


@router.post("/blocked-dates", status_code=status.HTTP_201_CREATED)
async def create_blocked_date(
    blocked_data: BlockedDateCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Create a blocked date.
    Requires authentication and TEACHER role.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can create blocked dates")
    
    from datetime import date
    
    blocked_date = BlockedDate(
        teacher_id=current_user.id,
        blocked_date=date.fromisoformat(blocked_data.blocked_date),
        reason=blocked_data.reason
    )
    
    db.add(blocked_date)
    await db.commit()
    
    return {"message": "Blocked date created successfully"}


@router.get("/my-blocked-dates", response_model=list[BlockedDateResponse])
async def get_my_blocked_dates(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get current user's blocked dates.
    Requires authentication and TEACHER role.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can view their blocked dates")
    
    query = select(BlockedDate).where(BlockedDate.teacher_id == current_user.id)
    result = await db.execute(query)
    blocked_dates = result.scalars().all()
    
    return [BlockedDateResponse.model_validate(bd) for bd in blocked_dates]


@router.delete("/blocked-dates/{blocked_date_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blocked_date(
    blocked_date_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Delete a blocked date.
    Requires authentication and TEACHER role.
    """
    if current_user.role != UserRole.TEACHER:
        raise HTTPException(status_code=403, detail="Only teachers can delete blocked dates")
    
    query = select(BlockedDate).where(BlockedDate.id == blocked_date_id)
    result = await db.execute(query)
    blocked_date = result.scalar_one_or_none()
    
    if not blocked_date:
        raise HTTPException(status_code=404, detail="Blocked date not found")
    
    if blocked_date.teacher_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only delete your own blocked dates")
    
    await db.delete(blocked_date)
    await db.commit()


@router.get("/subjects", response_model=list[SubjectResponse])
async def get_subjects(db: AsyncSession = Depends(get_db)):
    """
    Get all available subjects.
    """
    query = select(Subject).order_by(Subject.display_order, Subject.name)
    result = await db.execute(query)
    subjects = result.scalars().all()
    
    return [SubjectResponse.model_validate(s) for s in subjects]
