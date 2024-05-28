from pathlib import Path

from pydantic import BaseModel, Field

from .entity_types import EntityType


class BaseEntity(BaseModel):
    """Entity/object with name."""

    entity_type: EntityType

    name: str = Field(repr=True)
    image_path: Path | None = None
