from decimal import Decimal
from enum import Enum
from typing import Any, Literal

from pydantic import Field, field_validator

from traveller_models.base_entity import BaseEntity
from traveller_models.entity_types import EntityType
from traveller_models.validators import dash_is_zero, remove_asterisk


class ItemType(str, Enum):
    armour = "armour"
    augment = "augment"
    tool = "tool"
    weapon = "weapon"


class BaseItem(BaseEntity):
    entity_type: Literal[EntityType.ITEM] = EntityType.ITEM
    item_type: ItemType

    name: str = Field(repr=True)
    description: str = ""

    tech_level: int = Field(repr=True, ge=0)
    weight: Decimal  # In kilograms
    base_price: int | None = None  # In Credits

    item_type: ItemType = Field(repr=True)

    # Validators
    weight_asterisk = field_validator("weight", mode="before")(remove_asterisk)
    weight_zero = field_validator("weight", mode="before")(dash_is_zero)

    base_price_zero = field_validator("base_price",
                                      mode="before")(dash_is_zero)

    @field_validator("base_price", mode="before")
    def base_price_credits(
        cls: type["BaseItem"],  # noqa: N805
        value: Any,  # noqa: ANN401
    ) -> Any:  # noqa: ANN401
        if isinstance(value, str):
            if value.startswith("MCr"):
                value = value.removeprefix("MCr")
                value = float(value) * 1000000
            elif value.startswith("Cr"):
                value = value.removeprefix("Cr")

            return value
        return value
