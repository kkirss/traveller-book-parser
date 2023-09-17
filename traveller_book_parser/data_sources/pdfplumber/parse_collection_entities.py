from collections.abc import Iterable
import logging
from typing import Any

from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.data_parsers.data_frame.parse_entities import parse_entities
from traveller_book_parser.entity_collections.parse_entities import (
    parse_collection_entities,
)
from traveller_book_parser.traveller_models.entity import Entity
from traveller_book_parser.traveller_models.entity_types import EntityType

from .data_extract import extract_pdfplumber_data_frame
from .data_source_description import PDFPlumberDataSourceDescription

logger = logging.getLogger(__name__)


@parse_collection_entities.dispatch
def parse_pdfplumber_collection_entities(
    book_description: BookDescription,
    data_source_description: PDFPlumberDataSourceDescription,
    entity_type: EntityType,
    entity_fields: dict[str, Any],
) -> Iterable[Entity]:
    data_frame = extract_pdfplumber_data_frame(
        book_description,
        data_source_description,
    )
    logger.debug("Parsing entities from pdfplumber data frame:\n%s", data_frame)

    yield from parse_entities(
        data_frame,
        entity_type,
        entity_fields,
    )
