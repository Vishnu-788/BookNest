from pydantic import BaseModel
from app.core import enums

"""
Input schemas
"""


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: enums.RoleEnum = enums.RoleEnum.MEMBER


class MemberCreate(BaseModel):
    # Fields in MemberDetails table
    user_id: int
    address: str
    mobile_number: str
    country: str


class LibrarianCreate(BaseModel):
    # Fields in LibrarianDetails Table
    user_id: int
    library_address: str
    staff_address: str
    library_number: int
    mobile_number: int

class MemberRequest(UserCreate):
    address: str
    mobile_number: str
    country: str

class LibrarianRequest(UserCreate):
    library_address: str
    library_number: int
    staff_address: str
    mobile_number: int


class UserLogin(BaseModel):
    username: str
    password: str
    role: enums.RoleEnum = enums.RoleEnum.MEMBER


class TokenData(BaseModel):
    username: str


"""
Responses schemas
"""


class UserAuthResponse(BaseModel):
    id: int | str
    access_token: str
    token_type: str
    username: str
    email: str
    role: enums.RoleEnum

    model_config = {"from_attributes": True}


class UserResponse(BaseModel):
    username: str
    email: str
    role: enums.RoleEnum

    model_config = {"from_attributes": True}
