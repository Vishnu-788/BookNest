from enum import Enum
from sqlalchemy import Enum as SQLEnum
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column



class RoleEnum(str, Enum):
    LIBRARIAN = 'librarian'
    READER = 'reader'

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] =mapped_column(SQLEnum(RoleEnum), default=RoleEnum.READER, nullable=False)
