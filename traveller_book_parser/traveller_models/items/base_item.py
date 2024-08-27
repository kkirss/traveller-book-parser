from decimal import Decimal
from enum import Enum
from typing import Literal, Optional

from pydantic import Field, field_validator

from traveller_book_parser.traveller_models.trav_object_base import TravObjectBase
from traveller_book_parser.traveller_models.trav_object_types import TravObjectType
from traveller_book_parser.traveller_models.validators import (
    dash_is_zero,
    remove_asterisk,
    remove_credits_prefix,
)


class ItemType(str, Enum):
    """Item type."""

    armour = "armour"
    augment = "augment"
    tool = "tool"
    weapon = "weapon"


class BaseItem(TravObjectBase):
    """Item."""

    type: Literal[TravObjectType.ITEM] = TravObjectType.ITEM
    item_type: ItemType

    description: str = ""

    tech_level: int = Field(repr=True, ge=0)
    weight: Decimal  # In kilograms
    base_price: Optional[int] = None  # In Credits

    item_type: ItemType = Field(repr=True)

    # Validators
    weight_asterisk = field_validator("weight", mode="before")(remove_asterisk)
    weight_zero = field_validator("weight", mode="before")(dash_is_zero)

    base_price_zero = field_validator("base_price", mode="before")(dash_is_zero)
    base_price_credits = field_validator("base_price", mode="before")(
        remove_credits_prefix
    )
