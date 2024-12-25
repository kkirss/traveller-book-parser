from typing import Any

CREDIT = "Cr"
MEGA_CREDIT = "MCr"


def remove_credits_prefix(value: Any) -> Any:  # noqa: ANN401
    """Remove credits prefix, multiplying by size prefix if applicable.

    Example:
    --------
    >>> remove_credits_prefix("Cr10")
    10.0
    >>> remove_credits_prefix("MCr1.5")
    1500000.0
    """
    if isinstance(value, str):
        if value.startswith(MEGA_CREDIT):
            value = float(value.removeprefix(MEGA_CREDIT)) * 1000000
        elif value.startswith(CREDIT):
            value = float(value.removeprefix(CREDIT))
        else:
            return float(value)
    return value
