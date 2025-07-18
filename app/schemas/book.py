from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    in_stock: bool
    stock_count: int

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
    author: str
    in_stock: bool
    stock_count: int

    model_config = {
        "from_attributes": True
    }