from pydantic import BaseModel


class EntitySourceCollection(BaseModel):
    """Source collection of an entity."""

    name: str
