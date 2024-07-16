from collections.abc import Iterable

from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.data_sources.extract_source_data import extract_source_data
from traveller_book_parser.data_sources.html.data_extract import export_book_html_files
from traveller_book_parser.data_sources.html.data_source_description import (
    HTMLDataSourceDescription,
)
from traveller_book_parser.traveller_models.trav_object import TravObject


@extract_source_data.dispatch
def extract_html_table_data(
    book_description: BookDescription,
    data_source_description: HTMLDataSourceDescription,  # noqa: ARG001
) -> Iterable[TravObject]:
    """Extract DataFrame for a table, using pdftohtml."""
    export_book_html_files(book_description)
    # TODO: Parse the HTML files
    return []
