from syrupy.assertion import SnapshotAssertion
from typer.testing import CliRunner

from traveller_book_parser.cli_app.app import app

CLI_NO_EXPLICIT_HELP_ARG_ERROR_CODE = 2


def test_parse_help_cli(snapshot: SnapshotAssertion, cli_runner: CliRunner):
    # Arrange
    command = ["parse"]

    # Act
    result = cli_runner.invoke(app, [*command])

    # Assert
    assert result.exit_code == CLI_NO_EXPLICIT_HELP_ARG_ERROR_CODE, result.output
    assert result.output == snapshot
