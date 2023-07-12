from collections.abc import Iterable
import logging
from typing import Any

from description_models.book_description import BookDescription
from entity_collections.parse_entities import parse_collection_entities
from traveller_models.entity import Entity
from traveller_models.entity_types import EntityType

from .data_extract import extract_tabula_data_frame
from .data_source_description import TabulaDataSourceDescription

logger = logging.getLogger(__name__)


@parse_collection_entities.dispatch
def parse_tabula_collection_entities(
    book_description: BookDescription,
    data_source_description: TabulaDataSourceDescription,
    entity_type: EntityType,  # noqa: ARG001
    entity_fields: dict[str, Any],  # noqa: ARG001
) -> Iterable[Entity]:
    data_frame = extract_tabula_data_frame(
        book_description,
        data_source_description,
    )
    logger.debug("Parsing entities from tabula data frame:\n%s", data_frame)
    # TODO: Parsing logic
    return []
