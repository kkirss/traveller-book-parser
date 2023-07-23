from pandas import DataFrame


def remove_unnamed_columns(input_data_frame: DataFrame) -> DataFrame | None:
    data_frame = input_data_frame
    columns = data_frame.columns.to_list()

    unnamed_columns_count = 0
    for index, column in enumerate(columns):
        if "Unnamed: " in column:
            unnamed_columns_count += 1
            columns[index] = ""

    if unnamed_columns_count > (len(columns) / 2):
        first_row = data_frame.iloc[0].to_list()
        new_columns = [
            f"{column}{' ' if column else ''}{first_row_item}"
            for column, first_row_item in zip(columns, first_row, strict=True)
        ]

        data_frame.columns = new_columns
        data_frame = data_frame.drop(index=0)
        return data_frame
    return None
