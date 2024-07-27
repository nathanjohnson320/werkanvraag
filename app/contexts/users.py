from argon2 import PasswordHasher
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models, schemas

hasher = PasswordHasher()


def get(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def list(db: Session, skip: int = 0, limit: int = 100):
    return paginate(db, select(models.User).offset(skip).limit(limit))


def create(db: Session, user: schemas.UserCreate):
    hashed_password = hasher.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
