import os
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import books, auth, loans
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(debug=True)

# Create tables
Base.metadata.create_all(bind=engine)


# CORS related settings
origins = [
    "http://localhost:3000", 
    "http://localhost:5173", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# orrect static directory path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Go one level up
STATIC_DIR = os.path.join(BASE_DIR, "static")

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
app.include_router(loans.router, prefix="/api/v1/librarian", tags=["Loans"])
