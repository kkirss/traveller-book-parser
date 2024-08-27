from enum import Enum
from typing import Literal, Optional

from pydantic import Field, field_validator

from traveller_book_parser.traveller_models.items.base_item import BaseItem, ItemType
from traveller_book_parser.traveller_models.validators import (
    comma_separated_string_to_list,
    dash_is_none,
)

from .traits.traits_from_list import traits_from_list
from .traits.weapon_trait import WeaponTrait

WEAPON_RANGE_MELEE = "Melee"
WeaponRangeMelee = Literal["Melee"]


class WeaponType(str, Enum):
    """Weapon type."""

    melee = "melee"
    ranged = "ranged"


class BaseWeapon(BaseItem):
    """Weapon."""

    item_type: Literal[ItemType.weapon] = Field(repr=False, default=ItemType.weapon)
    weapon_type: WeaponType

    range: WeaponRangeMelee | Optional[int]
    damage: str
    traits: list[WeaponTrait] | None = Field(default_factory=list)

    # Validators
    range_none = field_validator("range", mode="before")(dash_is_none)

    traits_from_list = field_validator("traits", mode="before")(traits_from_list)
    traits_string_to_list = field_validator("traits", mode="before")(
        comma_separated_string_to_list
    )
    traits_none = field_validator("traits", mode="before")(dash_is_none)

    def _get_trav_id_pieces(self) -> list[str | int | None]:
        return [*super()._get_trav_id_pieces(), self.weapon_type.value]
