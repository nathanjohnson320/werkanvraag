from app.contexts import users
from app.core.config import settings
from app.core.db import get_db
from app.models import User
from app.schemas import UserBase, UserCreate
from app.security import get_current_active_user, Token, create_access_token
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page, Params
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated

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


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
) -> Token:
    user = users.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@router.post("/login")
def login_user(user: UserCreate, db: Session = Depends(get_db)) -> UserBase:
    db_user = users.get_by_email(db, email=user.email)

    if not db_user:
        raise HTTPException(status_code=400, detail="Could not authenticate user")

    if not users.verify_password(db_user.hashed_password, user.password):
        raise HTTPException(status_code=400, detail="Could not authenticate user")

    return db_user
