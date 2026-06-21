from sqlalchemy.ext.asyncio import AsyncSession


class MeritService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def apply_merit_delta(self, user_id: str, delta: int, reason: str, booking_id: str = None) -> None:
        """
        Apply a merit score change to a user.
        This will update the user's merit_score and create a MeritEvent record.
        """
        # TODO: Implement merit delta application
        pass
