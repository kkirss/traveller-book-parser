from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field, computed_field

from .trav_object_types import TravObjectType

TRAV_ID_SEPARATOR = ":"


class TravObjectBase(BaseModel):
    """A traveller object with name."""

    @computed_field
    @property
    def trav_id(self) -> str:
        """Get the Traveller ID of the object."""
        parent = self.type.value
        return self._create_id(parent, self._get_trav_id_pieces())

    type: TravObjectType

    name: str = Field(repr=True)
    description: str = Field(repr=False, default="")

    image_path: Optional[Path] = None

    @staticmethod
    def _create_id(parent: str, extra_suffixes: list[str | int | None]) -> str:
        suffixes_with_separators = "".join(
            [f"{TRAV_ID_SEPARATOR}{extra_suffix}" for extra_suffix in extra_suffixes]
        )
        return f"{parent}{suffixes_with_separators}"

    def _get_trav_id_pieces(self) -> list[str | int | None]:
        return [self.name.replace(TRAV_ID_SEPARATOR, "-")]
