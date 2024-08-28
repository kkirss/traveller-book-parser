from pydantic import BaseModel, Field

from .book import Book
from .trav_object import TravObject
from .trav_object_source_collection import ObjectSourceCollection


class TravDatabase(BaseModel):
    """A database of traveller related objects."""

    all_books: list[Book] = Field(
        description="A list of all books.",
        default_factory=list,
    )
    all_object_source_collections: list[ObjectSourceCollection] = Field(
        description="A list of all object source collections.",
        default_factory=list,
    )
    objects_by_id: dict[str, TravObject] = Field(
        description="A mapping of all objects by their trav_id.",
        default_factory=dict,
    )
