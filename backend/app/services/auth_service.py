import re
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import crud, schemas
from app.core import security, enums
from datetime import timedelta


def validate_username(username: str) -> str:
    # Username constraints
    if " " in username:
        raise ValueError("Username cannot contain spaces")
    if not re.match(r"^[A-Za-z0-9_]+$", username):
        raise ValueError("Username can only contain letters, numbers, and underscores")


"""
Register the user in the User table
"""


def register_user(data: schemas.auth.UserCreate, db: Session) -> schemas.auth.UserAuthResponse:
    # Validate fields
    if not data.username or not data.email or not data.password:
        raise ValueError("All fields are required")

    data.username = data.username.lower()
    validate_username(data.username)

    userExists = crud.user.get_user_by_username(data.username, db)
    if userExists: 
        raise ValueError("Username exists try another")
    
    emailExists = crud.user.get_user_by_email(data.email, db)
    if emailExists:
        raise ValueError("Email Exists")

    # Hash password
    hashed_password = security.Security.hash_password(data.password)
    data.password = hashed_password

    user = crud.user.create(data, db)

    if not user:
        raise ValueError("User creation failed")

    access_token_expires = timedelta(minutes=30)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return schemas.auth.UserAuthResponse(
        id=user.id,
        access_token=access_token,
        token_type="bearer",
        username=user.username,
        email=user.email,
        role=user.role,
    )


"""
Register the member in MemberTable
"""


def register_member(request: schemas.auth.MemberCreate, db: Session) -> schemas.auth.UserAuthResponse:
    user_data = schemas.auth.UserCreate(
        username=request.username,
        email=request.email,
        password=request.password,
        role=request.role
    )

    user = register_user(user_data, db)
    if not user:
        raise ValueError("User creation failed")

    memberData=schemas.auth.MemberCreate(
            user_id=user.id,
            address=request.address,
            country=request.country,
            mobile_number=request.mobile_number
    )

    member = crud.user.create_member(memberData, db)
    if not member:
        raise ValueError("User creation failed")

    return user
        

"""
Register the librarian in LibrarianTable
"""


def register_librarian(request: schemas.auth.LibrarianCreate, db: Session)-> schemas.auth.UserAuthResponse:
    user_data = schemas.auth.UserCreate(
        username=request.username,
        email=request.email,
        password=request.password,
        role=enums.RoleEnum.LIBRARIAN
    )

    user = register_user(user_data, db)
    if not user:
        pass

    librarianData= schemas.auth.LibrarianCreate(
        user_id=user.id,
        library_address=request.library_address,
        staff_address=request.staff_address,
        library_number=request.library_number,
        mobile_number=request.mobile_number

    )
    librarian = crud.user.create_librarian(librarianData, db)

    if not librarian:
        pass

    return user


"""
LogIn user
"""


def login_user(request: OAuth2PasswordRequestForm, db: Session)->schemas.auth.UserAuthResponse:
    if not request.username or not request.password:
        raise ValueError("Username and password are required")
    request.username = request.username.lower()
    user = crud.user.get_user_by_username(request.username, db)

    validate_username(request.username)

    if not user:
        raise ValueError(f"{request.username} does not exist")

    if not security.Security.verify_password(request.password, user.password):
        raise ValueError("incorrect password")

    access_token_expires = timedelta(minutes=30)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return schemas.auth.UserAuthResponse(
        id=user.id,
        access_token=access_token,
        token_type="bearer",
        username=user.username,
        email=user.email,
        role=user.role,
    )
