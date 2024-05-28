from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Luck(BaseCharacteristic):
    """Luck characteristic."""

    characteristic_type: Literal[CharacteristicType.LCK] = CharacteristicType.LCK

    NAME: ClassVar[str] = "Luck"
