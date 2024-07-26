from fastapi import APIRouter, Depends
from fastapi_pagination import Page, add_pagination, paginate
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import User
from app.core.db import get_db
from app.schemas import UserBase


router = APIRouter()


@router.get("/")
def get_users(db: Session = Depends(get_db)) -> Page[UserBase]:
    return paginate(db, select(User))
