"""variation schema change

Revision ID: a8476769cae0
Revises: a8f2ff38b5ea
Create Date: 2021-01-06 08:33:45.918052

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a8476769cae0'
down_revision = 'a8f2ff38b5ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('workbook', sa.Column('variations', postgresql.ARRAY(postgresql.JSONB(astext_type=sa.Text())), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('workbook', 'variations')
    # ### end Alembic commands ###