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


def create_characteristic(**kwargs: Any) -> Characteristic:  # noqa: ANN401
    """Create Characteristic model instance."""
    return RootModel[Characteristic](**kwargs).root
