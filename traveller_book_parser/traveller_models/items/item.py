from typing import Annotated, Any

from pydantic import Field, RootModel

from .armour import Armour
from .weapons.weapon import Weapon

Item = Annotated[Armour | Weapon, Field(discriminator="item_type")]


def get_item_model(**kwargs: Any) -> Item:  # noqa: ANN401
    return RootModel[Item](**kwargs).root
