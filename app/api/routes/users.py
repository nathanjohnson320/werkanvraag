from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, Params
from sqlalchemy.orm import Session
from app.models import User
from app.core.db import get_db
from app.schemas import UserBase, UserCreate
from app.contexts import users


router = APIRouter()


@router.get("/")
def get_users(
    pagination_params: Params = Depends(), db: Session = Depends(get_db)
) -> Page[UserBase]:
    return users.list(db, pagination_params)


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = users.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Could not register user")
    return users.create(db=db, user=user)


@router.post("/login")
def login_user(user: UserCreate, db: Session = Depends(get_db)) -> UserBase:
    db_user = users.get_by_email(db, email=user.email)

    if not db_user:
        raise HTTPException(status_code=400, detail="Could not authenticate user")

    if not users.verify_password(db_user.hashed_password, user.password):
        raise HTTPException(status_code=400, detail="Could not authenticate user")

    return db_user
