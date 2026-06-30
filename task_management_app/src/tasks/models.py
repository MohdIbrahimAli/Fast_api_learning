"""SQLAlchemy model for tasks."""

# pylint: disable=too-few-public-methods
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from src.utils.db import Base


class TaskModels(Base):
    """Represent a task belonging to a user."""

    __tablename__ = "users_tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user_table.id", ondelete="CASCADE"))
