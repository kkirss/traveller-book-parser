import json
from pathlib import Path

import pytest
from syrupy.assertion import SnapshotAssertion

from schema.test_schema_cli import runner
from traveller_book_parser.cli_app.app import app


@pytest.mark.parametrize(
    ("command_name", "check_snapshot"),
    [
        ("TravGlossary", True),
        ("trav_glossary", False),
        ("trav-glossary", False),
    ],
)
def test_schema_trav_glossary_cli(
    *,
    command_name: str,
    check_snapshot: bool,
    snapshot: SnapshotAssertion,
    tmp_path: Path,
):
    # Arrange
    command = ["schema", command_name]
    output_file = tmp_path / f"{'.'.join(command)}.json"

    # Act
    result = runner.invoke(app, [*command, "--path", str(output_file)])

    # Assert
    assert result.exit_code == 0, result.output
    assert output_file.exists()

    with output_file.open("r", encoding="utf-8") as f:
        schema = json.load(f)

    if check_snapshot:
        # Compare the schema with the snapshot
        assert schema == snapshot
