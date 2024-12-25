from typing import Annotated, Any

from pydantic import Field, RootModel

from .characteristics.characteristic import Characteristic
from .characters.character import Character
from .items.item import Item
from .skills.skill import Skill

TRAV_OBJ_DESCRIPTION = """A traveller-related object.

Traveller objects are defined as different sub-models, using `type` field to differentiate them:
* `characteristic` - A characteristic of a character (e.g. strength).
* `item` - An item (e.g. sword, phone, book).
* `skill` - A skill (e.g. athletics, pilot, science).
* `character` - A character.

Each type of traveller object has its own fields. Different types may have further sub-types with further fields.
These are intended to be usable with any edition of Traveller. (But completely untested so Your Mileage May Vary.)

Run `traveller-book-parser schema TravObject` for the full JSON schema.
See [`traveller_book_parser/traveller_models/trav_object.py`](traveller_book_parser/traveller_models/trav_object.py) for the actual models.
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
