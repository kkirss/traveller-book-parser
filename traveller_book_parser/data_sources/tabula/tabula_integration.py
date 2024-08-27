from collections.abc import Iterable
import copy
import json
import logging
from pathlib import Path
from typing import Any, Literal, Optional, TypedDict

import pandas as pd
import tabula

logger = logging.getLogger(__name__)

ExtractionMethod = Literal["lattice", "stream"] | None

TABULA_PANDAS_OPTIONS = {}


def read_tabula_data_file(
    path: Path,
    pandas_options: Optional[dict[str, Any]] = None,
) -> list[pd.DataFrame]:
    """Read tabula internal JSON formatted data from a file."""
    if pandas_options is None:
        pandas_options = copy.deepcopy(TABULA_PANDAS_OPTIONS)

    with path.open("r", encoding="utf-8") as f:
        raw_json = json.load(f)

    return tabula.io._extract_from(  # noqa: SLF001
        raw_json,
        pandas_options=pandas_options,
    )


class TabulaKwargs(TypedDict, total=False):
    """Arguments for Tabula parsing."""

    lattice: bool
    stream: bool


def export_tabula_data_file(
    book_pdf_path: Path,
    export_path: Path,
    pages: str | int | Iterable[int] | None,
    area: Optional[Iterable[float]] = None,
    extraction_method: ExtractionMethod = None,
) -> None:
    """Parse tables from a PDF file using Tabula and export them to a JSON file."""
    kwargs: TabulaKwargs = {}
    if extraction_method == "lattice":
        kwargs = {"lattice": True}
    elif extraction_method == "stream":
        kwargs = {"stream": True}

    tabula.io.convert_into(
        book_pdf_path,
        str(export_path),
        output_format="json",
        pages=pages,
        area=area,
        **kwargs,
    )
