from src.tasks.dtos import CreateTask
from sqlalchemy.orm import Session
from src.tasks.models import TaskModels

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