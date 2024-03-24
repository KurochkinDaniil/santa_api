import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from database import Base
from main import app

DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture(scope="session")
def db_engine():
    return create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


@pytest.fixture(scope="session")
def db_session_factory(db_engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=db_engine)


@pytest.fixture(scope="function")
def db_session(db_engine, db_session_factory):
    Base.metadata.create_all(bind=db_engine)
    db = db_session_factory()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=db_engine)
