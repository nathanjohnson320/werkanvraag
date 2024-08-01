from argon2 import PasswordHasher
from fastapi_pagination import Params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models, schemas

hasher = PasswordHasher()


def get(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def list(db: Session, params: Params):
    return paginate(db, select(models.User), params)


def hash_password(password: str):
    return hasher.hash(password)


def create(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def verify_password(hashed_password, plain_password):
    try:
        return hasher.verify(hashed_password, plain_password)
    except:
        return False


def authenticate_user(db: Session, email: str, password: str):
    print(email, password)
    user = get_by_email(db, email)
    if not user:
        return False
    if not verify_password(user.hashed_password, password):
        return False
    return user
