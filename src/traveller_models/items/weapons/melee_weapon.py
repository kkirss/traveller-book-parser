from typing import Literal

from .base_weapon import BaseWeapon, WeaponRangeMelee, WeaponType


class MeleeWeapon(BaseWeapon):
    weapon_type: Literal[WeaponType.melee]
    range: WeaponRangeMelee
