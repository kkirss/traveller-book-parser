from typing import Annotated

from pydantic import Field

from traveller_book_parser.data_sources.html_table.data_source_description import (
    HTMLTableDataSourceDescription,
)
from traveller_book_parser.data_sources.pdfplumber.data_source_description import (
    PDFPlumberDataSourceDescription,
)
from traveller_book_parser.data_sources.tabula.data_source_description import (
    TabulaDataSourceDescription,
)

DataSourceDescription = Annotated[
    HTMLTableDataSourceDescription
    | TabulaDataSourceDescription
    | PDFPlumberDataSourceDescription,
    Field(discriminator="type"),
]
