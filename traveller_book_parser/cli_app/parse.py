from traveller_book_parser.books.parse_books import parse_all_books, parse_book_entities
from traveller_book_parser.traveller_models.traveller_database import TravellerDatabase


def parse_book_cli(book_code_name: str):
    """Parse a book and print processed entities."""
    database = TravellerDatabase()
    parse_book_entities(database, book_code_name)

    print(database.model_dump_json(indent=2))


def parse_all_books_cli():
    """Parse all books and print processed entities."""
    database = TravellerDatabase()
    parse_all_books(database)

    print(database.model_dump_json(indent=2))
