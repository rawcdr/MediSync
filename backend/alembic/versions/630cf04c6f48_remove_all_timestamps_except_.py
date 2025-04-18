"""Remove all timestamps except appointment_time at 2025-04-02 13:44:46 by InvictusRex

Revision ID: 630cf04c6f48
Revises: c90c279c986d
Create Date: 2025-04-02 19:16:00.400602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '630cf04c6f48'
down_revision: Union[str, None] = 'c90c279c986d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('appointments', 'created_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('created_at', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###
