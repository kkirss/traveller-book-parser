from pydantic import BaseModel

from description_models.base_data_source_description import BaseDataSourceDescription


class CollectionDescription(BaseModel):
    """Description of a collection of entities."""

    entity_type: str

    data_source_description: BaseDataSourceDescription
