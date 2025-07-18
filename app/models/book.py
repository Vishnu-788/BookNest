from sqlalchemy import Column, String, Integer, Boolean
from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    in_stock = Column(Boolean, nullable=False, default=True)
    stock_count = Column(Integer, nullable=False, default=1)

    def __repr__(self):
        return f"Id: {self.id} title: {self.title}"