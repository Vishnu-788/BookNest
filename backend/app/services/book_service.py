from fastapi import UploadFile
from app import schemas, crud
from app.core.enums import RoleEnum
from sqlalchemy.orm import Session
from typing import Optional, List
import uuid
import shutil


STATIC_FOLDER = "static/images"

async def create_book_with_image(
    title: str,
    author: str,
    description: Optional[str],
    in_stock: Optional[bool],
    stock_count: Optional[int],
    genres: List[str],
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

    genres = crud.book.get_or_create_genre(genres, db)
    # Creating a pydantic model here
    book_data = schemas.book.BookCreate(
        lib_id=user.id,
        title=title,
        description=description,
        author=author,
        in_stock=in_stock,
        stock_count=stock_count,
        genres=genres,
        img_url=f"/static/images/{filename}"
    )

    return crud.book.create(book_data, db)

def flatten_genres(genres):
    """
    flaten the Genre(SQL alchemy object) to list of strings with only genre name
    """
    genres_list = [genre.name for genre in genres]
    return genres_list
    

def get_library_books(user: schemas.auth.UserAuthResponse, db: Session) -> schemas.book.BookResponse:
    books = crud.book.get_all_books_by_librarian(user.id, db)
    results = []
    for book in books:
        results.append({
            "id": book.id,
            "lib_id": book.lib_id,
            "title": book.title,
            "author": book.author,
            "description": book.description,
            "img_url": book.img_url,
            "genres": flatten_genres(book.genres),
        })
    return results

    

def get_all_books(db: Session) -> schemas.book.BookResponse:
    books = crud.book.get_all_books(db)
    results = []
    for book in books:
        results.append({
            "id": book.id,
            "lib_id": book.lib_id,
            "title": book.title,
            "author": book.author,
            "description": book.description,
            "img_url": book.img_url,
            "genres": flatten_genres(book.genres),
        })

    return results


