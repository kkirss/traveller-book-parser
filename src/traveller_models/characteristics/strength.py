from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Strength(BaseCharacteristic):
    type: Literal[CharacteristicType.STR]

    NAME: ClassVar[str] = "Strength"
