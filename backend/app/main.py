from fastapi import FastAPI
from app.database import Base, engine
from app.routers import books, auth


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

app.include_router(books.router, prefix="/api/v1/books", tags=["Books"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])