from enum import Enum
from typing import Optional

from pydantic import BaseModel, field_validator

from traveller_book_parser.traveller_models.validators import (
    infinite_is_none,
    remove_commas,
)


class WeaponTraitType(str, Enum):
    """Weapon trait type."""

    armor_piercing = "AP"
    artillery = "Artillery"
    auto = "Auto"
    blast = "Blast"
    bulky = "Bulky"
    very_bulky = "Very Bulky"
    dangerous = "Dangerous"
    very_dangerous = "Very Dangerous"
    fire = "Fire"
    one_use = "One Use"
    one_shot = "One Shot"
    radiation = "Radiation"
    scope = "Scope"
    silent = "Silent"
    smart = "Smart"
    smasher = "Smasher"
    stun = "Stun"
    special = "Special"
    zero_g = "Zero-G"


class BaseWeaponTrait(BaseModel):
    """Trait of a weapon with optional amount."""

    weapon_trait_type: WeaponTraitType
    amount: Optional[int] = None

    amount_infinite_is_none = field_validator("amount", mode="before")(infinite_is_none)
    amount_separators = field_validator("amount", mode="before")(remove_commas)
