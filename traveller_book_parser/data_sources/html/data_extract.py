import logging
from pathlib import Path

from traveller_book_parser.books.book_description import (
    BookDescription,
    get_book_file_path,
)
from traveller_book_parser.settings import SETTINGS
from traveller_book_parser.utils import ensure_folder

from .pdftohtml_integration import are_html_files_exported, export_html_files

logger = logging.getLogger(__name__)

HTML_CACHE_FOLDER = "html_data"


def _get_book_html_cache_folder(book_code_name: str) -> Path:
    html_cache_path = SETTINGS.cache_path / HTML_CACHE_FOLDER
    ensure_folder(html_cache_path)

    return html_cache_path / book_code_name


def export_book_html_files(book_description: BookDescription):
    """Export html files for a book."""
    book_pdf_path = get_book_file_path(book_description.code_name)
    book_html_cache_folder = _get_book_html_cache_folder(book_description.code_name)

    if not are_html_files_exported(book_html_cache_folder):
        logger.debug("Generating book html for %s", book_description.code_name)

        export_html_files(book_pdf_path, book_html_cache_folder)


def _get_page_html_file_path(book_code_name: str, page: int) -> Path:
    book_html_cache_folder = _get_book_html_cache_folder(book_code_name)
    return book_html_cache_folder / f"page{page}.html"


def _get_page_html_content(book_code_name: str, page: int) -> str:
    html_file_path = _get_page_html_file_path(book_code_name, page)
    return html_file_path.read_text(encoding="utf-8")
