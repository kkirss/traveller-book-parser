from typing import Annotated

from pydantic import Field

from traveller_book_parser.traveller_models.items.weapons.melee_weapon import (
    MeleeWeapon,
)
from traveller_book_parser.traveller_models.items.weapons.ranged_weapon import (
    RangedWeapon,
)

WeaponField = Field(
    title="Weapon",
    description="A weapon (e.g. sword, pistol).",
    discriminator="weapon_type",
)
Weapon = Annotated[MeleeWeapon | RangedWeapon, WeaponField]
