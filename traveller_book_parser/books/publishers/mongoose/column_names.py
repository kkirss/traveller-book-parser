COLUMN_TO_FIELD: dict[str, str] = {
    # General
    "NAME": "name",
    "TL": "tech_level",
    "KG": "weight",
    "COST": "base_price",
    # Items
    "TRAITS": "traits",
    # Armour
    "ARMOUR TYPE": "name",
    "PROTECTION": "protection",
    "REQUIRED SKILL": "required_skill",
    "RAD": "radiation_protection",
    "SLOTS": "slots_count",
    "DEX": "characteristic_bonuses.DEX",
    "STR": "characteristic_bonuses.STR",
    # Weapons
    "WEAPON": "name",
    "DAMAGE": "damage",
    "RANGE": "range",
    # Ranged weapons
    "MAGAZINE": "magazine_size",
    "MAGAZINE COST": "magazine_base_price",
    "POWER PACK COST": "magazine_base_price",
}
