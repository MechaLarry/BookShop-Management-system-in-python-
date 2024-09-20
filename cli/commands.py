import click
from sqlalchemy.orm import Session
from database.setup import engine
from models.book import Book
from models.customer import Customer
from models.transaction import Transaction

session = Session(bind=engine)

@click.group()
def cli():
    pass

# Add Book
@click.command()
@click.option('--title', prompt='Book Title')
@click.option('--author', prompt='Author Name')
@click.option('--genre', prompt='Genre')
@click.option('--price', prompt='Price', type=float)
@click.option('--stock', prompt='Stock Quantity', type=int)
def add_book(title, author, genre, price, stock):
    book = Book(title=title, author=author, genre=genre, price=price, stock_quantity=stock)
    session.add(book)
    session.commit()
    click.echo(f"Added book: {title}")

# View Books
@click.command()
def view_books():
    books = session.query(Book).all()
    for book in books:
        click.echo(f"{book.id}: {book.title} by {book.author} - {book.stock_quantity} in stock")

# Add Customer
@click.command()
@click.option('--name', prompt='Customer Name')
@click.option('--email', prompt='Customer Email')
@click.option('--phone', prompt='Customer Phone')
def add_customer(name, email, phone):
    customer = Customer(name=name, email=email, phone=phone)
    session.add(customer)
    session.commit()
    click.echo(f"Added customer: {name}")

# Make Transaction
@click.command()
@click.option('--customer_id', prompt='Customer ID', type=int)
@click.option('--book_id', prompt='Book ID', type=int)
@click.option('--quantity', prompt='Quantity', type=int)
def make_transaction(customer_id, book_id, quantity):
    book = session.query(Book).get(book_id)
    customer = session.query(Customer).get(customer_id)

    if book and customer:
        total_price = book.price * quantity
        transaction = Transaction(customer_id=customer_id, book_id=book_id, quantity=quantity, total_price=total_price)
        session.add(transaction)
        session.commit()
        book.stock_quantity -= quantity
        session.commit()
        click.echo(f"Transaction complete! {customer.name} purchased {quantity} copies of {book.title}")
    else:
        click.echo("Invalid entry!. Check if ID is correct")

# View Transactions
@click.command()
def view_transactions():
    transactions = session.query(Transaction).all()
    for t in transactions:
        click.echo(f"Transaction: {t.customer.name} bought {t.quantity} copies of {t.book.title} on {t.purchase_date}")


# Register commands with CLI
cli.add_command(add_book)
cli.add_command(view_books)
cli.add_command(add_customer)
cli.add_command(make_transaction)
cli.add_command(view_transactions)
