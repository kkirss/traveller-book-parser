import logging

from traveller_book_parser.books.book_description import (
    BookDescription,
    get_book_file_path,
)
from traveller_book_parser.data_sources.pdfplumber.guess_header import guess_page_header

from .collection_description import CollectionDescription

logger = logging.getLogger(__name__)


def get_collection_name_page(collection_description: CollectionDescription) -> int:
    """Get the page number of the collection name."""
    if collection_description.name_page is not None:
        return collection_description.name_page

    data_source_description = collection_description.data_source_description

    if hasattr(data_source_description, "page"):
        return (
            data_source_description.page  # pyright: ignore [reportAttributeAccessIssue]
        )

    raise NotImplementedError(
        f"Guessing collection name is not supported for this data source: {data_source_description}"
    )


def parse_collection_name(
    book_description: BookDescription, collection_description: CollectionDescription
) -> str:
    """Parse the name of a collection."""
    name = collection_description.name

    if name is not None:
        return name

    guess = guess_page_header(
        pdf_path=get_book_file_path(book_description.code_name),
        page_number=get_collection_name_page(collection_description),
        nth_largest_font_text=collection_description.name_nth_largest_font,
    )

    if guess is None:
        raise ValueError(
            f"Failed to guess collection name for {collection_description}"
        )

    name = guess.title()

    logger.info("Guessed collection name: %s", name)
    return name
