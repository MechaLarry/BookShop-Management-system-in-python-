from cli.commands import cli
from database.setup import init_db

if __name__ == '__main__':
    # Initialize database if not already created
    init_db()
    cli()
