from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Intellect(BaseCharacteristic):
    characteristic_type: Literal[CharacteristicType.INT
                                 ] = CharacteristicType.INT

    NAME: ClassVar[str] = "Intellect"
