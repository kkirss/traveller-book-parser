from collections.abc import Callable
from enum import Enum

from traveller_book_parser.traveller_models.trav_database import TravDatabase

from .json import format_database_json
from .none import format_database_none


class DatabaseOutputFormat(str, Enum):
    """Database output format."""

    json = "json"
    none = "none"


DatabaseOutputFormatter = Callable[[TravDatabase], str]

DATABASE_OUTPUT_FORMATTERS: dict[DatabaseOutputFormat, DatabaseOutputFormatter] = {
    DatabaseOutputFormat.json: format_database_json,
    DatabaseOutputFormat.none: format_database_none,
}


def format_output(database: TravDatabase, output_format: DatabaseOutputFormat) -> str:
    """Format database for output."""
    return DATABASE_OUTPUT_FORMATTERS[output_format](database)
