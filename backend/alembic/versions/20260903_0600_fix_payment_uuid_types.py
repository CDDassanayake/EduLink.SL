"""fix payment uuid types

Revision ID: 20260903_0600
Revises: 20260902_0500
Create Date: 2026-09-03 06:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '20260903_0600'
down_revision = '20260902_0500'
branch_labels = None
depends_on = None


def upgrade():
    # Convert payments columns from VARCHAR to UUID
    op.execute('ALTER TABLE payments ALTER COLUMN id TYPE UUID USING id::uuid')
    op.execute('ALTER TABLE payments ALTER COLUMN booking_id TYPE UUID USING booking_id::uuid')
    op.execute('ALTER TABLE payments ALTER COLUMN student_id TYPE UUID USING student_id::uuid')
    op.execute('ALTER TABLE payments ALTER COLUMN teacher_id TYPE UUID USING teacher_id::uuid')
    
    # Convert listing_payments columns from VARCHAR to UUID
    op.execute('ALTER TABLE listing_payments ALTER COLUMN id TYPE UUID USING id::uuid')
    op.execute('ALTER TABLE listing_payments ALTER COLUMN listing_id TYPE UUID USING listing_id::uuid')
    op.execute('ALTER TABLE listing_payments ALTER COLUMN teacher_id TYPE UUID USING teacher_id::uuid')


def downgrade():
    # Convert back from UUID to VARCHAR
    op.execute('ALTER TABLE payments ALTER COLUMN id TYPE VARCHAR(36) USING id::text')
    op.execute('ALTER TABLE payments ALTER COLUMN booking_id TYPE VARCHAR(36) USING booking_id::text')
    op.execute('ALTER TABLE payments ALTER COLUMN student_id TYPE VARCHAR(36) USING student_id::text')
    op.execute('ALTER TABLE payments ALTER COLUMN teacher_id TYPE VARCHAR(36) USING teacher_id::text')
    
    op.execute('ALTER TABLE listing_payments ALTER COLUMN id TYPE VARCHAR(36) USING id::text')
    op.execute('ALTER TABLE listing_payments ALTER COLUMN listing_id TYPE VARCHAR(36) USING listing_id::text')
    op.execute('ALTER TABLE listing_payments ALTER COLUMN teacher_id TYPE VARCHAR(36) USING teacher_id::text')
