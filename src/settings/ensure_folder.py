from pathlib import Path


def ensure_folder(path: Path):
    path.mkdir(parents=True, exist_ok=True)
