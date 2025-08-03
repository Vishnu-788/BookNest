import os
from fastapi import FastAPI, Request
from app.database import Base, engine
from app.routers import books, auth, loans
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.core.exceptions import AppException  # Assuming your exception file is in app/core/exceptions.py
from app.core.logger import logger  # If you're logging in a separate file like logger.py




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

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    logger.error(f"[{request.url.path}] -> {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message}
    )

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}



# Routers
app.include_router(books.router, prefix="/api/v1/books", tags=["Books"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(loans.router, prefix="/api/v1/librarian", tags=["Loans"])
