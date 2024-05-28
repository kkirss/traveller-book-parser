from collections.abc import Generator
from contextlib import contextmanager
import logging
from pathlib import Path
from typing import Any, Literal, cast

import pdfplumber
from pdfplumber.page import Page
from typing_extensions import TypedDict

logger = logging.getLogger(__name__)

PDFPlumberTable = list[list[str | None]]


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


@contextmanager
def open_pdfplumber_page(
    pdf_path: Path, page_number: int
) -> Generator[Page, None, None]:
    with pdfplumber.open(pdf_path, pages=[page_number]) as pdf:
        yield pdf.pages[0]


def get_pdfplumber_table(
    pdf_path: Path,
    page_number: int,
    table_index: int = 0,
    table_settings: TableSettingsDict | None = None,
) -> PDFPlumberTable:
    if table_settings is None:
        table_settings = {}

    with open_pdfplumber_page(pdf_path, page_number) as page:
        tables = page.extract_tables(cast(dict[str, Any], table_settings))
        try:
            return tables[table_index]
        except IndexError as e:
            raise ValueError(f"No tables found on page {page_number}") from e
