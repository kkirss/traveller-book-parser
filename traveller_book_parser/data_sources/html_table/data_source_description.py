from typing import Literal

from traveller_book_parser.data_sources.html.data_source_description import (
    HTMLDataSourceDescription,
)


class HTMLTableDataSourceDescription(HTMLDataSourceDescription):
    """Description of getting data from exported HTML table."""

    type: Literal["html-table"]
