"""GameUser table

Revision ID: 888999783498
Revises: c01c618ae62c
Create Date: 2022-05-22 13:49:09.554330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '888999783498'
down_revision = 'c01c618ae62c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('user_IPAddress', sa.String(length=64), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_game_user_date'), 'game_user', ['date'], unique=False)
    op.create_index(op.f('ix_game_user_user_IPAddress'), 'game_user', ['user_IPAddress'], unique=False)
    op.create_index(op.f('ix_game_user_username'), 'game_user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_game_user_username'), table_name='game_user')
    op.drop_index(op.f('ix_game_user_user_IPAddress'), table_name='game_user')
    op.drop_index(op.f('ix_game_user_date'), table_name='game_user')
    op.drop_table('game_user')
    # ### end Alembic commands ###
