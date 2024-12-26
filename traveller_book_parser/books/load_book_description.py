import logging
from pathlib import Path

from traveller_book_parser.settings import SETTINGS
from traveller_book_parser.utils import ensure_folder
from traveller_book_parser.utils.file_type_loaders import (
    get_supported_path,
    load_file_data,
)

from .book_description import BookDescription

logger = logging.getLogger(__name__)


class BookDescriptionFileNotFoundError(FileNotFoundError):
    """Exception raised when book description file not found for a book."""

    def __init__(self, book_code_name: str):
        super().__init__(f"Book description file not found for {book_code_name}")


def get_book_paths(book_code_name: str) -> list[Path]:
    """Get paths of books to parse."""
    ensure_folder(SETTINGS.book_descriptions_path)
    return list(SETTINGS.book_descriptions_path.glob(f"**/{book_code_name}.*"))


def get_book_description_path(book_code_name: str) -> Path:
    """Get path of book description file."""
    paths = get_book_paths(book_code_name)

    if not paths:
        raise BookDescriptionFileNotFoundError(book_code_name)

    return get_supported_path(paths)


def load_book_description(book_code_name: str) -> BookDescription:
    """Load the description of a book."""
    path = get_book_description_path(book_code_name)
    data = load_file_data(path)
    return BookDescription(**data)
