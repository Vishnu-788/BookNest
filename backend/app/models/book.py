from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.database import Base
from typing import Optional

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    lib_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[Optional[str]]
    author: Mapped[str] = mapped_column(nullable=False)
    in_stock: Mapped[bool] = mapped_column(default=True)
    stock_count: Mapped[int] = mapped_column(default=1)
    img_url: Mapped[str] = mapped_column(default="Image not available")

    def __repr__(self):
        return f"Id: {self.id} title: {self.title}"