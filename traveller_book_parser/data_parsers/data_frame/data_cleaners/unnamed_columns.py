from pandas import DataFrame

from .merge_first_row_with_columns import merge_first_row_with_columns


def is_unnamed_column(column: str) -> bool:
    """Check if a column is unnamed."""
    return isinstance(column, int) or "Unnamed: " in column or column == ""


def remove_unnamed_columns(input_data_frame: DataFrame) -> DataFrame | None:
    """Remove unnamed columns from a data frame.

    Example:
    -------
    >>> remove_unnamed_columns(DataFrame([
    ...     ["foo", "bar", "world"],
    ...     ["x", "y", "z"],
    ...     ], columns=["Unnamed: 1", "", "c"]))
      foo bar c world
    1   x   y       z
    >>> remove_unnamed_columns(DataFrame([
    ...     ["foo", "bar", "hello"],
    ...     ], columns=["Unnamed: 1", "b", "c"]))
    """
    data_frame = input_data_frame
    columns = data_frame.columns.to_list()

    unnamed_columns_count = 0
    for index, column in enumerate(columns):
        if is_unnamed_column(column):
            unnamed_columns_count += 1
            columns[index] = ""

    if unnamed_columns_count > (len(columns) / 2):
        data_frame.columns = columns
        return merge_first_row_with_columns(data_frame)
    return None
