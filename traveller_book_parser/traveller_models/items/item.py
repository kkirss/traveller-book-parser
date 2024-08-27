from typing import Annotated, Any

from pydantic import Field, RootModel

from .armour import Armour
from .weapons.weapon import Weapon

ItemField = Field(
    title="Item",
    description="An item (e.g. sword, phone, book).",
    discriminator="item_type",
)
Item = Annotated[Armour | Weapon, ItemField]


class ItemRoot(RootModel[Item]):
    """An item (e.g. sword, phone, book)."""


def create_item(**kwargs: Any) -> Item:  # noqa: ANN401
    """Create Item model instance."""
    return RootModel[Item](**kwargs).root
