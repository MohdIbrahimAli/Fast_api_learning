import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException, status, Request
from pwdlib import PasswordHash
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from src.users.dtos import UserSchema, LoginSchema
from src.users.models import UserModel
from src.utils.settings import settings

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def user_registration(body:UserSchema, db:Session):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(400, detail="Username already exists..")
    
    is_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_email:
        raise HTTPException(400, detail="Email address already exists..")
    
    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        name= body.name,
        username = body.username,
        hash_password = hash_password,
        email = body.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login(body:LoginSchema, db:Session):
    user = db.query(UserModel).filter(UserModel.username == body.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username not found")

    if not verify_password(body.password, user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Password is incorrect")
    
    exp_time = datetime.now() + timedelta(minutes = settings.EXP_TIME)
     
    token = jwt.encode({"_username":user.username, "exp":exp_time.timestamp()}, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return {"token":token}

