from traveller_book_parser.output_generators import generate_output_data
from traveller_book_parser.traveller_models.traveller_database import TravellerDatabase

from .output_generator import TwodsixOutputGenerator


@generate_output_data.dispatch
def generate_twodsix_data(
    output_generator: TwodsixOutputGenerator,  # noqa: ARG001
    traveller_database: TravellerDatabase,  # noqa: ARG001
) -> None:
    """Generate twodsix data from a database."""
    raise NotImplementedError
