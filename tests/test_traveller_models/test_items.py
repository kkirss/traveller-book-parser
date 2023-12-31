from decimal import Decimal
from typing import Any

from traveller_book_parser.traveller_models.items.armour import Armour
from traveller_book_parser.traveller_models.items.base_item import ItemType
from traveller_book_parser.traveller_models.items.item import get_item_model
from traveller_book_parser.traveller_models.items.weapons.base_weapon import WeaponType
from traveller_book_parser.traveller_models.items.weapons.melee_weapon import (
    MeleeWeapon,
)


def test_item_weapon_melee(melee_weapon_input_data: dict[str, Any]):
    model = get_item_model(**melee_weapon_input_data)

    assert {
        **melee_weapon_input_data,
        "item_type": ItemType.weapon,
        "weapon_type": WeaponType.melee,
        "weight": Decimal(0),
    } == model.model_dump(exclude_unset=True)
    assert isinstance(model, MeleeWeapon)


def test_item_armour(armour_input_data: dict[str, Any]):
    model = get_item_model(**armour_input_data)

    assert {
        **armour_input_data,
        "item_type": ItemType.armour,
        "weight": Decimal(5),
    } == model.model_dump(exclude_unset=True)
    assert isinstance(model, Armour)
