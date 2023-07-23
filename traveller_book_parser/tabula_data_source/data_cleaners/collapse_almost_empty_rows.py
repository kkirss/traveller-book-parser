import logging

from pandas import DataFrame, Series

logger = logging.getLogger(__name__)


def _is_almost_empty_row(row: Series) -> bool:
    empty_count = sum(value == "" for value in row)
    row_size = len(row.index)
    return row_size / 2 < empty_count < row_size


def _has_almost_empty_rows(data_frame: DataFrame) -> bool:
    return any(_is_almost_empty_row(row) for _, row in data_frame.iterrows())


def collapse_almost_empty_rows(input_data_frame: DataFrame) -> DataFrame | None:
    data_frame = input_data_frame
    if not _has_almost_empty_rows(data_frame):
        return None

    new_rows = []

    for _, row in data_frame.iterrows():
        if _is_almost_empty_row(row):
            try:
                previous_row = new_rows.pop()
            except IndexError:
                logger.error(
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
