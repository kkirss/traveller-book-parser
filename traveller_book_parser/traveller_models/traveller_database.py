from pydantic import BaseModel, Field

from .book import Book
from .trav_object import TravObject
from .trav_object_source_collection import ObjectSourceCollection


class TravellerDatabase(BaseModel):
    """A database of traveller related objects."""

    all_books: list[Book] = Field(
        description="A list of all books.",
        default_factory=list,
    )
    all_object_source_collections: list[ObjectSourceCollection] = Field(
        description="A list of all object source collections.",
        default_factory=list,
    )
    all_objects: list[TravObject] = Field(
        description="A list of all objects.",
        default_factory=list,
    )
