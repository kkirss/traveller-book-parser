from typing import Literal

from description_models.base_data_source_description import BaseDataSourceDescription
from pydantic import Field

HTML_TABLE_DATA_SOURCE_DESCRIPTION_TYPE = "html-table"
HTML_TABLE_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL = Literal["html-table"]


class HTMLTableDataSourceDescription(BaseDataSourceDescription):
    """Description of getting data from exported HTML table."""

    type: HTML_TABLE_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL

    page: int
    page_table_number: int = Field(
        default=1,
        description="The sequential number of the table on the page.",
    )
