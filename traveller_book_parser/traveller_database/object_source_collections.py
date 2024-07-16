from traveller_book_parser.traveller_models.trav_object_source_collection import (
    ObjectSourceCollection,
)
from traveller_book_parser.traveller_models.traveller_database import TravellerDatabase


def add_object_source_collection_to_database(
    database: TravellerDatabase,
    object_source_collection: ObjectSourceCollection,
) -> None:
    """Add an object source collection to a traveller database."""
    database.all_object_source_collections.append(object_source_collection)
