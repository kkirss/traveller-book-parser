from pydantic import BaseModel

from .entity_types import EntityType


class BaseEntity(BaseModel):
    entity_type: EntityType
