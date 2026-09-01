"""fix uuid column types

Revision ID: 20260902_0500
Revises: 000fd8fa88ef
Create Date: 2026-09-02 05:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '20260902_0500'
down_revision = '000fd8fa88ef'
branch_labels = None
depends_on = None


def upgrade():
    # Convert teacher_listings columns from VARCHAR to UUID
    op.execute('ALTER TABLE teacher_listings ALTER COLUMN id TYPE UUID USING id::uuid')
    op.execute('ALTER TABLE teacher_listings ALTER COLUMN teacher_id TYPE UUID USING teacher_id::uuid')
    op.execute('ALTER TABLE teacher_listings ALTER COLUMN subject_id TYPE UUID USING subject_id::uuid')
    
    # Convert subjects columns from VARCHAR to UUID
    op.execute('ALTER TABLE subjects ALTER COLUMN id TYPE UUID USING id::uuid')
    
    # Convert availability_slots columns from VARCHAR to UUID
    op.execute('ALTER TABLE availability_slots ALTER COLUMN id TYPE UUID USING id::uuid')
    op.execute('ALTER TABLE availability_slots ALTER COLUMN teacher_id TYPE UUID USING teacher_id::uuid')
    
    # Convert blocked_dates columns from VARCHAR to UUID
    op.execute('ALTER TABLE blocked_dates ALTER COLUMN id TYPE UUID USING id::uuid')
    op.execute('ALTER TABLE blocked_dates ALTER COLUMN teacher_id TYPE UUID USING teacher_id::uuid')
    
    # Convert bookings columns from VARCHAR to UUID
    op.execute('ALTER TABLE bookings ALTER COLUMN id TYPE UUID USING id::uuid')
    op.execute('ALTER TABLE bookings ALTER COLUMN student_id TYPE UUID USING student_id::uuid')
    op.execute('ALTER TABLE bookings ALTER COLUMN teacher_id TYPE UUID USING teacher_id::uuid')
    op.execute('ALTER TABLE bookings ALTER COLUMN listing_id TYPE UUID USING listing_id::uuid')
    op.execute('ALTER TABLE bookings ALTER COLUMN cancelled_by TYPE UUID USING cancelled_by::uuid')


def downgrade():
    # Convert back from UUID to VARCHAR
    op.execute('ALTER TABLE teacher_listings ALTER COLUMN id TYPE VARCHAR(36) USING id::text')
    op.execute('ALTER TABLE teacher_listings ALTER COLUMN teacher_id TYPE VARCHAR(36) USING teacher_id::text')
    op.execute('ALTER TABLE teacher_listings ALTER COLUMN subject_id TYPE VARCHAR(36) USING subject_id::text')
    
    op.execute('ALTER TABLE subjects ALTER COLUMN id TYPE VARCHAR(36) USING id::text')
    
    op.execute('ALTER TABLE availability_slots ALTER COLUMN id TYPE VARCHAR(36) USING id::text')
    op.execute('ALTER TABLE availability_slots ALTER COLUMN teacher_id TYPE VARCHAR(36) USING teacher_id::text')
    
    op.execute('ALTER TABLE blocked_dates ALTER COLUMN id TYPE VARCHAR(36) USING id::text')
    op.execute('ALTER TABLE blocked_dates ALTER COLUMN teacher_id TYPE VARCHAR(36) USING teacher_id::text')
    
    op.execute('ALTER TABLE bookings ALTER COLUMN id TYPE VARCHAR(36) USING id::text')
    op.execute('ALTER TABLE bookings ALTER COLUMN student_id TYPE VARCHAR(36) USING student_id::text')
    op.execute('ALTER TABLE bookings ALTER COLUMN teacher_id TYPE VARCHAR(36) USING teacher_id::text')
    op.execute('ALTER TABLE bookings ALTER COLUMN listing_id TYPE VARCHAR(36) USING listing_id::text')
    op.execute('ALTER TABLE bookings ALTER COLUMN cancelled_by TYPE VARCHAR(36) USING cancelled_by::text')
