from plum import dispatch

from traveller_book_parser.output_generators.base_output_generator import (
    BaseOutputGenerator,
)
from traveller_book_parser.traveller_models.trav_database import TravDatabase


@dispatch.abstract
def generate_output_data(
    output_generator: BaseOutputGenerator,  # noqa: ARG001
    database: TravDatabase,  # noqa: ARG001
) -> None:
    """Generate output data from a database."""
    raise NotImplementedError
