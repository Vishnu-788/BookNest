from passlib.context import CryptContext
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from typing import Annotated
from sqlalchemy.orm import Session
import jwt
from app import schemas, crud
from app.models.user import RoleEnum
from app.database import get_db
from app.core.config import get_settings
from typing import Optional


# Load environment variables
settings = get_settings()
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm

# Password hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme for extracting Bearer token from Authorization header
# tokenUrl is for OpenAPI (Swagger) docs only, so Swagger knows where to get token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# Exception to raise when credentials are invalid


"""
<---------------------- Hashing related functions ---------------------->
"""
class Security:
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash the plain password using bcrypt"""
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify plain password against its hashed version"""
        return pwd_context.verify(plain_password, hashed_password)

"""
<---------------------- Token related functions ---------------------->
"""

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Function to create a JWT access token.
    Input: data (dict) → payload, e.g., {"sub": "username"}
    Optional: expires_delta → timedelta for token expiration
    Output: Encoded JWT token as string
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})  # Add expiry to payload
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str, credentials_exception) -> schemas.auth.TokenData:
    """
    Function to verify and decode JWT token.
    Input: JWT token string
    Output: TokenData object with username if valid
    Raises: credentials_exception if token is invalid/expired
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return schemas.auth.TokenData(username=username)
    except jwt.PyJWTError:
        raise credentials_exception

def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
) -> schemas.auth.UserResponse:
    """
    Function to get the current user from the JWT token.
    Steps:
    1. Extract token using oauth2_scheme
    2. Verify token and decode payload
    3. Fetch user from DB using username
    Output: User object if valid
    Raises: credentials_exception if invalid
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = verify_token(token, credentials_exception)
    user = crud.user.get_user_by_username(username=token_data.username, db=db)
    if user is None:
        raise credentials_exception
    return user

def get_librarian(    
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
):
    """
    Checks if the user role is "librarian" else raise an exception
    """
    user = get_current_user(token, db)
    if user.role != RoleEnum.LIBRARIAN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access Forbidden"
        )
    return user

def get_reader(    
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
):
    # raise some kind of exception here that only librarians can accesss this route
    user = get_current_user(token, db)
    if user.role != RoleEnum.READER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access Forbidden"
        )
    return user


def get_current_user_optional(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
): 
    if token is None:
        return None
    user = get_current_user(token, db)
    return user