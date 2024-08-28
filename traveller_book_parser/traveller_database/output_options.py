from pathlib import Path
from typing import Optional

from pydantic import BaseModel

from .output_format.output_format import OutputFormat
from .output_io.output_type import OutputType


class DatabaseOutputOptions(BaseModel):
    """Options for outputting a database."""

    output_format: OutputFormat
    output_type: OutputType = OutputType.stdout
    output_path: Optional[Path] = None
