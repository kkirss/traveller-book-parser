from typing import Any

from .base_weapon_trait import BaseWeaponTrait

WeaponTrait = BaseWeaponTrait


def create_weapon_trait(**kwargs: Any) -> WeaponTrait:  # noqa: ANN401
    """Create WeaponTrait model instance."""
    return WeaponTrait(**kwargs)
