import typer

from .parse import parse_all_books_cli, parse_book_cli

app = typer.Typer(
    help="Parse Traveller books into other formats.",
    no_args_is_help=True,
)


app.command("parse-book", no_args_is_help=True)(parse_book_cli)
app.command("parse")(parse_all_books_cli)


def run_cli():
    """Run CLI."""
    app()
