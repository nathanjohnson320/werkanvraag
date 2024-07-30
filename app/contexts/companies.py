from fastapi_pagination import Params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models, schemas


def get(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()


def list(db: Session, params: Params):
    return paginate(db, select(models.Company), params)


def create(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company
