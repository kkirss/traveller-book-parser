from typing import Any

import pytest


@pytest.fixture()
def melee_weapon_input_data() -> dict[str, Any]:
    return {
        "item_type": "weapon",
        "weapon_type": "melee",
        "name": "Dagger",
        "tech_level": 4,
        "weight": 0,
        "range": "Melee",
        "damage": "2D",
    }


@pytest.fixture()
def armour_input_data() -> dict[str, Any]:
    return {
        "item_type": "armour",
        "name": "Cloth Armour",
        "tech_level": 8,
        "weight": 5,
        "protection": 8,
    }
