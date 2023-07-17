from typing import Any

from traveller_models.skills.skill import Skill, get_skill_model


def skill_from_name(value: Any) -> Skill | None:  # noqa: ANN401
    if isinstance(value, str):
        name, level = value.rsplit(" ", maxsplit=1)
        skill = get_skill_model(name=name, level=level)
        return skill
    return value
