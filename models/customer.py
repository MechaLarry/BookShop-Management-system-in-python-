from sqlalchemy import Column, Integer, String
from database.setup import Base

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    def __repr__(self):
        return f"<Customer(name={self.name}, email={self.email})>"
