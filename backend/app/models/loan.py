from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum, ForeignKey
from app.database import Base
from app.core import enums
from datetime import date


class Loan(Base):
    __tablename__ = "loan_records"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mem_id: Mapped[int] = mapped_column(ForeignKey("member_details.user_id"), nullable=False)
    lib_id: Mapped[int] = mapped_column(ForeignKey("librarian_details.user_id"), nullable=False)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    loaned_date: Mapped[date] = mapped_column(default=date.today)
    due_date: Mapped[date] = mapped_column()
    status: Mapped[str] = mapped_column(
        SQLEnum(enums.LoanStatus), default=enums.LoanStatus.LOANED, nullable=False
    )
