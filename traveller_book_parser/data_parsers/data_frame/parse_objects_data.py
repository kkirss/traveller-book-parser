from collections.abc import Callable, Hashable, Iterable
import logging
from typing import Any

from pandas import Series
from pydantic import ValidationError

from traveller_book_parser.books.publishers.column_names import get_column_field_name
from traveller_book_parser.data_parsers.data_cleaners.missing_tech_level import (
    is_missing_tech_level,
)
from traveller_book_parser.data_parsers.parse_objects_data import parse_objects
from traveller_book_parser.settings import SETTINGS
from traveller_book_parser.traveller_models.trav_object import (
    TravObject,
    create_trav_object,
)
from traveller_book_parser.traveller_models.trav_object_types import TravObjectType

from .data_cleaners.clean_data_frame import clean_data_frame
from .data_container import DataFrameDataContainer

logger = logging.getLogger(__name__)


def set_deep(
    obj: dict[str, Any], key: str, value: Any  # noqa: ANN401
) -> dict[str, Any]:
    """Set a value in a nested dictionary.

    Example:
    -------
    >>> set_deep({"foo": "bar"}, "a.b.c", 2)
    {'foo': 'bar', 'a': {'b': {'c': 2}}}
    """
    inner_obj = obj
    [*nested_keys, last_key] = key.split(".")

    for sub_key in nested_keys:
        inner_obj = inner_obj.setdefault(sub_key, {})

    inner_obj[last_key] = value
    return obj


def construct_obj_dict_from_row(
    row: Iterable[tuple[Hashable, Series]],
    _type: TravObjectType,
    default_values: dict[str, Any],
    add_unknown_column: Callable[[str], None],
) -> dict[str, Any]:
    """Construct a dictionary from a row of a data frame."""
    obj_dict = {
        "type": _type,
        **default_values,
    }
    obj_dict.items()
    for column, value in row:
        if not isinstance(column, str):
            continue
        try:
            field_name = get_column_field_name(column)
        except KeyError:
            add_unknown_column(column)
            continue

        set_deep(obj_dict, field_name, value)

    return obj_dict


@parse_objects.dispatch
def parse_objects_data_frame(
    data_container: DataFrameDataContainer,
    _type: TravObjectType,
    default_values: dict[str, Any],
) -> Iterable[TravObject]:
    """Parse a collection of objects from a data frame."""
    data_frame = data_container.data

    if SETTINGS.log_intermediate_data:
        logger.debug("Parsing objects from data frame:\n%s", data_frame)

    data_frame = clean_data_frame(data_frame)

    previous_obj = None
    unknown_columns = set()
    for _, row in data_frame.iterrows():
        obj_dict = construct_obj_dict_from_row(
            row.items(), _type, default_values, unknown_columns.add
        )

        if is_missing_tech_level(obj_dict):
            logger.warning(
                "Found object with missing tech level, skipping: %s", obj_dict
            )
            continue

        try:
            obj = create_trav_object(**obj_dict)
        except ValidationError:
            logger.exception("Failed to create trav_obj from %s", obj_dict)
            continue

        if obj.name == "":
            if previous_obj is None:
                logger.warning(
                    "Found first trav_obj with empty name, skipping: %s", obj_dict
                )
                continue
            if previous_obj.name == "":
                logger.warning(
                    "Found two objects with empty names, skipping: %s", obj_dict
                )
                continue
            obj.name = previous_obj.name

        previous_obj = obj
        yield obj

    for unknown_column in unknown_columns:
        logger.warning("Found unknown column: %s", unknown_column)
