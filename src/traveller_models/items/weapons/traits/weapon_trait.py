from typing import Any

from .base_weapon_trait import BaseWeaponTrait

WeaponTrait = BaseWeaponTrait


def get_trait_model(**kwargs: dict[str, Any]) -> WeaponTrait:
    return WeaponTrait(**kwargs)
