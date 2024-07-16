from typing import Any

from traveller_book_parser.traveller_models.validators.dashes import is_dash_value


def is_missing_tech_level(obj_dict: dict[str, Any]) -> bool:
    """Check if a tech level is missing."""
    tech_level = obj_dict.get("tech_level")
    return is_dash_value(tech_level)
