"""empty message

Revision ID: f13bd1ebe783
Revises: c51be6ffb9ce
Create Date: 2021-11-02 02:12:48.508327

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f13bd1ebe783'
down_revision = 'c51be6ffb9ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('codenum_UNIQUE')
        batch_op.drop_index('uq_user_email')
        batch_op.create_unique_constraint(batch_op.f('uq_user_codenum'), ['codenum'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_nickname'), ['nickname'])

    with op.batch_alter_table('videocard', schema=None) as batch_op:
        batch_op.alter_column('vcname',
               existing_type=mysql.TEXT(),
               nullable=False)
        batch_op.alter_column('score',
               existing_type=mysql.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('videocard', schema=None) as batch_op:
        batch_op.alter_column('score',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('vcname',
               existing_type=mysql.TEXT(),
               nullable=True)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_nickname'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_codenum'), type_='unique')
        batch_op.create_index('uq_user_email', ['nickname'], unique=False)
        batch_op.create_index('codenum_UNIQUE', ['codenum'], unique=False)

    # ### end Alembic commands ###