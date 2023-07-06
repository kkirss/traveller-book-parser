from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Intellect(BaseCharacteristic):
    type: Literal[CharacteristicType.INT]

    NAME: ClassVar[str] = "Intellect"
