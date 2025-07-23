from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    lib_id: int
    title: str
    author: str
    description: Optional[str] = None
    in_stock: Optional[bool] = None
    stock_count: Optional[int] = None
    img_url: str

class StockUpdate(BaseModel):
    stock: int

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    img_url: str
    model_config = {
        "from_attributes": True
    }
    
class BookDetailResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    author: str
    in_stock: bool
    stock_count: int
    img_url: str
    model_config = {
        "from_attributes": True
    }