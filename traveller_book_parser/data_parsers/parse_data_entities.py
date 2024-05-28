from collections.abc import Iterable
from typing import Any

from plum import dispatch

from traveller_book_parser.traveller_models.entity import Entity
from traveller_book_parser.traveller_models.entity_types import EntityType

from .base_data_container import BaseDataContainer


@dispatch.abstract
def parse_data_entities(
    data_container: BaseDataContainer,  # noqa: ARG001
    entity_type: EntityType,  # noqa: ARG001
    entity_fields: dict[str, Any],  # noqa: ARG001
) -> Iterable[Entity]:
    """Parse a collection of entities from a data container."""
    raise NotImplementedError
