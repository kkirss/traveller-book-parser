from typing import Literal

from description_models.base_data_source_description import BaseDataSourceDescription

from .pages_range import RangeList, get_pages_range_list

HTML_DATA_SOURCE_DESCRIPTION_TYPE = "html"
HTML_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL = Literal["html"]


class HTMLDataSourceDescription(BaseDataSourceDescription):
    """Description of getting data from HTML exported using pdftohtml."""

    type: HTML_DATA_SOURCE_DESCRIPTION_TYPE_LITERAL

    pages: str

    @property
    def pages_range_list(self) -> RangeList:
        return get_pages_range_list(self.pages)
