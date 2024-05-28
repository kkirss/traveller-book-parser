from typing import Literal

from pydantic import Field

from traveller_book_parser.traveller_models.base_entity import BaseEntity
from traveller_book_parser.traveller_models.entity_types import EntityType


class BaseSkill(BaseEntity):
    """Skill with optional level."""

    entity_type: Literal[EntityType.SKILL] = EntityType.SKILL

    # None signifies not knowing a skill
    level: int | None = Field(repr=True)
