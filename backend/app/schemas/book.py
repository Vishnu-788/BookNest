from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    in_stock: Optional[bool] = None
    stock_count: Optional[int] = None

class StockUpdate(BaseModel):
    stock: int

class BookResponse(BaseModel):
    id: int
    title: str
    author: str
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

    model_config = {
        "from_attributes": True
    }