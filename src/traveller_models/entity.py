from typing import Annotated, Any

from pydantic import Field, RootModel

from .characteristics.characteristic import Characteristic
from .items.item import Item
from .skills.skill import Skill

Entity = Annotated[
    Characteristic | Item | Skill,
    Field(discriminator="entity_type"),
]


def get_entity_model(**kwargs: dict[str, Any]) -> Entity:
    return RootModel[Entity](**kwargs).root
