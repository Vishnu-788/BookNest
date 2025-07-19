from pydantic import BaseModel
from app.models.user import RoleEnum

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: RoleEnum = RoleEnum.READER

class UserLogin(BaseModel):
    username: str
    password: str
    role: RoleEnum = RoleEnum.READER

class UserAuthResponse(BaseModel):
    token: str
    token_type: str
    username: str
    email: str
    role: RoleEnum