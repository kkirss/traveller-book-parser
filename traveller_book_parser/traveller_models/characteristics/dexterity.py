from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Dexterity(BaseCharacteristic):
    """Dexterity characteristic."""

    characteristic_type: Literal[CharacteristicType.DEX] = CharacteristicType.DEX

    NAME: ClassVar[str] = "Dexterity"
