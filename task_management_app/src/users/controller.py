import jwt

from sqlalchemy.orm import Session
from src.users.dtos import UserSchema


def user_registration(body:UserSchema, db:Session):
    return {"msg":"Registration successfull"}