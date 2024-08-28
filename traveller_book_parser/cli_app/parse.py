import typer

from traveller_book_parser.books.parse_books import parse_all_books, parse_book
from traveller_book_parser.traveller_database.output import outputted_database
from traveller_book_parser.traveller_database.output_format.output_format import (
    DatabaseOutputFormat,
)

parse_app = typer.Typer(no_args_is_help=True)


def parse_book_cli(
    book_code_name: str,
    output_format: DatabaseOutputFormat = DatabaseOutputFormat.json,
):
    """Parse a book and print processed objects."""
    with outputted_database(output_format) as database:
        parse_book(database, book_code_name)


parse_app.command("book")(parse_book_cli)


def parse_all_books_cli(
    output_format: DatabaseOutputFormat = DatabaseOutputFormat.json,
):
    """Parse all books and print processed objects."""
    with outputted_database(output_format) as database:
        parse_all_books(database)


parse_app.command("all")(parse_all_books_cli)
