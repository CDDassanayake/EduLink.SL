"""
FastAPI-Users authentication configuration
"""
import uuid
from typing import AsyncGenerator
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin, schemas, FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.database import get_db
from app.config import settings


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """Custom user manager for EduLink SL"""
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY
    
    async def on_after_register(self, user: User, request: Request | None = None):
        """Send verification email after registration"""
        print(f"User {user.id} has registered. Verification email should be sent.")
        # TODO: Implement email sending via Celery
    
    async def on_after_forgot_password(self, user: User, token: str, request: Request | None = None):
        """Send password reset email"""
        print(f"User {user.id} has forgot password. Reset token: {token}")
        # TODO: Implement password reset email
    
    async def on_after_request_verify(
        self, user: User, token: str, request: Request | None = None
    ):
        """Send verification email"""
        print(f"Verification requested for user {user.id}. Token: {token}")
        # TODO: Implement verification email


async def get_user_db(session: AsyncSession = Depends(get_db)) -> AsyncGenerator[SQLAlchemyUserDatabase, None]:
    """Get user database adapter"""
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)) -> AsyncGenerator[UserManager, None]:
    """Get user manager instance"""
    yield UserManager(user_db)


def get_jwt_strategy() -> JWTStrategy:
    """Get JWT authentication strategy"""
    from app.config import settings
    return JWTStrategy(secret=settings.SECRET_KEY, lifetime_seconds=1800)  # 30 minutes


bearer_transport = BearerTransport(tokenUrl="api/v1/auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

# Create FastAPIUsers instance
fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
