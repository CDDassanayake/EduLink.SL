from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from app.models.user import UserRole


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: EmailStr
    full_name: str
    city: Optional[str] = None
    phone: Optional[str] = None


class UserRegister(UserBase):
    password: str
    role: UserRole


class UserLogin(BaseModel):
    username: str  # email
    password: str


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: str
    role: UserRole
    is_verified: bool
    profile_photo_url: Optional[str] = None
    merit_score: int = 100


class TeacherProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    user_id: str
    bio: Optional[str] = None
    years_experience: Optional[int] = None
    verification_status: str
    stripe_connect_account_id: Optional[str] = None
    listing_active: bool = False


class UserWithProfile(UserResponse):
    teacher_profile: Optional[TeacherProfileResponse] = None


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenRefresh(BaseModel):
    refresh_token: str
