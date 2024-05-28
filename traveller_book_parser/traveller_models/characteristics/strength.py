from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Strength(BaseCharacteristic):
    """Strength characteristic."""

    characteristic_type: Literal[CharacteristicType.STR] = CharacteristicType.STR

    NAME: ClassVar[str] = "Strength"
