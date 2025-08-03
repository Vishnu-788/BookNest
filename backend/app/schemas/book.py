from pydantic import BaseModel, model_validator
from typing import Optional, List
from app.models.book import Genre

class BookCreate(BaseModel):
    lib_id: int
    title: str
    author: str
    description: Optional[str] = None
    in_stock: Optional[bool] = None
    stock_count: Optional[int] = None
    genres: List[Genre]
    img_url: str

    model_config={
        "arbitrary_types_allowed": True
    }

class StockUpdate(BaseModel):
    stock: int

    
class BookResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    author: str
    genres: List[str]
    img_url: str
    model_config = {
        "from_attributes": True,
    }



