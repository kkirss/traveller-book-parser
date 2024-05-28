from typing import Annotated, Any

from pydantic import Field, RootModel

from .armour import Armour
from .weapons.weapon import Weapon

Item = Annotated[Armour | Weapon, Field(discriminator="item_type")]


def create_item(**kwargs: Any) -> Item:  # noqa: ANN401
    """Create Item model instance."""
    return RootModel[Item](**kwargs).root
