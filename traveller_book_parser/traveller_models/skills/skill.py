from typing import Any, Literal, Optional

from pydantic import Field

from traveller_book_parser.traveller_models.trav_object_base import TravObjectBase
from traveller_book_parser.traveller_models.trav_object_types import TravObjectType


class Skill(TravObjectBase):
    """Skill with optional level."""

    type: Literal[TravObjectType.SKILL] = Field(
        repr=False, default=TravObjectType.SKILL
    )

    # None signifies not knowing a skill
    level: Optional[int] = Field(repr=True)

    def _get_trav_id_pieces(self) -> list[str | int | None]:
        return [*super()._get_trav_id_pieces(), self.level]


def create_skill(**kwargs: Any) -> Skill:  # noqa: ANN401
    """Create Skill model instance."""
    return Skill(**kwargs)
