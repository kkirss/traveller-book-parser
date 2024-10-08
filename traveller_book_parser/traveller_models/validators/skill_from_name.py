from typing import Any, Optional

from traveller_book_parser.traveller_models.skills.skill import Skill, create_skill


def skill_from_name(value: Any) -> Optional[Skill]:  # noqa: ANN401
    """Convert space-separated name and level to a Skill.

    >>> skill_from_name("Melee (blade) 1")
    Skill(name='Melee (blade)', image_path=None, level=1, trav_id='skill:Melee (blade):1')
    """
    if isinstance(value, str):
        name, level = value.rsplit(" ", maxsplit=1)
        return create_skill(name=name, level=level)
    return value
