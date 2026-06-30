"""Route definitions for user endpoints."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.users import controller
from src.users.dtos import LoginSchema, UserResponseSchema, UserSchema
from src.utils.db import get_db

user_routes = APIRouter(prefix="/user")


@user_routes.post(
    "/register",
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def user_registration(body: UserSchema, db: Session = Depends(get_db)):
    """Register a new user account."""
    return controller.user_registration(body, db)


@user_routes.post("/login", status_code=status.HTTP_200_OK)
def login(body: LoginSchema, db: Session = Depends(get_db)):
    """Authenticate a user and return a JWT token."""
    return controller.login(body, db)
