from typing import Any


def remove_commas(value: Any) -> Any:  # noqa: ANN401
    """Remove commas from string.

    >>> remove_commas("1,000,000")
    '1000000'
    """
    if isinstance(value, str) and "," in value:
        return value.replace(",", "")
    return value
