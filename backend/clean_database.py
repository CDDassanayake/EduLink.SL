import asyncio
from sqlalchemy import text
from app.database import engine

async def clean_database():
    """Clean up database by dropping all tables and types"""
    async with engine.begin() as conn:
        # Drop all tables
        await conn.execute(text("DROP TABLE IF EXISTS bookings CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS blocked_dates CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS availability_slots CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS listing_payments CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS payments CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS reviews CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS merit_events CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS messages CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS conversations CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS notifications CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS teacher_listings CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS teacher_profiles CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS subjects CASCADE"))
        await conn.execute(text("DROP TABLE IF EXISTS users CASCADE"))
        
        # Drop all enum types
        await conn.execute(text("DROP TYPE IF EXISTS bookingtype CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS bookingstatus CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS classmode CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS classtype CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS listingstatus CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS listingplan CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS listingpaymentstatus CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS paymentstatus CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS subjectcategory CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS userrole CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS verificationstatus CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS conversationtype CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS messagetype CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS notificationtype CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS teachingmode CASCADE"))
        await conn.execute(text("DROP TYPE IF EXISTS teachingtype CASCADE"))
        
        print("Database cleaned successfully")

if __name__ == "__main__":
    asyncio.run(clean_database())
