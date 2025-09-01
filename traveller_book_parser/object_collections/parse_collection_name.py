import logging

from traveller_book_parser.books.book_description import (
    BookDescription,
    get_book_file_path,
)
from traveller_book_parser.data_sources.html.data_source_description import (
    HTMLDataSourceDescription,
)
from traveller_book_parser.data_sources.pdfplumber.guess_header import guess_page_header
from traveller_book_parser.object_collections.collection_description import (
    CollectionDescription,
)

logger = logging.getLogger(__name__)


class FailedToGuessCollectionNameError(Exception):
    """Exception raised when failed to guess collection name."""

    def __init__(self, collection_description: CollectionDescription):
        super().__init__(
            f"Failed to guess collection name for {collection_description}"
        )


def get_collection_name_page(collection_description: CollectionDescription) -> int:
    """Get the page number of the collection name."""
    if collection_description.name_page is not None:
        return collection_description.name_page

    data_source_description = collection_description.data_source_description

    if hasattr(data_source_description, "page"):
        return (
            data_source_description.page  # pyright: ignore [reportAttributeAccessIssue]
        )

    if isinstance(data_source_description, HTMLDataSourceDescription):
        pages_list = data_source_description.pages_range_list
        if pages_list:
            return pages_list[0][0]  # Return the start of the first range

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
        raise FailedToGuessCollectionNameError(collection_description)

    name = guess.title()

    logger.info("Guessed collection name: %s", name)
    return name
