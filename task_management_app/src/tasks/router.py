from fastapi import APIRouter, Depends
from src.tasks import controller
from src.tasks.dtos import CreateTask
from src.utils.db import get_db

task_routes= APIRouter(prefix="/tasks")

@task_routes.post("/create")
def create_task(body:CreateTask, db = Depends(get_db)):
    return controller.create_task(body, db)

@task_routes.get("/all_tasks")
def get_tasks(db = Depends(get_db)):
    return controller.get_task(db)

@task_routes.get("/one_task/{id}")
def get_task_by_id(id:int, db = Depends(get_db)):
    return controller.get_task_by_id(id,db)

@task_routes.delete("/delete_task/{id}")
def delete_task(id, db = Depends(get_db)):
    return controller.delete_task(id, db)