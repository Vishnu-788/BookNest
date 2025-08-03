from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud, services
from app.core import security


from typing import Annotated

router = APIRouter(dependencies=[Depends(security.get_librarian)])

"""
To create a loan history entry when an member loans out a book 
"""


@router.post("/loan-out", status_code=status.HTTP_201_CREATED)
def loan_history_entry(
    request: schemas.loan.LoanRequest,
    db: Annotated[Session, Depends(get_db)],
    librarian: Annotated[schemas.auth.UserAuthResponse, Depends(security.get_librarian)]
):
    loan_entry = services.loan_services.create_loan(request, librarian=librarian, db=db)
    return loan_entry



@router.get("/")
def get_loan_history(
    db: Annotated[Session, Depends(get_db)],
    librarian: Annotated[
        schemas.auth.UserAuthResponse, Depends(security.get_librarian)
    ],
):
    pass
