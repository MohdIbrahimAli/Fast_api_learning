from fastapi import Request, HTTPException, Depends, status
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import InvalidTokenError

from src.utils.settings import settings
from src.users.models import UserModel
from src.utils.db import get_db

def is_authenticated(request:Request, db:Session = Depends(get_db)):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not Authorized")
        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        username = data.get("_username")

        user = db.query(UserModel).filter(UserModel.username == username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="username notfound")
        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not Authorized")