from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from app.api.deps import get_db
from app.models.user import User, UserRole, TeacherProfile, VerificationStatus
from pydantic import BaseModel


class TeacherVerificationResponse(BaseModel):
    id: str
    user_id: str
    full_name: str
    email: str
    city: Optional[str] = None
    bio: Optional[str] = None
    years_experience: Optional[int] = None
    document_urls: Optional[str] = None
    verification_status: str
    verification_note: Optional[str] = None
    created_at: str

router = APIRouter(prefix="/admin", tags=["admin"])


# Teacher verification endpoints

@router.get("/verifications", response_model=list[TeacherVerificationResponse])
async def get_verifications(
    status_filter: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    """
    Get teacher verifications.
    No authentication required for admin access.
    Optional status filter: PENDING, APPROVED, REJECTED
    """
    query = (
        select(TeacherProfile, User)
        .join(User, User.id == TeacherProfile.user_id)
        .where(User.role == UserRole.TEACHER)
    )

    if status_filter:
        try:
            filter_status = VerificationStatus(status_filter)
            query = query.where(TeacherProfile.verification_status == filter_status)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid status filter")

    result = await db.execute(query)
    rows = result.all()

    return [
        TeacherVerificationResponse(
            id=str(profile.id),
            user_id=str(profile.user_id),
            full_name=user.full_name,
            email=user.email,
            city=user.city,
            bio=profile.bio,
            years_experience=profile.years_experience,
            document_urls=profile.document_urls,
            verification_status=profile.verification_status.value,
            verification_note=profile.verification_note,
            created_at=profile.updated_at.isoformat()
        )
        for profile, user in rows
    ]


@router.patch("/verifications/{profile_id}/approve", response_model=TeacherVerificationResponse)
async def approve_verification(
    profile_id: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Approve a teacher verification.
    No authentication required for admin access.
    """

    query = select(TeacherProfile).where(TeacherProfile.id == profile_id)
    result = await db.execute(query)
    profile = result.scalar_one_or_none()

    if not profile:
        raise HTTPException(status_code=404, detail="Teacher profile not found")

    profile.verification_status = VerificationStatus.APPROVED
    profile.verification_note = None
    await db.commit()
    await db.refresh(profile)

    # Get user for response
    user_query = select(User).where(User.id == profile.user_id)
    user_result = await db.execute(user_query)
    user = user_result.scalar_one()

    return TeacherVerificationResponse(
        id=str(profile.id),
        user_id=str(profile.user_id),
        full_name=user.full_name,
        email=user.email,
        city=user.city,
        bio=profile.bio,
        years_experience=profile.years_experience,
        document_urls=profile.document_urls,
        verification_status=profile.verification_status.value,
        verification_note=profile.verification_note,
        created_at=profile.updated_at.isoformat()
    )


@router.patch("/verifications/{profile_id}/reject", response_model=TeacherVerificationResponse)
async def reject_verification(
    profile_id: str,
    reason: Optional[str] = Query(None, description="Rejection reason"),
    db: AsyncSession = Depends(get_db)
):
    """
    Reject a teacher verification.
    No authentication required for admin access.
    """

    query = select(TeacherProfile).where(TeacherProfile.id == profile_id)
    result = await db.execute(query)
    profile = result.scalar_one_or_none()

    if not profile:
        raise HTTPException(status_code=404, detail="Teacher profile not found")

    profile.verification_status = VerificationStatus.REJECTED
    profile.verification_note = reason
    await db.commit()
    await db.refresh(profile)

    # Get user for response
    user_query = select(User).where(User.id == profile.user_id)
    user_result = await db.execute(user_query)
    user = user_result.scalar_one()

    return TeacherVerificationResponse(
        id=str(profile.id),
        user_id=str(profile.user_id),
        full_name=user.full_name,
        email=user.email,
        city=user.city,
        bio=profile.bio,
        years_experience=profile.years_experience,
        document_urls=profile.document_urls,
        verification_status=profile.verification_status.value,
        verification_note=profile.verification_note,
        created_at=profile.updated_at.isoformat()
    )
