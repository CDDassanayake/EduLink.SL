"""
FastAPI-Users schemas for EduLink SL
"""
import uuid
from datetime import datetime
from typing import Optional
from fastapi_users import schemas
from app.models.user import User, UserRole


class UserRead(schemas.BaseUser[uuid.UUID]):
    """Schema for reading user data"""
    id: uuid.UUID
    email: str
    full_name: str
    role: UserRole
    city: Optional[str] = None
    phone: Optional[str] = None
    profile_photo_url: Optional[str] = None
    merit_score: int
    is_active: bool
    is_verified: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime


class UserCreate(schemas.BaseUserCreate):
    """Schema for user registration"""
    email: str
    password: str
    full_name: str
    role: UserRole = UserRole.STUDENT
    city: Optional[str] = None
    phone: Optional[str] = None


class UserUpdate(schemas.BaseUserUpdate):
    """Schema for updating user data"""
    full_name: Optional[str] = None
    city: Optional[str] = None
    phone: Optional[str] = None
    profile_photo_url: Optional[str] = None
