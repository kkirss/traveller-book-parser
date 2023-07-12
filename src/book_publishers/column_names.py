from . import mongoose

# TODO: This might lead to clashes between publishers

COLUMN_TO_FIELD: dict[str, str] = {
    **mongoose.COLUMN_TO_FIELD,
}


def get_column_field_name(column_name: str) -> str:
    return COLUMN_TO_FIELD[column_name]
