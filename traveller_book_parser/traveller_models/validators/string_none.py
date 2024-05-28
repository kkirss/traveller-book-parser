from typing import Any


def string_none_is_none(value: Any) -> Any:  # noqa: ANN401
    """Convert string "None" to None.

    >>> string_none_is_none("None")

    >>> string_none_is_none(None)

    """
    if value == "None":
        return None
    return value
