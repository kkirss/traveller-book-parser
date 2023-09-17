from collections.abc import Iterable
from typing import Any

from plum import dispatch

from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.data_sources.base_data_source_description import (
    BaseDataSourceDescription,
)
from traveller_book_parser.traveller_models.entity import Entity
from traveller_book_parser.traveller_models.entity_types import EntityType


@dispatch.abstract
def parse_collection_entities(
    book_description: BookDescription,  # noqa: ARG001
    data_source_description: BaseDataSourceDescription,  # noqa: ARG001
    entity_type: EntityType,  # noqa: ARG001
    entity_fields: dict[str, Any],  # noqa: ARG001
) -> Iterable[Entity]:
    """Parse a collection of entities from a collection description."""
    raise NotImplementedError()
