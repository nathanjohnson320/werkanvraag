from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.schemas import Company, CompanyCreate
from app.contexts import companies


router = APIRouter()


@router.get("/")
def get_companies(
    pagination_params: Params = Depends(), db: Session = Depends(get_db)
) -> Page[Company]:
    return companies.list(db, pagination_params)


@router.post("/")
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return companies.create(db=db, company=company)
