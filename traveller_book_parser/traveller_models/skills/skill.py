from typing import Any

from pydantic import RootModel

from .base_skill import BaseSkill

Skill = BaseSkill


def get_skill_model(**kwargs: Any) -> Skill:  # noqa: ANN401
    return RootModel[Skill](**kwargs).root
