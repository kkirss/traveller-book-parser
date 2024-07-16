from pydantic import BaseModel


class ObjectSourceCollection(BaseModel):
    """Source collection of a Traveller object."""

    name: str
