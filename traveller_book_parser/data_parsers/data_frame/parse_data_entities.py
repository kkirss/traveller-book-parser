from collections.abc import Iterable
import logging
from typing import Any

from pydantic import ValidationError

from traveller_book_parser.books.publishers.column_names import get_column_field_name
from traveller_book_parser.data_parsers.data_cleaners.missing_tech_level import (
    is_missing_tech_level,
)
from traveller_book_parser.data_parsers.parse_data_entities import parse_data_entities
from traveller_book_parser.settings import SETTINGS
from traveller_book_parser.traveller_models.entity import Entity, get_entity_model
from traveller_book_parser.traveller_models.entity_types import EntityType

from .data_cleaners.clean_data_frame import clean_data_frame
from .data_container import DataFrameDataContainer

logger = logging.getLogger(__name__)


@parse_data_entities.dispatch
def parse_data_frame_entities(
    data_container: DataFrameDataContainer,
    entity_type: EntityType,
    entity_fields: dict[str, Any],
) -> Iterable[Entity]:
    data_frame = data_container.data

    if SETTINGS.log_intermediate_data:
        logger.debug("Parsing entities from data frame:\n%s", data_frame)

    data_frame = clean_data_frame(data_frame)

    previous_entity = None
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
        except ValidationError:
            logger.exception("Failed to create entity from %s", entity_dict)
            continue

        if entity.name == "":
            if previous_entity is None:
                logger.warning(
                    "Found first entity with empty name, skipping: %s", entity_dict
                )
                continue
            if previous_entity.name == "":
                logger.warning(
                    "Found two entities with empty names, skipping: %s", entity_dict
                )
                continue
            entity.name = previous_entity.name

        previous_entity = entity
        yield entity

    for unknown_column in unknown_columns:
        logger.warning("Found unknown column: %s", unknown_column)
