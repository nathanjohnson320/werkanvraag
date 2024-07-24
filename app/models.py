from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Mapped,
    mapped_column,
)

from sqlalchemy.orm import relationship
from core.db import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    jobs: Mapped[list["Job"]] = relationship(back_populates="user")


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title = Column(String)
    description = Column(String)
    stage = Column(String, index=True)
    location = Column(String)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="jobs")

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"))
    company: Mapped["Company"] = relationship(back_populates="jobs")


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String, index=True)

    jobs: Mapped[list["Job"]] = relationship(back_populates="companies")
