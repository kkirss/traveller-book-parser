from typing import Annotated, Any

from pydantic import Field, RootModel

from .armour import Armour
from .weapons.weapon import Weapon

Item = Annotated[Armour | Weapon, Field(discriminator="item_type")]


def get_item_model(**kwargs: dict[str, Any]) -> Item:
    return RootModel[Item](**kwargs).root
