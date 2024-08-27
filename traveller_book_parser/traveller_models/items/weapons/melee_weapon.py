from typing import Literal

from pydantic import Field

from .base_weapon import BaseWeapon, WeaponRangeMelee, WeaponType


class MeleeWeapon(BaseWeapon):
    """Melee weapon."""

    weapon_type: Literal[WeaponType.melee] = Field(repr=False, default=WeaponType.melee)
    range: WeaponRangeMelee
