from operator import itemgetter
from pathlib import Path
from typing import Any

from .pdfplumber_integration import open_pdfplumber_page

ExtractTextLinesOptions = dict[str, Any]
EXTRACT_TEXT_LINES_OPTIONS_DEFAULT: ExtractTextLinesOptions = {
    "y_tolerance": 0,
}


def _get_line_font_size(line: dict[str, Any]) -> float:
    return line["chars"][0]["size"]


def guess_page_header(
    pdf_path: Path,
    page_number: int,
    nth_largest_font_text: int = 1,
    extract_text_lines_options: ExtractTextLinesOptions | None = None,
) -> str | None:
    """Guess the header of a page in a pdf."""
    if extract_text_lines_options is None:
        extract_text_lines_options = EXTRACT_TEXT_LINES_OPTIONS_DEFAULT

    with open_pdfplumber_page(pdf_path, page_number) as page:
        lines = page.extract_text_lines(**extract_text_lines_options)

    line_and_font_sizes = [(line, _get_line_font_size(line)) for line in lines]
    line_and_font_sizes.sort(key=itemgetter(1), reverse=True)

    if len(line_and_font_sizes) == 0:
        return None

    try:
        header_line = line_and_font_sizes[nth_largest_font_text - 1][0]
    except IndexError:
        return None

    return header_line["text"]
