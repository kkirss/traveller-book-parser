from typing import Any

from .base_weapon_trait import BaseWeaponTrait

WeaponTrait = BaseWeaponTrait


def get_trait_model(**kwargs: Any) -> WeaponTrait:  # noqa: ANN401
    """Create WeaponTrait model instance."""
    return WeaponTrait(**kwargs)
