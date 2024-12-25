from collections.abc import Callable
from enum import Enum

from traveller_book_parser.traveller_models.trav_database import TravDatabase

from .cheat_sheet_pdf import format_database_cheat_sheet_pdf
from .json import format_database_json
from .none import format_database_none


class OutputFormat(str, Enum):
    """Output format (e.g. json or none)."""

    cheat_sheet_pdf = "cheat_sheet_pdf"
    json = "json"
    none = "none"


DatabaseOutputFormatter = Callable[[TravDatabase], str]

DATABASE_OUTPUT_FORMATTERS: dict[OutputFormat, DatabaseOutputFormatter] = {
    OutputFormat.cheat_sheet_pdf: format_database_cheat_sheet_pdf,
    OutputFormat.json: format_database_json,
    OutputFormat.none: format_database_none,
}


def format_database_for_output(
    database: TravDatabase, output_format: OutputFormat
) -> str:
    """Format database for output."""
    return DATABASE_OUTPUT_FORMATTERS[output_format](database)
