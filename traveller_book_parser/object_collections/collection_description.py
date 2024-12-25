from typing import Any, Optional

from pydantic import BaseModel, Field

from traveller_book_parser.data_sources.data_source_description import (
    DataSourceDescription,
)
from traveller_book_parser.traveller_models.trav_object_types import TravObjectType


class Instrument(BaseModel):
    """Instrumentation settings for objects."""

    add_images: bool = Field(
        default=False,
        description="Add images for the objects in the collection."
        " Images are found by looking for the objects name in `image_pages` pages."
        " The closest image is used.",
    )
    image_pages: list[int] = Field(
        default_factory=list, description="""Pages in the book to search for images."""
    )


class CollectionDescription(BaseModel):
    """Description of a collection of objects."""

    name: Optional[str] = None
    name_page: Optional[int] = Field(
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
    check_amount: Optional[int] = None
    data_source_description: DataSourceDescription
