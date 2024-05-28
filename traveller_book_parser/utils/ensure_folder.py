from pathlib import Path


def ensure_folder(path: Path):
    """Create folder if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)
