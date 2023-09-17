from typing import Any

from pydantic import BaseModel, Field

from traveller_book_parser.data_sources.data_source_description import (
    DataSourceDescription,
)
from traveller_book_parser.traveller_models.entity_types import EntityType


class EntityInstrument(BaseModel):
    """Instrumentation settings for entities."""

    add_images: bool = False
    image_pages: list[int] = Field(default_factory=list)


class CollectionDescription(BaseModel):
    """Description of a collection of entities."""

    entity_type: EntityType
    entity_fields: dict[str, Any] = Field(
        description=(
            "Default values for entity fields (for e.g. item_type). "
            "Note: These are not validated."
        ),
        default_factory=dict,
    )
    entity_instrument: EntityInstrument = Field(
        description="Instrumentation for parsing entities.",
        default_factory=EntityInstrument,
    )
    check_amount: int | None = None
    data_source_description: DataSourceDescription
