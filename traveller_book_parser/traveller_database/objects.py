import logging

from traveller_book_parser.traveller_models.trav_database import TravDatabase
from traveller_book_parser.traveller_models.trav_object import TravObject

logger = logging.getLogger(__name__)


def add_objects_in_collection_to_database(
    database: TravDatabase,
    objects: list[TravObject],
) -> None:
    """Add objects in a collection to a database."""
    for trav_obj in objects:
        trav_id = trav_obj.trav_id

        if trav_id in database.objects_by_id:
            logger.warning("Object with ID %s already in database. Skipping.", trav_id)
        else:
            database.objects_by_id[trav_id] = trav_obj
