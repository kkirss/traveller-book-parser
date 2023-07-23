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


def get_book_paths(book_code_name: str) -> list[Path]:
    ensure_folder(SETTINGS.book_descriptions_path)
    return list(SETTINGS.book_descriptions_path.glob(f"**/{book_code_name}.*"))


def get_book_description_path(book_code_name: str) -> Path:
    paths = get_book_paths(book_code_name)

    if not paths:
        raise FileNotFoundError(
            f"Book description file not found for {book_code_name}",
        )

    return get_supported_path(paths)


def load_book_description(book_code_name: str) -> BookDescription:
    path = get_book_description_path(book_code_name)
    data = load_file_data(path)
    book_description = BookDescription(**data)
    return book_description
