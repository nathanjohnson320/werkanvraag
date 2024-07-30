"""create jobs table

Revision ID: 062e8fade188
Revises: c0a1051a9c32
Create Date: 2024-07-29 20:56:20.548345

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "062e8fade188"
down_revision: Union[str, None] = "c0a1051a9c32"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "jobs",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String),
        sa.Column("description", sa.String),
        sa.Column("stage", sa.String, index=True),
        sa.Column("location", sa.String),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("company_id", sa.Integer, sa.ForeignKey("companies.id")),
    )


def downgrade() -> None:
    op.drop_table("jobs")
