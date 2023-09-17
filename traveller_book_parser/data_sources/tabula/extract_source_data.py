import logging

from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.data_parsers.data_frame.data_container import (
    DataFrameDataContainer,
)
from traveller_book_parser.data_sources.extract_source_data import extract_source_data

from .data_extract import extract_tabula_data_frame
from .data_source_description import TabulaDataSourceDescription

logger = logging.getLogger(__name__)


@extract_source_data.dispatch
def extract_tabula_data(
    book_description: BookDescription,
    data_source_description: TabulaDataSourceDescription,
) -> DataFrameDataContainer:
    data_frame = extract_tabula_data_frame(
        book_description,
        data_source_description,
    )
    logger.debug("Parsing entities from tabula data frame:\n%s", data_frame)

    return DataFrameDataContainer(
        data=data_frame,
        data_source_description=data_source_description,
    )
