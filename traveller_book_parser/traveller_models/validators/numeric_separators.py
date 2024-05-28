from typing import Any


def remove_commas(value: Any) -> Any:  # noqa: ANN401
    """Remove commas from string."""
    if isinstance(value, str) and "," in value:
        return value.replace(",", "")
    return value
