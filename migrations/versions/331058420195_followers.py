"""followers

Revision ID: 331058420195
Revises: 9caaec6ce3e1
Create Date: 2019-06-22 14:22:27.229933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '331058420195'
down_revision = '9caaec6ce3e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
