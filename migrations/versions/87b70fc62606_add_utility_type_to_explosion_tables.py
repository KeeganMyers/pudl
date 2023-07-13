"""Add utility type to explosion tables

Revision ID: 87b70fc62606
Revises: 88d9201ae4c4
Create Date: 2023-06-14 12:02:38.977231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87b70fc62606'
down_revision = '9a32db1fbe6e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('denorm_depreciation_amortization_summary_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utility_type', sa.Text(), nullable=True, comment='Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.'))

    with op.batch_alter_table('denorm_electric_operating_expenses_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utility_type', sa.Text(), nullable=True, comment='Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.'))

    with op.batch_alter_table('denorm_electric_operating_revenues_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utility_type', sa.Text(), nullable=True, comment='Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.'))

    with op.batch_alter_table('denorm_plant_in_service_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utility_type', sa.Text(), nullable=True, comment='Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.'))

    with op.batch_alter_table('depreciation_amortization_summary_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utility_type', sa.Text(), nullable=True, comment='Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.'))

    with op.batch_alter_table('electric_operating_expenses_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utility_type', sa.Text(), nullable=True, comment='Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.'))

    with op.batch_alter_table('electric_operating_revenues_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utility_type', sa.Text(), nullable=True, comment='Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.'))

    with op.batch_alter_table('plant_in_service_ferc1', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utility_type', sa.Text(), nullable=True, comment='Listing of utility plant types. Examples include Electric Utility, Gas Utility, and Other Utility.'))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plant_in_service_ferc1', schema=None) as batch_op:
        batch_op.drop_column('utility_type')

    with op.batch_alter_table('electric_operating_revenues_ferc1', schema=None) as batch_op:
        batch_op.drop_column('utility_type')

    with op.batch_alter_table('electric_operating_expenses_ferc1', schema=None) as batch_op:
        batch_op.drop_column('utility_type')

    with op.batch_alter_table('depreciation_amortization_summary_ferc1', schema=None) as batch_op:
        batch_op.drop_column('utility_type')

    with op.batch_alter_table('denorm_plant_in_service_ferc1', schema=None) as batch_op:
        batch_op.drop_column('utility_type')

    with op.batch_alter_table('denorm_electric_operating_revenues_ferc1', schema=None) as batch_op:
        batch_op.drop_column('utility_type')

    with op.batch_alter_table('denorm_electric_operating_expenses_ferc1', schema=None) as batch_op:
        batch_op.drop_column('utility_type')

    with op.batch_alter_table('denorm_depreciation_amortization_summary_ferc1', schema=None) as batch_op:
        batch_op.drop_column('utility_type')

    # ### end Alembic commands ###
