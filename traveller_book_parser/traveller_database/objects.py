from traveller_book_parser.traveller_models.trav_object import TravObject
from traveller_book_parser.traveller_models.traveller_database import TravellerDatabase


def add_objects_in_collection_to_database(
    database: TravellerDatabase,
    objects: list[TravObject],
) -> None:
    """Add objects in a collection to a database."""
    database.all_objects.extend(objects)
