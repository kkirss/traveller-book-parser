from contextlib import contextmanager

from traveller_book_parser.traveller_models.trav_database import TravDatabase

from .output_format.output_format import format_database_for_output
from .output_io.output_database_to_io import output_database_to_io
from .output_options import DatabaseOutputOptions


@contextmanager
def outputted_database(options: DatabaseOutputOptions):
    """Context manager for a TravDatabase, which outputs it at the end."""
    database = TravDatabase()

    yield database

    output = format_database_for_output(database, options.output_format)

    output_database_to_io(output, options.output_type, options.output_path)
