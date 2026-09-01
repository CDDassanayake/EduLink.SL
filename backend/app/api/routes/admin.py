from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from app.api.deps import get_db, get_current_user
from app.models.user import User, UserRole
from app.models.listing import TeacherListing, ListingStatus
from app.schemas.tutor import TutorListingResponse

router = APIRouter(prefix="/admin", tags=["admin"])


# Listing approval endpoints

@router.get("/listings/pending", response_model=list[TutorListingResponse])
async def get_pending_listings(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get all pending listings awaiting approval.
    Requires authentication and ADMIN role.
    """
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Only admins can view pending listings")
    
    query = select(TeacherListing).where(TeacherListing.status == ListingStatus.INACTIVE)
    result = await db.execute(query)
    listings = result.scalars().all()
    
    return [TutorListingResponse.model_validate(l) for l in listings]


@router.patch("/listings/{listing_id}/approve", response_model=TutorListingResponse)
async def approve_listing(
    listing_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Approve a teacher listing.
    Requires authentication and ADMIN role.
    Changes status from INACTIVE to ACTIVE.
    """
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Only admins can approve listings")
    
    query = select(TeacherListing).where(TeacherListing.id == listing_id)
    result = await db.execute(query)
    listing = result.scalar_one_or_none()
    
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    
    if listing.status == ListingStatus.ACTIVE:
        raise HTTPException(status_code=400, detail="Listing is already active")
    
    listing.status = ListingStatus.ACTIVE
    await db.commit()
    await db.refresh(listing)
    
    return TutorListingResponse.model_validate(listing)


@router.patch("/listings/{listing_id}/reject", status_code=status.HTTP_204_NO_CONTENT)
async def reject_listing(
    listing_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Reject a teacher listing.
    Requires authentication and ADMIN role.
    Changes status from INACTIVE to EXPIRED.
    """
    if current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Only admins can reject listings")
    
    query = select(TeacherListing).where(TeacherListing.id == listing_id)
    result = await db.execute(query)
    listing = result.scalar_one_or_none()
    
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    
    listing.status = ListingStatus.EXPIRED
    await db.commit()


# TODO: Implement other admin routes
# GET /analytics
# GET /verifications
# PATCH /verifications/{id}/approve
# PATCH /verifications/{id}/reject
# POST /verifications/{id}/request-docs
# GET /users
# PATCH /users/{id}/suspend
# GET /disputes
# PATCH /disputes/{id}/resolve
# GET /reviews
# DELETE /reviews/{id}
