from traveller_book_parser.traveller_models.book import Book
from traveller_book_parser.traveller_models.traveller_database import TravellerDatabase


def add_book_to_database(database: TravellerDatabase, book: Book) -> None:
    """Add a book to a database."""
    database.all_books.append(book)
