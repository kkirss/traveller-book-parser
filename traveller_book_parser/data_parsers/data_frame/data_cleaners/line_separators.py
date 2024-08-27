from collections.abc import Iterable
import logging
from typing import Any, Optional

from pandas import DataFrame, Index, Series

logger = logging.getLogger(__name__)

SEPARATOR = "\r"  # Tabula uses return character as line separator


def _get_cells_with_return_count(series: Series | Index) -> int:
    return sum((isinstance(value, str)) and (SEPARATOR in value) for value in series)


def _replace_return_with_space(value: Any) -> Any:  # noqa: ANN401
    if isinstance(value, str):
        return value.replace(SEPARATOR, " ")
    return value


def replace_few_returns_with_spaces(input_data_frame: DataFrame) -> Optional[DataFrame]:
    """Replace return characters with spaces in a data frame.

    Returns are replaced if they occur in less than half of the cells.
    This is done because Tabula uses return character as line separator.
    """
    data_frame = input_data_frame
    columns = data_frame.columns
    has_updates = False

    values_with_return = _get_cells_with_return_count(columns)
    if 0 < values_with_return < len(columns) / 2:
        values = list(map(_replace_return_with_space, columns))
        data_frame.columns = values
        has_updates = True

    for row_index, row in data_frame.iterrows():
        values_with_return = _get_cells_with_return_count(row)
        if 0 < values_with_return < len(row) / 2:
            values = list(map(_replace_return_with_space, row))
            data_frame.iloc[row_index] = values
            has_updates = True

    if has_updates:
        return data_frame
    return None


def _get_return_counts_per_index(series: Series) -> dict[int, int]:
    return_counts = {}
    for column_index, value in enumerate(series):
        if isinstance(value, str):
            return_counts[column_index] = value.count(SEPARATOR)
        else:
            return_counts[column_index] = 0

    return return_counts


def _get_spread_by_return_rows_for_row(
    row: Series,
    column_return_counts: dict[int, int],
    return_count: int,
) -> Iterable[list]:
    for loc_index in range(return_count + 1):
        new_list = []
        for column_index, value in enumerate(row):
            if column_return_counts[column_index] > 0 and isinstance(value, str):
                new_value = value.split(SEPARATOR)[loc_index]
            else:
                new_value = value

            new_list.append(new_value)
        yield new_list


def spread_returns_to_multiple_rows(
    input_data_frame: DataFrame,
) -> Optional[DataFrame]:
    r"""Spread rows with most cells containing return characters to multiple rows.

    This is done because Tabula uses return character as line separator.

    Example:
    -------
    >>> spread_returns_to_multiple_rows(DataFrame([
    ...     ["a", "foo\rbar", "first\rsecond"],
    ... ]))
       0    1       2
    0  a  foo   first
    1  a  bar  second
    """
    data_frame = input_data_frame

    if not any(
        _get_cells_with_return_count(row) > len(row) / 2
        for _, row in data_frame.iterrows()
    ):
        return None

    new_rows = []

    for row_index in range(len(data_frame.index)):
        row: Series = data_frame.iloc[row_index]
        values_with_return = _get_cells_with_return_count(row)

        if values_with_return > len(row) / 2:
            column_return_counts = _get_return_counts_per_index(row)
            unique_return_counts = set(column_return_counts.values()) - {0}

            if len(unique_return_counts) == 1:
                return_count = next(iter(unique_return_counts))
                new_rows.extend(
                    _get_spread_by_return_rows_for_row(
                        row,
                        column_return_counts,
                        return_count,
                    ),
                )
                continue

            if len(unique_return_counts) > 1:
                logger.warning(
                    "Found row with mixed number of return characters (%s),"
                    " skipping: %s",
                    unique_return_counts,
                    row,
                )

        new_rows.append(row.values)

    return DataFrame(data=new_rows, columns=input_data_frame.columns)
