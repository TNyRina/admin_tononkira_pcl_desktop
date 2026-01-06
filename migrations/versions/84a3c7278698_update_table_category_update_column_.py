"""update table category : update column name to unique and unullable 

Revision ID: 84a3c7278698
Revises: 28e9ec7cc951
Create Date: 2025-12-23 07:32:36.097396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84a3c7278698'
down_revision: Union[str, Sequence[str], None] = '28e9ec7cc951'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("categories") as batch_op:
        batch_op.alter_column(
            "name",
            existing_type=sa.String(),
            nullable=False
        )
        batch_op.create_unique_constraint(
            "uq_categories_name",
            ["name"]
        )



def downgrade() -> None:
    with op.batch_alter_table("categories") as batch_op:
        batch_op.drop_constraint(
            "uq_categories_name",
            type_="unique"
        )
        batch_op.alter_column(
            "name",
            existing_type=sa.String(),
            nullable=True
        )
