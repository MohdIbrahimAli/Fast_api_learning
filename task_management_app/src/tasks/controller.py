"""Business logic for managing tasks."""

from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.tasks.dtos import CreateTask
from src.tasks.models import TaskModels
from src.users.models import UserModel


def create_task(body: CreateTask, db: Session, user: UserModel) -> TaskModels:
    """Create a new task for the authenticated user."""
    data = body.model_dump()
    new_task = TaskModels(
        title=data["title"],
        description=data["description"],
        is_completed=data["is_completed"],
        user_id=user.id,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_task(db: Session, user: UserModel) -> list[TaskModels]:
    """Fetch all tasks belonging to the authenticated user."""
    return db.query(TaskModels).filter(TaskModels.user_id == user.id).all()


def get_task_by_id(task_id: int, db: Session, user: UserModel) -> TaskModels:
    """Fetch a single task if it belongs to the authenticated user."""
    task = (
        db.query(TaskModels)
        .filter(TaskModels.user_id == user.id, TaskModels.id == task_id)
        .first()
    )
    if task is None:
        raise HTTPException(status_code=404, detail="Invalid Task ID")
    return task


def delete_task(task_id: int, db: Session, user: UserModel) -> None:
    """Delete an existing task if it exists and belongs to the user."""
    task = (
        db.query(TaskModels)
        .filter(TaskModels.user_id == user.id, TaskModels.id == task_id)
        .first()
    )
    if task is None:
        raise HTTPException(status_code=404, detail="Invalid Task ID")
    db.delete(task)
    db.commit()


def update_task(task_id: int, body: CreateTask, db: Session, user: UserModel) -> TaskModels:
    """Update an existing task if it belongs to the authenticated user."""
    task = (
        db.query(TaskModels)
        .filter(TaskModels.user_id == user.id, TaskModels.id == task_id)
        .first()
    )
    if task is None:
        raise HTTPException(status_code=404, detail="Invalid Task ID")

    data = body.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(task, field, value)

    db.add(task)
    db.commit()
    db.refresh(task)
    return task
