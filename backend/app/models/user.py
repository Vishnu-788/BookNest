from sqlalchemy import Enum as SQLEnum, ForeignKey
from app.core import enums
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


"""
Common table for storing both types of users(LIBRARIAN, MEMBER)
"""


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(
        SQLEnum(enums.RoleEnum), default=enums.RoleEnum.MEMBER, nullable=False
    )

    # Relationships
    member_details = relationship(
        "MemberDetails", back_populates="user", uselist=False
    )
    librarian_details = relationship(
        "LibrarianDetails", back_populates="user", uselist=False
    )


"""
Table for storing Members details
"""


class MemberDetails(Base):
    __tablename__ = "member_details"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), primary_key=True, index=True
    )
    address: Mapped[str] = mapped_column(nullable=False)
    mobile_number: Mapped[int] = mapped_column()
    country: Mapped[str] = mapped_column()

    # Relationship
    user = relationship("User", back_populates="member_details")
    


"""
Table for stroing Librarian details
"""


class LibrarianDetails(Base):
    __tablename__ = "librarian_details"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), primary_key=True, index=True
    )
    library_address: Mapped[str] = mapped_column(nullable=False)
    staff_address: Mapped[str] = mapped_column(nullable=False)
    mobile_number: Mapped[str] = mapped_column(nullable=False)
    library_number: Mapped[str] = mapped_column(nullable=False)

    # Relationship
    user = relationship("User", back_populates="librarian_details")
