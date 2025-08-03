from app import schemas, crud
from sqlalchemy.orm import Session
from app.core import exceptions

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
        raise exceptions.NotFoundException(f"User with email {data.member_email} not found")

    loan_data = schemas.loan.LoanCreate(
        mem_id=member.id,
        book_id=data.book_id,
        lib_id=librarian.id,
        loaned_date=data.loaned_date,
        due_date=data.due_date,
    )

    loan = crud.loan.create_loan(loan_data, db=db)
    if not loan:
        raise exceptions.InternalServerError("Trouble creating loan entry")
    
    return loan
