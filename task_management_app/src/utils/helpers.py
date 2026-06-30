"""Authentication helpers for protecting API endpoints."""

from fastapi import Depends, HTTPException, Request, status
import jwt
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session

from src.users.models import UserModel
from src.utils.db import get_db
from src.utils.settings import settings


def is_authenticated(request: Request, db: Session = Depends(get_db)):
    """Validate the Authorization header and return the authenticated user."""
    try:
        token_header = request.headers.get("authorization", "")
        if not token_header:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not Authorized",
            )
        token = token_header.split(" ", maxsplit=1)[-1]

        payload = jwt.decode(
            token,
            key=settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        username = payload.get("_username")
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not Authorized",
            )

        user = db.query(UserModel).filter(UserModel.username == username).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="username notfound",
            )
        return user
    except InvalidTokenError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not Authorized",
        ) from exc
