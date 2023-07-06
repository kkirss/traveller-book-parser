from typing import Literal

from pydantic import Field

from traveller_models.characteristics.characteristic import Characteristic
from traveller_models.skills.skill import Skill

from .base_item import BaseItem, ItemType


class Armour(BaseItem):
    item_type: Literal[ItemType.armour]

    protection: int
    protection_laser: int | None = None

    radiation_protection: int = 0
    required_skill: Skill | None = None

    characteristic_bonuses: list[Characteristic] = Field(default_factory=list)
