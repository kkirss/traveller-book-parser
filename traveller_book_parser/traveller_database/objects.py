from traveller_book_parser.traveller_models.trav_database import TravDatabase
from traveller_book_parser.traveller_models.trav_object import TravObject


def add_objects_in_collection_to_database(
    database: TravDatabase,
    objects: list[TravObject],
) -> None:
    """Add objects in a collection to a database."""
    database.all_objects.extend(objects)
