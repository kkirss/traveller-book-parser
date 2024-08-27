import json
from pathlib import Path

from syrupy.assertion import SnapshotAssertion
from typer.testing import CliRunner

from traveller_book_parser.cli_app.app import app

runner = CliRunner()


def test_schema_trav_object_cli(snapshot: SnapshotAssertion, tmp_path: Path):
    # Arrange
    command = ["schema", "TravObject"]
    output_file = tmp_path / f"{'.'.join(command)}.json"

    # Act
    result = runner.invoke(app, [*command, "--path", str(output_file)])

    # Assert
    assert result.exit_code == 0, result.output
    assert output_file.exists()

    with output_file.open("r", encoding="utf-8") as f:
        schema = json.load(f)

    # Compare the schema with the snapshot
    assert schema == snapshot


def test_schema_traveller_database_cli(snapshot: SnapshotAssertion, tmp_path: Path):
    # Arrange
    command = ["schema", "TravellerDatabase"]
    output_file = tmp_path / f"{'.'.join(command)}.json"

    # Act
    result = runner.invoke(app, [*command, "--path", str(output_file)])

    # Assert
    assert result.exit_code == 0, result.output
    assert output_file.exists()

    with output_file.open("r", encoding="utf-8") as f:
        schema = json.load(f)

    # Compare the schema with the snapshot
    assert schema == snapshot


def test_schema_book_description_cli(snapshot: SnapshotAssertion, tmp_path: Path):
    # Arrange
    command = ["schema", "BookDescription"]
    output_file = tmp_path / f"{'.'.join(command)}.json"

    # Act
    result = runner.invoke(app, [*command, "--path", str(output_file)])

    # Assert
    assert result.exit_code == 0, result.output
    assert output_file.exists()

    with output_file.open("r", encoding="utf-8") as f:
        schema = json.load(f)

    # Compare the schema with the snapshot
    assert schema == snapshot
