from pandas import DataFrame

from traveller_book_parser.data_parsers.base_data_container import BaseDataContainer


class DataFrameDataContainer(BaseDataContainer):
    """Data container for a pandas DataFrame."""

    data: DataFrame
