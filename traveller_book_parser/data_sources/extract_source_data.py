from plum import dispatch

from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.data_parsers.base_data_container import BaseDataContainer

from .base_data_source_description import BaseDataSourceDescription


@dispatch.abstract
def extract_source_data(
    book_description: BookDescription,  # noqa: ARG001
    data_source_description: BaseDataSourceDescription,  # noqa: ARG001
) -> BaseDataContainer:
    """Parse data from a collection."""
    raise NotImplementedError()
