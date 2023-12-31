from collections.abc import Hashable

from pandas import DataFrame


def merge_first_row_with_columns(input_data_frame: DataFrame) -> DataFrame | None:
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
        raise ValueError("No index to drop")

    data_frame = data_frame.drop(index=drop_index)
    return data_frame
