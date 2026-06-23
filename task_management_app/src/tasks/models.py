from sqlalchemy import Column, Integer, String, Boolean
from src.utils.db import Base

class TaskModels(Base):
    __tablename__ = "users_tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default=False)
