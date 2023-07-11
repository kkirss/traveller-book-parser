from traveller_models.characteristics.base_characteristic import CharacteristicType
from traveller_models.characteristics.characteristic import get_characteristic_model
from traveller_models.characteristics.strength import Strength


def test_characteristic():
    input_data = {
        "characteristic_type": "STR",
        "level": 3,
    }

    model = get_characteristic_model(**input_data)

    assert {
        **input_data,
        "characteristic_type": CharacteristicType.STR,
        "name": "Strength",
    } == model.model_dump(exclude_defaults=True)
    assert isinstance(model, Strength)
