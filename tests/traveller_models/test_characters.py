from syrupy.assertion import SnapshotAssertion

from traveller_book_parser.traveller_models.characteristics.characteristic import (
    CharacteristicType,
)
from traveller_book_parser.traveller_models.characters.character import create_character


def test_character(snapshot: SnapshotAssertion):
    input_data = {
        "type": "character",
        "name": "John Doe",
        "characteristics": [
            {
                "characteristic_type": CharacteristicType.STR.value,
                "name": "Strength",
                "level": 7,
            },
            {
                "characteristic_type": CharacteristicType.DEX.value,
                "name": "Dexterity",
                "level": 5,
            },
        ],
        "skills": [{"name": "Admin", "level": 1}],
    }
    model = create_character(**input_data)

    assert model.model_dump(exclude_unset=True) == snapshot
    assert model.trav_id == "character:John Doe"


def test_character_with_colon_in_name(snapshot: SnapshotAssertion):
    input_data = {
        "type": "character",
        "name": "hello:world",
        "characteristics": [],
        "skills": [],
    }
    model = create_character(**input_data)

    assert model.model_dump(exclude_unset=True) == snapshot
    assert model.trav_id == "character:hello-world"
