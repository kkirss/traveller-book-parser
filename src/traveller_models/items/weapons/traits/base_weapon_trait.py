from enum import Enum

from pydantic import BaseModel


class WeaponTraitType(str, Enum):
    armor_piercing = "AP"
    artillery = "Artillery"
    auto = "Auto"
    blast = "Blast"
    bulky = "Bulky"
    very_bulky = "Very Bulky"
    dangerous = "Dangerous"
    very_dangerous = "Very Dangerous"
    fire = "Fire"
    one_use = "One Use"
    one_shot = "One Shot"
    radiation = "Radiation"
    scope = "Scope"
    silent = "Silent"
    smart = "Smart"
    smasher = "Smasher"
    stun = "Stun"
    zero_g = "Zero-G"


class BaseWeaponTrait(BaseModel):
    weapon_trait_type: WeaponTraitType
    amount: int | None = None
