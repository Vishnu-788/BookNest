from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models


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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book


def update_stock(id: int, request: schemas.book.StockUpdate, db: Session):
    book = get_book(id, db)
    book.stock_count = request.stock
    book.in_stock = book.stock_count > 0
    db.commit()
    db.refresh(book)
    return book
