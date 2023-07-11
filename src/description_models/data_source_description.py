from typing import Annotated

from html_table_data_source.data_source_description import (
    HTMLTableDataSourceDescription,
)
from pydantic import Field
from tabula_data_source.data_source_description import TabulaDataSourceDescription

DataSourceDescription = Annotated[
    HTMLTableDataSourceDescription
    | TabulaDataSourceDescription,
    Field(discriminator="type"),
]
