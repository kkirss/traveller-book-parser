from pathlib import Path

from pandas import DataFrame

from traveller_book_parser.books.book_description import (
    BookDescription,
    get_book_file_path,
)
from traveller_book_parser.data_parsers.data_frame.data_container import (
    DataFrameDataContainer,
)
from traveller_book_parser.data_sources.extract_source_data import extract_source_data
from traveller_book_parser.settings import SETTINGS
from traveller_book_parser.utils import ensure_folder

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
    return data_frame


@extract_source_data.dispatch
def extract_tabula_data(
    book_description: BookDescription,
    data_source_description: TabulaDataSourceDescription,
) -> DataFrameDataContainer:
    data_frame = extract_tabula_data_frame(
        book_description,
        data_source_description,
    )
    return DataFrameDataContainer(
        data=data_frame,
        data_source_description=data_source_description,
    )
