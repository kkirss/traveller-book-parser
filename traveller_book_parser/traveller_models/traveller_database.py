from pydantic import BaseModel, Field

from .book import Book
from .entity import Entity
from .entity_source_collection import EntitySourceCollection


class TravellerDatabase(BaseModel):
    """A database of traveller related objects."""

    all_books: list[Book] = Field(
        description="A list of all books.",
        default_factory=list,
    )
    all_entity_source_collections: list[EntitySourceCollection] = Field(
        description="A list of all entity source collections.",
        default_factory=list,
    )
    all_entities: list[Entity] = Field(
        description="A list of all entities.",
        default_factory=list,
    )
