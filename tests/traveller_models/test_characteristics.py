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

    assert model.model_dump(exclude_unset=True) == {
        "characteristic_type": input_data["characteristic_type"],
        "name": input_data["name"],
        "trav_id": "characteristic:Strength",
    }

    assert model.characteristic_type == input_data["characteristic_type"]
    assert model.name == input_data["name"]


def test_characteristic_with_level():
    input_data = {
        "characteristic_type": CharacteristicType.STR.value,
        "name": "Strength",
        "level": 9001,
    }
    model = create_characteristic(**input_data)

    assert model.model_dump(exclude_unset=True) == {
        "characteristic_type": input_data["characteristic_type"],
        "name": input_data["name"],
        "level": input_data["level"],
        "trav_id": "characteristic:Strength",
    }

    assert model.characteristic_type == input_data["characteristic_type"]
    assert model.name == input_data["name"]


def test_characteristic_custom_name():
    input_data = {
        "characteristic_type": CharacteristicType.STR.value,
        "name": "Custom Name",
    }
    model = create_characteristic(**input_data)

    assert model.model_dump(exclude_unset=True) == {
        "characteristic_type": input_data["characteristic_type"],
        "name": input_data["name"],
        "trav_id": "characteristic:Custom Name",
    }

    assert model.characteristic_type == input_data["characteristic_type"]
    assert model.name == input_data["name"]


def test_characteristic_default_name_dex():
    input_data = {
        "characteristic_type": CharacteristicType.DEX.value,
    }
    model = create_characteristic(**input_data)

    assert model.model_dump(exclude_unset=True) == {
        "characteristic_type": input_data["characteristic_type"],
        "name": "Dexterity",
        "trav_id": "characteristic:Dexterity",
    }

    assert model.characteristic_type == input_data["characteristic_type"]
    assert model.name == "Dexterity"
