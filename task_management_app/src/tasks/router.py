from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.tasks import controller
from src.tasks.dtos import CreateTask, ResponseTask
from src.utils.db import get_db
from src.utils.helpers import is_authenticated
from src.users.models import UserModel

task_routes= APIRouter(prefix="/tasks")


@task_routes.get("/all_tasks", response_model=List[ResponseTask], status_code=status.HTTP_200_OK)
def get_tasks(db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.get_task(db,user)



@task_routes.get("/one_task/{id}", response_model=ResponseTask, status_code=status.HTTP_200_OK)
def get_task_by_id(id:int, db:Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.get_task_by_id(id,db,user)



@task_routes.post("/create",response_model=ResponseTask,status_code=status.HTTP_201_CREATED)
def create_task(body:CreateTask, db:Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.create_task(body, db,user)



@task_routes.put("/update_task/{id}",response_model=ResponseTask, status_code=status.HTTP_201_CREATED)
def update_task(id:int, body:CreateTask, db:Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.update_task(id, body, db, user)



@task_routes.delete("/delete_task/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int, db:Session = Depends(get_db),user:UserModel = Depends(is_authenticated)):
    return controller.delete_task(id, db, user)