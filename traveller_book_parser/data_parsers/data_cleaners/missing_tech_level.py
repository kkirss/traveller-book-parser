from typing import Any

from traveller_book_parser.traveller_models.validators.dashes import is_dash_value


def is_missing_tech_level(entity_dict: dict[str, Any]) -> bool:
    """Check if an entity is missing a tech level."""
    tech_level = entity_dict.get("tech_level")
    return is_dash_value(tech_level)
