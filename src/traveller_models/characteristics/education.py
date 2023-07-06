from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Education(BaseCharacteristic):
    type: Literal[CharacteristicType.EDU]

    NAME: ClassVar[str] = "Education"
