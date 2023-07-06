from typing import Any

from pydantic import RootModel

from traveller_models.skills.base_skill import BaseSkill

Skill = BaseSkill


def get_skill_model(**kwargs: dict[str, Any]) -> Skill:
    return RootModel[Skill](**kwargs).root
