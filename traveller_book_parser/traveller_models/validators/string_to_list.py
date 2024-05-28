from typing import Any


def comma_separated_string_to_list(value: Any) -> Any:  # noqa: ANN401
    """Convert comma+space-separated string to a list."""
    if isinstance(value, str):
        return value.split(", ")
    return value
