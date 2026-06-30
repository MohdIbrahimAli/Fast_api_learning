"""Business logic for user registration and authentication."""

from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from src.users.dtos import LoginSchema, UserSchema
from src.users.models import UserModel
from src.utils.settings import settings

password_hash = PasswordHash.recommended()


def get_password_hash(password: str) -> str:
    """Hash a plain-text password."""
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain-text password against a stored hash."""
    return password_hash.verify(plain_password, hashed_password)


def user_registration(body: UserSchema, db: Session) -> UserModel:
    """Register a new user if the username and email are both unused."""
    existing_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if existing_user is not None:
        raise HTTPException(status_code=400, detail="Username already exists..")

    existing_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if existing_email is not None:
        raise HTTPException(status_code=400, detail="Email address already exists..")

    hashed_password = get_password_hash(body.password)
    new_user = UserModel(
        name=body.name,
        username=body.username,
        hash_password=hashed_password,
        email=body.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login(body: LoginSchema, db: Session) -> dict[str, str]:
    """Authenticate a user and return a JWT token."""
    user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username not found")

    if not verify_password(body.password, user.hash_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password is incorrect",
        )

    expiration_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)
    token = jwt.encode(
        {"_username": user.username, "exp": expiration_time.timestamp()},
        key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    return {"token": token}
