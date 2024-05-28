from typing import Any

from .dashes import DASH_VALUES


def value_range_use_max(value: Any) -> Any:  # noqa: ANN401
    """Convert dash-separated range to its max value."""
    if isinstance(value, str):
        for dash in DASH_VALUES:
            if dash in value:
                return value.split(dash)[-1]
    return value
