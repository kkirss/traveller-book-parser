from enum import Enum
from typing import Literal

from pydantic import Field, field_validator

from traveller_models.items.base_item import BaseItem, ItemType
from traveller_models.validators import dash_is_none

from .traits.weapon_trait import WeaponTrait

WEAPON_RANGE_MELEE = "Melee"
WeaponRangeMelee = Literal["Melee"]


class WeaponType(str, Enum):
    melee = "melee"
    ranged = "ranged"


class BaseWeapon(BaseItem):
    item_type: Literal[ItemType.weapon] = ItemType.weapon
    weapon_type: WeaponType

    range: WeaponRangeMelee | int | None
    damage: str
    traits: list[WeaponTrait] | None = Field(default_factory=list)

    # Validators
    range_none = field_validator("range", mode="before")(dash_is_none)
