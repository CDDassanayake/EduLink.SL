from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.user import User, UserRole
from app.api.routes.auth import fastapi_users


async def get_current_user(
    user: User = Depends(fastapi_users.current_user()),
) -> User:
    """
    Get the current authenticated user from JWT token.
    """
    return user


async def get_current_active_user(
    user: User = Depends(get_current_user),
) -> User:
    """
    Get the current active user.
    """
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive"
        )
    return user


async def require_student(user: User = Depends(get_current_active_user)) -> User:
    """
    Require the current user to have STUDENT role.
    """
    if user.role != "STUDENT":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Student access required"
        )
    return user


async def require_teacher(user: User = Depends(get_current_active_user)) -> User:
    """
    Require the current user to have TEACHER role.
    """
    if user.role != "TEACHER":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Teacher access required"
        )
    return user


async def require_admin(user: User = Depends(get_current_active_user)) -> User:
    """Require admin role"""
    if user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return user
