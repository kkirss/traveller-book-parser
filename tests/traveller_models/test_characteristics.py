
from traveller_book_parser.traveller_models.characteristics.characteristic import (
    CharacteristicType,
    create_characteristic,
)


def test_characteristic():
    input_data = {
        "characteristic_type": CharacteristicType.STR.value,
        "name": "Strength",
    }
    model = create_characteristic(**input_data)

    assert {
        "characteristic_type": input_data["characteristic_type"],
        "name": input_data["name"],
    } == model.model_dump(exclude_unset=True)

    assert model.characteristic_type == input_data["characteristic_type"]
    assert model.name == input_data["name"]


def test_characteristic_custom_name():
    input_data = {
        "characteristic_type": CharacteristicType.STR.value,
        "name": "Custom Name",
    }
    model = create_characteristic(**input_data)

    assert {
        "characteristic_type": input_data["characteristic_type"],
        "name": input_data["name"],
    } == model.model_dump(exclude_unset=True)

    assert model.characteristic_type == input_data["characteristic_type"]
    assert model.name == input_data["name"]


def test_characteristic_default_name_dex():
    input_data = {
        "characteristic_type": CharacteristicType.DEX.value,
    }
    model = create_characteristic(**input_data)

    assert {
        "characteristic_type": input_data["characteristic_type"],
        "name": "Dexterity",
    } == model.model_dump(exclude_unset=True)

    assert model.characteristic_type == input_data["characteristic_type"]
    assert model.name == "Dexterity"
