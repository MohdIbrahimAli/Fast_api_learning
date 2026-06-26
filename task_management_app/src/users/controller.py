import jwt
from fastapi import HTTPException
from pwdlib import PasswordHash

from sqlalchemy.orm import Session
from src.users.dtos import UserSchema
from src.users.models import UserModel

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)


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