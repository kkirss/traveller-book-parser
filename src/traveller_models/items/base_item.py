from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field


class ItemType(str, Enum):
    armour = "Armour"
    augment = "Augment"
    tool = "Tool"
    weapon = "Weapon"


class BaseItem(BaseModel):
    name: str = Field(repr=True)
    description: str = ""

    tech_level: int = Field(repr=True, ge=0)
    weight: Decimal  # In kilograms
    base_price: int | None = None  # In Credits

    item_type: ItemType = Field(repr=True)
