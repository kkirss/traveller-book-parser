from collections.abc import Callable
import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


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
            raise ValueError("No paths found")
        case [path] if not is_supported_file_type(path):
            raise ValueError(
                f"Loading data from '{path.suffix}' file-type is not supported.",
            )
        case [path]:
            return path
        case _:
            path = next(filter(is_supported_file_type, paths), None)
            if path:
                logger.info("Found multiple supported files. Using %s", path)
                return path

            file_types = ",".join({path.suffix for path in paths})
            raise ValueError(
                f"Loading data from '{file_types}' file-types is not supported.",
            )
