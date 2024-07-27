from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, add_pagination, paginate
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from app.models import User
from app.core.db import get_db
from app.schemas import UserBase, UserCreate
from app.contexts import users


router = APIRouter()


@router.get("/")
def get_users(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
) -> Page[UserBase]:
    return users.list(db)


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = users.get_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Could not register user")
    return users.create(db=db, user=user)
