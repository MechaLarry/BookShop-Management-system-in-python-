from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Setup SQLite database
DATABASE_URL = "sqlite:///bookstore.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db():
    # Import models here to ensure they are created
    from models.book import Book
    from models.customer import Customer
    from models.transaction import Transaction
    Base.metadata.create_all(engine)
