from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Dexterity(BaseCharacteristic):
    type: Literal[CharacteristicType.DEX]

    NAME: ClassVar[str] = "Dexterity"
