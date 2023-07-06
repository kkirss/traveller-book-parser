from decimal import Decimal

from traveller_models.items.armour import Armour
from traveller_models.items.base_item import ItemType
from traveller_models.items.item import get_item_model
from traveller_models.items.weapons.base_weapon import WeaponType
from traveller_models.items.weapons.melee_weapon import MeleeWeapon


def test_item_weapon_melee():
    input_data = {
        "item_type": "Weapon",
        "weapon_type": "Melee",
        "name": "Dagger",
        "tech_level": 4,
        "weight": 0,
        "range": "Melee",
        "damage": "2D",
    }

    model = get_item_model(**input_data)

    assert {
        **input_data,
        "item_type": ItemType.weapon,
        "weapon_type": WeaponType.melee,
        "weight": Decimal(0),
    } == model.model_dump(exclude_defaults=True)
    assert isinstance(model, MeleeWeapon)


def test_item_armour():
    input_data = {
        "item_type": "Armour",
        "name": "Cloth Armour",
        "tech_level": 8,
        "weight": 5,
        "protection": 8,
    }

    model = get_item_model(**input_data)

    assert {
        **input_data,
        "item_type": ItemType.armour,
        "weight": Decimal(5),
    } == model.model_dump(exclude_defaults=True)
    assert isinstance(model, Armour)
