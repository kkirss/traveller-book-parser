import json
import logging
import pathlib
from typing import Optional

from pydantic import BaseModel
import typer

from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.settings import SETTINGS, Settings
from traveller_book_parser.traveller_models.trav_database import TravDatabase
from traveller_book_parser.traveller_models.trav_glossary import (
    TravBookParserGlossary,
    TravModelsGlossary,
)
from traveller_book_parser.traveller_models.trav_object import TravObjectRoot
from traveller_book_parser.utils import ensure_folder

logger = logging.getLogger(__name__)

schema_app = typer.Typer(no_args_is_help=True)


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


schema_app.command("BookDescription")(book_description_schema_cli)
schema_app.command("book_description", hidden=True)(book_description_schema_cli)
schema_app.command("book-description", hidden=True)(book_description_schema_cli)


def trav_database_schema_cli(path: Optional[pathlib.Path] = None):
    """Dump the JSON schema of the 'TravDatabase' model."""
    dump_model_schema(path, TravDatabase, "TravDatabase")


schema_app.command("TravDatabase")(trav_database_schema_cli)
schema_app.command("trav_database", hidden=True)(trav_database_schema_cli)
schema_app.command("trav-database", hidden=True)(trav_database_schema_cli)


def trav_object_schema_cli(path: Optional[pathlib.Path] = None):
    """Dump the JSON schema of the 'TravObject' model."""
    dump_model_schema(path, TravObjectRoot, "TravObject")


schema_app.command("TravObject")(trav_object_schema_cli)
schema_app.command("trav_object", hidden=True)(trav_object_schema_cli)
schema_app.command("trav-object", hidden=True)(trav_object_schema_cli)


def trav_models_glossary_schema_cli(path: Optional[pathlib.Path] = None):
    """Dump the JSON schema of the 'TravModelsGlossary' model."""
    dump_model_schema(path, TravModelsGlossary, "TravModelsGlossary")


schema_app.command("TravModels")(trav_models_glossary_schema_cli)
schema_app.command("TravModelsGlossary", hidden=True)(trav_models_glossary_schema_cli)
schema_app.command("trav_models_glossary", hidden=True)(trav_models_glossary_schema_cli)
schema_app.command("trav-models-glossary", hidden=True)(trav_models_glossary_schema_cli)


def trav_book_parser_glossary_schema_cli(path: Optional[pathlib.Path] = None):
    """Dump the JSON schema of the 'TravBookParserGlossary' model."""
    dump_model_schema(path, TravBookParserGlossary, "TravBookParserGlossary")


schema_app.command("TravBookParser")(trav_book_parser_glossary_schema_cli)
schema_app.command("TravBookParserGlossary", hidden=True)(
    trav_book_parser_glossary_schema_cli
)
schema_app.command("trav_book_parser_glossary", hidden=True)(
    trav_book_parser_glossary_schema_cli
)
schema_app.command("trav-book-parser-glossary", hidden=True)(
    trav_book_parser_glossary_schema_cli
)


def trav_settings_schema_cli(path: Optional[pathlib.Path] = None):
    """Dump the JSON schema of the 'Settings' model."""
    dump_model_schema(path, Settings, "Settings")


schema_app.command("Settings")(trav_settings_schema_cli)
schema_app.command("settings", hidden=True)(trav_settings_schema_cli)


def all_schema_cli(path: Optional[pathlib.Path] = None):
    """Dump all JSON schema files."""
    book_description_schema_cli(path)
    trav_database_schema_cli(path)
    trav_object_schema_cli(path)
    trav_models_glossary_schema_cli(path)
    trav_book_parser_glossary_schema_cli(path)
    trav_settings_schema_cli(path)


schema_app.command("all")(all_schema_cli)
