from decimal import Decimal
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field

from traveller_models.entity_types import EntityType


class ItemType(str, Enum):
    armour = "armour"
    augment = "augment"
    tool = "tool"
    weapon = "weapon"


class BaseItem(BaseModel):
    entity_type: Literal[EntityType.ITEM] = EntityType.ITEM
    item_type: ItemType

    name: str = Field(repr=True)
    description: str = ""

    tech_level: int = Field(repr=True, ge=0)
    weight: Decimal  # In kilograms
    base_price: int | None = None  # In Credits

    item_type: ItemType = Field(repr=True)
