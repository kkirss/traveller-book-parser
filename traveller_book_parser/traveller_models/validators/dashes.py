from typing import Any

DASH_VALUES = ("-", "\u2014", "\u2013")


def is_dash_value(value: Any) -> bool:  # noqa: ANN401
    """Check if value is a dash.

    >>> is_dash_value("-")
    True
    """
    return value in DASH_VALUES


def dash_is_zero(value: Any) -> Any:  # noqa: ANN401
    """Convert dash to 0.

    >>> dash_is_zero("-")
    0
    """
    if value in DASH_VALUES:
        return 0
    return value


def dash_is_none(value: Any) -> Any:  # noqa: ANN401
    """Convert dash to None.

    >>> dash_is_none("-")

    """
    if value in DASH_VALUES:
        return None
    return value
