from typing import Any


def remove_asterisk(value: Any) -> Any:  # noqa: ANN401
    """Remove asterisk suffix from string.

    >>> remove_asterisk("10*")
    '10'
    """
    if isinstance(value, str) and value.endswith("*"):
        return value.removesuffix("*")
    return value
