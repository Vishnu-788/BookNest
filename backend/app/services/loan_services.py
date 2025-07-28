from app import schemas, crud
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.core.result import Result

"""
Service layer to extract the member from the provided email and get librarian id from librarian
"""


def create_loan(
    data: schemas.loan.LoanRequest,
    librarian: schemas.auth.UserAuthResponse,
    db: Session,
):
    # get member
    member = crud.user.get_user_by_email(data.member_email, db)
    if not member:
        return Result.fail(f"Cannot find user with email {data.member_email}", 404)

    loan_data = schemas.loan.LoanCreate(
        mem_id=member.id,
        book_id=data.book_id,
        lib_id=librarian.id,
        loaned_date=data.loaned_date,
        due_date=data.due_date,
    )

    loan = crud.loan.create_loan(loan_data, db=db)
    if not loan:
        return Result.fail("Cannot create loan entry in loan history", 502)
    
    return Result.ok(loan, 201)
