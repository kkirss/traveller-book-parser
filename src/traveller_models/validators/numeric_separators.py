from typing import Any


def remove_comma_separators(value: Any) -> Any:  # noqa: ANN401
    if isinstance(value, str) and "," in value:
        return value.replace(",", "")
    return value
