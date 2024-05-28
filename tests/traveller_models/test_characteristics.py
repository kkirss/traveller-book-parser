from typing import Any

from traveller_book_parser.traveller_models.characteristics.base_characteristic import (
    CharacteristicType,
)
from traveller_book_parser.traveller_models.characteristics.characteristic import (
    create_characteristic,
)
from traveller_book_parser.traveller_models.characteristics.strength import Strength


def test_characteristic(characteristic_input_data: dict[str, Any]):
    model = create_characteristic(**characteristic_input_data)

    assert {
        **characteristic_input_data,
        "characteristic_type": CharacteristicType.STR,
        "name": "Strength",
    } == model.model_dump(exclude_unset=True)
    assert isinstance(model, Strength)
