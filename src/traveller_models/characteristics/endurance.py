from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Endurance(BaseCharacteristic):
    characteristic_type: Literal[CharacteristicType.END] = CharacteristicType.END

    NAME: ClassVar[str] = "Endurance"
