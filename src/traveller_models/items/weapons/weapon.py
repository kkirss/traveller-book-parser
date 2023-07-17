from typing import Annotated

from pydantic import Field, TypeAdapter

from traveller_models.items.weapons.melee_weapon import MeleeWeapon
from traveller_models.items.weapons.ranged_weapon import RangedWeapon

Weapon = Annotated[MeleeWeapon | RangedWeapon, Field(discriminator="weapon_type")]
WeaponAdapter = TypeAdapter(Weapon)
