"""Create Edge Server ID for access log register

Revision ID: e21a1e9baa9f
Revises: 1ea2205a4e05
Create Date: 2024-06-11 16:32:27.101022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e21a1e9baa9f'
down_revision: Union[str, None] = '1ea2205a4e05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('AccessLog', sa.Column('edge_server_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_AccessLog_edge_server_id'), 'AccessLog', ['edge_server_id'], unique=False)
    op.create_foreign_key(None, 'AccessLog', 'edge_server', ['edge_server_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'AccessLog', type_='foreignkey')
    op.drop_index(op.f('ix_AccessLog_edge_server_id'), table_name='AccessLog')
    op.drop_column('AccessLog', 'edge_server_id')
    # ### end Alembic commands ###
