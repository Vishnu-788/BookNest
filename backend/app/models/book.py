from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey, Table, Column
from app.database import Base
from typing import Optional, List

book_genre = Table(
    'book_genre',
    Base.metadata,
    Column('book_id', ForeignKey('books.id')),
    Column('genre_id', ForeignKey('genres.id'))
)


class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    # Relationship
    books: Mapped[List["Book"]] = relationship(secondary=book_genre, back_populates="genres")

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

    # Relationship
    genres: Mapped[List[Genre]] = relationship(secondary=book_genre, back_populates="books")

    

