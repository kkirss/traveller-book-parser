from decimal import Decimal
from typing import Any

from traveller_book_parser.traveller_models.items.armour import Armour
from traveller_book_parser.traveller_models.items.base_item import ItemType
from traveller_book_parser.traveller_models.items.item import create_item
from traveller_book_parser.traveller_models.items.weapons.base_weapon import WeaponType
from traveller_book_parser.traveller_models.items.weapons.melee_weapon import (
    MeleeWeapon,
)
from traveller_book_parser.traveller_models.items.weapons.ranged_weapon import (
    RangedWeapon,
)
from traveller_book_parser.traveller_models.items.weapons.traits.base_weapon_trait import (
    WeaponTraitType,
)


def test_item_weapon_melee(melee_weapon_input_data: dict[str, Any]):
    model = create_item(**melee_weapon_input_data)

    assert model.model_dump(exclude_unset=True) == {
        **melee_weapon_input_data,
        "item_type": ItemType.weapon,
        "weapon_type": WeaponType.melee,
        "weight": Decimal(0),
        "trav_id": "item:Dagger:TL:4:weapon:melee",
    }
    assert isinstance(model, MeleeWeapon)


def test_item_weapon_ranged():
    ranged_weapon_input_data: dict[str, Any] = {
        "item_type": "weapon",
        "weapon_type": "ranged",
        "name": "Maser Pistol",
        "tech_level": 17.0,
        "range": 20.0,
        "damage": "3D+3",
        "weight": "2",
        "base_price": "Cr25000",
        "magazine_size": "12",
        "magazine_base_price": "—",
        "traits": "AP 10, Zero-G",
    }

    model = create_item(**ranged_weapon_input_data)
    result = model.model_dump(exclude_unset=True)

    assert result == {
        **ranged_weapon_input_data,
        "item_type": ItemType.weapon,
        "weapon_type": WeaponType.ranged,
        "tech_level": 17,
        "range": 20.0,
        "weight": 2.0,
        "base_price": 25000.0,
        "magazine_size": 12,
        "magazine_base_price": 0.0,
        "traits": [
            {"amount": 10, "weapon_trait_type": WeaponTraitType.armor_piercing},
            {"weapon_trait_type": WeaponTraitType.zero_g},
        ],
        "trav_id": "item:Maser Pistol:TL:17:weapon:ranged",
    }
    assert isinstance(model, RangedWeapon)


def test_item_armour(armour_input_data: dict[str, Any]):
    model = create_item(**armour_input_data)

    assert model.model_dump(exclude_unset=True) == {
        **armour_input_data,
        "item_type": ItemType.armour,
        "weight": Decimal(5),
        "trav_id": "item:Cloth Armour:TL:8:armour",
    }
    assert isinstance(model, Armour)
