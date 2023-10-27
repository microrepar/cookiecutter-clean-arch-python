"""teste create table

Revision ID: 42b7e7a10b45
Revises: 
Create Date: 2023-10-27 16:03:08.026620

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42b7e7a10b45'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sentence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('foreign_language', sa.String(), nullable=True),
    sa.Column('mother_tongue', sa.String(), nullable=True),
    sa.Column('foreign_idiom', sa.String(), nullable=True),
    sa.Column('mother_idiom', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sentence')
    # ### end Alembic commands ###
