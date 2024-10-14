from typing import Any, Literal

from pydantic.v1 import Field

from traveller_book_parser.traveller_models.characteristics.characteristic import (
    Characteristic,
)
from traveller_book_parser.traveller_models.skills.skill import Skill
from traveller_book_parser.traveller_models.trav_object_base import TravObjectBase
from traveller_book_parser.traveller_models.trav_object_types import TravObjectType


class Character(TravObjectBase):
    """Character."""

    type: Literal[TravObjectType.CHARACTER] = Field(
        repr=False, default=TravObjectType.CHARACTER
    )

    characteristics: list[Characteristic] = Field(default_factory=list)
    skills: list[Skill] = Field(default_factory=list)


def create_character(**kwargs: Any) -> Character:  # noqa: ANN401
    """Create Character model instance."""
    return Character(**kwargs)
