from typing import Literal

from pydantic import BaseModel, Field

from traveller_models.entity_types import EntityType


class BaseSkill(BaseModel):
    entity_type: Literal[EntityType.SKILL] = EntityType.SKILL

    name: str = Field(repr=True)

    # None signifies not knowing a skill
    level: int | None = Field(repr=True)
