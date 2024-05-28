from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Education(BaseCharacteristic):
    """Education characteristic."""

    characteristic_type: Literal[CharacteristicType.EDU] = CharacteristicType.EDU

    NAME: ClassVar[str] = "Education"
