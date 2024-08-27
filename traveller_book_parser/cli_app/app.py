import typer

from .parse import parse_all_books_cli, parse_book_cli
from .schema import schema_app

app = typer.Typer(
    help="Parse Traveller books into other formats.",
    no_args_is_help=True,
)


app.command("parse-book", no_args_is_help=True)(parse_book_cli)
app.command("parse")(parse_all_books_cli)
app.add_typer(schema_app, name="schema", help="Dump the JSON schema of models.")


def run_cli():
    """Run CLI."""
    app()
