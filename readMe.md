BookStore Management System
Overview
The BookStore Management System is a command-line interface (CLI) application built with Python that helps small bookstores manage their inventory, track customer data, and record sales transactions. It leverages SQLAlchemy ORM to handle the underlying database and offers a user-friendly CLI to perform various operations such as adding books, managing customers, and processing transactions.

Features
Book Inventory Management: Add, update, and remove books from the inventory. Track stock levels and book prices.
Customer Management: Add, update, and delete customer information. Track purchase history for each customer.
Transaction Management: Record and process book sales, updating inventory levels and tracking transactions.
Sales Reports: Generate reports for total revenue, top-selling books, and top customers based on sales history.

Technology Stack
Language: Python 3
Database: SQLite (via SQLAlchemy ORM)
Libraries:
SQLAlchemy: ORM for database management
Click: Python package for creating beautiful command-line interfaces
Pipenv: Python dependency management and virtual environments
Setup and Installation

Prerequisites
Make sure you have the following installed on your machine:

Python 3
Pipenv (for managing dependencies and the virtual environment)
Installation Steps
Clone the repository:
git clone git@github.com:MechaLarry/BookShop-Management-system-in-python-.git
cd bookstore_management
Set up a virtual environment with Pipenv:
pipenv install
This will install all the dependencies listed in the Pipfile.

Activate the virtual environment:
pipenv shell
Initialize the database:

Inside your virtual environment, run the following command to create the database schema:
python main.py init-db
This will create an SQLite database file (bookstore.db) and the necessary tables.

Usage
After setting up the project, you can use the CLI to interact with the system.

Common Commands
Add a new book:
python3 main.py add-book --title "Book Title" --author "Author Name" --price 19.99 --stock 50

View all books:
python3 main.py view-books

Add a customer:
python3 main.py add-customer --name "John Doe" --email "johndoe@example.com"

Process a sale (record a transaction):
python3 main.py record-sale --customer-id 1 --book-id 2 --quantity 1

Generate a sales report:
python3 main.py sales-report

Database Schema
The database consists of three related tables:

Book:

id: Primary key
title: Title of the book
author: Author of the book
price: Price of the book
stock: Quantity available in stock
Customer:

id: Primary key
name: Customer's name
email: Customer's email
Transaction:

id: Primary key
customer_id: Foreign key (references Customer.id)
book_id: Foreign key (references Book.id)
quantity: Number of books sold
total_price: Total price of the transaction
