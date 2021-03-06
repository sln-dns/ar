"""empty message

Revision ID: 6d9a6235cadb
Revises: 3384c537b956
Create Date: 2021-07-10 01:09:32.424429

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d9a6235cadb'
down_revision = '3384c537b956'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('board', schema=None) as batch_op:
        batch_op.alter_column('adress',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('memorys',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('board', schema=None) as batch_op:
        batch_op.alter_column('memorys',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('adress',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
