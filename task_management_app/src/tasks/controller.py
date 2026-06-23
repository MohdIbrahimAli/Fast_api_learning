from src.tasks.dtos import CreateTask
from sqlalchemy.orm import Session
from src.tasks.models import TaskModels
from fastapi import HTTPException

def create_task(body:CreateTask, db:Session):
    data = body.model_dump()
    new_task = TaskModels(
        title = data["title"],
        description = data["description"],
        is_completed = data["is_completed"]
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status":"task created successfully", "data":new_task}

def get_task(db:Session):
    tasks = db.query(TaskModels).all()
    return {"status":"All the rows successfully imported", "data":tasks}

def get_task_by_id(id:int,db:Session):
    task = db.query(TaskModels).get(id)
    if not task:
        raise HTTPException(404, detail="Invalid Task ID")
    return {'status':"Task found", "Task":task}
