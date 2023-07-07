from pydantic import BaseModel, Field

from .collection_description import CollectionDescription


class BookDescription(BaseModel):
    """Description of a book and the content within."""

    name: str = Field(repr=True)
    code_name: str

    pages_not_numbered: int = 0

    collection_descriptions: list[CollectionDescription]
