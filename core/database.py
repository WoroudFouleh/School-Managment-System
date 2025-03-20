from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.base import Base

DATABASE_URL = "mysql://root:s120WOROUD#@localhost/school_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db_session():
    return SessionLocal()