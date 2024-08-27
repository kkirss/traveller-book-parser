from pydantic import BaseModel

from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.data_sources.data_source_description import (
    DataSourceDescription,
)
from traveller_book_parser.object_collections.collection_description import (
    CollectionDescription,
)

from .characteristics.characteristic import Characteristic
from .items.base_item import BaseItem
from .items.item import Item
from .items.weapons.base_weapon import BaseWeapon
from .items.weapons.melee_weapon import MeleeWeapon
from .items.weapons.ranged_weapon import RangedWeapon
from .skills.skill import Skill
from .trav_database import TravDatabase
from .trav_object import TravObject


class TravGlossary(BaseModel):
    """Glossary/collection of all Traveller models.

    This is not a model itself but simply a collection of all Traveller models.
    """

    book_description: BookDescription
    collection_description: CollectionDescription
    data_source_description: DataSourceDescription

    trav_database: TravDatabase

    # TravObject
    trav_object: TravObject

    # Characteristic
    characteristic: Characteristic

    # Item
    item: Item
    base_item: BaseItem

    base_weapon: BaseWeapon
    ranged_weapon: RangedWeapon
    melee_weapon: MeleeWeapon

    # Skill
    skill: Skill
