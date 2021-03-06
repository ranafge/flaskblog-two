"""added language to posts

Revision ID: 8132960f2e99
Revises: 7e00dcc2fc72
Create Date: 2018-10-22 20:06:25.676839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8132960f2e99'
down_revision = '7e00dcc2fc72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
