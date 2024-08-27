import logging
from typing import Optional

from pandas import DataFrame, Series

from .merge_first_row_with_columns import merge_first_row_with_columns

logger = logging.getLogger(__name__)


def _is_almost_empty_row(row: Series) -> bool:
    empty_count = sum(value == "" for value in row)
    row_size = len(row.index)
    return row_size / 2 < empty_count < row_size


def _has_almost_empty_rows(data_frame: DataFrame) -> bool:
    return any(_is_almost_empty_row(row) for _, row in data_frame.iterrows())


def collapse_almost_empty_rows(input_data_frame: DataFrame) -> Optional[DataFrame]:
    """Collapse almost empty rows into full rows in a data frame.

    Each almost empty row is merged into the previous row.
    Merging of values is done as concatenation with a space separator.

    Returns None if:
    - there are no almost empty rows in the data frame.
    - the first row is almost empty.

    Example:
    -------
    >>> collapse_almost_empty_rows(DataFrame([
    ...     ["a", "foo", "hello"],
    ...     ["b", "", ""],
    ...     ["c", "", ""]]))
           0    1      2
    0  a b c  foo  hello
    """
    data_frame = input_data_frame
    if not _has_almost_empty_rows(data_frame):
        return None

    first_row = data_frame.iloc[0]
    if _is_almost_empty_row(first_row):
        return merge_first_row_with_columns(data_frame)

    new_rows = []

    for _, row in data_frame.iterrows():
        if _is_almost_empty_row(row):
            try:
                previous_row = new_rows.pop()
            except IndexError:
                # This should be prevented by the above first_row check
                logger.warning(
                    "Found almost empty row as the first row, skipping clean:\n%s", row
                )
                return None

            replace_row = []
            for previous_value, new_value in zip(previous_row, row.values, strict=True):
                if new_value != "":
                    if isinstance(previous_value, str) and isinstance(new_value, str):
                        value = f"{previous_value} {new_value}"
                    else:
                        logger.warning(
                            "Found almost empty row with non-string data, using"
                            " previous: %s + %s",
                            previous_value,
                            new_value,
                        )
                        value = previous_value
                else:
                    value = previous_value
                replace_row.append(value)
            new_rows.append(replace_row)
        else:
            new_rows.append(row.values)

    return DataFrame(data=new_rows, columns=input_data_frame.columns)
