from collections.abc import Callable
import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class FileTypeNotSupportedError(Exception):
    """Exception raised when file type is not supported."""

    def __init__(self, file_type: str):
        super().__init__(f"File type is not supported: {file_type}")


def load_json_data(path: Path) -> dict[str, Any]:
    """Load data from a JSON file."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


FILE_TYPE_LOADERS: dict[str, Callable[[Path], dict[str, Any]]] = {
    ".json": load_json_data,
}


def load_file_data(path: Path) -> dict[str, Any]:
    """Load data from a file."""
    try:
        file_type_loader = FILE_TYPE_LOADERS[path.suffix]
    except KeyError as e:
        raise NotImplementedError(
            f"File type is not supported: {path.suffix}",
        ) from e

    return file_type_loader(path)


def is_supported_file_type(path: Path) -> bool:
    """Check if file type is supported."""
    return path.suffix in FILE_TYPE_LOADERS


def get_supported_path(paths: list[Path]) -> Path:
    """Get the first supported path from a list of paths."""
    match paths:
        case []:
            raise ValueError(  # noqa: TRY003
                "No paths given. This should be handled earlier."
            )
        case [path] if not is_supported_file_type(path):
            raise FileTypeNotSupportedError(path.suffix)
        case [path]:
            return path
        case _:
            path = next(filter(is_supported_file_type, paths), None)
            if path:
                logger.info("Found multiple supported files. Using %s", path)
                return path

            raise FileTypeNotSupportedError(", ".join([path.suffix for path in paths]))
