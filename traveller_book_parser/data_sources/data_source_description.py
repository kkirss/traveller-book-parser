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

DataSourceDescriptionField = Field(
    title="Data Source Description",
    description="Description of a source of data (e.g. a table).",
    discriminator="type",
)
DataSourceDescription = Annotated[
    HTMLTableDataSourceDescription
    | TabulaDataSourceDescription
    | PDFPlumberDataSourceDescription,
    DataSourceDescriptionField,
]
