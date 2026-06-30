"""Pydantic schemas for authentication payloads."""

from pydantic import BaseModel


class UserSchema(BaseModel):
    """Schema used for user registration."""

    name: str
    username: str
    password: str
    email: str


class UserResponseSchema(BaseModel):
    """Schema returned after successful registration."""

    name: str
    username: str
    email: str


class LoginSchema(BaseModel):
    """Schema used for user login."""

    username: str
    password: str
