from traveller_book_parser.traveller_models.trav_database import TravDatabase
from traveller_book_parser.traveller_models.trav_object_source_collection import (
    ObjectSourceCollection,
)


def add_object_source_collection_to_database(
    database: TravDatabase,
    object_source_collection: ObjectSourceCollection,
) -> None:
    """Add an object source collection to a traveller database."""
    database.all_object_source_collections.append(object_source_collection)
