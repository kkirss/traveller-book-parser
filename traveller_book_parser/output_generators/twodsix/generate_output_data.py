from traveller_book_parser.output_generators import generate_output_data
from traveller_book_parser.traveller_models.trav_database import TravDatabase

from .output_generator import TwodsixOutputGenerator


@generate_output_data.dispatch
def generate_twodsix_data(
    output_generator: TwodsixOutputGenerator,
    database: TravDatabase,
) -> None:
    """Generate twodsix data from a database."""
    raise NotImplementedError
