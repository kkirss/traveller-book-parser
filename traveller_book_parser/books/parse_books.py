from collections.abc import Iterable
import logging
from pathlib import Path

from pydantic import ValidationError

from traveller_book_parser.entity_collections import (
    all_collection_parsers,  # noqa: F401
)
from traveller_book_parser.entity_collections.collection_description import (
    CollectionDescription,
)
from traveller_book_parser.entity_collections.parse_entities import (
    parse_collection_entities,
)
from traveller_book_parser.settings import SETTINGS
from traveller_book_parser.traveller_models.entity import Entity
from traveller_book_parser.utils import ensure_folder, get_indented_exception_text

from .book_description import BookDescription
from .load_book_description import load_book_description

logger = logging.getLogger(__name__)


def get_book_paths() -> list[Path]:
    """Get paths of books to parse.

    Note: Currently only supporting .pdf files
    """
    ensure_folder(SETTINGS.books_path)
    return list(SETTINGS.books_path.glob("**/*.pdf"))


def parse_book_collection(
    book_description: BookDescription,
    collection_description: CollectionDescription,
) -> Iterable[Entity]:
    return parse_collection_entities(
        book_description,
        collection_description,
    )


def _check_collection_amount(
    entity_count: int,
    collection_description: CollectionDescription,
):
    check_amount = collection_description.check_amount
    if check_amount is not None and check_amount != entity_count:
        logger.warning(
            "Expected to find %i items in collection but found %i instead: %s",
            check_amount,
            entity_count,
            collection_description,
        )


def parse_book(path: Path) -> list[Entity]:
    book_code_name = path.stem
    try:
        book_description = load_book_description(book_code_name)
    except (FileNotFoundError, ValueError, ValidationError) as e:
        logger.error(
            "Failed to load description for book %s:\n%s",
            book_code_name,
            get_indented_exception_text(e),
        )
        return []

    logger.info("Parsing book %s", book_description.name)
    logger.debug("Parsing book with description %s", book_description)

    all_entities = []
    for collection_description in book_description.collection_descriptions:
        logger.debug(
            "Parsing collection with description %s",
            collection_description,
        )
        entities = parse_collection_entities(
            book_description,
            collection_description.data_source_description,
            collection_description.entity_type,
            collection_description.entity_fields,
        )
        entities = list(entities)
        _check_collection_amount(len(entities), collection_description)

        all_entities.extend(entities)

    logger.info("Parsed entities from book %s:", book_description.name)
    for entity in all_entities:
        logger.info("    %s", entity)

    return all_entities


def parse_all_books() -> list[Entity]:
    paths = get_book_paths()
    if not paths:
        logger.error(
            "Did not find any books in `books_path`: %s",
            SETTINGS.books_path,
        )
        return []

    all_entities = []
    for path in paths:
        entities = parse_book(path)
        all_entities.extend(entities)
    return all_entities
