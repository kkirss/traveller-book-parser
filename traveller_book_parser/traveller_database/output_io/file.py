from pathlib import Path


def output_to_file(output: str, file_path: Path) -> None:
    """Output to file."""
    with file_path.open("w", encoding="utf-8") as f:
        f.write(output)
