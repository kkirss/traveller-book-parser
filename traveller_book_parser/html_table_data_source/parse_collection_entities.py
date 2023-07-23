from collections.abc import Iterable
from typing import Any

from traveller_book_parser.books.book_description import BookDescription
from traveller_book_parser.entity_collections.parse_entities import (
    parse_collection_entities,
)
from traveller_book_parser.html_data_source.data_extract import export_book_html_files
from traveller_book_parser.html_data_source.data_source_description import (
    HTMLDataSourceDescription,
)
from traveller_book_parser.traveller_models.entity import Entity
from traveller_book_parser.traveller_models.entity_types import EntityType


@parse_collection_entities.dispatch
def parse_tabula_collection_entities(
    book_description: BookDescription,
    data_source_description: HTMLDataSourceDescription,  # noqa: ARG001
    entity_type: EntityType,  # noqa: ARG001
    entity_fields: dict[str, Any],  # noqa: ARG001
) -> Iterable[Entity]:
    export_book_html_files(book_description)
    # TODO: Parse the HTML files
    return []
