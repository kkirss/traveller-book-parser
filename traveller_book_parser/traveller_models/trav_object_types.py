from enum import Enum


class TravObjectType(str, Enum):
    """Type of traveller object."""

    CHARACTER = "character"
    CHARACTERISTIC = "characteristic"
    ITEM = "item"
    SKILL = "skill"
