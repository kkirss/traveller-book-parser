from enum import Enum


class EntityType(str, Enum):
    """Entity type."""

    CHARACTERISTIC = "characteristic"
    ITEM = "item"
    SKILL = "skill"
