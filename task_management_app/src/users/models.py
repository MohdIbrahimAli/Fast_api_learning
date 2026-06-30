"""SQLAlchemy model for users."""

# pylint: disable=too-few-public-methods
from sqlalchemy import Column, Integer, String

from src.utils.db import Base


class UserModel(Base):
    """Represent a user account in the database."""

    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    email = Column(String, nullable=False)
