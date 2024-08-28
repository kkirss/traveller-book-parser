from syrupy.assertion import SnapshotAssertion
from typer.testing import CliRunner

from traveller_book_parser.cli_app.app import app


def test_schema_help_cli(snapshot: SnapshotAssertion, cli_runner: CliRunner):
    # Arrange
    command = ["schema"]

    # Act
    result = cli_runner.invoke(app, [*command])

    # Assert
    assert result.exit_code == 0, result.output
    assert result.output == snapshot
