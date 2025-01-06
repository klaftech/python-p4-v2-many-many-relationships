"""renamed related table

Revision ID: 42669d7e7c66
Revises: 31e004e41fde
Create Date: 2025-01-06 18:28:59.745875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42669d7e7c66'
down_revision = '31e004e41fde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('employees_meetings','employee_meetings')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('employee_meetings','employees_meetings')
    # ### end Alembic commands ###
