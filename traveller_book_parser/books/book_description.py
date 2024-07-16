from pathlib import Path

from pydantic import BaseModel, Field

from traveller_book_parser.object_collections.collection_description import (
    CollectionDescription,
)
from traveller_book_parser.settings import SETTINGS


def get_book_file_path(code_name: str) -> Path:
    """Get path of book file."""
    return SETTINGS.books_path / f"{code_name}.pdf"


class BookDescription(BaseModel):
    """Description of a book and the content within."""

    name: str = Field(repr=True)
    code_name: str

    collection_descriptions: list[CollectionDescription]
