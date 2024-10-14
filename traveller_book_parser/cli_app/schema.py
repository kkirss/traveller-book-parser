from collections.abc import Callable
import json
import logging
from pathlib import Path
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

SchemaModelCLIFunction = Callable[[Path | None], None]


class SchemaModelRegistration(BaseModel):
    """Registration of a model for dumping its schema using CLI."""

    model_cls: type[BaseModel]
    name: str
    name_aliases: tuple[str, ...]
    description: Optional[str]


def dump_model_schema(
    path: Optional[Path],
    model_cls: type[BaseModel],
    name: str,
):
    """Dump the JSON schema of a model."""
    if not model_cls.__doc__:
        logger.warning("Model '%s' has no docstring.", model_cls.__name__)

    if path is None:
        path = SETTINGS.default_schema_output_path / f"{name}.json"
    elif path.is_dir():
        path = path / f"{name}.json"

    ensure_folder(path.parent)

    with path.open("w") as f:
        json.dump(model_cls.model_json_schema(), f, indent=2)


def _create_model_cli_function(
    model_cls: type[BaseModel],
    name: str,
    description: Optional[str] = None,
) -> SchemaModelCLIFunction:

    def _model_schema_cli(path: Optional[Path] = None):
        dump_model_schema(path, model_cls, name)

    if description:
        _model_schema_cli.__doc__ = description

    return _model_schema_cli


def _add_commands_for_model(
    name: str, name_aliases: tuple[str, ...], cli_function: SchemaModelCLIFunction
):
    schema_app.command(name)(cli_function)

    for name_alias in name_aliases:
        schema_app.command(name_alias, hidden=True)(cli_function)


def register_model_for_cli(
    registration: SchemaModelRegistration,
) -> SchemaModelCLIFunction:
    """Register a model for the CLI."""
    cli_function = _create_model_cli_function(
        registration.model_cls, registration.name, registration.description
    )

    _add_commands_for_model(registration.name, registration.name_aliases, cli_function)

    return cli_function


def register_models_for_cli(
    registrations: list[SchemaModelRegistration],
) -> list[SchemaModelCLIFunction]:
    """Register models for the CLI."""
    output_functions = []
    for registration in registrations:
        cli_function = register_model_for_cli(registration)
        output_functions.append(cli_function)
    return output_functions


SCHEMA_MODEL_REGISTRATIONS = [
    SchemaModelRegistration(
        model_cls=BookDescription,
        name="BookDescription",
        name_aliases=("book_description", "book-description"),
        description="""Dump the JSON schema of the 'BookDescription' model.""",
    ),
    SchemaModelRegistration(
        model_cls=TravDatabase,
        name="TravDatabase",
        name_aliases=("trav_database", "trav-database"),
        description="""Dump the JSON schema of the 'TravDatabase' model.""",
    ),
    SchemaModelRegistration(
        model_cls=TravObjectRoot,
        name="TravObject",
        name_aliases=("trav_object", "trav-object"),
        description="""Dump the JSON schema of the 'TravObject' model.""",
    ),
    SchemaModelRegistration(
        model_cls=TravModelsGlossary,
        name="TravModels",
        name_aliases=(
            "trav_models_glossary",
            "trav-models-glossary",
            "TravModelsGlossary",
        ),
        description="""Dump the JSON schema of the 'TravModelsGlossary' model.""",
    ),
    SchemaModelRegistration(
        model_cls=TravBookParserGlossary,
        name="TravBookParser",
        name_aliases=(
            "trav_book_parser_glossary",
            "trav-book-parser-glossary",
            "TravBookParserGlossary",
        ),
        description="""Dump the JSON schema of the 'TravBookParserGlossary' model.""",
    ),
    SchemaModelRegistration(
        model_cls=Settings,
        name="Settings",
        name_aliases=("settings",),
        description="""Dump the JSON schema of the 'Settings' model.""",
    ),
]

ALL_CLI_FUNCTIONS = register_models_for_cli(SCHEMA_MODEL_REGISTRATIONS)


def all_schema_cli(path: Optional[Path] = None):
    """Dump all JSON schema files."""
    for cli_function in ALL_CLI_FUNCTIONS:
        cli_function(path)


schema_app.command("all")(all_schema_cli)
