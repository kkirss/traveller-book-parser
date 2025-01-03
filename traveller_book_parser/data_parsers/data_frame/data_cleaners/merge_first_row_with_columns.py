from collections.abc import Hashable
from typing import Optional

from pandas import DataFrame


def merge_first_row_with_columns(input_data_frame: DataFrame) -> Optional[DataFrame]:
    """Merge the first row of a data frame with the columns.

    >>> merge_first_row_with_columns(DataFrame([
    ...     ["", "", "extra"],
    ...     ["a", "b", "c"],
    ... ], columns=["header1", "header2", "header"]))
      header1 header2 header extra
    1       a       b            c
    """
    data_frame = input_data_frame
    columns = data_frame.columns.to_list()

    first_row = data_frame.iloc[0].to_list()
    new_columns = [
        f"{column}{' ' if column and first_row_item else ''}{first_row_item}"
        for column, first_row_item in zip(columns, first_row, strict=True)
    ]

    data_frame.columns = new_columns

    drop_index = data_frame.index[0]
    if not isinstance(drop_index, Hashable):
        raise TypeError("No index to drop")  # noqa: TRY003

    return data_frame.drop(index=drop_index)
