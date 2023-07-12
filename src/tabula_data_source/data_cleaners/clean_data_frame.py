import logging

from pandas import DataFrame

from .line_separators import (
    replace_few_returns_with_spaces,
    spread_returns_to_multiple_rows,
)
from .unnamed_columns import remove_unnamed_columns

logger = logging.getLogger(__name__)


def clean_data_frame(input_data_frame: DataFrame) -> DataFrame:
    data_frame = input_data_frame

    data_frame = data_frame.fillna("")

    while True:
        if (new_data_frame := remove_unnamed_columns(data_frame)) is not None:
            data_frame = new_data_frame
            continue

        if (
            new_data_frame := spread_returns_to_multiple_rows(data_frame)
        ) is not None:
            data_frame = new_data_frame
            continue

        data_frame = replace_few_returns_with_spaces(data_frame)

        return data_frame
