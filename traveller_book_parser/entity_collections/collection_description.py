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

    name: str | None = None
    name_page: int | None = Field(
        description="Page number where the collection name is found (defaults to data source page, if available).",
        default=None,
    )
    name_nth_largest_font: int = Field(
        description="Text with the Nth largest font is used as the collection name.",
        default=1,
    )

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
