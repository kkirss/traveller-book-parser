import logging
import math
from operator import itemgetter
from pathlib import Path
from typing import Any, Optional

from pdfminer.image import ImageWriter
from pdfminer.layout import LTFigure, LTImage
from pdfplumber._typing import T_bbox, T_point
from pdfplumber.page import Page

from traveller_book_parser.books.book_description import (
    BookDescription,
    get_book_file_path,
)
from traveller_book_parser.data_sources.pdfplumber.pdfplumber_integration import (
    open_pdfplumber_page,
)
from traveller_book_parser.object_collections.collection_description import (
    CollectionDescription,
)
from traveller_book_parser.settings import SETTINGS
from traveller_book_parser.traveller_models.trav_object import TravObject

logger = logging.getLogger(__name__)


class ImageExportError(Exception):
    """Failed to export image for trav_obj."""

    def __init__(self, obj: TravObject) -> None:
        super().__init__(f"Failed to export image for trav_obj {obj}")


class ImagePagesNotSetError(Exception):
    """Must specify instrument.image_pages to add image to trav_obj."""

    def __init__(self) -> None:
        super().__init__(
            "Must specify instrument.image_pages to add image to trav_obj."
        )


def get_obj_image_path(obj: TravObject) -> Optional[Path]:
    """Get the path to an objects image, if it exists."""
    matched_files = list(SETTINGS.images_path.glob(f"{obj.name}.*"))
    if len(matched_files) == 0:
        return None
    return matched_files[0]


def get_center(bbox: T_bbox) -> T_point:
    """Get the center of a pdfplumber/pdfminer bbox."""
    (x0, y0, x1, y1) = bbox
    x_center = (x0 + x1) / 2
    y_center = (y0 + y1) / 2
    return x_center, y_center


def get_text_center(text: dict[str, Any]) -> T_point:
    """Get the center of a pdfplumber text object."""
    x0 = text["x0"]
    y0 = text["chars"][-1]["y0"]
    x1 = text["x1"]
    y1 = text["chars"][0]["y1"]
    bbox = (x0, y0, x1, y1)
    return get_center(bbox)


def get_distance(point_1: T_point, point_2: T_point) -> float:
    """Get the cartesian distance between two points."""
    x_delta = point_1[0] - point_2[0]
    y_delta = point_1[1] - point_2[1]
    return math.sqrt(x_delta**2 + y_delta**2)


def _get_closest_figures_and_distances(
    to_point: T_point, page: Page
) -> list[tuple[LTFigure, float]]:
    """Get the closest pdfminer figures to a point in a pdfplumber page."""
    page_objects = list(page.layout)
    page_figures = [obj for obj in page_objects if isinstance(obj, LTFigure)]

    figure_distances = [
        (figure, get_distance(get_center(figure.bbox), to_point))
        for figure in page_figures
    ]
    figure_distances.sort(key=itemgetter(1))

    return figure_distances


def _find_point_closest_image_and_distance(
    to_point: T_point, page: Page
) -> tuple[LTImage, float] | None:
    """Find the closest image to a point in a pdfplumber page."""
    figure_distances = _get_closest_figures_and_distances(to_point, page)

    if len(figure_distances) == 0:
        return None

    closest_figure, distance = figure_distances[0]
    closest_image = next(iter(closest_figure))

    if not isinstance(closest_image, LTImage):
        return None

    return closest_image, distance


def find_page_text_closest_image_and_distance(
    text: str, page: Page
) -> tuple[LTImage, float] | None:
    """Find the closest image to a text string in a pdfplumber page."""
    closest_images_and_distances: list[tuple[LTImage, float]] = []
    text_matches = page.search(text, regex=False)

    for text_dict in text_matches:
        text_center = get_text_center(text_dict)

        closest_image_and_distance = _find_point_closest_image_and_distance(
            text_center, page
        )

        if closest_image_and_distance is not None:
            closest_images_and_distances.append(closest_image_and_distance)

    if len(closest_images_and_distances) == 0:
        return None

    closest_images_and_distances.sort(key=itemgetter(1))
    return closest_images_and_distances[0]


def find_pdf_text_closest_image_and_distance(
    text: str, pdf_path: Path, page_numbers: list[int]
) -> Optional[LTImage]:
    """Find the closest image to a text string in a pdf."""
    closest_images_and_distances: list[tuple[LTImage, float]] = []

    for page_number in page_numbers:
        with open_pdfplumber_page(pdf_path, page_number) as page:
            closest_image_and_distance = find_page_text_closest_image_and_distance(
                text, page
            )

            if closest_image_and_distance is not None:
                closest_images_and_distances.append(closest_image_and_distance)

    if len(closest_images_and_distances) == 0:
        return None

    closest_images_and_distances.sort(key=itemgetter(1))
    return closest_images_and_distances[0][0]


def export_image(image: LTImage, output_dir_path: Path) -> str:
    """Export an image from a pdfminer LTImage."""
    return ImageWriter(str(output_dir_path)).export_image(image)


def export_obj_image(
    obj: TravObject, pdf_path: Path, page_numbers: list[int]
) -> Optional[Path]:
    """Export an image for an object, using pdfplumber and pdfminer."""
    closest_image = find_pdf_text_closest_image_and_distance(
        obj.name, pdf_path, page_numbers
    )

    if closest_image is None:
        return None

    closest_image.name = obj.name

    export_image(closest_image, SETTINGS.images_path)

    image_path = get_obj_image_path(obj)

    if image_path is None:
        raise ImageExportError(obj)

    return image_path


def add_obj_image_path(
    obj: TravObject,
    book_description: BookDescription,
    collection_description: CollectionDescription,
) -> None:
    """Add an image path to an object."""
    image_path = get_obj_image_path(obj)

    if image_path is None:
        if len(collection_description.instrument.image_pages) == 0:
            raise ImagePagesNotSetError

        image_path = export_obj_image(
            obj,
            pdf_path=get_book_file_path(book_description.code_name),
            page_numbers=collection_description.instrument.image_pages,
        )

    if image_path is not None:
        obj.image_path = image_path
    else:
        logger.warning("Failed to find image_path for trav_obj %s", obj)
