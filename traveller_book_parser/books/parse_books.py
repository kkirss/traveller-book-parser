from collections.abc import Iterable
import logging
from pathlib import Path

from pydantic import ValidationError

from traveller_book_parser.data_parsers import all_data_parsers  # noqa: F401
from traveller_book_parser.data_parsers.parse_objects_data import parse_objects
from traveller_book_parser.data_sources import all_data_extractors  # noqa: F401
from traveller_book_parser.data_sources.extract_source_data import extract_source_data
from traveller_book_parser.object_collections.collection_description import (
    CollectionDescription,
)
from traveller_book_parser.object_collections.parse_collection_name import (
    parse_collection_name,
)
from traveller_book_parser.object_instrumentation.instrument_object import (
    instrument_object,
)
from traveller_book_parser.output_generators import all_output_generators  # noqa: F401
from traveller_book_parser.settings import SETTINGS
from traveller_book_parser.traveller_database.books import add_book_to_database
from traveller_book_parser.traveller_database.object_source_collections import (
    add_object_source_collection_to_database,
)
from traveller_book_parser.traveller_database.objects import (
    add_objects_in_collection_to_database,
)
from traveller_book_parser.traveller_models.book import Book
from traveller_book_parser.traveller_models.trav_database import TravDatabase
from traveller_book_parser.traveller_models.trav_object import TravObject
from traveller_book_parser.traveller_models.trav_object_source_collection import (
    ObjectSourceCollection,
)
from traveller_book_parser.utils import ensure_folder

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


def parse_book_collection_objects(
    book_description: BookDescription,
    collection_description: CollectionDescription,
) -> Iterable[TravObject]:
    """Parse a collection of objs from a book."""
    data_container = extract_source_data(
        book_description,
        collection_description.data_source_description,
    )
    objs = parse_objects(
        data_container,
        collection_description.type,
        collection_description.default_values,
    )

    for obj in objs:
        instrumented_obj = instrument_object(
            obj,
            book_description,
            collection_description,
        )
        if SETTINGS.log_parsed_objects:
            logger.debug("Parsed trav_obj: %s", instrumented_obj)
        yield instrumented_obj


def _check_collection_amount(
    object_count: int,
    collection_description: CollectionDescription,
):
    """Check that the number of objects in a collection is as expected."""
    check_amount = collection_description.check_amount
    if check_amount is not None and check_amount != object_count:
        logger.warning(
            "Expected to find %i items in collection but found %i instead: %s",
            check_amount,
            object_count,
            collection_description,
        )


def parse_book(database: TravDatabase, book_code_name: str) -> None:
    """Parse a book into a database."""
    try:
        book_description = load_book_description(book_code_name)
    except (FileNotFoundError, ValueError, ValidationError):
        logger.exception(
            "Failed to load description for book %s:",
            book_code_name,
        )
        return

    logger.info("Parsing book %s", book_description.name)
    logger.debug("Parsing book with description %s", book_description)

    book = Book(name=book_description.name)

    if SETTINGS.log_parsed_objects:
        logger.debug("Parsed book: %s", book)

    add_book_to_database(database, book)

    book_objects_count = 0
    for collection_description in book_description.collection_descriptions:
        logger.debug(
            "Parsing collection with description %s",
            collection_description,
        )

        object_source_collection = ObjectSourceCollection(
            name=parse_collection_name(book_description, collection_description),
        )

        if SETTINGS.log_parsed_objects:
            logger.debug(
                "Parsed object source collection: %s", object_source_collection
            )

        add_object_source_collection_to_database(database, object_source_collection)

        collection_objects = parse_book_collection_objects(
            book_description,
            collection_description,
        )
        collection_objects = list(collection_objects)
        book_objects_count += len(collection_objects)
        _check_collection_amount(len(collection_objects), collection_description)

        add_objects_in_collection_to_database(database, collection_objects)

    logger.info(
        "Parsed %i objects from book %s", book_objects_count, book_description.name
    )


def parse_books(database: TravDatabase, book_code_names: list[str]) -> None:
    """Parse books into a database."""
    for book_code_name in book_code_names:
        parse_book(database, book_code_name)


def parse_all_books(database: TravDatabase) -> None:
    """Parse all books into a database."""
    book_code_names = get_book_code_names()

    if book_code_names:
        parse_books(database, book_code_names)
    else:
        logger.error(
            "Did not find any books in `books_path`: %s",
            SETTINGS.books_path,
        )
