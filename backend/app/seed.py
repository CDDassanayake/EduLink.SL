"""
Seed script to populate the subjects table.
Run this after running migrations: python -m app.seed
"""
import asyncio
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import AsyncSessionLocal, engine
from app.models.listing import Subject, SubjectCategory


async def seed_subjects():
    """Seed the subjects table with Sri Lankan curriculum subjects"""
    subjects_data = [
        # O/L Subjects
        {"name": "O/L Mathematics", "category": SubjectCategory.OL, "display_order": 1},
        {"name": "O/L Science", "category": SubjectCategory.OL, "display_order": 2},
        {"name": "O/L English", "category": SubjectCategory.OL, "display_order": 3},
        {"name": "O/L Sinhala", "category": SubjectCategory.OL, "display_order": 4},
        {"name": "O/L Tamil", "category": SubjectCategory.OL, "display_order": 5},
        {"name": "O/L History", "category": SubjectCategory.OL, "display_order": 6},
        {"name": "O/L Geography", "category": SubjectCategory.OL, "display_order": 7},
        {"name": "O/L Commerce", "category": SubjectCategory.OL, "display_order": 8},
        {"name": "O/L ICT", "category": SubjectCategory.OL, "display_order": 9},

        # A/L Science Stream
        {"name": "A/L Physics", "category": SubjectCategory.AL_SCIENCE, "display_order": 10},
        {"name": "A/L Chemistry", "category": SubjectCategory.AL_SCIENCE, "display_order": 11},
        {"name": "Combined Mathematics", "category": SubjectCategory.AL_SCIENCE, "display_order": 12},
        {"name": "A/L Biology", "category": SubjectCategory.AL_SCIENCE, "display_order": 13},
        {"name": "A/L Applied Mathematics", "category": SubjectCategory.AL_SCIENCE, "display_order": 14},

        # A/L Arts Stream
        {"name": "A/L Economics", "category": SubjectCategory.AL_ARTS, "display_order": 15},
        {"name": "A/L Geography", "category": SubjectCategory.AL_ARTS, "display_order": 16},
        {"name": "A/L History", "category": SubjectCategory.AL_ARTS, "display_order": 17},
        {"name": "A/L Political Science", "category": SubjectCategory.AL_ARTS, "display_order": 18},
        {"name": "A/L Logic", "category": SubjectCategory.AL_ARTS, "display_order": 19},

        # A/L Commerce Stream
        {"name": "A/L Accounting", "category": SubjectCategory.AL_COMMERCE, "display_order": 20},
        {"name": "A/L Business Studies", "category": SubjectCategory.AL_COMMERCE, "display_order": 21},
        {"name": "A/L Economics", "category": SubjectCategory.AL_COMMERCE, "display_order": 22},

        # A/L Technology Stream
        {"name": "A/L Engineering Technology", "category": SubjectCategory.AL_TECHNOLOGY, "display_order": 23},
        {"name": "A/L Bio Systems Technology", "category": SubjectCategory.AL_TECHNOLOGY, "display_order": 24},
        {"name": "A/L Science for Technology", "category": SubjectCategory.AL_TECHNOLOGY, "display_order": 25},

        # University Subjects
        {"name": "Engineering Mathematics", "category": SubjectCategory.UNIVERSITY, "display_order": 26},
        {"name": "Computer Science", "category": SubjectCategory.UNIVERSITY, "display_order": 27},
        {"name": "Data Structures & Algorithms", "category": SubjectCategory.UNIVERSITY, "display_order": 28},
        {"name": "Calculus", "category": SubjectCategory.UNIVERSITY, "display_order": 29},
        {"name": "Statistics", "category": SubjectCategory.UNIVERSITY, "display_order": 30},

        # Languages
        {"name": "English Language", "category": SubjectCategory.LANGUAGE, "display_order": 31},
        {"name": "Sinhala Language", "category": SubjectCategory.LANGUAGE, "display_order": 32},
        {"name": "Tamil Language", "category": SubjectCategory.LANGUAGE, "display_order": 33},
        {"name": "French", "category": SubjectCategory.LANGUAGE, "display_order": 34},
        {"name": "German", "category": SubjectCategory.LANGUAGE, "display_order": 35},

        # Other
        {"name": "General Knowledge", "category": SubjectCategory.OTHER, "display_order": 36},
        {"name": "Interview Preparation", "category": SubjectCategory.OTHER, "display_order": 37},
    ]

    async with AsyncSessionLocal() as session:
        # Check if subjects already exist
        result = await session.execute("SELECT COUNT(*) FROM subjects")
        count = result.scalar()
        
        if count > 0:
            print(f"Subjects table already has {count} records. Skipping seed.")
            return

        # Add subjects
        for subject_data in subjects_data:
            subject = Subject(
                id=str(uuid.uuid4()),
                **subject_data
            )
            session.add(subject)

        await session.commit()
        print(f"Seeded {len(subjects_data)} subjects successfully.")


async def main():
    """Main entry point for seed script"""
    print("Starting database seed...")
    await seed_subjects()
    print("Seed completed.")


if __name__ == "__main__":
    asyncio.run(main())
