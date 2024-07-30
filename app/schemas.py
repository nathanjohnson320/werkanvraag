from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    email: str
    password: str


class User(UserBase):
    id: int
    hashed_password: str

    class ConfigDict:
        from_attributes = True


class JobBase(BaseModel):
    title: str
    description: str
    stage: str
    location: str
    company_id: int
    user_id: int


class JobCreate(JobBase):
    title: str
    description: str
    stage: str
    location: str
    company_id: int
    user_id: int


class Job(JobBase):
    id: int

    class ConfigDict:
        from_attributes = True


class CompanyBase(BaseModel):
    name: str


class CompanyCreate(CompanyBase):
    name: str


class Company(CompanyBase):
    id: int

    class ConfigDict:
        from_attributes = True
