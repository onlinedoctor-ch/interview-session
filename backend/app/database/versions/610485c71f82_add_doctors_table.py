"""Add doctors table

Revision ID: 610485c71f82
Revises: 
Create Date: 2022-02-03 19:59:39.810285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '610485c71f82'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('doctors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('specialization', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('doctors')
