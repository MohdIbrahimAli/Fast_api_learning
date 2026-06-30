"""Route definitions for task-related endpoints."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.tasks import controller
from src.tasks.dtos import CreateTask, ResponseTask
from src.users.models import UserModel
from src.utils.db import get_db
from src.utils.helpers import is_authenticated


task_routes = APIRouter(prefix="/tasks")


@task_routes.get("/all_tasks", response_model=list[ResponseTask], status_code=status.HTTP_200_OK)
def get_tasks(
    db: Session = Depends(get_db),
    user: UserModel = Depends(is_authenticated),
):
    """List all tasks for the authenticated user."""
    return controller.get_task(db, user)


@task_routes.get("/one_task/{task_id}", response_model=ResponseTask, status_code=status.HTTP_200_OK)
def get_task_by_id(
    task_id: int,
    db: Session = Depends(get_db),
    user: UserModel = Depends(is_authenticated),
):
    """Fetch a single task for the authenticated user."""
    return controller.get_task_by_id(task_id, db, user)


@task_routes.post("/create", response_model=ResponseTask, status_code=status.HTTP_201_CREATED)
def create_task(
    body: CreateTask,
    db: Session = Depends(get_db),
    user: UserModel = Depends(is_authenticated),
):
    """Create a task for the authenticated user."""
    return controller.create_task(body, db, user)


@task_routes.put(
    "/update_task/{task_id}",
    response_model=ResponseTask,
    status_code=status.HTTP_201_CREATED,
)
def update_task(
    task_id: int,
    body: CreateTask,
    db: Session = Depends(get_db),
    user: UserModel = Depends(is_authenticated),
):
    """Update an existing task belonging to the authenticated user."""
    return controller.update_task(task_id, body, db, user)


@task_routes.delete("/delete_task/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    user: UserModel = Depends(is_authenticated),
):
    """Delete a task belonging to the authenticated user."""
    return controller.delete_task(task_id, db, user)
