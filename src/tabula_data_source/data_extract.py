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
    data_source_description: TabulaDataSourceDescription,
) -> Path:
    tabula_cache_path = SETTINGS.cache_path / TABULA_CACHE_FOLDER
    ensure_folder(tabula_cache_path)

    cache_name = f"{book_code_name}-{data_source_description.page}"
    if data_source_description.extraction_method is not None:
        cache_name = f"{cache_name}-{data_source_description.extraction_method}"
    if data_source_description.area is not None:
        cache_name = f"{cache_name}-{int(data_source_description.area[0])}"
    return tabula_cache_path / f"{cache_name}.json"


def _get_book_page_tabula_data(
    book_code_name: str,
    data_source_description: TabulaDataSourceDescription,
) -> list[DataFrame]:
    book_path = get_book_file_path(book_code_name)
    tabula_cache_path = get_tabula_cache_path(book_code_name, data_source_description)

    if not tabula_cache_path.exists():
        export_tabula_data_file(
            book_path,
            tabula_cache_path,
            pages=data_source_description.page,
            area=data_source_description.area,
            extraction_method=data_source_description.extraction_method,
        )

    return read_tabula_data_file(tabula_cache_path)


def extract_tabula_data_frame(
    book_description: BookDescription,
    data_source_description: TabulaDataSourceDescription,
) -> DataFrame:
    """Extract DataFrame for a table, using Tabula."""
    page_dfs = _get_book_page_tabula_data(
        book_description.code_name,
        data_source_description,
    )
    data_frame = page_dfs[data_source_description.page_table_index]
    data_frame = clean_data_frame(data_frame)
    return data_frame
