from contextlib import contextmanager

from traveller_book_parser.traveller_models.trav_database import TravDatabase

from .output_format.output_format import DatabaseOutputFormat, format_output


@contextmanager
def outputted_database(output_format: DatabaseOutputFormat):
    """Context manager for a TravDatabase, which outputs it at the end."""
    database = TravDatabase()

    yield database

    # TODO: Take output IO as argument instead of using print
    print(format_output(database, output_format))  # noqa: T201
