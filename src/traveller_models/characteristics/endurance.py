from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Endurance(BaseCharacteristic):
    type: Literal[CharacteristicType.END]

    NAME: ClassVar[str] = "Endurance"
