import json
import logging
import pathlib
from typing import Optional

from pydantic import BaseModel
import typer

from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.settings import SETTINGS
from traveller_book_parser.traveller_models.trav_object import TravObjectRoot
from traveller_book_parser.traveller_models.traveller_database import TravellerDatabase
from traveller_book_parser.utils import ensure_folder

logger = logging.getLogger(__name__)

schema_app = typer.Typer()


def dump_model_schema(
    path: Optional[pathlib.Path],
    cls: type[BaseModel],
    name: str,
):
    """Dump the JSON schema of a model."""
    if not cls.__doc__:
        logger.warning("Model '%s' has no docstring.", cls.__name__)

    if path is None:
        path = SETTINGS.default_schema_output_path / f"{name}.json"
    elif path.is_dir():
        path = path / f"{name}.json"

    ensure_folder(path.parent)

    with path.open("w") as f:
        json.dump(cls.model_json_schema(), f, indent=2)


def book_description_schema_cli(path: Optional[pathlib.Path] = None):
    """Dump the JSON schema of the 'BookDescription' model."""
    dump_model_schema(path, BookDescription, "BookDescription")


schema_app.command("book_description")(book_description_schema_cli)
schema_app.command("BookDescription")(book_description_schema_cli)


def database_schema_cli(path: Optional[pathlib.Path] = None):
    """Dump the JSON schema of the 'TravellerDatabase' model."""
    dump_model_schema(path, TravellerDatabase, "TravellerDatabase")


schema_app.command("traveller_database")(database_schema_cli)
schema_app.command("TravellerDatabase")(database_schema_cli)


def trav_object_schema_cli(path: Optional[pathlib.Path] = None):
    """Dump the JSON schema of the 'TravObject' model."""
    dump_model_schema(path, TravObjectRoot, "TravObject")


schema_app.command("trav_object")(trav_object_schema_cli)
schema_app.command("TravObject")(trav_object_schema_cli)


def all_schema_cli(path: Optional[pathlib.Path] = None):
    """Dump all JSON schema files."""
    book_description_schema_cli(path)
    database_schema_cli(path)
    trav_object_schema_cli(path)


schema_app.command("all")(all_schema_cli)
