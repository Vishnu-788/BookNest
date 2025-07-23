from fastapi import UploadFile
from app import schemas, crud, models
from sqlalchemy.orm import Session
from typing import Optional
import uuid
import shutil


STATIC_FOLDER = "static/images"

async def create_book_with_image(
    title: str,
    author: str,
    description: Optional[str],
    in_stock: Optional[bool],
    stock_count: Optional[int],
    image: UploadFile,
    db: Session,
    user: schemas.auth.UserAuthResponse
):
    """
    Input: Takes the image and other data as form input
    Returns: other form data and image url passes it to crud
    Note: In db only the url is stored. The image is stored in the /static/images directory
    """

    filename = f"{uuid.uuid4()}.{image.filename.split('.')[-1]}"
    file_path = f"{STATIC_FOLDER}/{filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Creating a pydantic model here
    book_data = schemas.book.BookCreate(
        lib_id=user.id,
        title=title,
        description=description,
        author=author,
        in_stock=in_stock,
        stock_count=stock_count,
        img_url=f"/static/images/{filename}"
    )

    return crud.book.create(book_data, db)

def get_all_books(user: schemas.auth.UserAuthResponse | None, db: Session):
    if user and user.role == models.user.RoleEnum.LIBRARIAN:
        return crud.book.get_all_books_by_librarian(user.id, db)
    return crud.book.get_all_books(db)

