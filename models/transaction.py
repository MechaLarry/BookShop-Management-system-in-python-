from sqlalchemy import Column, Integer, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database.setup import Base
from datetime import date

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    purchase_date = Column(Date, default=date.today)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)

    # Relationships
    book = relationship("Book")
    customer = relationship("Customer")

    def __repr__(self):
        return f"<Transaction(book={self.book.title}, customer={self.customer.name}, total_price={self.total_price})>"
