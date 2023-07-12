from collections.abc import Iterable

from description_models.base_data_source_description import BaseDataSourceDescription
from description_models.book_description import BookDescription
from plum import dispatch
from traveller_models.entity import Entity
from traveller_models.entity_types import EntityType


@dispatch.abstract
def parse_collection_entities(
    book_description: BookDescription,  # noqa: ARG001
    data_source_description: BaseDataSourceDescription,  # noqa: ARG001
    entity_type: EntityType,  # noqa: ARG001
) -> Iterable[Entity]:
    """Parse a collection of entities from a collection description."""
