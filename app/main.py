from fastapi import FastAPI
from app.database import Base, engine
from app.routers import books

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

app.include_router(books.router, prefix="/api/v1")