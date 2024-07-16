from enum import Enum


class TravObjectType(str, Enum):
    """Type of traveller object."""

    CHARACTERISTIC = "characteristic"
    ITEM = "item"
    SKILL = "skill"
