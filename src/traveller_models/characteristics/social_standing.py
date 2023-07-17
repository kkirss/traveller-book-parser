from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class SocialStanding(BaseCharacteristic):
    characteristic_type: Literal[CharacteristicType.SOC] = CharacteristicType.SOC

    NAME: ClassVar[str] = "Social Standing"
