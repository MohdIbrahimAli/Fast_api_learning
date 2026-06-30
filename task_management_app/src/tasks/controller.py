from src.tasks.dtos import CreateTask
from sqlalchemy.orm import Session
from src.tasks.models import TaskModels
from fastapi import HTTPException
from src.users.models import UserModel


def create_task(body:CreateTask, db:Session, user:UserModel):
    data = body.model_dump()
    new_task = TaskModels(
        title = data["title"],
        description = data["description"],
        is_completed = data["is_completed"],
        user_id = user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task



def get_task(db:Session, user:UserModel):
    tasks = db.query(TaskModels).filter(TaskModels.user_id == user.id).all()
    return tasks



def get_task_by_id(id:int,db:Session, user:UserModel):
    task = db.query(TaskModels).filter(
        TaskModels.user_id == user.id,
        TaskModels.id == id
    ).first()
    if not task:
        raise HTTPException(404, detail="Invalid Task ID")
    return task



def delete_task(id:int, db:Session, user:UserModel):
    task = db.query(TaskModels).filter(
        TaskModels.user_id == user.id,
        TaskModels.id == id
    ).first()
    if not task:
        raise HTTPException(404, detail = "Invalid Task ID")
    db.delete(task)
    db.commit()
    return None



def update_task(id:int, body:CreateTask,db:Session, user:UserModel):
    task = (db.query(TaskModels).filter(
        TaskModels.user_id == user.id,
        TaskModels.id == id
    ).first())

    if task is None:
        raise HTTPException(status_code=404, detail = "Invalid Task ID")
    
    body = body.model_dump(exclude_unset=True)

    for field, value in body.items():
        setattr(task, field, value)

    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task