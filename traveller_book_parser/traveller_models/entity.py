from typing import Annotated, Any

from pydantic import Field, RootModel

from .characteristics.characteristic import Characteristic
from .items.item import Item
from .skills.skill import Skill

Entity = Annotated[
    Characteristic | Item | Skill,
    Field(discriminator="entity_type"),
]


def create_entity(**kwargs: Any) -> Entity:  # noqa: ANN401
    """Create Entity model instance."""
    return RootModel[Entity](**kwargs).root
