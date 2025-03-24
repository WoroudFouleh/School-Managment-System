from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Database connection URL
DATABASE_URL: str = "mysql://root:s120WOROUD#@localhost/school_db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db_session() -> Session:
    """
    Returns a new database session.

    Usage:
        with get_db_session() as session:
            result = session.query(User).all()

    Returns:
        Session: A new SQLAlchemy session object.
    """
    return SessionLocal()
