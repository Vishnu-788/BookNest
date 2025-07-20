from pydantic import BaseModel
from app import models

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: models.user.RoleEnum = models.user.RoleEnum.READER

class UserLogin(BaseModel):
    username: str
    password: str
    role: models.user.RoleEnum = models.user.RoleEnum.READER

class TokenData(BaseModel):
    username: str

class UserAuthResponse(BaseModel):
    access_token: str
    token_type: str
    username: str
    email: str
    role: models.user.RoleEnum

    model_config = {
        'from_attributes': True
    }

class UserResponse(BaseModel):
    username: str
    email: str
    role: models.user.RoleEnum

    model_config = {
        'from_attributes': True
    }