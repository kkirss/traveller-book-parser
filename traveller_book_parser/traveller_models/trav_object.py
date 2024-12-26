from typing import Annotated, Any

from pydantic import Field, RootModel, TypeAdapter

from .characteristics.characteristic import Characteristic
from .characters.character import Character
from .items.item import Item
from .skills.skill import Skill

TRAV_OBJ_DESCRIPTION = """A traveller-related object."""

TravObjectField = Field(
    discriminator="type",
    title="TravObject",
    description=TRAV_OBJ_DESCRIPTION,
)
TravObject = Annotated[
    Character | Characteristic | Item | Skill,
    TravObjectField,
]

TravObject.__doc__ = TRAV_OBJ_DESCRIPTION


class TravObjectRoot(RootModel[TravObject]):
    """A traveller-related object."""


def create_trav_object(**kwargs: Any) -> TravObject:  # noqa: ANN401
    """Create TravObject model instance."""
    return TypeAdapter(TravObject).validate_python(kwargs)
