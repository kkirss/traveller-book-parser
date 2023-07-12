from typing import Any

CREDIT = "Cr"
MEGA_CREDIT = "MCr"


def remove_credits_prefix(value: Any) -> Any:  # noqa: ANN401
    if isinstance(value, str):
        if value.startswith(MEGA_CREDIT):
            value = value.removeprefix(MEGA_CREDIT)
            value = float(value) * 1000000
        elif value.startswith(CREDIT):
            value = value.removeprefix(CREDIT)

        return value
    return value
