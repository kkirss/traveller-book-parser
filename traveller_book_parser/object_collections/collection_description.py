from typing import Any

from pydantic import BaseModel, Field

from traveller_book_parser.data_sources.data_source_description import (
    DataSourceDescription,
)
from traveller_book_parser.traveller_models.trav_object_types import TravObjectType


class Instrument(BaseModel):
    """Instrumentation settings for objects."""

    add_images: bool = False
    image_pages: list[int] = Field(default_factory=list)


class CollectionDescription(BaseModel):
    """Description of a collection of objects."""

    name: str | None = None
    name_page: int | None = Field(
        description="Page number where the collection name is found (defaults to data source page, if available).",
        default=None,
    )
    name_nth_largest_font: int = Field(
        description="Text with the Nth largest font is used as the collection name.",
        default=1,
    )

    type: TravObjectType
    default_values: dict[str, Any] = Field(
        description=(
            "Default values for trav_obj fields (for e.g. item_type). "
            "Note: These are not validated."
        ),
        default_factory=dict,
    )
    instrument: Instrument = Field(
        # TODO: Add examples
        description="Instrument objects with additional data.",
        default_factory=Instrument,
    )
    check_amount: int | None = None
    data_source_description: DataSourceDescription
