import asyncio
from sqlalchemy import select
from app.database import AsyncSessionLocal
from app.models.user import User

async def check_users():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User))
        users = result.all()
        print(f'Users in database: {len(users)}')
        for user in users:
            print(f'  - {user.email} (role: {user.role})')

if __name__ == "__main__":
    asyncio.run(check_users())
