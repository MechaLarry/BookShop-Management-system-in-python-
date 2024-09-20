from sqlalchemy import Column, Integer, String, Float
from database.setup import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author}, price={self.price})>"
