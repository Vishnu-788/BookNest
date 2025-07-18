from fastapi import APIRouter, status, Depends
from app.database import get_db
from sqlalchemy.orm import Session
from app import schemas, crud
from typing import Annotated, List

router = APIRouter(
    prefix="/books",
    tags=["books"]
)


@router.get("/", response_model=List[schemas.book.BookResponse], status_code=status.HTTP_200_OK)
def get_books(db: Annotated[Session, Depends(get_db)]):
    return crud.book.get_all(db)

@router.get("/{book_id}", response_model=schemas.book.BookDetailResponse, status_code=status.HTTP_200_OK)
def get_book_by_id(book_id: int, db: Annotated[Session, Depends(get_db)]):
    return crud.book.get_book(book_id, db)

@router.post("/add", status_code=status.HTTP_201_CREATED)
def add_book(request: schemas.book.BookCreate, db: Annotated[Session, Depends(get_db)]):
    return crud.book.create(request, db)

@router.patch("/{book_id}/stock", status_code=status.HTTP_200_OK)
def update_book_stock(book_id: int, request: schemas.book.StockUpdate, db: Annotated[Session, Depends(get_db)]):
    return crud.book.update_stock(book_id, request, db)

