from typing import Literal, Optional

from pydantic import Field

from traveller_book_parser.traveller_models.trav_object_base import TravObjectBase
from traveller_book_parser.traveller_models.trav_object_types import TravObjectType


class BaseSkill(TravObjectBase):
    """Skill with optional level."""

    type: Literal[TravObjectType.SKILL] = TravObjectType.SKILL

    # None signifies not knowing a skill
    level: Optional[int] = Field(repr=True)
