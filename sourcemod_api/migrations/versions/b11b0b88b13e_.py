"""empty message

Revision ID: b11b0b88b13e
Revises: a2a2320d065a
Create Date: 2023-10-25 22:22:07.242129

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b11b0b88b13e'
down_revision: Union[str, None] = 'a2a2320d065a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins_groups', sa.Column('group_id', sa.Integer(), nullable=True))
    op.add_column('admins_groups', sa.Column('admin_id', sa.Integer(), nullable=True))
    op.drop_constraint('fk_admins_groups_sm_groups_group_id', 'admins_groups', type_='foreignkey')
    op.drop_constraint('fk_admins_groups_sm_admins_admin_id', 'admins_groups', type_='foreignkey')
    op.create_foreign_key('fk_admins_groups_sm_groups_group_id_id', 'admins_groups', 'sm_groups', ['group_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key('fk_admins_groups_sm_admins_admin_id_id', 'admins_groups', 'sm_admins', ['admin_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_column('admins_groups', 'group')
    op.drop_column('admins_groups', 'admin')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admins_groups', sa.Column('admin', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('admins_groups', sa.Column('group', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint('fk_admins_groups_sm_admins_admin_id_id', 'admins_groups', type_='foreignkey')
    op.drop_constraint('fk_admins_groups_sm_groups_group_id_id', 'admins_groups', type_='foreignkey')
    op.create_foreign_key('fk_admins_groups_sm_admins_admin_id', 'admins_groups', 'sm_admins', ['admin'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.create_foreign_key('fk_admins_groups_sm_groups_group_id', 'admins_groups', 'sm_groups', ['group'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_column('admins_groups', 'admin_id')
    op.drop_column('admins_groups', 'group_id')
    # ### end Alembic commands ###
