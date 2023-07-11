from pydantic import BaseModel
from traveller_models.entity_types import EntityType

from .data_source_description import DataSourceDescription


class CollectionDescription(BaseModel):
    """Description of a collection of entities."""

    entity_type: EntityType
    data_source_description: DataSourceDescription
