from pydantic import BaseModel, Field

from .entity import Entity


class TravellerDatabase(BaseModel):
    all_entities: list[Entity] = Field(
        description="A list of all entities.",
        default_factory=list,
    )
