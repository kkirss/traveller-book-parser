from traveller_book_parser.traveller_models.entity import Entity
from traveller_book_parser.traveller_models.traveller_database import TravellerDatabase


def add_collection_entities_to_database(
    database: TravellerDatabase,
    entities: list[Entity],
) -> None:
    database.all_entities.extend(entities)
