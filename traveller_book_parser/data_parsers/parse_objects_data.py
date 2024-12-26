from collections.abc import Iterable
from typing import Any

from plum import dispatch

from traveller_book_parser.traveller_models.trav_object import TravObject
from traveller_book_parser.traveller_models.trav_object_types import TravObjectType

from .base_data_container import BaseDataContainer


@dispatch.abstract
def parse_objects(
    data_container: BaseDataContainer,
    _type: TravObjectType,
    default_values: dict[str, Any],
) -> Iterable[TravObject]:
    """Parse a collection of objects from a data container."""
    raise NotImplementedError
