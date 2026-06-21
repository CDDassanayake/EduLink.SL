from sqlalchemy.ext.asyncio import AsyncSession


class NotificationService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_notification(self, user_id: str, notification_type: str, title: str, body: str, link: str = None) -> None:
        """
        Create a notification for a user.
        """
        # TODO: Implement notification creation
        pass

    async def send_notification_email(self, user_id: str, notification_type: str, data: dict) -> None:
        """
        Send an email notification via Celery task.
        """
        # TODO: Implement email notification via Celery
        pass
