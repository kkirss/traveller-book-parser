from collections.abc import Generator
from contextlib import contextmanager
import logging
from pathlib import Path
from typing import Any, cast

import pdfplumber
from pdfplumber.page import Page

from traveller_book_parser.data_sources.pdfplumber.data_source_description import (
    TableSettingsDict,
)

logger = logging.getLogger(__name__)

PDFPlumberTable = list[list[str | None]]


def get_pdfplumber_page(
    pdf_path: Path,
    page_number: int,
) -> Page:
    pdf = pdfplumber.open(pdf_path, pages=[page_number])
    return pdf.pages[0]


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
        page.to_image()
        tables = page.extract_tables(cast(dict[str, Any], table_settings))
        try:
            return tables[table_index]
        except IndexError as e:
            raise ValueError(f"No tables found on page {page_number}") from e
