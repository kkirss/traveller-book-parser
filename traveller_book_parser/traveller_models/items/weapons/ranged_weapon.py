from typing import Literal, Optional

from pydantic import Field, field_validator

from traveller_book_parser.traveller_models.validators import (
    dash_is_none,
    dash_is_zero,
    remove_credits_prefix,
    value_range_use_max,
)

from .base_weapon import BaseWeapon, WeaponType

UNLIMITED_MAGAZINE_SIZE = "Unlimited"
UNLIMITED_LITERAL = Literal["Unlimited"]


class RangedWeapon(BaseWeapon):
    """Ranged weapon."""

    weapon_type: Literal[WeaponType.ranged] = Field(
        repr=False, default=WeaponType.ranged
    )
    range: Optional[float]

    magazine_size: Optional[int | UNLIMITED_LITERAL] = None
    magazine_base_price: Optional[float] = None  # In Credits

    magazine_size_range_max = field_validator("magazine_size", mode="before")(
        value_range_use_max
    )
    magazine_size_dash = field_validator("magazine_size", mode="before")(dash_is_none)

    magazine_base_price_zero = field_validator("magazine_base_price", mode="before")(
        dash_is_zero
    )
    magazine_base_price_credits = field_validator("magazine_base_price", mode="before")(
        remove_credits_prefix
    )
