from typing import Literal, Optional

from pydantic import Field

from traveller_book_parser.data_sources.base_data_source_description import (
    BaseDataSourceDescription,
)

from .pdfplumber_integration import TableSettingsDict

PDFPLUMBER_DATA_SOURCE_DESCRIPTION_TYPE = "pdfplumber-table"
PDFPLUMBER_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL = Literal["pdfplumber-table"]


class PDFPlumberDataSourceDescription(BaseDataSourceDescription):
    """Description of getting data using pdfplumber."""

    type: PDFPLUMBER_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL

    page: int
    page_table_number: int = Field(
        default=1,
        description="The sequential number of the table on the page.",
    )

    table_settings: Optional[TableSettingsDict] = Field(
        default=None,
        description="Settings for table extraction, used by pdfplumber."
        "See https://github.com/jsvine/pdfplumber/blob/stable/README.md#table-extraction-settings",
    )

    @property
    def page_table_index(self) -> int:
        """Zero-based index of the table on the page."""
        return self.page_table_number - 1
