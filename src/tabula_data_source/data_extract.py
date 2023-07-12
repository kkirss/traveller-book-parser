from pathlib import Path

from description_models.book_description import BookDescription, get_book_file_path
from pandas import DataFrame
from settings import SETTINGS
from utils import ensure_folder

from .data_cleaners.clean_data_frame import clean_data_frame
from .data_source_description import TabulaDataSourceDescription
from .tabula_integration import export_tabula_data_file, read_tabula_data_file

TABULA_CACHE_FOLDER = "tabula_data"


def get_tabula_cache_path(
    book_code_name: str,
    page: int,
    tabula_data_source: TabulaDataSourceDescription,
) -> Path:
    tabula_cache_path = SETTINGS.cache_path / TABULA_CACHE_FOLDER
    ensure_folder(tabula_cache_path)

    cache_name = f"{book_code_name}-{page}"
    if tabula_data_source.extraction_method is not None:
        cache_name = f"{cache_name}-{tabula_data_source.extraction_method}"
    if tabula_data_source.area is not None:
        cache_name = f"{cache_name}-{int(tabula_data_source.area[0])}"
    return tabula_cache_path / f"{cache_name}.json"


def _get_book_page_tabula_data(
    book_code_name: str,
    page: int,
    tabula_data_source: TabulaDataSourceDescription,
) -> list[DataFrame]:
    book_path = get_book_file_path(book_code_name)
    tabula_cache_path = get_tabula_cache_path(
        book_code_name, page, tabula_data_source
    )

    if not tabula_cache_path.exists():
        export_tabula_data_file(
            book_path,
            tabula_cache_path,
            page,
            area=tabula_data_source.area,
            extraction_method=tabula_data_source.extraction_method,
        )

    return read_tabula_data_file(tabula_cache_path)


def extract_tabula_data_frame(
    book_description: BookDescription,
    tabula_data_source: TabulaDataSourceDescription,
) -> DataFrame:
    """Extract DataFrame for a table, using Tabula."""
    page = book_description.pages_not_numbered + tabula_data_source.page
    page_dfs = _get_book_page_tabula_data(
        book_description.code_name,
        page,
        tabula_data_source,
    )
    data_frame = page_dfs[tabula_data_source.page_table_index]
    data_frame = clean_data_frame(data_frame)
    return data_frame
