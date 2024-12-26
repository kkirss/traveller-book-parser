from decimal import Decimal
from typing import Any

from traveller_book_parser.traveller_models.items.base_item import ItemType
from traveller_book_parser.traveller_models.items.weapons.base_weapon import WeaponType
from traveller_book_parser.traveller_models.items.weapons.melee_weapon import (
    MeleeWeapon,
)
from traveller_book_parser.traveller_models.trav_object import create_trav_object
from traveller_book_parser.traveller_models.trav_object_types import TravObjectType


def test_item_weapon_melee(melee_weapon_input_data: dict[str, Any]):
    model = create_trav_object(
        **{
            "type": "item",
            **melee_weapon_input_data,
        },
    )

    assert model.model_dump(exclude_unset=True) == {
        **melee_weapon_input_data,
        "type": TravObjectType.ITEM,
        "item_type": ItemType.weapon,
        "weapon_type": WeaponType.melee,
        "weight": Decimal(0),
        "trav_id": "item:Dagger:TL:4:weapon:melee",
    }
    assert isinstance(model, MeleeWeapon)
