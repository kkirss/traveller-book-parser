from collections.abc import Iterable
import logging
from pathlib import Path
import textwrap
from traceback import format_exception_only

from description_loaders.book_description_loader import load_book_description
from description_models.book_description import BookDescription
from description_models.collection_description import CollectionDescription
from entity_collections import all_collection_parsers  # noqa: F401
from entity_collections.parse_entities import parse_collection_entities
from pydantic import ValidationError
from settings import SETTINGS, ensure_folder
from traveller_models.entity import Entity

logger = logging.getLogger(__name__)


def get_book_paths() -> list[Path]:
    """Get paths of books to parse.

    Note: Currently only supporting .pdf files
    """
    ensure_folder(SETTINGS.books_path)
    return list(SETTINGS.books_path.glob("**/*.pdf"))


def get_indented_exception_text(exception: Exception) -> str:
    exception_text = "".join(format_exception_only(exception))
    return textwrap.indent(exception_text, " " * 4)


def parse_book_collection(
    book_description: BookDescription,
    collection_description: CollectionDescription,
) -> Iterable[Entity]:
    return parse_collection_entities(
        book_description,
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
        )
        all_entities.extend(entities)
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
