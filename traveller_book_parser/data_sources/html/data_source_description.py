from traveller_book_parser.data_sources.base_data_source_description import (
    BaseDataSourceDescription,
)

from .pages_range import RangeList, get_pages_range_list


class HTMLDataSourceDescription(BaseDataSourceDescription):
    """Description of getting data from HTML exported using pdftohtml."""

    pages: str

    @property
    def pages_range_list(self) -> RangeList:
        """List of page ranges."""
        return get_pages_range_list(self.pages)
