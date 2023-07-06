from pydantic import BaseModel, Field


class BaseSkill(BaseModel):
    name: str = Field(repr=True)

    # None signifies not knowing a skill
    level: int | None = Field(repr=True)
