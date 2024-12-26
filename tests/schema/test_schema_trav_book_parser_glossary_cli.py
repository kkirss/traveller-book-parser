from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion
from typer.testing import CliRunner

from traveller_book_parser.cli_app.app import app


@pytest.mark.parametrize(
    ("command_name", "check_snapshot"),
    [
        ("TravBookParserGlossary", True),
        ("TravBookParser", False),
        ("trav_book_parser_glossary", False),
        ("trav-book-parser-glossary", False),
    ],
)
def test_schema_trav_book_parser_glossary_cli(
    *,
    command_name: str,
    check_snapshot: bool,
    cli_runner: CliRunner,
    snapshot: SnapshotAssertion,
    tmp_path: Path,
):
    # Arrange
    command = ["schema", command_name]
    output_file = tmp_path / f"{'.'.join(command)}.json"

    # Act
    result = cli_runner.invoke(app, [*command, "--path", str(output_file)])

    # Assert
    assert result.exit_code == 0, result.output
    assert output_file.exists()

    with output_file.open("r", encoding="utf-8") as f:
        schema = f.read()

    if check_snapshot:
        # Compare the schema with the snapshot
        assert schema == snapshot
