import os
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import books, auth
from starlette.staticfiles import StaticFiles

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# orrect static directory path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Go one level up
STATIC_DIR = os.path.join(BASE_DIR, "static")
print("BASE_DIR", BASE_DIR)
print("STATIC_DIR", STATIC_DIR)

# Ensure static folder exists (optional but safe)
os.makedirs(STATIC_DIR, exist_ok=True)

# Mount static
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# Routers
app.include_router(books.router, prefix="/api/v1/books", tags=["Books"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
