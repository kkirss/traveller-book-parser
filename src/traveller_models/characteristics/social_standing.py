from typing import ClassVar, Literal

from .base_characteristic import BaseCharacteristic, CharacteristicType


class SocialStanding(BaseCharacteristic):
    type: Literal[CharacteristicType.SOC]

    NAME: ClassVar[str] = "Social Standing"
