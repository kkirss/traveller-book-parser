from typing import Annotated, Any

from pydantic import Field, RootModel

from .dexterity import Dexterity
from .education import Education
from .endurance import Endurance
from .influence import Influence
from .intellect import Intellect
from .luck import Luck
from .social_standing import SocialStanding
from .strength import Strength

Characteristic = Annotated[
    Strength
    | Dexterity
    | Endurance
    | Intellect
    | Education
    | SocialStanding
    | Influence
    | Luck,
    Field(discriminator="characteristic_type"),
]


def get_characteristic_model(**kwargs: dict[str, Any]) -> Characteristic:
    return RootModel[Characteristic](**kwargs).root
