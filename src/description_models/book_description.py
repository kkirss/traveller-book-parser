from pathlib import Path

from pydantic import BaseModel, Field
from settings import SETTINGS

from .collection_description import CollectionDescription


def get_book_file_path(code_name: str) -> Path:
    return SETTINGS.books_path / f"{code_name}.pdf"


class BookDescription(BaseModel):
    """Description of a book and the content within."""

    name: str = Field(repr=True)
    code_name: str

    pages_not_numbered: int = 0

    collection_descriptions: list[CollectionDescription]

    @property
    def file_path(self) -> Path:
        return get_book_file_path(self.code_name)
