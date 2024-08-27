from enum import Enum
from typing import Any, Literal, Optional

from pydantic import Field, model_validator

from traveller_book_parser.traveller_models.trav_object_base import TravObjectBase
from traveller_book_parser.traveller_models.trav_object_types import TravObjectType


class CharacteristicType(str, Enum):
    """Characteristic type."""

    STR = "STR"
    DEX = "DEX"
    END = "END"

    INT = "INT"
    EDU = "EDU"
    SOC = "SOC"

    LCK = "LCK"
    INF = "INF"


CHARACTERISTIC_NAMES: dict[CharacteristicType, str] = {
    CharacteristicType.STR: "Strength",
    CharacteristicType.DEX: "Dexterity",
    CharacteristicType.END: "Endurance",
    CharacteristicType.INT: "Intelligence",
    CharacteristicType.EDU: "Education",
    CharacteristicType.SOC: "Social",
    CharacteristicType.LCK: "Luck",
    CharacteristicType.INF: "Influence",
}


class Characteristic(TravObjectBase):
    """Characteristic with optional level."""

    type: Literal[TravObjectType.CHARACTERISTIC] = Field(
        repr=False, default=TravObjectType.CHARACTERISTIC
    )
    characteristic_type: CharacteristicType = Field(repr=True)

    level: Optional[int] = Field(default=None, repr=True)

    @model_validator(mode="before")
    @classmethod
    def set_default_name(
        cls: "type[Characteristic]",
        data: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        if "name" not in data and "characteristic_type" in data:
            data["name"] = CHARACTERISTIC_NAMES[data["characteristic_type"]]
        return data


def create_characteristic(**kwargs: Any) -> Characteristic:  # noqa: ANN401
    """Create Characteristic model instance."""
    return Characteristic(**kwargs)
