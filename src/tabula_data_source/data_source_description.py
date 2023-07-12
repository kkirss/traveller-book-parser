from typing import Literal

from description_models.base_data_source_description import BaseDataSourceDescription
from pydantic import Field

TABULA_DATA_SOURCE_DESCRIPTION_TYPE = "tabula-table"
TABULA_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL = Literal["tabula-table"]


class TabulaDataSourceDescription(BaseDataSourceDescription):
    """Description of getting data using Tabula."""

    type: TABULA_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL

    page: int
    page_table_number: int = Field(
        default=1,
        description="The sequential number of the table on the page.",
    )
    # For getting the area, see:
    # https://github.com/tabulapdf/tabula-java/wiki/Using-the-command-line-tabula-extractor-tool#grab-coordinates-of-the-table-you-want
    area: list[float] | None = Field(
        description="Area of page to look for table in.",
        default=None,
    )

    @property
    def page_table_index(self) -> int:
        return self.page_table_number - 1
