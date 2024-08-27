from typing import Literal, Optional

from pydantic import Field

from traveller_book_parser.data_sources.base_data_source_description import (
    BaseDataSourceDescription,
)


class TabulaDataSourceDescription(BaseDataSourceDescription):
    """Description of getting data using Tabula."""

    type: Literal["tabula-table"]

    page: int
    page_table_number: int = Field(
        default=1,
        description="The sequential number of the table on the page.",
    )
    extraction_method: Optional[Literal["lattice", "stream"]] = None
    # For getting the area, see:
    # https://github.com/tabulapdf/tabula-java/wiki/Using-the-command-line-tabula-extractor-tool#grab-coordinates-of-the-table-you-want
    area: list[float] | None = Field(
        description="Area of page to look for table in.",
        default=None,
    )

    @property
    def page_table_index(self) -> int:
        """Zero-based index of the table on the page."""
        return self.page_table_number - 1
