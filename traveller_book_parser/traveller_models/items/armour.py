from collections.abc import Callable
import re
from typing import Any, Literal, Optional

from pydantic import Field, field_validator, model_validator

from traveller_book_parser.traveller_models.skills.skill import Skill
from traveller_book_parser.traveller_models.validators import (
    dash_is_zero,
    skill_from_name,
    string_none_is_none,
)

from .base_item import BaseItem, ItemType


def _get_type_protection_from_protection(
    field_name: str,
    damage_type: str,
) -> Callable:
    """Get model validator to split protection to base and typed fields.

    >>> _get_type_protection_from_protection("protection_laser", "laser")(Armour, {"protection": "5 (10 vs. laser)"})
    {'protection': '5', 'protection_laser': '10'}
    >>> _get_type_protection_from_protection("protection_laser", "laser")(Armour, {"protection": "5 (10 vs. plasma)"})
    {'protection': '5 (10 vs. plasma)', 'protection_laser': '5'}
    """

    def type_protection_from_protection(
        cls: type["Armour"],  # noqa: ARG001
        data: dict[str, Any],
    ) -> dict[str, Any]:
        if (
            data.get(field_name) is None
            and "protection" in data
            and isinstance(data["protection"], str)
        ):
            protection: str = data["protection"]
            if "vs." in protection and damage_type in protection:
                protection, second = protection.split(" (", maxsplit=1)
                protection_type = second.split(" vs.", maxsplit=1)[0]
                data["protection"] = protection
                data[field_name] = protection_type
            else:
                data[field_name] = protection.split(" (", maxsplit=1)[0]
        return data

    return type_protection_from_protection


_CHAR_BOOST_REGEX = re.compile(r"(.+) \((.+) (.{3})\)")


def characteristic_boost(value: Any) -> Any:  # noqa: ANN401, D103
    if isinstance(value, str) and (match := _CHAR_BOOST_REGEX.match(value)):
        # TODO: Make use of the characteristic boost
        # characteristic_boost_amount = match.group(2)
        # boost_characteristic = match.group(3)
        return match.group(1)
    return value


class Armour(BaseItem):
    """Armour."""

    item_type: Literal[ItemType.armour] = Field(repr=False, default=ItemType.armour)

    protection: int
    protection_laser: Optional[int] = Field(default=None)
    protection_plasma: Optional[int] = Field(default=None)
    protection_psionics: Optional[int] = Field(default=None)

    radiation_protection: int = 0
    required_skill: Optional[Skill] = None
    slots_count: Optional[int] = None

    characteristic_bonuses: dict[str, int] = Field(default_factory=dict)

    # Validators
    laser_protection_from_protection = model_validator(mode="before")(
        _get_type_protection_from_protection("protection_laser", "laser")
    )
    plasma_protection_from_protection = model_validator(mode="before")(
        _get_type_protection_from_protection("protection_plasma", "plasma")
    )
    psionics_protection_from_protection = model_validator(mode="before")(
        _get_type_protection_from_protection("protection_psionics", "psionics")
    )

    protection_characteristic_boost = field_validator("protection", mode="before")(
        characteristic_boost
    )
    protection_zero = field_validator("protection", mode="before")(dash_is_zero)
    radiation_protection_zero = field_validator(
        "radiation_protection",
        mode="before",
    )(dash_is_zero)

    required_skill_from_name = field_validator("required_skill", mode="before")(
        skill_from_name
    )
    required_skill_text_none = field_validator(
        "required_skill",
        mode="before",
    )(string_none_is_none)
