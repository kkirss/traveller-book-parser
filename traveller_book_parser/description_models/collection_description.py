from typing import Any

from pydantic import BaseModel, Field

from traveller_book_parser.traveller_models.entity_types import EntityType

from .data_source_description import DataSourceDescription


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
    check_amount: int | None = None
    data_source_description: DataSourceDescription
