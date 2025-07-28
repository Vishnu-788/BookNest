from pydantic import BaseModel
from datetime import date
from app.core.enums import LoanStatus
from typing import Optional


class LoanRequest(BaseModel):
    member_email: str
    book_id: int
    loaned_date: date
    due_date: date
    status: Optional[LoanStatus] = LoanStatus.LOANED


class LoanCreate(BaseModel):
    mem_id: int
    book_id: int
    lib_id: int
    loaned_date: date
    due_date: date
    status: Optional[LoanStatus] = LoanStatus.LOANED
