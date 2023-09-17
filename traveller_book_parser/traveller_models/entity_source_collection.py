from pydantic import BaseModel


class EntitySourceCollection(BaseModel):
    name: str
