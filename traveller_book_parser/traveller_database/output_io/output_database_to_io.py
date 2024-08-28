from pathlib import Path
from typing import Optional

from .file import output_to_file
from .output_type import OutputType
from .stdout import output_to_stdout


def output_database_to_io(
    output: str, output_type: OutputType, output_path: Optional[Path]
) -> None:
    """Output database to IO base on output type."""
    if output_type == OutputType.stdout:
        output_to_stdout(output)

    elif output_type == OutputType.file and output_path is None:
        raise ValueError("Output path is required for file output.")

    elif output_type == OutputType.file and output_path is not None:
        output_to_file(output, output_path)

    else:
        raise ValueError(f"Unknown output type: {output_type}")
