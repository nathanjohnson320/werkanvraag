from fastapi import APIRouter

from app.api.routes import jobs, users, companies

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(companies.router, prefix="/companies", tags=["companies"])
