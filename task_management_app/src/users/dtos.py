from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    name : str
    username : str
    password : str
    email : str