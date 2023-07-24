from pathlib import Path

from traveller_book_parser.books.parse_books import parse_all_books, parse_book

from .entities import print_entities


def parse_book_cli(book_path: Path):
    """Parse a book and print processed entities."""
    entities = parse_book(book_path)
    print_entities(entities)


def parse_all_books_cli():
    """Parse all books and print processed entities."""
    entities = parse_all_books()
    print_entities(entities)
