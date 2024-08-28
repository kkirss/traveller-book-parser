from syrupy.assertion import SnapshotAssertion
from typer.testing import CliRunner

from traveller_book_parser.cli_app.app import app


def test_parse_book_help_cli(snapshot: SnapshotAssertion, cli_runner: CliRunner):
    # Arrange
    command = ["parse", "book", "--help"]

    # Act
    result = cli_runner.invoke(app, [*command])

    # Assert
    assert result.exit_code == 0, result.output
    assert result.output == snapshot
