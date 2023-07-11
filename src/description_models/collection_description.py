from pydantic import BaseModel

from .data_source_description import DataSourceDescription


class CollectionDescription(BaseModel):
    """Description of a collection of entities."""

    entity_type: str
    data_source_description: DataSourceDescription
