import logging
import os
from pathlib import Path

from settings import SETTINGS

logger = logging.getLogger(__name__)


def are_html_files_exported(export_folder: Path) -> bool:
    """Check if HTML files are exported."""
    return (export_folder / "index.html").exists()


def export_html_files(pdf_path: Path, export_folder: Path):
    """Export HTML files from PDF file using pdftohtml."""
    pdf_to_html_command = (
        f'{SETTINGS.pdf_to_html_executable} "{pdf_path}" "{export_folder}"'
    )
    logger.debug("pdf_to_html_command %s", pdf_to_html_command)

    out = os.system(pdf_to_html_command)  # noqa: S605

    logger.debug("out %s", out)
