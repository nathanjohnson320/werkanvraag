from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.schemas import Job, JobCreate
from app.contexts import jobs


router = APIRouter()


@router.get("/")
def get_jobs(
    pagination_params: Params = Depends(), db: Session = Depends(get_db)
) -> Page[Job]:
    return jobs.list(db, pagination_params)


@router.post("/")
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return jobs.create(db=db, job=job)
