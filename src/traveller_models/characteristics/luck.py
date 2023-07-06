from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Luck(BaseCharacteristic):
    type: Literal[CharacteristicType.LCK]

    NAME: ClassVar[str] = "Luck"
