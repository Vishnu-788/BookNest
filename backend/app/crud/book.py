from sqlalchemy.orm import Session
from app import schemas, models
from app.core import exceptions
from typing import List


"""
Book realted model crud operations
"""
def create(data: schemas.book.BookCreate, db: Session):
    new_book = models.book.Book(**data.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def get_all_books(db: Session):
    books = db.query(models.book.Book).all()
    return books


def get_all_books_by_librarian(id: int, db: Session):
    books = db.query(models.book.Book).filter(models.book.Book.lib_id == id).all()
    return books


def get_book(id: int, db: Session):
    book = db.query(models.book.Book).filter(models.book.Book.id == id).first()
    if not book:
        raise exceptions.NotFoundException(f"Book with id: {id} doesnt exist")
    return book


def update_stock(id: int, request: schemas.book.StockUpdate, db: Session):
    book = get_book(id, db)
    book.stock_count = request.stock
    book.in_stock = book.stock_count > 0
    db.commit()
    db.refresh(book)
    return book

""" 
Genre related table crud operations
"""

def get_or_create_genre(genre_names: List[str], db: Session) -> List[str]:
    genres=[]
    for name in genre_names:
        genre = db.query(models.book.Genre).filter(models.book.Genre.name == name).first()
        if not genre:
            genre=models.book.Genre(name=name)
            db.add(genre)
            db.flush()
        genres.append(genre)
    return genres
