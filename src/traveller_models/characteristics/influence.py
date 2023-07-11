from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Influence(BaseCharacteristic):
    characteristic_type: Literal[CharacteristicType.INF]

    NAME: ClassVar[str] = "Influence"
