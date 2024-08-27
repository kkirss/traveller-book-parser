from typing import Annotated, Any

from pydantic import Field, RootModel

from .characteristics.characteristic import Characteristic
from .items.item import Item
from .skills.skill import Skill

TravObject = Annotated[
    Characteristic | Item | Skill,
    Field(discriminator="type"),
]


class TravObjectRoot(RootModel[TravObject]):
    """A traveller-related object.

    The `type: TravObjectType` signifies different types of traveller objects:
        * `characteristic` - An attribute of a character (e.g. strength).
        * `item` - An item (e.g. sword, phone, book).
        * `skill` - A skill (e.g. athletics, pilot, science).
    """


def create_trav_object(**kwargs: Any) -> TravObject:  # noqa: ANN401
    """Create TravObject model instance."""
    return RootModel[TravObject](**kwargs).root
