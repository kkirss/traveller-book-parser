from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Influence(BaseCharacteristic):
    type: Literal[CharacteristicType.INF]

    NAME: ClassVar[str] = "Influence"
