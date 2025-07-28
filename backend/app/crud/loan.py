from sqlalchemy.orm import Session
from app import schemas, models
from app.core import enums


def create_loan(data: schemas.loan.LoanCreate, db: Session):
    newLoan = models.loan.Loan(**data.model_dump())
    db.add(newLoan)
    db.commit()
    db.refresh(newLoan)
    return newLoan


def find_loan_by_id(id: int, db: Session):
    loan_instance = (
        db.query(models.loan.Loan).filter(models.loan.Loan.id == id).one_or_none()
    )
    return loan_instance


def update_loan_status(id: int, db: Session):
    loan = find_loan_by_id(id, db)
    loan.status = enums.LoanStatus.RETURNED
    db.commit()
    db.refresh(loan)
    return loan
