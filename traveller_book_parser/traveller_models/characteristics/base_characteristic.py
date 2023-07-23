from enum import Enum
from typing import ClassVar, Literal

from pydantic import Field, computed_field

from traveller_book_parser.traveller_models.base_entity import BaseEntity
from traveller_book_parser.traveller_models.entity_types import EntityType


class CharacteristicType(str, Enum):
    STR = "STR"
    DEX = "DEX"
    END = "END"

    INT = "INT"
    EDU = "EDU"
    SOC = "SOC"

    LCK = "LCK"
    INF = "INF"


class BaseCharacteristic(BaseEntity):
    entity_type: Literal[EntityType.CHARACTERISTIC] = EntityType.CHARACTERISTIC
    characteristic_type: CharacteristicType = Field(repr=True)

    level: int | None = Field(default=None, repr=True)

    NAME: ClassVar[str] = NotImplemented

    @computed_field
    @property
    def name(self) -> str:
        return self.NAME
