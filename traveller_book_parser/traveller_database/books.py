from traveller_book_parser.traveller_models.book import Book
from traveller_book_parser.traveller_models.trav_database import TravDatabase


def add_book_to_database(database: TravDatabase, book: Book) -> None:
    """Add a book to a database."""
    database.all_books.append(book)
