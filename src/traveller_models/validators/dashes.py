from typing import Any

DASH_VALUES = ("-", "—")


def dash_is_zero(value: Any) -> Any:  # noqa: ANN401
    if value in DASH_VALUES:
        return 0
    return value


def dash_is_none(value: Any) -> Any:  # noqa: ANN401
    if value in DASH_VALUES:
        return None
    return value
