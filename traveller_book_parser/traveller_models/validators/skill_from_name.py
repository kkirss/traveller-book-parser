from typing import Any

from traveller_book_parser.traveller_models.skills.skill import Skill, get_skill_model


def skill_from_name(value: Any) -> Skill | None:  # noqa: ANN401
    """Convert space-separated name and level to a Skill."""
    if isinstance(value, str):
        name, level = value.rsplit(" ", maxsplit=1)
        skill = get_skill_model(name=name, level=level)
        return skill
    return value
