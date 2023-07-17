from typing import Any, Literal

from pydantic import field_validator

from traveller_models.validators import dash_is_zero, remove_credits_prefix
from traveller_models.validators.dashes import DASH_VALUES, dash_is_none

from .base_weapon import BaseWeapon, WeaponType

UNLIMITED_MAGAZINE_SIZE = "Unlimited"
UNLIMITED_LITERAL = Literal["Unlimited"]


class RangedWeapon(BaseWeapon):
    weapon_type: Literal[WeaponType.ranged] = WeaponType.ranged
    range: int | None

    magazine_size: int | UNLIMITED_LITERAL | None = None
    magazine_base_price: int | None = None  # In Credits

    @field_validator("magazine_size", mode="before")
    def magazine_size_range_max(
        cls: type["RangedWeapon"], value: Any  # noqa: N805,ANN401
    ) -> Any:  # noqa: ANN401
        if isinstance(value, str):
            for dash in DASH_VALUES:
                if dash in value:
                    return value.split(dash)[-1]
        return value

    magazine_size_dash = field_validator("magazine_size", mode="before")(dash_is_none)

    magazine_base_price_zero = field_validator("magazine_base_price", mode="before")(
        dash_is_zero
    )
    magazine_base_price_credits = field_validator("magazine_base_price", mode="before")(
        remove_credits_prefix
    )
