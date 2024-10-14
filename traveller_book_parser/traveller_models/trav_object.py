from typing import Annotated, Any

from pydantic import Field, RootModel

from .characteristics.characteristic import Characteristic
from .characters.character import Character
from .items.item import Item
from .skills.skill import Skill

TRAV_OBJ_DESCRIPTION = """A traveller-related object.

The `type: TravObjectType` signifies different types of traveller objects:
    * `characteristic` - An attribute of a character (e.g. strength).
    * `item` - An item (e.g. sword, phone, book).
    * `skill` - A skill (e.g. athletics, pilot, science).
    * `character` - A character.
"""

TravObjectField = Field(
    discriminator="type",
    title="TravObject",
    description=TRAV_OBJ_DESCRIPTION,
)
TravObject = Annotated[
    Character | Characteristic | Item | Skill,
    TravObjectField,
]


class TravObjectRoot(RootModel[TravObject]):  # noqa: D101
    ...


TravObject.__doc__ = TRAV_OBJ_DESCRIPTION
TravObjectRoot.__doc__ = TRAV_OBJ_DESCRIPTION


def create_trav_object(**kwargs: Any) -> TravObject:  # noqa: ANN401
    """Create TravObject model instance."""
    return RootModel[TravObject](**kwargs).root
