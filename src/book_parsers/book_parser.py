import logging
from pathlib import Path
import textwrap
from traceback import format_exception_only

from description_loaders.book_description_loader import load_book_description
from pydantic import ValidationError
from settings import SETTINGS, ensure_folder

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


def parse_book(path: Path):
    book_code_name = path.stem
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
    # TODO: Parse the book


def parse_all_books():
    paths = get_book_paths()
    if not paths:
        logger.error(
            "Did not find any books in `books_path`: %s",
            SETTINGS.books_path,
        )
        return

    for path in paths:
        try:
            parse_book(path)
        except Exception:
            logger.exception("Parsing book %s failed.", path.stem)
