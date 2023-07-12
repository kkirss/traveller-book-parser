from typing import Literal

from pydantic import field_validator

from traveller_models.validators import dash_is_zero, remove_credits_prefix

from .base_weapon import BaseWeapon, WeaponType


class RangedWeapon(BaseWeapon):
    weapon_type: Literal[WeaponType.ranged] = WeaponType.ranged
    range: int | None

    magazine_size: int | None = None
    magazine_base_price: int | None = None  # In Credits

    magazine_base_price_zero = field_validator(
        "magazine_base_price", mode="before"
    )(dash_is_zero)
    magazine_base_price_credits = field_validator(
        "magazine_base_price", mode="before"
    )(remove_credits_prefix)
