from decimal import Decimal
from typing import Any

from traveller_book_parser.traveller_models.entity import get_entity_model
from traveller_book_parser.traveller_models.entity_types import EntityType
from traveller_book_parser.traveller_models.items.base_item import ItemType
from traveller_book_parser.traveller_models.items.weapons.base_weapon import WeaponType
from traveller_book_parser.traveller_models.items.weapons.melee_weapon import (
    MeleeWeapon,
)


def test_entity_item_weapon_melee(melee_weapon_input_data: dict[str, Any]):
    model = get_entity_model(
        **{
            "entity_type": "item",
            **melee_weapon_input_data,
        },
    )

    assert {
        **melee_weapon_input_data,
        "entity_type": EntityType.ITEM,
        "item_type": ItemType.weapon,
        "weapon_type": WeaponType.melee,
        "weight": Decimal(0),
    } == model.model_dump(exclude_unset=True)
    assert isinstance(model, MeleeWeapon)
