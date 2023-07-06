from pydantic import RootModel

from .base_weapon_trait import BaseWeaponTrait

WeaponTrait = RootModel[BaseWeaponTrait]
