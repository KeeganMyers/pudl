"""EIA861 short form changes

Revision ID: 7992e5e19487
Revises: 827e88186933
Create Date: 2024-06-14 22:35:55.353939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7992e5e19487'
down_revision = '827e88186933'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('core_eia861__yearly_short_form', schema=None) as batch_op:
        batch_op.drop_constraint('fk_core_eia861__yearly_short_form_utility_id_eia_core_eia__entity_utilities', type_='foreignkey')
        batch_op.drop_constraint('fk_core_eia861__yearly_short_form_balancing_authority_code_eia_core_eia__codes_balancing_authorities', type_='foreignkey')
        batch_op.drop_column('num_water_heaters')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('core_eia861__yearly_short_form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('num_water_heaters', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_core_eia861__yearly_short_form_balancing_authority_code_eia_core_eia__codes_balancing_authorities', 'core_eia__codes_balancing_authorities', ['balancing_authority_code_eia'], ['code'])
        batch_op.create_foreign_key('fk_core_eia861__yearly_short_form_utility_id_eia_core_eia__entity_utilities', 'core_eia__entity_utilities', ['utility_id_eia'], ['utility_id_eia'])

    # ### end Alembic commands ###