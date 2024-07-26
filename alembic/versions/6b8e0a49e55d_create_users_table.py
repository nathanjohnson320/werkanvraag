"""create users table

Revision ID: 6b8e0a49e55d
Revises: 
Create Date: 2024-07-25 21:44:06.954733

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6b8e0a49e55d"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("hashed_password", sa.Unicode(255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
