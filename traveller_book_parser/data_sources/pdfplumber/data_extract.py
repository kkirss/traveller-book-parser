from pandas import DataFrame

from traveller_book_parser.books.book_description import (
    BookDescription,
    get_book_file_path,
)

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
    data_frame = DataFrame(table[1:], columns=table[0])
    return data_frame
