from unittest.mock import MagicMock, patch

import pytest

from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.data_sources.html_table.data_source_description import (
    HTMLTableDataSourceDescription,
)
from traveller_book_parser.data_sources.tabula.data_source_description import (
    TabulaDataSourceDescription,
)
from traveller_book_parser.object_collections.collection_description import (
    CollectionDescription,
    TravObjectType,
)
from traveller_book_parser.object_collections.parse_collection_name import (
    FailedToGuessCollectionNameError,
    get_collection_name_page,
    parse_collection_name,
)

# Constants for test page numbers
TEST_PAGE_NUMBER = 5
TEST_RANGE_START_PAGE = 10


def test_get_collection_name_page_explicit() -> None:
    """Test getting collection name page when explicitly set."""
    collection_desc = CollectionDescription(
        name_page=TEST_PAGE_NUMBER,
        type=TravObjectType.SKILL,
        data_source_description=TabulaDataSourceDescription(
            type="tabula-table",
            page=1,
        ),
    )
    assert get_collection_name_page(collection_desc) == TEST_PAGE_NUMBER


def test_get_collection_name_page_from_source() -> None:
    """Test getting collection name page from data source page."""
    collection_desc = CollectionDescription(
        type=TravObjectType.SKILL,
        data_source_description=TabulaDataSourceDescription(
            type="tabula-table",
            page=TEST_RANGE_START_PAGE,
        ),
    )
    assert get_collection_name_page(collection_desc) == TEST_RANGE_START_PAGE


def test_get_collection_name_page_from_html_source() -> None:
    """Test getting collection name page from HTML data source."""
    collection_desc = CollectionDescription(
        type=TravObjectType.SKILL,
        data_source_description=HTMLTableDataSourceDescription(
            type="html-table",
            pages="10-20",
        ),
    )
    assert get_collection_name_page(collection_desc) == TEST_RANGE_START_PAGE


def test_get_collection_name_page_unsupported() -> None:
    """Test getting collection name page with unsupported data source."""
    collection_desc = CollectionDescription(
        name_page=None,
        type=TravObjectType.ITEM,
        data_source_description=HTMLTableDataSourceDescription(
            type="html-table", pages=str(TEST_RANGE_START_PAGE)
        ),
    )
    assert get_collection_name_page(collection_desc) == TEST_RANGE_START_PAGE


def test_parse_collection_name_predefined() -> None:
    """Test parsing collection name when it's predefined."""
    book_desc = MagicMock(spec=BookDescription)
    collection_desc = CollectionDescription(
        name="Test Collection",
        type=TravObjectType.ITEM,
        data_source_description=TabulaDataSourceDescription(
            type="tabula-table", page=10
        ),
    )
    assert parse_collection_name(book_desc, collection_desc) == "Test Collection"


@patch(
    "traveller_book_parser.object_collections.parse_collection_name.get_book_file_path"
)
@patch(
    "traveller_book_parser.object_collections.parse_collection_name.guess_page_header"
)
def test_parse_collection_name_guessed_success(
    mock_guess_header: MagicMock, mock_get_file_path: MagicMock
) -> None:
    """Test parsing collection name when it needs to be guessed."""
    book_desc = MagicMock(spec=BookDescription)
    book_desc.code_name = "test_book"
    collection_desc = CollectionDescription(
        name=None,
        name_page=TEST_PAGE_NUMBER,
        type=TravObjectType.ITEM,
        data_source_description=TabulaDataSourceDescription(
            type="tabula-table", page=TEST_RANGE_START_PAGE
        ),
    )

    mock_get_file_path.return_value = "test_file.pdf"
    mock_guess_header.return_value = "Guessed Name"

    assert parse_collection_name(book_desc, collection_desc) == "Guessed Name"
    mock_get_file_path.assert_called_once_with("test_book")
    mock_guess_header.assert_called_once_with(
        pdf_path="test_file.pdf",
        page_number=TEST_PAGE_NUMBER,
        nth_largest_font_text=collection_desc.name_nth_largest_font,
    )


@patch(
    "traveller_book_parser.object_collections.parse_collection_name.get_book_file_path"
)
@patch(
    "traveller_book_parser.object_collections.parse_collection_name.guess_page_header"
)
def test_parse_collection_name_guessed_failure(
    mock_guess_header: MagicMock, mock_get_file_path: MagicMock
) -> None:
    """Test parsing collection name when guessing fails."""
    book_desc = MagicMock(spec=BookDescription)
    book_desc.code_name = "test_book"
    collection_desc = CollectionDescription(
        name=None,
        name_page=TEST_PAGE_NUMBER,
        type=TravObjectType.ITEM,
        data_source_description=TabulaDataSourceDescription(
            type="tabula-table", page=TEST_RANGE_START_PAGE
        ),
    )

    mock_get_file_path.return_value = "test_file.pdf"
    mock_guess_header.return_value = None

    with pytest.raises(FailedToGuessCollectionNameError):
        parse_collection_name(book_desc, collection_desc)
