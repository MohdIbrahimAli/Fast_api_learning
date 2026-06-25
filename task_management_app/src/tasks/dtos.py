from pydantic import BaseModel, ConfigDict

class CreateTask(BaseModel):
    title:str
    description:str
    is_completed:bool = False

    model_config = ConfigDict(from_attributes=True)

class ResponseTask(BaseModel):
    id : int
    title : str
    model_config = ConfigDict(from_attributes=True)