from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from traveller_book_parser.data_sources.base_data_source_description import (
    BaseDataSourceDescription,
)

PDFPLUMBER_DATA_SOURCE_DESCRIPTION_TYPE = "pdfplumber-table"
PDFPLUMBER_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL = Literal["pdfplumber-table"]


TableStrategy = Literal["lines", "lines_strict", "text", "explicit"]


class TableSettingsDict(TypedDict, total=False):
    """Settings for table extraction, used by pdfplumber.

    See https://github.com/jsvine/pdfplumber/blob/stable/README.md#table-extraction-settings
    """

    vertical_strategy: TableStrategy
    horizontal_strategy: TableStrategy
    explicit_vertical_lines: list[float]
    explicit_horizontal_lines: list[float]
    snap_x_tolerance: float
    snap_y_tolerance: float
    join_x_tolerance: float
    join_y_tolerance: float
    min_words_vertical: int
    min_words_horizontal: int
    text_x_tolerance: float
    text_y_tolerance: float
    intersection_x_tolerance: float
    intersection_y_tolerance: float


class PDFPlumberDataSourceDescription(BaseDataSourceDescription):
    """Description of getting data using pdfplumber."""

    type: PDFPLUMBER_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL

    page: int
    page_table_number: int = Field(
        default=1,
        description="The sequential number of the table on the page.",
    )

    table_settings: TableSettingsDict | None = Field(
        default=None,
        description="Settings for table extraction, used by pdfplumber."
        "See https://github.com/jsvine/pdfplumber/blob/stable/README.md#table-extraction-settings",
    )

    @property
    def page_table_index(self) -> int:
        return self.page_table_number - 1


TABLE_SETTINGS_DEFAULTS: TableSettingsDict = {
    "vertical_strategy": "lines",
    "horizontal_strategy": "lines",
    "explicit_vertical_lines": [],
    "explicit_horizontal_lines": [],
    # "snap_tolerance": 3,
    "snap_x_tolerance": 3,
    "snap_y_tolerance": 3,
    # "join_tolerance": 3,
    "join_x_tolerance": 3,
    "join_y_tolerance": 3,
    # "edge_min_length": 3,
    "min_words_vertical": 3,
    "min_words_horizontal": 1,
    # "keep_blank_chars": False,
    # "text_tolerance": 3,
    "text_x_tolerance": 3,
    "text_y_tolerance": 3,
    # "intersection_tolerance": 3,
    "intersection_x_tolerance": 3,
    "intersection_y_tolerance": 3,
}
