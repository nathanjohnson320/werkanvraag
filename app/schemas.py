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
