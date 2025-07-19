from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, models
from typing import Annotated

router = APIRouter(prefix="/users", tags=["users"])

# Reader based Routes
# @router.get("/register")
# def register_user(request: schemas.user.User, db: Annotated[Session, Depends(get_db)]):
