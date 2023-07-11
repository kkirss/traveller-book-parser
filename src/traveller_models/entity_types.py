from enum import Enum


class EntityType(str, Enum):
    CHARACTERISTIC = "characteristic"
    ITEM = "item"
    SKILL = "skill"
