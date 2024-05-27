from contextlib import contextmanager

from traveller_book_parser.traveller_models.traveller_database import TravellerDatabase

from .output_format.output_format import DatabaseOutputFormat, format_output


@contextmanager
def outputted_database(output_format: DatabaseOutputFormat):
    """Context manager for a TravellerDatabase, which outputs it at the end."""
    database = TravellerDatabase()

    yield database

    print(format_output(database, output_format))
