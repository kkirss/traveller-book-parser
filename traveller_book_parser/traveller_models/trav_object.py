from typing import Annotated, Any

from pydantic import Field, RootModel

from .characteristics.characteristic import Characteristic
from .items.item import Item
from .skills.skill import Skill

TravObject = Annotated[
    Characteristic | Item | Skill,
    Field(discriminator="type"),
]


def create_trav_object(**kwargs: Any) -> TravObject:  # noqa: ANN401
    """Create TravObject model instance."""
    return RootModel[TravObject](**kwargs).root
