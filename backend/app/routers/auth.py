from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, services
from typing import Annotated

router = APIRouter()


# Reader based Routes
@router.post("/register")
def register_member(
    request: schemas.auth.MemberRequest, db: Annotated[Session, Depends(get_db)]
):
    try:
        return services.auth_service.register_member(request, db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/register/librarian")
def register_librarian(
    request: schemas.auth.LibrarianRequest, db: Annotated[Session, Depends(get_db)]
):
    try:
        return services.auth_service.register_librarian(request, db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/login")
def login_user(
    request: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Annotated[Session, Depends(get_db)],
):
    try:
        return services.auth_service.login_user(request, db)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
