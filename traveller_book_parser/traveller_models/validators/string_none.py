from typing import Any


def string_none_is_none(value: Any) -> Any:  # noqa: ANN401
    """Convert string "None" to None."""
    if value == "None":
        return None
    return value
