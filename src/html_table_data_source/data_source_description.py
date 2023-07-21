from typing import Literal

from html_data_source.data_source_description import HTMLDataSourceDescription

HTML_TABLE_DATA_SOURCE_DESCRIPTION_TYPE = "html-table"
HTML_TABLE_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL = Literal["html-table"]


class HTMLTableDataSourceDescription(HTMLDataSourceDescription):
    """Description of getting data from exported HTML table."""

    type: HTML_TABLE_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL
