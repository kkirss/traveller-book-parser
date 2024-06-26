import logging
from typing import Any

from .base_weapon_trait import WeaponTraitType
from .weapon_trait import WeaponTrait, create_weapon_trait

logger = logging.getLogger(__name__)


def traits_from_list(value: Any) -> list[WeaponTrait]:  # noqa: ANN401
    """Create list of weapon traits from list of strings.

    Example:
    -------
    >>> traits_from_list(["Bulky", "Auto 5"])
    [BaseWeaponTrait(weapon_trait_type=<WeaponTraitType.bulky: 'Bulky'>, amount=None), BaseWeaponTrait(weapon_trait_type=<WeaponTraitType.auto: 'Auto'>, amount=5)]
    """
    if isinstance(value, list):
        traits = []
        for element in value:
            if not isinstance(element, str):
                continue

            try:
                trait_type = WeaponTraitType(element)
            except ValueError:
                trait_name, trait_amount = element.rsplit(" ", maxsplit=1)
                try:
                    trait_type = WeaponTraitType(trait_name)
                except ValueError:
                    logger.warning("Found invalid trait type, skipping: %s", trait_name)
                    continue
                trait = create_weapon_trait(
                    weapon_trait_type=trait_type,
                    amount=trait_amount if trait_amount != "" else None,
                )
            else:
                trait = create_weapon_trait(weapon_trait_type=trait_type)

            traits.append(trait)
        return traits
    return value
