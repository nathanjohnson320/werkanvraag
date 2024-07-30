from fastapi_pagination import Params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session
from app import models, schemas


def get(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()


def list(db: Session, params: Params):
    return paginate(db, select(models.Job), params)


def create(db: Session, job: schemas.JobCreate):
    db_job = models.Job(**job.model_dump())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
