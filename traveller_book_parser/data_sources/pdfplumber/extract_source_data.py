from pandas import DataFrame, Series

from traveller_book_parser.books.book_description import (
    BookDescription,
    get_book_file_path,
)
from traveller_book_parser.data_parsers.data_frame.data_container import (
    DataFrameDataContainer,
)
from traveller_book_parser.data_sources.extract_source_data import extract_source_data

from .data_source_description import PDFPlumberDataSourceDescription
from .pdfplumber_integration import get_pdfplumber_table


def extract_pdfplumber_data_frame(
    book_description: BookDescription,
    data_source_description: PDFPlumberDataSourceDescription,
) -> DataFrame:
    """Extract DataFrame for a table, using pdfplumber."""
    pdf_path = get_book_file_path(book_description.code_name)
    table = get_pdfplumber_table(
        pdf_path=pdf_path,
        page_number=data_source_description.page,
        table_index=data_source_description.page_table_index,
        table_settings=data_source_description.table_settings,
    )
    data_frame = DataFrame(table[1:], columns=Series(table[0]))
    return data_frame


@extract_source_data.dispatch
def extract_pdfplumber_data(
    book_description: BookDescription,
    data_source_description: PDFPlumberDataSourceDescription,
) -> DataFrameDataContainer:
    """Extract DataFrame for a table, using pdfplumber."""
    data_frame = extract_pdfplumber_data_frame(
        book_description,
        data_source_description,
    )
    return DataFrameDataContainer(
        data=data_frame,
        data_source_description=data_source_description,
    )
