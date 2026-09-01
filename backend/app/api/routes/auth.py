import uuid
from fastapi import APIRouter, Depends
from app.auth import auth_backend, get_user_manager, fastapi_users
from app.auth_schemas import UserRead, UserCreate, UserUpdate
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])

# FastAPI-Users standard routes
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/reset-password",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/verify",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["auth"],
)

# Custom current user endpoint
@router.get("/me")
async def get_current_user(
    user: User = Depends(fastapi_users.current_user()),
):
    """Get current user information"""
    return UserRead.model_validate(user)
