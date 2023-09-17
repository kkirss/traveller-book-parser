from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.entity_collections.collection_description import (
    CollectionDescription,
)
from traveller_book_parser.traveller_models.entity import Entity

from .image import add_entity_image_path


def instrument_entity(
    entity: Entity,
    book_description: BookDescription,
    collection_description: CollectionDescription,
) -> Entity:
    """Instrument an entity with additional data."""
    entity_instrument = collection_description.entity_instrument

    if entity_instrument.add_images:
        add_entity_image_path(entity, book_description, collection_description)

    return entity
