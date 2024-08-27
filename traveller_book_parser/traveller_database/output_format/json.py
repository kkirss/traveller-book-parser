from traveller_book_parser.traveller_models.trav_database import TravDatabase


def format_database_json(database: TravDatabase) -> str:
    """Format database as JSON."""
    return database.model_dump_json(indent=2)
