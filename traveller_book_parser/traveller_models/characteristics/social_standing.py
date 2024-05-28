from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class SocialStanding(BaseCharacteristic):
    """Social Standing characteristic."""

    characteristic_type: Literal[CharacteristicType.SOC] = CharacteristicType.SOC

    NAME: ClassVar[str] = "Social Standing"
