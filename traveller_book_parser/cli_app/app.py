import typer

from .parse import parse_app
from .schema import schema_app

app = typer.Typer(
    help="Parse Traveller books into other formats.",
    no_args_is_help=True,
)


app.add_typer(parse_app, name="parse", help="Parse books for content.")
app.add_typer(schema_app, name="schema", help="Dump the JSON schema of models.")


def run_cli():
    """Run CLI."""
    app()
