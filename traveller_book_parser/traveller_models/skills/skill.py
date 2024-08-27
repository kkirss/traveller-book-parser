from typing import Any, Literal, Optional

from pydantic import RootModel, Field

from traveller_book_parser.traveller_models.trav_object_base import TravObjectBase
from traveller_book_parser.traveller_models.trav_object_types import TravObjectType


class Skill(TravObjectBase):
    """Skill with optional level."""

    type: Literal[TravObjectType.SKILL] = TravObjectType.SKILL

    # None signifies not knowing a skill
    level: Optional[int] = Field(repr=True)


def create_skill(**kwargs: Any) -> Skill:  # noqa: ANN401
    """Create Skill model instance."""
    return Skill(**kwargs)
