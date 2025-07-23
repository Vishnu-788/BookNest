from fastapi import APIRouter, status, Depends, Form, UploadFile, File
from typing import Optional
from app.database import get_db
from sqlalchemy.orm import Session
from app import schemas, crud, services
from app.core import security
from typing import Annotated, List


router = APIRouter()

@router.get("/", response_model=List[schemas.book.BookResponse],status_code=status.HTTP_200_OK)
def get_books(
    db: Annotated[Session, Depends(get_db)],
    user: Annotated[schemas.auth.UserAuthResponse | None, Depends(security.get_current_user_optional)]
):
    return services.book_service.get_all_books(user, db)

@router.get("/{book_id}", response_model=schemas.book.BookResponse, status_code=status.HTTP_200_OK)
def get_book_by_id(book_id: int, db: Annotated[Session, Depends(get_db)]):
    return crud.book.get_book(book_id, db)

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def add_book(
    db: Annotated[Session, Depends(get_db)],
    user: Annotated[schemas.auth.UserAuthResponse, Depends(security.get_librarian)],
    title: Annotated[str, Form()],
    author: Annotated[str, Form()],
    image: UploadFile = File(...),
    description: Annotated[Optional[str], Form()] = None,
    in_stock: Annotated[Optional[bool], Form()] = None,
    stock_count: Annotated[Optional[int], Form()] = None,
):


    return await services.book_service.create_book_with_image(
        title, author, description, in_stock, stock_count, image, db, user
    )
@router.patch("/{book_id}/stock", status_code=status.HTTP_200_OK)
def update_book_stock(
    book_id: int, 
    request: schemas.book.StockUpdate, 
    db: Annotated[Session, Depends(get_db)], 
    user: Annotated[schemas.auth.UserAuthResponse, Depends(security.get_librarian)]
):
    return crud.book.update_stock(book_id, request, db)

