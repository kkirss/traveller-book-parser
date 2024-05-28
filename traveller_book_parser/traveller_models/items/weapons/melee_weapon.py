from typing import Literal

from .base_weapon import BaseWeapon, WeaponRangeMelee, WeaponType


class MeleeWeapon(BaseWeapon):
    """Melee weapon."""

    weapon_type: Literal[WeaponType.melee] = WeaponType.melee
    range: WeaponRangeMelee
