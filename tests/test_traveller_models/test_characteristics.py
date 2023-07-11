from typing import Any

from traveller_models.characteristics.base_characteristic import CharacteristicType
from traveller_models.characteristics.characteristic import get_characteristic_model
from traveller_models.characteristics.strength import Strength


def test_characteristic(characteristic_input_data: dict[str, Any]):
    model = get_characteristic_model(**characteristic_input_data)

    assert {
        **characteristic_input_data,
        "characteristic_type": CharacteristicType.STR,
        "name": "Strength",
    } == model.model_dump(exclude_defaults=True)
    assert isinstance(model, Strength)
