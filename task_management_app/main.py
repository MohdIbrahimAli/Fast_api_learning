from fastapi import FastAPI 
from src.utils.db import Base, engine
from src.tasks.models import TaskModels

Base.metadata.create_all(engine)

app = FastAPI(title="Task Management application made using FastAPI")
