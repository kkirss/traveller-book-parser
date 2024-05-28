from pydantic import BaseModel


class Book(BaseModel):
    """Book."""

    name: str
