from typing import Any

INFINITE_VALUE = "∞"


def infinite_is_none(value: Any) -> Any:  # noqa: ANN401
    """Convert infinity string (∞) to None.

    >>> infinite_is_none("∞")

    """
    if isinstance(value, str) and value == INFINITE_VALUE:
        return None
    return value
