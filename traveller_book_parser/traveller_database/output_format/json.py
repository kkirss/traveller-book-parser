from traveller_book_parser.traveller_models.traveller_database import TravellerDatabase


def format_database_json(database: TravellerDatabase) -> str:
    return database.model_dump_json(indent=2)
