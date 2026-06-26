from fastapi import APIRouter, status, Depends
from src.utils.db import get_db
from src.users import controller
from src.users.dtos import UserSchema, UserResponseSchema, LoginSchema
from sqlalchemy.orm import Session



user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", response_model=UserResponseSchema,status_code=status.HTTP_201_CREATED)
def user_registration(body:UserSchema, db : Session = Depends(get_db)):
    return controller.user_registration(body, db)

@user_routes.post("/login", status_code=status.HTTP_200_OK)
def login(body:LoginSchema, db:Session = Depends(get_db)):
    return controller.login(body, db)