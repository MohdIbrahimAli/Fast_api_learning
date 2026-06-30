"""Pydantic schemas for task payloads."""

from pydantic import BaseModel, ConfigDict


class CreateTask(BaseModel):
    """Schema used to create or update a task."""

    title: str | None = None
    description: str | None = None
    is_completed: bool = False

    model_config = ConfigDict(from_attributes=True)


class ResponseTask(BaseModel):
    """Schema returned to clients for task resources."""

    id: int
    title: str
    description: str
    is_completed: bool

    model_config = ConfigDict(from_attributes=True)
