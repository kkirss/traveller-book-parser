from plum import dispatch

from traveller_book_parser.output_generators.base_output_generator import (
    BaseOutputGenerator,
)
from traveller_book_parser.traveller_models.trav_database import TravDatabase


@dispatch.abstract
def generate_output_data(
    output_generator: BaseOutputGenerator,
    database: TravDatabase,
) -> None:
    """Generate output data from a database."""
    raise NotImplementedError
