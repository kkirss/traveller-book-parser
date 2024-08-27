from decimal import Decimal
from typing import Any

from traveller_book_parser.traveller_models.items.armour import Armour
from traveller_book_parser.traveller_models.items.base_item import ItemType
from traveller_book_parser.traveller_models.items.item import create_item
from traveller_book_parser.traveller_models.items.weapons.base_weapon import WeaponType
from traveller_book_parser.traveller_models.items.weapons.melee_weapon import (
    MeleeWeapon,
)


def test_item_weapon_melee(melee_weapon_input_data: dict[str, Any]):
    model = create_item(**melee_weapon_input_data)

    assert {
        **melee_weapon_input_data,
        "item_type": ItemType.weapon,
        "weapon_type": WeaponType.melee,
        "weight": Decimal(0),
        "trav_id": "item:Dagger:TL:4:weapon:melee",
    } == model.model_dump(exclude_unset=True)
    assert isinstance(model, MeleeWeapon)


def test_item_armour(armour_input_data: dict[str, Any]):
    model = create_item(**armour_input_data)

    assert {
        **armour_input_data,
        "item_type": ItemType.armour,
        "weight": Decimal(5),
        "trav_id": "item:Cloth Armour:TL:8:armour",
    } == model.model_dump(exclude_unset=True)
    assert isinstance(model, Armour)
