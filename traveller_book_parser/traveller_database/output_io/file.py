from pathlib import Path
from typing import Optional


class OutputPathNotSetError(Exception):
    """Output path is required for file output."""

    def __init__(self):
        super().__init__("Output path is required for file output.")


def output_to_file(output: str, file_path: Optional[Path]) -> None:
    """Output to file."""
    if file_path is None:
        raise OutputPathNotSetError

    with file_path.open("w", encoding="utf-8") as f:
        f.write(output)
