from enum import Enum
from typing import Any

from pydantic import BaseModel, field_validator

from traveller_models.validators import remove_comma_separators


class WeaponTraitType(str, Enum):
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
    zero_g = "Zero-G"


class BaseWeaponTrait(BaseModel):
    weapon_trait_type: WeaponTraitType
    amount: int | None = None

    @field_validator("amount", mode="before")
    def amount_infinite(
        cls: type["BaseWeaponTrait"], value: Any  # noqa: N805,ANN401
    ) -> Any:  # noqa: ANN401
        if isinstance(value, str) and value == "∞":
            return None
        return value

    amount_separators = field_validator("amount", mode="before")(
        remove_comma_separators
    )
