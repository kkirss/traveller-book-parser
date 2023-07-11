from enum import Enum
from typing import Literal

from pydantic import Field

from traveller_models.items.base_item import BaseItem, ItemType

from .traits.weapon_trait import WeaponTrait

WEAPON_RANGE_MELEE = "Melee"
WeaponRangeMelee = Literal["Melee"]


class WeaponType(str, Enum):
    melee = "Melee"
    ranged = "Ranged"


class BaseWeapon(BaseItem):
    item_type: Literal[ItemType.weapon] = ItemType.weapon
    weapon_type: WeaponType

    range: WeaponRangeMelee | int
    damage: str
    traits: list[WeaponTrait] = Field(default_factory=list)
