"""users table

Revision ID: c01c618ae62c
Revises: 
Create Date: 2022-05-21 18:21:49.299984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c01c618ae62c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_IPAddress', sa.String(length=64), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_date'), 'user', ['date'], unique=False)
    op.create_index(op.f('ix_user_user_IPAddress'), 'user', ['user_IPAddress'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_user_IPAddress'), table_name='user')
    op.drop_index(op.f('ix_user_date'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###