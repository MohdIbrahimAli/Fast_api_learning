"""Database configuration and session dependency."""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.utils.settings import settings

Base = declarative_base()
engine = create_engine(settings.DB_CONNECTION, echo=False)

SESSION_FACTORY = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    """Provide a database session for each request."""
    session = SESSION_FACTORY()
    try:
        yield session
    finally:
        session.close()
