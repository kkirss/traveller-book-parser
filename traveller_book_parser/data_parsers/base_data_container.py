from typing import Any

from pydantic import BaseModel, ConfigDict

from traveller_book_parser.data_sources.data_source_description import (
    DataSourceDescription,
)


class BaseDataContainer(BaseModel):
    """Container for data from a data source."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    data_source_description: DataSourceDescription
    data: Any
