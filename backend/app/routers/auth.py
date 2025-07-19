from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, services
from typing import Annotated

router = APIRouter()

# Reader based Routes
@router.post("/register")
def register_user(request: schemas.auth.UserCreate, db: Annotated[Session, Depends(get_db)]):
    try:
        return services.auth_service.register_user(request, db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    
@router.post("/login")
def login_user(request: schemas.auth.UserLogin, db: Annotated[Session, Depends(get_db)]):
    try:
        return services.auth_service.login_user(request, db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))