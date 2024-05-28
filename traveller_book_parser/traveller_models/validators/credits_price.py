from typing import Any

CREDIT = "Cr"
MEGA_CREDIT = "MCr"


def remove_credits_prefix(value: Any) -> Any:  # noqa: ANN401
    """Remove credits prefix, multiplying by size prefix if applicable.

    Example:
    --------
    >>> remove_credits_prefix("Cr10")
    '10'
    >>> remove_credits_prefix("MCr1.5")
    1500000.0
    """
    if isinstance(value, str):
        if value.startswith(MEGA_CREDIT):
            value = value.removeprefix(MEGA_CREDIT)
            value = float(value) * 1000000
        elif value.startswith(CREDIT):
            value = value.removeprefix(CREDIT)

        return value
    return value
