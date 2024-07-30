"""create companies table

Revision ID: c0a1051a9c32
Revises: 6b8e0a49e55d
Create Date: 2024-07-29 20:55:07.521217

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c0a1051a9c32"
down_revision: Union[str, None] = "6b8e0a49e55d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "companies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, index=True),
    )


def downgrade() -> None:
    op.drop_table("companies")
