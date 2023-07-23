from typing import Annotated

from pydantic import Field

from traveller_book_parser.html_table_data_source.data_source_description import (
    HTMLTableDataSourceDescription,
)
from traveller_book_parser.tabula_data_source.data_source_description import (
    TabulaDataSourceDescription,
)

DataSourceDescription = Annotated[
    HTMLTableDataSourceDescription | TabulaDataSourceDescription,
    Field(discriminator="type"),
]
