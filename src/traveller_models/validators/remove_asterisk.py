from typing import Any


def remove_asterisk(value: Any) -> Any:  # noqa: ANN401
    if isinstance(value, str) and value.endswith("*"):
        return value.removesuffix("*")
    return value
