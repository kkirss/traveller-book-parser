from typing import Literal

from .base_weapon import BaseWeapon, WeaponType


class RangedWeapon(BaseWeapon):
    weapon_type: Literal[WeaponType.ranged] = WeaponType.ranged
    range: int

    magazine_size: int | None = None
    magazine_base_cost: int | None = None  # In Credits
