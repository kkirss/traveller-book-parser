from typing import Any

import pytest


@pytest.fixture
def characteristic_input_data() -> dict[str, Any]:
    return {
        "characteristic_type": "STR",
        "level": 3,
    }


@pytest.fixture
def melee_weapon_input_data() -> dict[str, Any]:
    return {
        "item_type": "Weapon",
        "weapon_type": "melee",
        "name": "Dagger",
        "tech_level": 4,
        "weight": 0,
        "range": "Melee",
        "damage": "2D",
    }


@pytest.fixture
def armour_input_data() -> dict[str, Any]:
    return {
        "item_type": "Armour",
        "name": "Cloth Armour",
        "tech_level": 8,
        "weight": 5,
        "protection": 8,
    }
