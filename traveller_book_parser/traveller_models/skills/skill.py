from typing import Any

from pydantic import RootModel

from .base_skill import BaseSkill

Skill = BaseSkill


def create_skill(**kwargs: Any) -> Skill:  # noqa: ANN401
    """Create Skill model instance."""
    return RootModel[Skill](**kwargs).root
