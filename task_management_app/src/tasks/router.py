from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import CreateTask
from src.utils.db import get_db

task_routes= APIRouter(prefix="/tasks")


@task_routes.get("/all_tasks",status_code=status.HTTP_200_OK)
def get_tasks(db = Depends(get_db)):
    return controller.get_task(db)



@task_routes.get("/one_task/{id}",status_code=status.HTTP_200_OK)
def get_task_by_id(id:int, db = Depends(get_db)):
    return controller.get_task_by_id(id,db)



@task_routes.post("/create",status_code=status.HTTP_201_CREATED)
def create_task(body:CreateTask, db = Depends(get_db)):
    return controller.create_task(body, db)



@task_routes.put("/update_task/{id}", status_code=status.HTTP_201_CREATED)
def update_task(id:int, body:CreateTask, db = Depends(get_db)):
    return controller.update_task(id, body, db)



@task_routes.delete("/delete_task/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int, db = Depends(get_db)):
    return controller.delete_task(id, db)