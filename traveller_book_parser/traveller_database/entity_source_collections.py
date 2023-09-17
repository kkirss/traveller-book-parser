from traveller_book_parser.traveller_models.entity_source_collection import (
    EntitySourceCollection,
)
from traveller_book_parser.traveller_models.traveller_database import TravellerDatabase


def add_entity_source_collection_to_database(
    database: TravellerDatabase,
    entity_source_collection: EntitySourceCollection,
) -> None:
    """Add an entity source collection to a traveller database."""
    database.all_entity_source_collections.append(entity_source_collection)
