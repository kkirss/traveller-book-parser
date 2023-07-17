from collections.abc import Iterable
import logging
from typing import Any

from book_publishers.column_names import get_column_field_name
from description_models.book_description import BookDescription
from entity_collections.parse_entities import parse_collection_entities
from pydantic import ValidationError
from traveller_models.entity import Entity, get_entity_model
from traveller_models.entity_types import EntityType
from utils import get_indented_exception_text

from .data_cleaners.missing_tech_level import is_missing_tech_level
from .data_extract import extract_tabula_data_frame
from .data_source_description import TabulaDataSourceDescription

logger = logging.getLogger(__name__)


@parse_collection_entities.dispatch
def parse_tabula_collection_entities(
    book_description: BookDescription,
    data_source_description: TabulaDataSourceDescription,
    entity_type: EntityType,
    entity_fields: dict[str, Any],
) -> Iterable[Entity]:
    data_frame = extract_tabula_data_frame(
        book_description,
        data_source_description,
    )
    logger.debug("Parsing entities from tabula data frame:\n%s", data_frame)

    unknown_columns = set()
    for _, row in data_frame.iterrows():
        entity_dict = {
            "entity_type": entity_type,
            **entity_fields,
        }
        for column, value in row.items():
            if not isinstance(column, str):
                continue
            try:
                field_name = get_column_field_name(column)
            except KeyError:
                unknown_columns.add(column)
                continue

            entity_dict[field_name] = value

        if is_missing_tech_level(entity_dict):
            logger.warning(
                "Found entity with missing tech level, skipping: %s", entity_dict
            )
            continue

        try:
            entity = get_entity_model(**entity_dict)
        except ValidationError as e:
            logger.error(
                "Failed to create entity:\n%s",
                get_indented_exception_text(e),
            )
            continue

        logger.debug("Parsed entity: %s", entity)
        yield entity

    for unknown_column in unknown_columns:
        logger.warning("Found unknown column: %s", unknown_column)
