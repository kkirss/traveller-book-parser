from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class Influence(BaseCharacteristic):
    """Influence characteristic."""

    characteristic_type: Literal[CharacteristicType.INF] = CharacteristicType.INF

    NAME: ClassVar[str] = "Influence"
