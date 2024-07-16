from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.object_collections.collection_description import (
    CollectionDescription,
)
from traveller_book_parser.traveller_models.trav_object import TravObject

from .image import add_obj_image_path


def instrument_object(
    trav_obj: TravObject,
    book_description: BookDescription,
    collection_description: CollectionDescription,
) -> TravObject:
    """Instrument a traveller object with additional data."""
    instrument = collection_description.instrument

    if instrument.add_images:
        add_obj_image_path(trav_obj, book_description, collection_description)

    return trav_obj
