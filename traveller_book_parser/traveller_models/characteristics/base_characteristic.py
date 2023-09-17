from enum import Enum
from typing import Any, ClassVar, Literal

from pydantic import Field, model_validator

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

    @model_validator(mode="before")
    @classmethod
    def set_name_from_class(
        cls: type["BaseCharacteristic"],
        data: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        if isinstance(data, dict):
            data["name"] = cls.NAME
        return data
