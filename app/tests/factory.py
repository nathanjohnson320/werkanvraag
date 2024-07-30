from app.tests.db import TestingSessionLocal
from sqlalchemy.orm import sessionmaker, Session
from app import models


def user_factory(db: sessionmaker[Session]):
    user = models.User(email="test@test.com")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def company_factory(db: sessionmaker[Session]):
    company = models.Company(name="test company")
    db.add(company)
    db.commit()
    db.refresh(company)
    return company
