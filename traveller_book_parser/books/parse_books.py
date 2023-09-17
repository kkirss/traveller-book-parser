from collections.abc import Iterable
import logging
from pathlib import Path

from pydantic import ValidationError

from traveller_book_parser.data_parsers import all_data_parsers  # noqa: F401
from traveller_book_parser.data_parsers.parse_data_entities import parse_data_entities
from traveller_book_parser.data_sources import all_data_extractors  # noqa: F401
from traveller_book_parser.data_sources.extract_source_data import extract_source_data
from traveller_book_parser.entity_collections.collection_description import (
    CollectionDescription,
)
from traveller_book_parser.entity_instrumentation.instrument_entity import (
    instrument_entity,
)
from traveller_book_parser.settings import SETTINGS
from traveller_book_parser.traveller_database.update_database import (
    add_collection_entities_to_database,
)
from traveller_book_parser.traveller_models.entity import Entity
from traveller_book_parser.traveller_models.traveller_database import TravellerDatabase
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


def get_book_code_names() -> list[str]:
    """Get code names of books to parse.

    Note: Currently only supporting .pdf files
    """
    paths = get_book_paths()
    return [path.stem for path in paths]


def parse_book_collection(
    book_description: BookDescription,
    collection_description: CollectionDescription,
) -> Iterable[Entity]:
    data_container = extract_source_data(
        book_description,
        collection_description.data_source_description,
    )
    entities = parse_data_entities(
        data_container,
        collection_description.entity_type,
        collection_description.entity_fields,
    )

    for entity in entities:
        entity = instrument_entity(
            entity,
            book_description,
            collection_description,
        )
        if SETTINGS.log_parsed_entities:
            logger.debug("Parsed entity: %s", entity)
        yield entity


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


def parse_book_entities(database: TravellerDatabase, book_code_name: str) -> None:
    try:
        book_description = load_book_description(book_code_name)
    except (FileNotFoundError, ValueError, ValidationError) as e:
        logger.error(
            "Failed to load description for book %s:\n%s",
            book_code_name,
            get_indented_exception_text(e),
        )
        return

    logger.info("Parsing book %s", book_description.name)
    logger.debug("Parsing book with description %s", book_description)

    book_entities_count = 0
    for collection_description in book_description.collection_descriptions:
        logger.debug(
            "Parsing collection with description %s",
            collection_description,
        )
        collection_entities = parse_book_collection(
            book_description,
            collection_description,
        )
        collection_entities = list(collection_entities)
        book_entities_count += len(collection_entities)
        _check_collection_amount(len(collection_entities), collection_description)

        add_collection_entities_to_database(database, collection_entities)

    logger.info(
        "Parsed %i entities from book %s", book_entities_count, book_description.name
    )


def parse_books(database: TravellerDatabase, book_code_names: list[str]) -> None:
    for book_code_name in book_code_names:
        parse_book_entities(database, book_code_name)


def parse_all_books(database: TravellerDatabase) -> None:
    book_code_names = get_book_code_names()

    if book_code_names:
        parse_books(database, book_code_names)
    else:
        logger.error(
            "Did not find any books in `books_path`: %s",
            SETTINGS.books_path,
        )
